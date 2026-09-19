import { z } from 'zod';
import type { components } from '@/shared/api/schema';
export type ManualApplicationEntry =
  components['schemas']['ManualApplicationEntry'];

// Validate the read boundary, not editable-input admission (owned by the server).
export const entrySchema: z.ZodType<ManualApplicationEntry> = z.strictObject({
  manual_application_entry_id: z.uuidv4().regex(/^[0-9a-f-]+$/),
  company_name: z.string().min(1),
  role_title: z.string().min(1),
  application_url: z.string().min(1),
  revision: z.number().int().min(1).max(Number.MAX_SAFE_INTEGER),
  created_at: z.iso.datetime({ precision: 3 }),
  updated_at: z.iso.datetime({ precision: 3 }),
});
export const entryListSchema = z.strictObject({ items: z.array(entrySchema) });
