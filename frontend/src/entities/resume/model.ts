import { z } from 'zod';
import type { components } from '@/shared/api/schema';
import {
  uuid,
  revision,
  timestamp,
  shortText,
  bodyText,
} from '@/shared/lib/candidate-values';
import { controls, trimOuterWhitespace } from '@/shared/lib/unicode-text';
import { kinds, type EvidenceContent } from '@/entities/evidence/model';
import { httpUrlIssue } from '@/shared/lib/http-url';
export type ResumePair = components['schemas']['ResumePair'];
export type ResumeVersion = components['schemas']['ResumeVersion'];
export type Resume = components['schemas']['Resume'];
export type ResumeList = components['schemas']['ResumeList'];
export type ResumeDocument = Omit<
  components['schemas']['ResumeSave'],
  'request_id' | 'revision'
>;
export type LocalContent =
  components['schemas']['ResumeMember-Input']['content'];
export type TextRun = components['schemas']['TextRun-Input'];
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
const mark = z.union([
  z.strictObject({ type: z.enum(['BOLD', 'ITALIC', 'UNDERLINE']) }),
  z.strictObject({
    type: z.literal('LINK'),
    url: z
      .string()
      .refine((v) => !httpUrlIssue(v), '请输入有效的 HTTP 或 HTTPS 链接'),
  }),
]);
const run = z
  .strictObject({ text: z.string().min(1), marks: z.array(mark).max(4) })
  .superRefine((v, c) => {
    const textResult = bodyText.safeParse(v.text);
    if (!textResult.success && trimOuterWhitespace(v.text))
      for (const issue of textResult.error.issues)
        c.addIssue({ code: 'custom', path: ['text'], message: issue.message });
    if (controls.test(v.text) || /[\ud800-\udfff]/u.test(v.text))
      c.addIssue({
        code: 'custom',
        path: ['text'],
        message: '内容包含无效字符',
      });
    if (!trimOuterWhitespace(v.text) && v.marks.length)
      c.addIssue({
        code: 'custom',
        path: ['marks'],
        message: '空白文字不能添加格式',
      });
    if (new Set(v.marks.map((m) => m.type)).size !== v.marks.length)
      c.addIssue({ code: 'custom', path: ['marks'], message: '格式不能重复' });
  });
const runs = z
  .array(run)
  .min(1)
  .superRefine((v, c) => {
    const text = v.map((r) => r.text).join('');
    if (!trimOuterWhitespace(text) || [...text].length > 10000)
      c.addIssue({
        code: 'custom',
        message: '每段需为非空内容，最多 10000 个字符',
      });
    let count = 0,
      previous = '';
    for (const r of v) {
      const key = JSON.stringify(
        [...r.marks].sort((a, b) => a.type.localeCompare(b.type)),
      );
      if (key !== previous || !count) count++;
      previous = key;
    }
    if (count > 256)
      c.addIssue({ code: 'custom', message: '每段文字格式片段过多' });
  });
export const localContent = z
  .array(
    z.union([
      z.strictObject({ type: z.literal('PARAGRAPH'), runs }),
      z.strictObject({
        type: z.enum(['ORDERED_LIST', 'UNORDERED_LIST']),
        items: z.array(z.strictObject({ runs })).min(1).max(100),
      }),
    ]),
  )
  .max(100)
  .refine((v) => contentLength(v) <= 50000, '单条经历内容最多 50000 个字符');
export function contentLength(content: LocalContent) {
  return content.reduce(
    (n, b) =>
      n +
      (b.type === 'PARAGRAPH' ? [b.runs] : b.items.map((i) => i.runs))
        .flat()
        .reduce((sum, r) => sum + [...r.text].length, 0),
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
  .refine((v) => v.line_spacing_pt >= v.font_size_pt + 2, {
    path: ['line_spacing_pt'],
    message: '行高至少比字号大 2 磅',
  });
export const resumeDocument = z
  .strictObject({
    profile_version_id: uuid,
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
          (v) => new Set(v.map((i) => i.kind)).size === v.length,
          '附加信息不能重复',
        ),
    }),
    sections: z
      .array(
        z.strictObject({
          kind: z.enum(kinds),
          members: z
            .array(
              z.strictObject({
                evidence_item_id: uuid,
                evidence_item_version_id: uuid,
                content: localContent,
              }),
            )
            .min(1),
        }),
      )
      .max(6),
    document_presentation: presentation,
  })
  .superRefine((v, c) => {
    if (new Set(v.sections.map((s) => s.kind)).size !== v.sections.length)
      c.addIssue({
        code: 'custom',
        path: ['sections'],
        message: '经历分类不能重复',
      });
    const members = v.sections.flatMap((s) => s.members);
    if (
      new Set(members.map((m) => m.evidence_item_id)).size !== members.length ||
      members.length > 100
    )
      c.addIssue({
        code: 'custom',
        path: ['sections'],
        message: '最多 100 条经历，同一资料不能重复添加',
      });
    if (members.reduce((n, m) => n + contentLength(m.content), 0) > 200000)
      c.addIssue({
        code: 'custom',
        path: ['sections'],
        message: '简历总内容过长',
      });
  });
export const resumeRoot = z.strictObject({
  resume_id: uuid,
  resume_name: shortText(120),
  status: z.enum(['ACTIVE', 'REMOVED']),
  current_resume_version_id: uuid,
  revision,
  created_at: timestamp,
  updated_at: timestamp,
});
export const resumeVersion = resumeDocument.safeExtend({
  resume_version_id: uuid,
  resume_id: uuid,
  schema_version: z.literal(1),
  created_at: timestamp,
});
const same = (v: ResumePair) =>
  v.resume.resume_id === v.resume_version.resume_id &&
  v.resume.current_resume_version_id === v.resume_version.resume_version_id;
export const resumePair = z
  .strictObject({ resume: resumeRoot, resume_version: resumeVersion })
  .refine(same);
export const defaultSelection = z.strictObject({
  default_resume_id: uuid.nullable(),
  revision,
});
export const resumeList = z
  .strictObject({
    resumes: z.array(resumeRoot),
    default_resume_selection: defaultSelection,
  })
  .refine(
    (v) =>
      v.resumes.every((r) => r.status === 'ACTIVE') &&
      (v.resumes.length
        ? v.resumes.some(
            (r) => r.resume_id === v.default_resume_selection.default_resume_id,
          )
        : v.default_resume_selection.default_resume_id === null),
  );
export const resumeResult = z
  .strictObject({
    resume: resumeRoot,
    resume_version: resumeVersion,
    request_id: uuid,
    outcome: z.enum(['UPDATED', 'UNCHANGED']),
  })
  .refine(same);
export const resumeSelectionResult = z
  .strictObject({
    resume: resumeRoot,
    resume_version: resumeVersion,
    request_id: uuid,
    outcome: z.enum(['CREATED', 'REMOVED', 'UNCHANGED']),
    default_resume_selection: defaultSelection,
  })
  .refine(same);
export const selectionResult = z.strictObject({
  request_id: uuid,
  outcome: z.enum(['UPDATED', 'UNCHANGED']),
  default_resume_selection: defaultSelection,
});
export function initializeContent(content: EvidenceContent): LocalContent {
  return content.map((b) =>
    b.type === 'PARAGRAPH'
      ? { type: b.type, runs: [{ text: b.text, marks: [] }] }
      : {
          type: b.type,
          items: b.items.map((text) => ({ runs: [{ text, marks: [] }] })),
        },
  );
}
export function documentFromVersion(v: ResumeVersion): ResumeDocument {
  return structuredClone({
    profile_version_id: v.profile_version_id,
    header_presentation: v.header_presentation,
    sections: v.sections,
    document_presentation: v.document_presentation,
  });
}
