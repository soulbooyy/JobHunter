import { describe, expect, it } from 'vitest';
import {
  configurationSchema,
  draftFromCurrent,
  configurationFromDraft,
  textIssue,
} from '@/features/preferences/model';
import { apiResult } from '@/shared/api/result';
import { z } from 'zod';
const unlimited = { mode: 'UNLIMITED' } as const;
const configuration = {
  target_job_keywords: ['工程师'],
  accepted_cities: unlimited,
  minimum_salary: unlimited,
  recruitment_types: unlimited,
  excluded_companies: unlimited,
  max_required_education: unlimited,
};
describe('Preferences admission', () => {
  it('requires explicit complete choices and omits inactive values', () => {
    expect(configurationSchema.safeParse(configuration).success).toBe(true);
    expect(
      configurationSchema.safeParse({
        ...configuration,
        accepted_cities: { ...unlimited, value: [] },
      }).success,
    ).toBe(false);
    const draft = draftFromCurrent({ status: 'NOT_CONFIGURED' });
    expect(
      configurationSchema.safeParse(configurationFromDraft(draft)).success,
    ).toBe(false);
  });
  it('preserves commas, exact spelling and submitted array indices', () => {
    const value = {
      ...configuration,
      target_job_keywords: [' Java,Python ', 'Java,Python'],
    };
    expect(configurationSchema.parse(value)).toEqual(value);
  });
  it('counts canonical unique items but validates every original item', () => {
    expect(
      configurationSchema.safeParse({
        ...configuration,
        target_job_keywords: Array(25).fill(' x '),
      }).success,
    ).toBe(true);
    const result = configurationSchema.safeParse({
      ...configuration,
      target_job_keywords: ['x', 'x', '\u0000'],
    });
    expect(result.success).toBe(false);
    if (!result.success)
      expect(result.error.issues[0]?.path).toEqual(['target_job_keywords', 2]);
  });
  it('uses scalar legality, fixed whitespace and code-point length', () => {
    expect(textIssue('\u0085工程师\u0085', 100)).toBeUndefined();
    expect(textIssue('😀'.repeat(100), 100)).toBeUndefined();
    expect(textIssue('😀'.repeat(101), 100)).toBeDefined();
    expect(textIssue('\ud800', 100)).toBeDefined();
    expect(textIssue('a\u2028b', 100)).toBeDefined();
    expect(textIssue('\ufeff', 100)).toBeUndefined();
  });
  it.each([
    '1e4',
    '1.0',
    '1,000',
    '15k',
    '-1',
    ' 100 ',
    '￥100',
    '300001',
    '0',
  ])('rejects salary UI spelling %s', (salary) => {
    const draft = draftFromCurrent({ status: 'NOT_CONFIGURED' });
    draft.salary = salary;
    expect(
      configurationSchema.safeParse({
        ...configuration,
        minimum_salary: configurationFromDraft(draft).minimum_salary,
      }).success,
    ).toBe(false);
  });
  it('accepts the full education enum and salary endpoints', () => {
    for (const education of [
      'JUNIOR_HIGH_OR_BELOW',
      'UPPER_SECONDARY',
      'ASSOCIATE',
      'BACHELOR',
      'MASTER',
      'DOCTORATE',
    ]) {
      expect(
        configurationSchema.safeParse({
          ...configuration,
          max_required_education: { mode: 'LIMITED', value: education },
          minimum_salary: { mode: 'LIMITED', value: 300000 },
        }).success,
      ).toBe(true);
    }
  });
});
describe('M2 error boundary preserves M1 scope', () => {
  const operation =
    (status: number, code: string, fields: unknown[] = []) =>
    async () => ({
      response: new Response(null, { status }),
      error: { code, message: 'sanitized', field_errors: fields },
    });
  it('accepts known nested original-index errors only in preferences scope', async () => {
    const op = operation(422, 'VALIDATION_ERROR', [
      { field: 'configuration.accepted_cities.value[1]', code: 'BLANK_VALUE' },
    ]);
    await expect(
      apiResult(op, z.object({}), true, 'preferences'),
    ).rejects.toMatchObject({
      kind: 'rejected',
      fields: [{ field: 'configuration.accepted_cities.value[1]' }],
    });
    await expect(apiResult(op, z.object({}), true)).rejects.toMatchObject({
      kind: 'unknown',
    });
  });
  it('recognizes 413 and fails closed for arbitrary nested paths', async () => {
    await expect(
      apiResult(
        operation(413, 'REQUEST_TOO_LARGE'),
        z.object({}),
        true,
        'preferences',
      ),
    ).rejects.toMatchObject({ kind: 'rejected', code: 'REQUEST_TOO_LARGE' });
    await expect(
      apiResult(
        operation(422, 'VALIDATION_ERROR', [
          { field: 'configuration.secret.value[0]', code: 'REQUIRED' },
        ]),
        z.object({}),
        true,
        'preferences',
      ),
    ).rejects.toMatchObject({ kind: 'unknown' });
  });
});
