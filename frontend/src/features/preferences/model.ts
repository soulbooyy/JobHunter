import { z } from 'zod';
import type { components } from '@/shared/api/schema';
import { trimOuterWhitespace, controls } from '@/shared/lib/unicode-text';
export const recruitmentLabels = {
  CAMPUS: '校招',
  INTERNSHIP: '实习',
  EXPERIENCED: '社招',
  PART_TIME: '兼职',
} as const;
export const educationLabels = {
  JUNIOR_HIGH_OR_BELOW: '初中及以下',
  UPPER_SECONDARY: '高中 / 中职',
  ASSOCIATE: '大专',
  BACHELOR: '本科',
  MASTER: '硕士',
  DOCTORATE: '博士',
} as const;
export type Recruitment = keyof typeof recruitmentLabels;
export type Education = keyof typeof educationLabels;
export const fieldLabels = {
  target_job_keywords: '目标岗位关键词',
  accepted_cities: '接受城市',
  minimum_salary: '最低月薪',
  recruitment_types: '招聘类型',
  excluded_companies: '排除公司',
  max_required_education: '最高学历要求',
} as const;
export type PreferenceField = keyof typeof fieldLabels;
export type TagField =
  'target_job_keywords' | 'accepted_cities' | 'excluded_companies';
export type Configuration = components['schemas']['Configuration-Input'];
export type SavePreferences = components['schemas']['SavePreferences'];
export type SaveResult = components['schemas']['SaveResult'];
export type CurrentPreferences =
  components['schemas']['Configured'] | components['schemas']['NotConfigured'];
export function textIssue(raw: string, max: number): string | undefined {
  if (/[\ud800-\udfff]/u.test(raw)) return '内容包含无效字符';
  const value = trimOuterWhitespace(raw);
  if (!value) return '请输入内容';
  if (controls.test(value)) return '请使用不含控制字符的单行文本';
  if ([...value].length > max) return `每项最多 ${max} 个字符`;
}
const text = (max: number) =>
  z.string().superRefine((value, ctx) => {
    const message = textIssue(value, max);
    if (message) ctx.addIssue({ code: 'custom', message });
  });
const textSet = (max: number, length: number) =>
  z
    .array(text(length))
    .min(1, '请至少添加一项')
    .max(1000, '提交项数过多')
    .superRefine((values, ctx) => {
      if (new Set(values.map(trimOuterWhitespace)).size > max)
        ctx.addIssue({ code: 'custom', message: `最多添加 ${max} 项` });
    });
const unlimited = z.strictObject({ mode: z.literal('UNLIMITED') });
const choice = <T extends z.ZodType>(value: T) =>
  z.discriminatedUnion('mode', [
    unlimited,
    z.strictObject({ mode: z.literal('LIMITED'), value }),
  ]);
export const configurationSchema = z.strictObject({
  target_job_keywords: textSet(20, 100),
  accepted_cities: choice(textSet(50, 100)),
  minimum_salary: choice(
    z
      .number({ error: '请输入 1–300000 之间的整数' })
      .int('请输入 1–300000 之间的整数')
      .min(1, '请输入 1–300000 之间的整数')
      .max(300000, '请输入 1–300000 之间的整数'),
  ),
  recruitment_types: choice(
    z
      .array(z.enum(['CAMPUS', 'INTERNSHIP', 'EXPERIENCED', 'PART_TIME']))
      .min(1, '请至少选择一种招聘类型')
      .max(1000),
  ),
  excluded_companies: choice(textSet(200, 200)),
  max_required_education: choice(
    z.enum(
      [
        'JUNIOR_HIGH_OR_BELOW',
        'UPPER_SECONDARY',
        'ASSOCIATE',
        'BACHELOR',
        'MASTER',
        'DOCTORATE',
      ],
      { error: '请选择最高学历要求' },
    ),
  ),
});
const uuid = z.uuidv4().regex(/^[0-9a-f-]+$/);
const timestamp = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/);
const revision = z.number().int().min(1).max(Number.MAX_SAFE_INTEGER);
export const versionSchema = z.strictObject({
  preference_set_version_id: uuid,
  preference_set_id: uuid,
  created_at: timestamp,
  configuration: configurationSchema,
});
export const currentSchema = z
  .discriminatedUnion('status', [
    z.strictObject({ status: z.literal('NOT_CONFIGURED') }),
    z.strictObject({
      status: z.literal('CONFIGURED'),
      preference_set: z.strictObject({
        preference_set_id: uuid,
        current_preference_set_version_id: uuid,
        revision,
        created_at: timestamp,
        updated_at: timestamp,
      }),
      current_preference_set_version: versionSchema,
    }),
  ])
  .superRefine((current, ctx) => {
    if (
      current.status === 'CONFIGURED' &&
      (current.preference_set.preference_set_id !==
        current.current_preference_set_version.preference_set_id ||
        current.preference_set.current_preference_set_version_id !==
          current.current_preference_set_version.preference_set_version_id)
    )
      ctx.addIssue({
        code: 'custom',
        message: 'Inconsistent current reference',
      });
  });
export const saveResultSchema = z.strictObject({
  preference_set_id: uuid,
  preference_set_version_id: uuid,
  revision,
  outcome: z.enum(['CREATED', 'UPDATED', 'UNCHANGED']),
});
export interface PreferenceDraft {
  target_job_keywords: string[];
  accepted_cities: string[];
  excluded_companies: string[];
  salary: string;
  recruitment_types: Recruitment[];
  education: Education | '';
  unlimited: Record<Exclude<PreferenceField, 'target_job_keywords'>, boolean>;
  pending: Record<TagField, string>;
}
export function draftFromCurrent(current: CurrentPreferences): PreferenceDraft {
  const c =
    current.status === 'CONFIGURED'
      ? current.current_preference_set_version.configuration
      : undefined;
  return {
    target_job_keywords: c ? [...c.target_job_keywords] : [],
    accepted_cities:
      c?.accepted_cities.mode === 'LIMITED' ? [...c.accepted_cities.value] : [],
    excluded_companies:
      c?.excluded_companies.mode === 'LIMITED'
        ? [...c.excluded_companies.value]
        : [],
    salary:
      c?.minimum_salary.mode === 'LIMITED'
        ? String(c.minimum_salary.value)
        : '',
    recruitment_types:
      c?.recruitment_types.mode === 'LIMITED'
        ? [...c.recruitment_types.value]
        : [],
    education:
      c?.max_required_education.mode === 'LIMITED'
        ? c.max_required_education.value
        : '',
    unlimited: {
      accepted_cities: c?.accepted_cities.mode === 'UNLIMITED',
      minimum_salary: c?.minimum_salary.mode === 'UNLIMITED',
      recruitment_types: c?.recruitment_types.mode === 'UNLIMITED',
      excluded_companies: !c || c.excluded_companies.mode === 'UNLIMITED',
      max_required_education: c?.max_required_education.mode === 'UNLIMITED',
    },
    pending: {
      target_job_keywords: '',
      accepted_cities: '',
      excluded_companies: '',
    },
  };
}
export function configurationFromDraft(draft: PreferenceDraft) {
  const choiceValue = <T>(
    key: Exclude<PreferenceField, 'target_job_keywords'>,
    value: T,
  ) =>
    draft.unlimited[key]
      ? { mode: 'UNLIMITED' as const }
      : { mode: 'LIMITED' as const, value };
  return {
    target_job_keywords: draft.target_job_keywords,
    accepted_cities: choiceValue('accepted_cities', draft.accepted_cities),
    minimum_salary: choiceValue(
      'minimum_salary',
      /^[0-9]+$/.test(draft.salary) ? Number(draft.salary) : NaN,
    ),
    recruitment_types: choiceValue(
      'recruitment_types',
      draft.recruitment_types,
    ),
    excluded_companies: choiceValue(
      'excluded_companies',
      draft.excluded_companies,
    ),
    max_required_education: choiceValue(
      'max_required_education',
      draft.education,
    ),
  };
}
