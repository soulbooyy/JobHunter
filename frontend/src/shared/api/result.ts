import { z } from 'zod';
const fieldCode = z.enum([
  'REQUIRED',
  'UNKNOWN_FIELD',
  'INVALID_TYPE',
  'BLANK_VALUE',
  'TOO_LONG',
  'INVALID_CHARACTERS',
  'INVALID_FORMAT',
  'OUT_OF_RANGE',
]);
const statuses = {
  BAD_REQUEST: 400,
  REQUEST_TOO_LARGE: 413,
  ACCESS_DENIED: 403,
  VALIDATION_ERROR: 422,
  NOT_FOUND: 404,
  REVISION_CONFLICT: 409,
  REQUEST_CONFLICT: 409,
  ORIGINAL_ENTRY_DELETED: 409,
  REVISION_EXHAUSTED: 409,
  STORAGE_UNAVAILABLE: 503,
  OUTCOME_UNKNOWN: 503,
  INTERNAL_ERROR: 500,
} as const;
const errorSchema = z.strictObject({
  code: z.enum(
    Object.keys(statuses) as [
      keyof typeof statuses,
      ...(keyof typeof statuses)[],
    ],
  ),
  message: z.string().min(1),
  field_errors: z.array(
    z.strictObject({
      field: z.string(),
      code: fieldCode,
    }),
  ),
});
export type FieldError = z.infer<typeof errorSchema>['field_errors'][number];
export class ApiFailure extends Error {
  constructor(
    public kind: 'rejected' | 'unknown' | 'read',
    public code: string,
    public fields: FieldError[] = [],
  ) {
    super(code);
  }
}
export async function apiResult<T>(
  operation: () => Promise<{
    response: Response;
    data?: unknown;
    error?: unknown;
  }>,
  schema: z.ZodType<T>,
  write = false,
  scope: 'entry' | 'preferences' = 'entry',
): Promise<T> {
  try {
    const result = await operation();
    if (result.response.status === 200) return schema.parse(result.data);
    const failure = errorSchema.safeParse(result.error);
    if (
      failure.success &&
      statuses[failure.data.code] === result.response.status &&
      (scope === 'entry'
        ? failure.data.code !== 'REQUEST_TOO_LARGE'
        : failure.data.code !== 'ORIGINAL_ENTRY_DELETED') &&
      failure.data.field_errors.every((field) =>
        validErrorField(field.field, scope),
      ) &&
      (failure.data.code !== 'VALIDATION_ERROR' ||
        failure.data.field_errors.length > 0) &&
      (failure.data.code === 'VALIDATION_ERROR' ||
        failure.data.field_errors.length === 0)
    ) {
      const { code, field_errors } = failure.data;
      const uncertain = code === 'OUTCOME_UNKNOWN' || code === 'INTERNAL_ERROR';
      throw new ApiFailure(
        write ? (uncertain ? 'unknown' : 'rejected') : 'read',
        code,
        field_errors,
      );
    }
    throw new Error('Unrecognized response');
  } catch (error) {
    if (error instanceof ApiFailure) throw error;
    throw new ApiFailure(
      write ? 'unknown' : 'read',
      write ? 'OUTCOME_UNKNOWN' : 'READ_FAILED',
    );
  }
}
export function failureMessage(error: ApiFailure): string {
  const messages: Record<string, string> = {
    BAD_REQUEST: '请求无法处理，请保留输入并重试。',
    REQUEST_TOO_LARGE: '提交内容过大，请减少内容后重试。',
    ACCESS_DENIED: '当前无法访问本地服务，请检查连接配置。',
    VALIDATION_ERROR: '请检查标记的字段后重试。',
    NOT_FOUND: '这条记录已不存在。',
    REVISION_CONFLICT: '这条记录已在其他页面发生修改。',
    REQUEST_CONFLICT: '这次请求与之前的内容不一致，请先检查已保存记录。',
    ORIGINAL_ENTRY_DELETED: '这次添加对应的原记录已被删除，不会自动重新创建。',
    REVISION_EXHAUSTED: '这条记录无法继续保存新的修改。',
    STORAGE_UNAVAILABLE: '暂时无法完成操作，本次操作未生效。请稍后重试。',
  };
  return messages[error.code] ?? '暂时无法读取当前记录，请稍后重试。';
}
export function fieldErrorMessage(error: FieldError): string {
  const messages: Record<FieldError['code'], string> = {
    REQUIRED: '请填写此项',
    UNKNOWN_FIELD: '请求包含不支持的字段',
    INVALID_TYPE: '内容类型不正确',
    BLANK_VALUE: '请填写此项',
    TOO_LONG: '内容过长，请缩短后重试',
    INVALID_CHARACTERS: '内容包含不允许的字符',
    INVALID_FORMAT:
      error.field === 'application_url'
        ? '请输入有效的 HTTP 或 HTTPS 链接'
        : '内容格式不正确',
    OUT_OF_RANGE: '内容超出允许范围',
  };
  return messages[error.code];
}

function validErrorField(field: string, scope: 'entry' | 'preferences') {
  if (scope === 'entry')
    return [
      '$',
      'company_name',
      'role_title',
      'application_url',
      'revision',
      'request_id',
      'manual_application_entry_id',
    ].includes(field);
  return /^(?:\$|request_id|revision|preference_set_version_id|configuration(?:\.(?:target_job_keywords(?:\[(?:0|[1-9][0-9]*)\])?|(?:accepted_cities|recruitment_types|excluded_companies)(?:\.(?:mode|value(?:\[(?:0|[1-9][0-9]*)\])?))?|(?:minimum_salary|max_required_education)(?:\.(?:mode|value))?))?)$/.test(
    field,
  );
}
