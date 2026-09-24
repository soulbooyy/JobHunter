import {
  controls,
  anywhereWhitespace,
  trimOuterWhitespace,
} from './unicode-text';
export function httpUrlIssue(raw: string): string | undefined {
  const value = trimOuterWhitespace(raw);
  if (/[\ud800-\udfff]/u.test(raw) || [...value].length > 8192)
    return '请输入有效的 HTTP 或 HTTPS 链接';
  const invalid = '请输入有效的 HTTP 或 HTTPS 链接';
  if (
    controls.test(value) ||
    anywhereWhitespace.test(value) ||
    value.includes('\\') ||
    /%(?![0-9a-f]{2})/i.test(value)
  )
    return invalid;
  const authority = /^https?:\/\/([^/?#]+)/i.exec(value)?.[1];
  if (!authority || authority.includes('@')) return invalid;
  // Reject empty/out-of-range ports and IPv4 spellings repaired by URL().
  const parts = /^(\[[^\]]+\]|[^:]+)(?::(.*))?$/.exec(authority);
  if (!parts) return invalid;
  if (
    parts[2] !== undefined &&
    (!/^\d+$/.test(parts[2]) || Number(parts[2]) > 65535)
  )
    return invalid;
  try {
    const parsed = new URL(value);
    if (
      !['http:', 'https:'].includes(parsed.protocol) ||
      !parsed.hostname ||
      parsed.username ||
      parsed.password
    )
      return invalid;
    if (
      /^\d+\.\d+\.\d+\.\d+$/.test(parsed.hostname) &&
      parts[1] !== parsed.hostname
    )
      return invalid;
  } catch {
    return invalid;
  }
  // Full pinned WHATWG validity remains server-owned; never serialize/repair input.
}
