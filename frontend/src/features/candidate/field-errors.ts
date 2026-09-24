import type { ZodError } from 'zod';
import { fieldErrorMessage, type ApiFailure } from '@/shared/api/result';
export type Errors = Record<string, string>;
export function localErrors(error: ZodError): Errors {
  return Object.fromEntries(
    error.issues.map((i) => [
      i.path
        .map((p) => (typeof p === 'number' ? `[${p}]` : p))
        .join('.')
        .replace(/\.\[/g, '['),
      i.message,
    ]),
  );
}
export function serverErrors(error?: ApiFailure): Errors {
  return Object.fromEntries(
    (error?.fields ?? []).map((f) => [f.field, fieldErrorMessage(f)]),
  );
}
export function errorAt(errors: Errors, path: string) {
  return (
    Object.entries(errors)
      .filter(
        ([key]) =>
          key === path ||
          key.startsWith(path + '.') ||
          key.startsWith(path + '['),
      )
      .map(([, value]) => value)
      .filter((v, i, a) => a.indexOf(v) === i)
      .join('；') || undefined
  );
}
