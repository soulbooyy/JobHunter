import { z } from 'zod';
import { api } from '@/shared/api/client';
import { apiResult, ApiFailure } from '@/shared/api/result';
import {
  entrySchema,
  entryListSchema,
} from '@/entities/manual-application-entry/model';
import type { components } from '@/shared/api/schema';
export type CreateEntry = components['schemas']['CreateEntry'];
export type UpdateEntry = components['schemas']['UpdateEntry'];
const identity = z.strictObject({
  manual_application_entry_id: z.uuidv4().regex(/^[0-9a-f-]+$/),
});
const path = (id: string) => ({ path: { manual_application_entry_id: id } });
const timeout = () => AbortSignal.timeout(15_000);
export const entryApi = {
  list: (signal?: AbortSignal) =>
    apiResult(
      () =>
        api.GET('/api/v1/manual-application-entries', {
          signal: signal ? AbortSignal.any([signal, timeout()]) : timeout(),
        }),
      entryListSchema,
    ),
  read: (id: string) =>
    apiResult(
      () =>
        api.GET(
          '/api/v1/manual-application-entries/{manual_application_entry_id}',
          { params: path(id), signal: timeout() },
        ),
      entrySchema,
    ).then((entry) => {
      if (entry.manual_application_entry_id !== id)
        throw new ApiFailure('read', 'READ_FAILED');
      return entry;
    }),
  create: (body: CreateEntry) =>
    apiResult(
      () =>
        api.POST('/api/v1/manual-application-entries', {
          body,
          signal: timeout(),
        }),
      identity,
      true,
    ),
  update: (id: string, body: UpdateEntry) =>
    apiResult(
      () =>
        api.PUT(
          '/api/v1/manual-application-entries/{manual_application_entry_id}',
          { params: path(id), body, signal: timeout() },
        ),
      entrySchema,
      true,
    ).then((entry) => {
      if (entry.manual_application_entry_id !== id)
        throw new ApiFailure('unknown', 'OUTCOME_UNKNOWN');
      return entry;
    }),
  delete: (id: string, revision: number) =>
    apiResult(
      () =>
        api.POST(
          '/api/v1/manual-application-entries/{manual_application_entry_id}/delete',
          { params: path(id), body: { revision }, signal: timeout() },
        ),
      identity,
      true,
    ).then((entry) => {
      if (entry.manual_application_entry_id !== id)
        throw new ApiFailure('unknown', 'OUTCOME_UNKNOWN');
      return entry;
    }),
  resolve: (id: string, revision: number) =>
    apiResult(
      () =>
        api.POST(
          '/api/v1/manual-application-entries/{manual_application_entry_id}/resolve-url',
          { params: path(id), body: { revision }, signal: timeout() },
        ),
      z.strictObject({
        application_url: z.string().refine((value) => {
          try {
            const u = new URL(value);
            return (
              ['http:', 'https:'].includes(u.protocol) &&
              !u.username &&
              !u.password
            );
          } catch {
            return false;
          }
        }),
      }),
    ),
};
