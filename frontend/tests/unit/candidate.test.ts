import { describe, it, expect } from 'vitest';
import { profileValues } from '@/entities/profile/model';
import { evidenceValues } from '@/entities/evidence/model';
import {
  initializeContent,
  resumeDocument,
  defaultPresentation,
} from '@/entities/resume/model';
describe('Candidate source and document admission', () => {
  it('allows cleared contacts but not blank strings or invalid phone spelling', () => {
    expect(
      profileValues.safeParse({
        full_name: null,
        phone_number: null,
        email: null,
      }).success,
    ).toBe(true);
    expect(
      profileValues.safeParse({
        full_name: ' ',
        phone_number: null,
        email: null,
      }).success,
    ).toBe(false);
    expect(
      profileValues.safeParse({
        full_name: null,
        phone_number: 'abc',
        email: null,
      }).success,
    ).toBe(false);
  });
  it('validates kind fields and exact months without requiring known dates', () => {
    const v = {
      fields: {
        project_name: '项目',
        role_title: null,
        project_url: null,
        start_month: null,
        end_month: null,
      },
      content: [],
    };
    expect(evidenceValues('PROJECT').safeParse(v).success).toBe(true);
    expect(
      evidenceValues('PROJECT').safeParse({
        ...v,
        fields: { ...v.fields, start_month: '2026-09', end_month: '2025-01' },
      }).success,
    ).toBe(false);
  });
  it('rejects controls in source body before trimming and initializes unmarked local content once', () => {
    expect(
      evidenceValues('SKILL').safeParse({
        fields: { skill_name: 'React' },
        content: [{ type: 'PARAGRAPH', text: '\tReact' }],
      }).success,
    ).toBe(false);
    const source = [{ type: 'PARAGRAPH' as const, text: 'React' }];
    const local = initializeContent(source);
    source[0]!.text = 'Changed';
    expect(local).toEqual([
      { type: 'PARAGRAPH', runs: [{ text: 'React', marks: [] }] },
    ]);
  });
  it('allows empty documents but rejects duplicate sections and marked whitespace', () => {
    const draft = {
      profile_version_id: '11111111-1111-4111-8111-111111111111',
      header_presentation: { optional_items: [] },
      sections: [],
      document_presentation: defaultPresentation,
    };
    expect(resumeDocument.safeParse(draft).success).toBe(true);
    const member = {
      evidence_item_id: draft.profile_version_id,
      evidence_item_version_id: draft.profile_version_id,
      content: [
        { type: 'PARAGRAPH', runs: [{ text: ' ', marks: [{ type: 'BOLD' }] }] },
      ],
    };
    expect(
      resumeDocument.safeParse({
        ...draft,
        sections: [{ kind: 'SKILL', members: [member] }],
      }).success,
    ).toBe(false);
    expect(
      resumeDocument.safeParse({
        ...draft,
        document_presentation: { ...defaultPresentation, font_size_pt: 12.1 },
      }).success,
    ).toBe(false);
  });
});
