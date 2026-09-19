import createClient from 'openapi-fetch';
import type { paths } from './schema';
// Same-origin /api is proxied by Vite. No auth token, retry, or persisted queue.
export const api = createClient<paths>({ baseUrl: window.location.origin });
