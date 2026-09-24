import { httpUrlIssue } from '@/shared/lib/http-url';
import { z } from 'zod';
import { trimOuterWhitespace, controls } from '@/shared/lib/unicode-text';
export { trimOuterWhitespace } from '@/shared/lib/unicode-text';
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
  return httpUrlIssue(raw);
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
