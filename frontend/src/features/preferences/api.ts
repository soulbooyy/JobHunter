import { api } from '@/shared/api/client';
import { apiResult, ApiFailure } from '@/shared/api/result';
import {
  currentSchema,
  saveResultSchema,
  versionSchema,
  type SavePreferences,
} from './model';
const timeout = () => AbortSignal.timeout(15_000);
export const preferencesApi = {
  current: (signal?: AbortSignal) =>
    apiResult(
      () =>
        api.GET('/api/v1/preferences', {
          signal: signal ? AbortSignal.any([signal, timeout()]) : timeout(),
        }),
      currentSchema,
      false,
      'preferences',
    ),
  save: (body: SavePreferences) =>
    apiResult(
      () => api.POST('/api/v1/preferences/save', { body, signal: timeout() }),
      saveResultSchema,
      true,
      'preferences',
    ),
  version: (id: string) =>
    apiResult(
      () =>
        api.GET('/api/v1/preferences/versions/{preference_set_version_id}', {
          params: { path: { preference_set_version_id: id } },
          signal: timeout(),
        }),
      versionSchema,
      false,
      'preferences',
    ).then((version) => {
      if (version.preference_set_version_id !== id)
        throw new ApiFailure('read', 'READ_FAILED');
      return version;
    }),
};
export const preferencesQuery = {
  queryKey: ['preferences'] as const,
  queryFn: ({ signal }: { signal: AbortSignal }) =>
    preferencesApi.current(signal),
  staleTime: 0,
  gcTime: 0,
};
