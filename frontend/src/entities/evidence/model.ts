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
export const kinds = [
  'WORK_EXPERIENCE',
  'PROJECT',
  'EDUCATION',
  'SKILL',
  'AWARD',
  'CERTIFICATION',
] as const;
export type EvidenceKind = (typeof kinds)[number];
export const kindLabels: Record<EvidenceKind, string> = {
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
export const evidenceContent = z
  .array(
    z.union([
      z.strictObject({ type: z.literal('PARAGRAPH'), text: bodyText }),
      z.strictObject({
        type: z.enum(['ORDERED_LIST', 'UNORDERED_LIST']),
        items: z.array(bodyText).min(1).max(100),
      }),
    ]),
  )
  .max(100)
  .refine(
    (blocks) =>
      blocks.reduce(
        (n, b) =>
          n +
          (b.type === 'PARAGRAPH' ? [b.text] : b.items).reduce(
            (m, t) => m + [...t].length,
            0,
          ),
        0,
      ) <= 50000,
    '内容总长最多 50000 个字符',
  );
export function evidenceValues(kind: EvidenceKind) {
  return z
    .strictObject({ fields: fieldsByKind[kind], content: evidenceContent })
    .superRefine((v, c) => {
      if (
        'start_month' in v.fields &&
        v.fields.start_month &&
        v.fields.end_month &&
        v.fields.start_month > v.fields.end_month
      )
        c.addIssue({
          code: 'custom',
          path: ['fields', 'end_month'],
          message: '结束时间不能早于开始时间',
        });
    });
}
export type EvidencePair = components['schemas']['EvidencePair'];
export type EvidenceVersion = components['schemas']['EvidenceVersion'];
export type EvidenceProjection = components['schemas']['EvidenceProjection'];
export type EvidenceContent = EvidenceVersion['content'];
export type EvidenceFields = EvidenceVersion['fields'];
const fieldUnion = z.union(
  Object.values(fieldsByKind) as [
    typeof fieldsByKind.EDUCATION,
    ...(typeof fieldsByKind)[keyof typeof fieldsByKind][],
  ],
);
export const evidenceRoot = z.strictObject({
  evidence_item_id: uuid,
  kind: z.enum(kinds),
  status: z.enum(['ACTIVE', 'RETIRED']),
  current_evidence_item_version_id: uuid,
  revision,
  created_at: timestamp,
  updated_at: timestamp,
});
export const evidenceVersion = z.strictObject({
  evidence_item_version_id: uuid,
  evidence_item_id: uuid,
  schema_version: z.literal(1),
  fields: fieldUnion,
  content: evidenceContent,
  created_at: timestamp,
});
const validPair = (v: EvidencePair) =>
  v.evidence_item.evidence_item_id ===
    v.evidence_item_version.evidence_item_id &&
  v.evidence_item.current_evidence_item_version_id ===
    v.evidence_item_version.evidence_item_version_id &&
  evidenceValues(v.evidence_item.kind).safeParse({
    fields: v.evidence_item_version.fields,
    content: v.evidence_item_version.content,
  }).success;
export const evidencePair = z
  .strictObject({
    evidence_item: evidenceRoot,
    evidence_item_version: evidenceVersion,
  })
  .refine(validPair);
export const evidenceResult = z
  .strictObject({
    evidence_item: evidenceRoot,
    evidence_item_version: evidenceVersion,
    request_id: uuid,
    outcome: z.enum(['CREATED', 'UPDATED', 'RETIRED', 'UNCHANGED']),
    evidence_baseline_snapshot_id: uuid,
  })
  .refine(validPair);
export const evidenceList = z.strictObject({
  evidence_items: z.array(
    z
      .strictObject({
        evidence_item: evidenceRoot,
        current_evidence_item_version_id: uuid,
        fields: fieldUnion,
      })
      .refine(
        (v) =>
          v.evidence_item.status === 'ACTIVE' &&
          v.evidence_item.current_evidence_item_version_id ===
            v.current_evidence_item_version_id &&
          fieldsByKind[v.evidence_item.kind].safeParse(v.fields).success,
      ),
  ),
});
export const evidenceExact = z
  .strictObject({ kind: z.enum(kinds), evidence_item_version: evidenceVersion })
  .refine(
    (v) =>
      evidenceValues(v.kind).safeParse({
        fields: v.evidence_item_version.fields,
        content: v.evidence_item_version.content,
      }).success,
  );
export function evidenceName(fields: EvidenceFields): string {
  return (
    Object.entries(fields).find(([k]) =>
      [
        'company_name',
        'project_name',
        'school_name',
        'skill_name',
        'award_name',
        'certification_name',
      ].includes(k),
    )?.[1] ?? ''
  );
}
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
export function emptyFields(kind: EvidenceKind): Record<string, string | null> {
  return Object.fromEntries(
    Object.entries(fieldsByKind[kind].shape).map(([k, v]) => [
      k,
      v.isNullable() ? null : '',
    ]),
  );
}
