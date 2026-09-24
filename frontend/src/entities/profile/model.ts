import { z } from 'zod';
import type { components } from '@/shared/api/schema';
import {
  shortText,
  uuid,
  revision,
  timestamp,
} from '@/shared/lib/candidate-values';
import {
  trimOuterWhitespace,
  anywhereWhitespace,
} from '@/shared/lib/unicode-text';
export type ProfilePair = components['schemas']['ProfilePair'];
export type ProfileVersion = components['schemas']['ProfileVersion'];
export const profileValues = z.strictObject({
  full_name: shortText(100).nullable(),
  phone_number: shortText(50)
    .refine(
      (v) => /^\+?[0-9 ()-]*$/.test(trimOuterWhitespace(v)) && /[0-9]/.test(v),
      '请输入有效电话号码',
    )
    .nullable(),
  email: shortText(254)
    .refine((v) => {
      const t = trimOuterWhitespace(v);
      return /^[^@]+@[^@]+$/.test(t) && !anywhereWhitespace.test(t);
    }, '请输入有效邮箱地址')
    .nullable(),
});
export const profileVersion = profileValues.extend({
  profile_version_id: uuid,
  profile_id: uuid,
  schema_version: z.literal(1),
  created_at: timestamp,
});
export const profileRoot = z.strictObject({
  profile_id: uuid,
  current_profile_version_id: uuid,
  revision,
  created_at: timestamp,
  updated_at: timestamp,
});
export const profilePair = z
  .strictObject({ profile: profileRoot, profile_version: profileVersion })
  .refine(
    (v) =>
      v.profile.profile_id === v.profile_version.profile_id &&
      v.profile.current_profile_version_id ===
        v.profile_version.profile_version_id,
  );
export const profileResult = z
  .strictObject({
    profile: profileRoot,
    profile_version: profileVersion,
    request_id: uuid,
    outcome: z.enum(['UPDATED', 'UNCHANGED']),
  })
  .refine(
    (v) =>
      v.profile.current_profile_version_id ===
        v.profile_version.profile_version_id &&
      v.profile.profile_id === v.profile_version.profile_id,
  );
