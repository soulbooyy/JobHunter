import { describe, it, expect, vi } from 'vitest';
import {
  contacts,
  copyResumeEntry,
  defaultPresentation,
  fieldsByKind,
  resumeDocument,
} from '@/entities/resume/model';

const entryId = '11111111-1111-4111-8111-111111111111';
const blockId = '22222222-2222-4222-8222-222222222222';
describe('independent Resume admission', () => {
  it('allows cleared document-owned contacts but rejects blank names and invalid phones', () => {
    expect(defaultPresentation.font_family).toBe('SOURCE_HAN_SANS');
    expect(
      contacts.safeParse({
        full_name: null,
        phone_number: null,
        email: null,
      }).success,
    ).toBe(true);
    expect(
      contacts.safeParse({
        full_name: ' ',
        phone_number: null,
        email: null,
      }).success,
    ).toBe(false);
    expect(
      contacts.safeParse({
        full_name: null,
        phone_number: 'abc',
        email: null,
      }).success,
    ).toBe(false);
  });
  it('validates each kind fields without inventing dates', () => {
    const fields = {
      project_name: '项目',
      role_title: null,
      project_url: null,
      start_month: null,
      end_month: null,
    };
    expect(fieldsByKind.PROJECT.safeParse(fields).success).toBe(true);
    expect(
      fieldsByKind.PROJECT.safeParse({
        ...fields,
        project_url: 'javascript:alert(1)',
      }).success,
    ).toBe(false);
  });
  it('keeps entry and block identities and rejects duplicates', () => {
    const draft = {
      contacts: { full_name: null, phone_number: null, email: null },
      header_presentation: { optional_items: [] },
      sections: [
        {
          kind: 'SKILL' as const,
          members: [
            {
              entry_id: entryId,
              fields: { skill_name: 'React' },
              content: [
                {
                  type: 'PARAGRAPH' as const,
                  block_id: blockId,
                  runs: [{ text: 'React', marks: [] }],
                },
              ],
            },
          ],
        },
      ],
      document_presentation: defaultPresentation,
    };
    expect(resumeDocument.safeParse(draft).success).toBe(true);
    expect(
      resumeDocument.safeParse({
        ...draft,
        sections: [
          {
            ...draft.sections[0],
            members: [
              ...draft.sections[0]!.members,
              draft.sections[0]!.members[0],
            ],
          },
        ],
      }).success,
    ).toBe(false);
  });
  it('assigns fresh logical identities when duplicating an entry', () => {
    vi.stubGlobal('crypto', {
      randomUUID: vi
        .fn()
        .mockReturnValueOnce('33333333-3333-4333-8333-333333333333')
        .mockReturnValueOnce('44444444-4444-4444-8444-444444444444'),
    });
    const copied = copyResumeEntry({
      entry_id: entryId,
      fields: { skill_name: 'React' },
      content: [
        {
          type: 'PARAGRAPH',
          block_id: blockId,
          runs: [{ text: 'React', marks: [] }],
        },
      ],
    });
    expect(copied.entry_id).not.toBe(entryId);
    const copiedBlock = copied.content[0]!;
    expect(copiedBlock.type).toBe('PARAGRAPH');
    if (copiedBlock.type === 'PARAGRAPH') {
      expect(copiedBlock.block_id).not.toBe(blockId);
    }
    vi.unstubAllGlobals();
  });
});
