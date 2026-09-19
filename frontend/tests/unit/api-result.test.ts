import { describe, it, expect } from 'vitest';
import { z } from 'zod';
import { apiResult } from '@/shared/api/result';
const result = z.strictObject({ id: z.string() });
const failure =
  (status: number, code: string, fields: unknown[] = []) =>
  async () => ({
    response: new Response(null, { status }),
    error: {
      code,
      message: 'Server text must not drive behavior',
      field_errors: fields,
    },
  });
describe('write result classification', () => {
  it.each([
    [400, 'BAD_REQUEST'],
    [403, 'ACCESS_DENIED'],
    [404, 'NOT_FOUND'],
    [409, 'REVISION_CONFLICT'],
    [503, 'STORAGE_UNAVAILABLE'],
  ] as const)('recognizes confirmed rejection %s %s', async (status, code) => {
    await expect(
      apiResult(failure(status, code), result, true),
    ).rejects.toMatchObject({ kind: 'rejected', code });
  });
  it.each([
    [500, 'INTERNAL_ERROR'],
    [503, 'OUTCOME_UNKNOWN'],
    [503, 'REVISION_CONFLICT'],
    [502, 'PROXY_ERROR'],
  ] as const)('does not infer rollback from %s %s', async (status, code) => {
    await expect(
      apiResult(failure(status, code), result, true),
    ).rejects.toMatchObject({ kind: 'unknown' });
  });
  it('treats malformed success and lost connection as unknown', async () => {
    await expect(
      apiResult(
        async () => ({
          response: new Response(null, { status: 200 }),
          data: {},
        }),
        result,
        true,
      ),
    ).rejects.toMatchObject({ kind: 'unknown' });
    await expect(
      apiResult(
        async () => {
          throw new TypeError('fetch');
        },
        result,
        true,
      ),
    ).rejects.toMatchObject({ kind: 'unknown' });
  });
  it('keeps a network read error distinct from a command outcome', async () => {
    await expect(
      apiResult(async () => {
        throw new TypeError('fetch');
      }, result),
    ).rejects.toMatchObject({ kind: 'read' });
  });
});
