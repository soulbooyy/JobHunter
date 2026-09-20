import type {
  Configuration,
  CurrentPreferences,
  SaveResult,
} from '@/features/preferences/model';
const root = '22222222-2222-4222-8222-222222222222';
const version = '33333333-3333-4333-8333-333333333333';
export const configuration: Configuration = {
  target_job_keywords: ['工程师'],
  accepted_cities: { mode: 'UNLIMITED' },
  minimum_salary: { mode: 'LIMITED', value: 15000 },
  recruitment_types: { mode: 'UNLIMITED' },
  excluded_companies: { mode: 'UNLIMITED' },
  max_required_education: { mode: 'UNLIMITED' },
};
export function current(
  revision = 1,
  keywords = ['工程师'],
): CurrentPreferences {
  return {
    status: 'CONFIGURED',
    preference_set: {
      preference_set_id: root,
      current_preference_set_version_id: version,
      revision,
      created_at: '2026-09-20T01:00:00.000Z',
      updated_at: '2026-09-20T01:00:00.000Z',
    },
    current_preference_set_version: {
      preference_set_id: root,
      preference_set_version_id: version,
      created_at: '2026-09-20T01:00:00.000Z',
      configuration: { ...configuration, target_job_keywords: keywords },
    },
  };
}
export const saved: SaveResult = {
  preference_set_id: root,
  preference_set_version_id: version,
  revision: 2,
  outcome: 'UPDATED',
};
