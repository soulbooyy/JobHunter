import { z } from 'zod';
import type { components } from '@/shared/api/schema';
import { uuid, revision, timestamp } from '@/shared/lib/candidate-values';
import { controls, trimOuterWhitespace } from '@/shared/lib/unicode-text';

const scalarText = z.string().superRefine((value, context) => {
  if (
    !trimOuterWhitespace(value) ||
    controls.test(value) ||
    /[\ud800-\udfff]/u.test(value)
  )
    context.addIssue({ code: 'custom', message: '画像文字格式无效' });
});

const selection = z.strictObject({
  default_resume_id: uuid.nullable(),
  revision,
});
const state = z
  .strictObject({
    default_resume_selection: selection,
    source_resume_version_id: uuid.nullable(),
    status: z.enum([
      'NO_SOURCE',
      'EMPTY_SOURCE',
      'QUEUED',
      'RUNNING',
      'READY',
      'FAILED',
    ]),
    build_id: uuid.nullable(),
    portrait_id: uuid.nullable(),
    failure_code: z
      .enum([
        'SOURCE_UNAVAILABLE',
        'CONFIGURATION_UNAVAILABLE',
        'INPUT_NOT_ADMITTED',
        'OUTPUT_INVALID',
        'INVOCATION_FAILED',
        'OUTCOME_UNKNOWN',
      ])
      .nullable(),
  })
  .superRefine((value, context) => {
    const valid =
      (value.status === 'NO_SOURCE' &&
        !value.default_resume_selection.default_resume_id &&
        !value.source_resume_version_id &&
        !value.build_id &&
        !value.portrait_id &&
        !value.failure_code) ||
      (value.status === 'EMPTY_SOURCE' &&
        !!value.default_resume_selection.default_resume_id &&
        !!value.source_resume_version_id &&
        !value.build_id &&
        !value.portrait_id &&
        !value.failure_code) ||
      ((value.status === 'QUEUED' || value.status === 'RUNNING') &&
        !!value.default_resume_selection.default_resume_id &&
        !!value.source_resume_version_id &&
        !!value.build_id &&
        !value.portrait_id &&
        !value.failure_code) ||
      (value.status === 'READY' &&
        !!value.default_resume_selection.default_resume_id &&
        !!value.source_resume_version_id &&
        !!value.build_id &&
        !!value.portrait_id &&
        !value.failure_code) ||
      (value.status === 'FAILED' &&
        !!value.default_resume_selection.default_resume_id &&
        !!value.source_resume_version_id &&
        !!value.build_id &&
        !value.portrait_id &&
        !!value.failure_code);
    if (!valid)
      context.addIssue({ code: 'custom', message: '画像状态组合无效' });
  });
const ref = z.strictObject({
  resume_version_id: uuid,
  extraction_key: scalarText,
  evidence_id: scalarText,
});
const profileEntry = z
  .strictObject({
    source_entry_id: uuid,
    name: scalarText,
    description: scalarText,
    evidence_refs: z.array(ref).min(1),
  })
  .refine(
    (value) =>
      new Set(
        value.evidence_refs.map(
          (item) =>
            `${item.resume_version_id}:${item.extraction_key}:${item.evidence_id}`,
        ),
      ).size === value.evidence_refs.length,
    '画像证据引用不能重复',
  );
const profile = z.strictObject({
  schema_version: z.literal(1),
  resume_version_id: uuid,
  extraction_key: scalarText,
  entries: z.array(profileEntry),
});
const evidence = z.strictObject({
  schema_version: z.literal(1),
  resume_version_id: uuid,
  extraction_key: scalarText,
  entries: z.array(
    z.object({ evidence_id: scalarText, entry_id: uuid }).passthrough(),
  ),
  blocks: z.array(
    z
      .object({
        evidence_id: scalarText,
        entry_id: uuid,
        block_id: uuid,
        text: scalarText,
      })
      .passthrough(),
  ),
});
const generation = z
  .strictObject({
    kind: z.enum(['MODEL', 'INCREMENTAL', 'REUSE']),
    run_id: uuid.nullable(),
    reused_from_portrait_id: uuid.nullable(),
  })
  .refine(
    (value) =>
      value.kind === 'MODEL'
        ? !!value.run_id && !value.reused_from_portrait_id
        : value.kind === 'INCREMENTAL'
          ? !!value.run_id && !!value.reused_from_portrait_id
          : !value.run_id && !!value.reused_from_portrait_id,
    '画像生成来源无效',
  );
const portrait = z
  .strictObject({
    portrait_id: uuid,
    schema_version: z.literal(1),
    resume_version_id: uuid,
    extraction_key: scalarText,
    profile,
    evidence,
    generation,
    created_at: timestamp,
  })
  .superRefine((value, context) => {
    if (
      value.profile.resume_version_id !== value.resume_version_id ||
      value.evidence.resume_version_id !== value.resume_version_id ||
      value.profile.extraction_key !== value.extraction_key ||
      value.evidence.extraction_key !== value.extraction_key
    )
      context.addIssue({ code: 'custom', message: '画像来源不一致' });
    const evidenceOwners = new Map([
      ...value.evidence.entries.map(
        (item) => [item.evidence_id, item.entry_id] as const,
      ),
      ...value.evidence.blocks.map(
        (item) => [item.evidence_id, item.entry_id] as const,
      ),
    ]);
    const entryIds = new Set(
      value.evidence.entries.map((item) => item.entry_id),
    );
    if (!value.profile.entries.length)
      context.addIssue({ code: 'custom', message: '可用画像不能为空' });
    for (const item of value.profile.entries) {
      if (
        !entryIds.has(item.source_entry_id) ||
        item.evidence_refs.some(
          (evidenceRef) =>
            evidenceRef.resume_version_id !== value.resume_version_id ||
            evidenceRef.extraction_key !== value.extraction_key ||
            evidenceOwners.get(evidenceRef.evidence_id) !==
              item.source_entry_id,
        )
      )
        context.addIssue({ code: 'custom', message: '画像条目来源不一致' });
    }
  });
export const portraitRead = z
  .strictObject({ state, portrait: portrait.nullable() })
  .superRefine((value, context) => {
    if (
      (value.state.status === 'READY') !== (value.portrait !== null) ||
      (value.portrait &&
        (value.state.portrait_id !== value.portrait.portrait_id ||
          value.state.source_resume_version_id !==
            value.portrait.resume_version_id))
    )
      context.addIssue({ code: 'custom', message: '当前画像与状态不一致' });
  });
export const portraitRefreshResult = z.strictObject({
  request_id: uuid,
  outcome: z.enum(['UPDATED', 'UNCHANGED']),
  state,
});
export type PortraitRead = components['schemas']['PortraitRead'];
export type CurrentPortraitState =
  components['schemas']['CurrentPortraitState'];
export type ProfileIndexEntry = components['schemas']['ProfileIndexEntry'];
export const portraitFailureLabels: Record<
  NonNullable<CurrentPortraitState['failure_code']>,
  string
> = {
  SOURCE_UNAVAILABLE: '来源简历暂不可用',
  CONFIGURATION_UNAVAILABLE: '画像生成尚未配置',
  INPUT_NOT_ADMITTED: '来源内容无法进入画像生成',
  OUTPUT_INVALID: '生成结果未通过完整性检查',
  INVOCATION_FAILED: '画像生成失败',
  OUTCOME_UNKNOWN: '暂时无法确认画像生成结果',
};
