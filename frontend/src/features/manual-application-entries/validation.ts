import { z } from 'zod';
const whitespace =
  '\u0009-\u000d\u0020\u0085\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000';
const edgeWhitespace = new RegExp(`^[${whitespace}]+|[${whitespace}]+$`, 'gu');
const anywhereWhitespace = new RegExp(`[${whitespace}]`, 'u');
// COM-026 explicitly defines these control characters for rejection.
// eslint-disable-next-line no-control-regex
const controls = /[\u0000-\u001f\u007f-\u009f\u2028\u2029]/u;
export function trimOuterWhitespace(value: string) {
  return value.replace(edgeWhitespace, '');
}
export const fieldLabels = {
  company_name: '公司',
  role_title: '职位名称',
  application_url: '申请链接',
};
export type EntryField = keyof typeof fieldLabels;
export const entryFields = Object.keys(fieldLabels) as EntryField[];
function issueForText(raw: string, field: EntryField): string | undefined {
  if (/[\ud800-\udfff]/u.test(raw)) return '内容包含无效字符';
  const value = trimOuterWhitespace(raw);
  if (!value)
    return `请输入${field === 'company_name' ? '公司名称' : fieldLabels[field]}`;
  if ([...value].length > (field === 'application_url' ? 8192 : 200))
    return '内容过长，请缩短后重试';
  if (field !== 'application_url')
    return controls.test(value) ? '请使用不含控制字符的单行文本' : undefined;
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
const field = (name: EntryField) =>
  z
    .string({ error: `请输入${fieldLabels[name]}` })
    .superRefine((value, context) => {
      const message = issueForText(value, name);
      if (message) context.addIssue({ code: 'custom', message });
    });
export const entryFormSchema = z.strictObject({
  company_name: field('company_name'),
  role_title: field('role_title'),
  application_url: field('application_url'),
});
export type EntryFormValues = z.infer<typeof entryFormSchema>;
