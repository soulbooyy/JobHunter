import { describe, expect, it } from 'vitest';
import fixtures from '../../../backend/tests/fixtures/manual_application_entry_admission.json';
import {
  entryFormSchema,
  trimOuterWhitespace,
} from '@/features/manual-application-entries/validation';
const valid = {
  company_name: '公司',
  role_title: '岗位',
  application_url: 'https://example.test',
};
describe('entry form admission', () => {
  it.each(fixtures.urls)(
    'matches shared URL example $value',
    ({ value, status }) => {
      expect(
        entryFormSchema.safeParse({ ...valid, application_url: value }).success,
      ).toBe(status === 200);
    },
  );
  it('preserves admitted raw URL input and leaves authoritative trimming to the server', () => {
    const value = ' HTTP://Example.test:80/./apply ';
    expect(
      entryFormSchema.parse({ ...valid, application_url: value })
        .application_url,
    ).toBe(value);
  });
  it('counts code points and never truncates', () => {
    expect(
      entryFormSchema.safeParse({ ...valid, company_name: '😀'.repeat(200) })
        .success,
    ).toBe(true);
    expect(
      entryFormSchema.safeParse({ ...valid, company_name: '😀'.repeat(201) })
        .success,
    ).toBe(false);
  });
  it('uses fixed whitespace rather than JavaScript trim', () => {
    expect(trimOuterWhitespace('\u0085 公司 \u0085')).toBe('公司');
    expect(trimOuterWhitespace('\ufeff公司\ufeff')).toBe('\ufeff公司\ufeff');
    expect(
      entryFormSchema.safeParse({
        ...valid,
        company_name: ' '.repeat(250) + '公司',
      }).success,
    ).toBe(true);
  });
  it.each(['\ud800', 'a\nb', 'a\u0000b'])(
    'rejects invalid scalar or line content',
    (value) => {
      expect(
        entryFormSchema.safeParse({ ...valid, company_name: value }).success,
      ).toBe(false);
    },
  );
  it('rejects extra fields and admits a URL beyond 2083 characters', () => {
    expect(
      entryFormSchema.safeParse({ ...valid, status: 'APPLIED' }).success,
    ).toBe(false);
    expect(
      entryFormSchema.safeParse({
        ...valid,
        application_url: 'https://example.test/' + 'a'.repeat(3000),
      }).success,
    ).toBe(true);
  });
});
