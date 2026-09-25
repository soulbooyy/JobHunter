import { z } from 'zod';
import type { components } from '@/shared/api/schema';
import {
  shortText,
  bodyText,
  month,
  uuid,
  revision,
  timestamp,
} from '@/shared/lib/candidate-values';
import { httpUrlIssue } from '@/shared/lib/http-url';
import { controls, trimOuterWhitespace } from '@/shared/lib/unicode-text';

export const kinds = [
  'WORK_EXPERIENCE',
  'PROJECT',
  'EDUCATION',
  'SKILL',
  'AWARD',
  'CERTIFICATION',
] as const;
export type ResumeKind = (typeof kinds)[number];
export const kindLabels: Record<ResumeKind, string> = {
  WORK_EXPERIENCE: '工作经历',
  PROJECT: '项目经历',
  EDUCATION: '教育经历',
  SKILL: '技能',
  AWARD: '奖项',
  CERTIFICATION: '证书',
};
export const degrees = {
  SECONDARY_VOCATIONAL: '中专',
  HIGH_SCHOOL: '高中',
  ASSOCIATE: '大专',
  BACHELOR: '本科',
  MASTER: '硕士',
  MBA: 'MBA',
  DOCTORATE: '博士',
} as const;
const period = { start_month: month, end_month: month };
export const fieldsByKind = {
  EDUCATION: z.strictObject({
    school_name: shortText(),
    degree: z.enum(
      Object.keys(degrees) as [
        keyof typeof degrees,
        ...(keyof typeof degrees)[],
      ],
    ),
    major: shortText().nullable(),
    ...period,
  }),
  WORK_EXPERIENCE: z.strictObject({
    company_name: shortText(),
    role_title: shortText(),
    ...period,
  }),
  PROJECT: z.strictObject({
    project_name: shortText(),
    role_title: shortText().nullable(),
    project_url: z
      .string()
      .refine((v) => !httpUrlIssue(v), '请输入有效的 HTTP 或 HTTPS 链接')
      .nullable(),
    ...period,
  }),
  SKILL: z.strictObject({ skill_name: shortText() }),
  AWARD: z.strictObject({
    award_name: shortText(),
    awarding_organization: shortText().nullable(),
    awarded_month: month,
  }),
  CERTIFICATION: z.strictObject({
    certification_name: shortText(),
    issuing_organization: shortText().nullable(),
    issued_month: month,
  }),
};
export const fieldLabels: Record<string, string> = {
  company_name: '公司名称',
  role_title: '担任角色',
  project_name: '项目名称',
  project_url: '项目链接',
  school_name: '学校名称',
  degree: '学历',
  major: '专业',
  skill_name: '技能名称',
  award_name: '奖项名称',
  awarding_organization: '颁发机构',
  certification_name: '证书名称',
  issuing_organization: '颁发机构',
  start_month: '开始时间',
  end_month: '结束时间',
  awarded_month: '获奖时间',
  issued_month: '取得时间',
};
export function emptyFields(kind: ResumeKind): Record<string, string | null> {
  return Object.fromEntries(
    Object.entries(fieldsByKind[kind].shape).map(([key, schema]) => [
      key,
      schema.isNullable() ? null : key === 'degree' ? 'BACHELOR' : '',
    ]),
  );
}
export function entryName(fields: Record<string, unknown>): string {
  return String(
    Object.entries(fields).find(([key]) =>
      [
        'company_name',
        'project_name',
        'school_name',
        'skill_name',
        'award_name',
        'certification_name',
      ].includes(key),
    )?.[1] ?? '',
  );
}

export const headerLabels = {
  JOB_SEARCH_STATUS: '求职状态',
  JOB_INTENTION: '求职意向',
  EXPECTED_POSITION: '期望职位',
  EXPECTED_CITY: '期望城市',
  EXPECTED_SALARY: '期望薪资',
  HIGHEST_EDUCATION: '最高学历',
  GENDER: '性别',
  POLITICAL_AFFILIATION: '政治面貌',
  YEARS_OF_EXPERIENCE: '工作年限',
} as const;
export const fonts = {
  SOURCE_HAN_SANS: '思源黑体',
  HEITI: '黑体',
  SONGTI: '宋体',
  KAITI: '楷体',
} as const;
export const defaultPresentation = {
  font_family: 'SOURCE_HAN_SANS' as const,
  font_size_pt: 12,
  line_spacing_pt: 18,
  theme_color: '#1F2937',
};

const phone = z
  .string()
  .superRefine((raw, ctx) => {
    const value = trimOuterWhitespace(raw);
    if (
      !value ||
      [...value].length > 50 ||
      controls.test(value) ||
      !/^\+?[0-9 ()-]+$/.test(value) ||
      !/[0-9]/.test(value)
    )
      ctx.addIssue({ code: 'custom', message: '请输入有效电话号码' });
  })
  .nullable();
const email = z
  .string()
  .superRefine((value, ctx) => {
    if (
      !value ||
      [...value].length > 254 ||
      /\s/u.test(value) ||
      value.split('@').length !== 2 ||
      value.startsWith('@') ||
      value.endsWith('@')
    )
      ctx.addIssue({ code: 'custom', message: '请输入有效邮箱' });
  })
  .nullable();
export const contacts = z.strictObject({
  full_name: shortText(100).nullable(),
  phone_number: phone,
  email,
});

export type TextMark =
  { type: 'BOLD' | 'ITALIC' | 'UNDERLINE' } | { type: 'LINK'; url: string };
export type TextRun = { text: string; marks: TextMark[] };
export type LocalContent = Array<
  | { type: 'PARAGRAPH'; block_id: string; runs: TextRun[] }
  | {
      type: 'ORDERED_LIST' | 'UNORDERED_LIST';
      items: Array<{ block_id: string; runs: TextRun[] }>;
    }
>;
const mark = z.discriminatedUnion('type', [
  z.strictObject({ type: z.enum(['BOLD', 'ITALIC', 'UNDERLINE']) }),
  z.strictObject({
    type: z.literal('LINK'),
    url: z
      .string()
      .refine(
        (value) => !httpUrlIssue(value),
        '请输入有效的 HTTP 或 HTTPS 链接',
      ),
  }),
]);
const run = z
  .strictObject({ text: z.string().min(1), marks: z.array(mark).max(4) })
  .superRefine((value, context) => {
    const result = bodyText.safeParse(value.text);
    if (!result.success && trimOuterWhitespace(value.text))
      for (const issue of result.error.issues)
        context.addIssue({
          code: 'custom',
          path: ['text'],
          message: issue.message,
        });
    if (controls.test(value.text) || /[\ud800-\udfff]/u.test(value.text))
      context.addIssue({
        code: 'custom',
        path: ['text'],
        message: '内容包含无效字符',
      });
    if (!trimOuterWhitespace(value.text) && value.marks.length)
      context.addIssue({
        code: 'custom',
        path: ['marks'],
        message: '空白文字不能添加格式',
      });
    if (
      new Set(value.marks.map((item) => item.type)).size !== value.marks.length
    )
      context.addIssue({
        code: 'custom',
        path: ['marks'],
        message: '格式不能重复',
      });
  });
const runs = z
  .array(run)
  .min(1)
  .superRefine((value, context) => {
    const text = value.map((item) => item.text).join('');
    if (!trimOuterWhitespace(text) || [...text].length > 10000)
      context.addIssue({
        code: 'custom',
        message: '每段需为非空内容，最多 10000 个字符',
      });
    let canonicalFragments = 0;
    let previous = '';
    for (const item of value) {
      const key = JSON.stringify(
        [...item.marks].sort((a, b) => a.type.localeCompare(b.type)),
      );
      if (!canonicalFragments || key !== previous) canonicalFragments += 1;
      previous = key;
    }
    if (canonicalFragments > 256)
      context.addIssue({
        code: 'custom',
        message: '每段文字格式片段最多 256 个',
      });
  });
const paragraph = z.strictObject({
  type: z.literal('PARAGRAPH'),
  block_id: uuid,
  runs,
});
const listItem = z.strictObject({ block_id: uuid, runs });
export const localContent = z
  .array(
    z.union([
      paragraph,
      z.strictObject({
        type: z.enum(['ORDERED_LIST', 'UNORDERED_LIST']),
        items: z.array(listItem).min(1).max(100),
      }),
    ]),
  )
  .max(100)
  .refine(
    (value) => contentLength(value as LocalContent) <= 50000,
    '单条经历内容最多 50000 个字符',
  ) as unknown as z.ZodType<LocalContent>;
export function contentLength(content: LocalContent) {
  return content.reduce(
    (total, block) =>
      total +
      (block.type === 'PARAGRAPH'
        ? [block.runs]
        : block.items.map((item) => item.runs)
      )
        .flat()
        .reduce((sum, item) => sum + [...item.text].length, 0),
    0,
  );
}
export const presentation = z
  .strictObject({
    font_family: z.enum(
      Object.keys(fonts) as [keyof typeof fonts, ...(keyof typeof fonts)[]],
    ),
    font_size_pt: z.number().min(12).max(20).multipleOf(0.5),
    line_spacing_pt: z.number().min(14).max(30).multipleOf(0.5),
    theme_color: z.string().regex(/^#[0-9a-fA-F]{6}$/),
  })
  .refine((value) => value.line_spacing_pt >= value.font_size_pt + 2, {
    path: ['line_spacing_pt'],
    message: '行高至少比字号大 2 磅',
  });
const fieldUnion = z.union(
  Object.values(fieldsByKind) as [
    typeof fieldsByKind.EDUCATION,
    ...(typeof fieldsByKind)[keyof typeof fieldsByKind][],
  ],
);
const resumeEntry = z.strictObject({
  entry_id: uuid,
  fields: fieldUnion,
  content: localContent,
});
export const resumeDocument = z
  .strictObject({
    contacts,
    header_presentation: z.strictObject({
      optional_items: z
        .array(
          z.strictObject({
            kind: z.enum(
              Object.keys(headerLabels) as [
                keyof typeof headerLabels,
                ...(keyof typeof headerLabels)[],
              ],
            ),
            value: shortText(),
          }),
        )
        .max(9)
        .refine(
          (value) =>
            new Set(value.map((item) => item.kind)).size === value.length,
          '附加信息不能重复',
        ),
    }),
    sections: z
      .array(
        z.strictObject({
          kind: z.enum(kinds),
          members: z.array(resumeEntry).min(1).max(100),
        }),
      )
      .max(6),
    document_presentation: presentation,
  })
  .superRefine((value, context) => {
    if (
      new Set(value.sections.map((section) => section.kind)).size !==
      value.sections.length
    )
      context.addIssue({
        code: 'custom',
        path: ['sections'],
        message: '经历分类不能重复',
      });
    const entries = value.sections.flatMap((section) => section.members);
    const entryIds = entries.map((entry) => entry.entry_id);
    const blockIds = entries.flatMap((entry) =>
      entry.content.flatMap((block) =>
        block.type === 'PARAGRAPH'
          ? [block.block_id]
          : block.items.map((item) => item.block_id),
      ),
    );
    if (
      new Set(entryIds).size !== entryIds.length ||
      new Set(blockIds).size !== blockIds.length
    )
      context.addIssue({
        code: 'custom',
        path: ['sections'],
        message: '经历或段落标识不能重复',
      });
    if (
      entries.length > 100 ||
      entries.reduce((sum, entry) => sum + contentLength(entry.content), 0) >
        200000
    )
      context.addIssue({
        code: 'custom',
        path: ['sections'],
        message: '简历内容超出允许范围',
      });
    value.sections.forEach((section, sectionIndex) =>
      section.members.forEach((entry, entryIndex) => {
        if (!fieldsByKind[section.kind].safeParse(entry.fields).success)
          context.addIssue({
            code: 'custom',
            path: ['sections', sectionIndex, 'members', entryIndex, 'fields'],
            message: '经历字段与分类不匹配',
          });
        if (
          'start_month' in entry.fields &&
          'end_month' in entry.fields &&
          entry.fields.start_month &&
          entry.fields.end_month &&
          entry.fields.start_month > entry.fields.end_month
        ) {
          context.addIssue({
            code: 'custom',
            path: [
              'sections',
              sectionIndex,
              'members',
              entryIndex,
              'fields',
              'end_month',
            ],
            message: '结束时间不能早于开始时间',
          });
        }
      }),
    );
  });

export type ResumeDocument = z.infer<typeof resumeDocument>;
export type ResumeEntry = ResumeDocument['sections'][number]['members'][number];
export type Resume = components['schemas']['Resume'];
export type ResumeVersion = components['schemas']['ResumeVersion'];
export type ResumePair = components['schemas']['ResumePair'];
export type ResumeList = components['schemas']['ResumeList'];
export const resumeRoot = z.strictObject({
  resume_id: uuid,
  resume_name: shortText(120),
  status: z.enum(['ACTIVE', 'REMOVED']),
  current_resume_version_id: uuid,
  revision,
  created_at: timestamp,
  updated_at: timestamp,
});
export const defaultSelection = z.strictObject({
  default_resume_id: uuid.nullable(),
  revision,
});
export const resumeVersion = resumeDocument.safeExtend({
  resume_version_id: uuid,
  resume_id: uuid,
  schema_version: z.literal(2),
  created_at: timestamp,
});
const exactPair = (value: ResumePair) =>
  value.resume.resume_id === value.resume_version.resume_id &&
  value.resume.current_resume_version_id ===
    value.resume_version.resume_version_id;
export const resumePair = z
  .strictObject({ resume: resumeRoot, resume_version: resumeVersion })
  .refine(exactPair);
export const resumeList = z
  .strictObject({
    resumes: z.array(resumeRoot),
    default_resume_selection: defaultSelection,
  })
  .refine(
    (value) =>
      value.resumes.every((resume) => resume.status === 'ACTIVE') &&
      (value.default_resume_selection.default_resume_id === null
        ? value.resumes.length === 0
        : value.resumes.some(
            (resume) =>
              resume.resume_id ===
              value.default_resume_selection.default_resume_id,
          )),
  );
export const resumeResult = z
  .strictObject({
    resume: resumeRoot,
    resume_version: resumeVersion,
    request_id: uuid,
    outcome: z.enum(['UPDATED', 'UNCHANGED']),
  })
  .refine(exactPair);
export const resumeSelectionResult = z
  .strictObject({
    resume: resumeRoot,
    resume_version: resumeVersion,
    request_id: uuid,
    outcome: z.enum(['CREATED', 'REMOVED', 'UNCHANGED']),
    default_resume_selection: defaultSelection,
  })
  .refine(exactPair);
export const selectionResult = z.strictObject({
  request_id: uuid,
  outcome: z.enum(['UPDATED', 'UNCHANGED']),
  default_resume_selection: defaultSelection,
});

export function documentFromVersion(version: ResumeVersion): ResumeDocument {
  return structuredClone({
    contacts: version.contacts,
    header_presentation: version.header_presentation,
    sections: version.sections,
    document_presentation: version.document_presentation,
  }) as ResumeDocument;
}
export function newResumeEntry(kind: ResumeKind): ResumeEntry {
  return {
    entry_id: crypto.randomUUID(),
    fields: emptyFields(kind),
    content: [],
  } as unknown as ResumeEntry;
}
export function copyContent(content: LocalContent): LocalContent {
  return content.map((block) =>
    block.type === 'PARAGRAPH'
      ? { ...structuredClone(block), block_id: crypto.randomUUID() }
      : {
          ...structuredClone(block),
          items: block.items.map((item) => ({
            ...item,
            block_id: crypto.randomUUID(),
          })),
        },
  );
}
export function copyResumeEntry(entry: ResumeEntry): ResumeEntry {
  return {
    entry_id: crypto.randomUUID(),
    fields: structuredClone(entry.fields),
    content: copyContent(entry.content),
  } as ResumeEntry;
}
