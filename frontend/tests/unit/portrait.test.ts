import { describe, expect, it } from 'vitest';
import { portraitRead } from '@/entities/profile/model';

const resumeVersionId = '11111111-1111-4111-8111-111111111111';
const entryId = '22222222-2222-4222-8222-222222222222';
const blockId = '33333333-3333-4333-8333-333333333333';
const portraitId = '44444444-4444-4444-8444-444444444444';
const buildId = '55555555-5555-4555-8555-555555555555';
const evidenceId = `block/${entryId}/${blockId}`;

function readyPortrait(sourceEntryId = entryId, reference = evidenceId) {
  return {
    state: {
      default_resume_selection: {
        default_resume_id: '66666666-6666-4666-8666-666666666666',
        revision: 3,
      },
      source_resume_version_id: resumeVersionId,
      status: 'READY',
      build_id: buildId,
      portrait_id: portraitId,
      failure_code: null,
    },
    portrait: {
      portrait_id: portraitId,
      schema_version: 1,
      resume_version_id: resumeVersionId,
      extraction_key: 'portrait.v1',
      profile: {
        schema_version: 1,
        resume_version_id: resumeVersionId,
        extraction_key: 'portrait.v1',
        entries: [
          {
            source_entry_id: sourceEntryId,
            name: '前端能力',
            description: '来自一条明确经历',
            evidence_refs: [
              {
                resume_version_id: resumeVersionId,
                extraction_key: 'portrait.v1',
                evidence_id: reference,
              },
            ],
          },
        ],
      },
      evidence: {
        schema_version: 1,
        resume_version_id: resumeVersionId,
        extraction_key: 'portrait.v1',
        entries: [
          {
            evidence_id: `entry/${entryId}`,
            entry_id: entryId,
            kind: 'PROJECT',
            fields: {},
            content: [],
          },
        ],
        blocks: [
          {
            evidence_id: evidenceId,
            entry_id: entryId,
            block_id: blockId,
            text: '证据文本',
          },
        ],
      },
      generation: {
        kind: 'MODEL',
        run_id: '88888888-8888-4888-8888-888888888888',
        reused_from_portrait_id: null,
      },
      created_at: '2026-09-24T00:00:00Z',
    },
  };
}

describe('entry-scoped portrait parsing', () => {
  it('accepts a READY portrait whose index entry and evidence share one source entry', () => {
    expect(portraitRead.safeParse(readyPortrait()).success).toBe(true);
  });

  it('rejects a profile entry that borrows evidence from another Resume entry', () => {
    const otherEntry = '77777777-7777-4777-8777-777777777777';
    expect(
      portraitRead.safeParse(readyPortrait(otherEntry, evidenceId)).success,
    ).toBe(false);
  });

  it('rejects READY without a matching portrait and accepts unavailable states without one', () => {
    expect(
      portraitRead.safeParse({ ...readyPortrait(), portrait: null }).success,
    ).toBe(false);
    expect(
      portraitRead.safeParse({
        state: {
          default_resume_selection: {
            default_resume_id: null,
            revision: 1,
          },
          source_resume_version_id: null,
          status: 'NO_SOURCE',
          build_id: null,
          portrait_id: null,
          failure_code: null,
        },
        portrait: null,
      }).success,
    ).toBe(true);
  });
});
