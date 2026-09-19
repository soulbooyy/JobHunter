import { queryOptions } from '@tanstack/react-query';
import { entryApi } from './api';
export const manualApplicationEntriesQuery = queryOptions({
  queryKey: ['manual-application-entries'],
  queryFn: async ({ signal }) => (await entryApi.list(signal)).items,
});
