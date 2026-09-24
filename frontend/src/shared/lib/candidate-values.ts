import { z } from 'zod';
import { controls, trimOuterWhitespace } from './unicode-text';
export const uuid = z
  .string()
  .regex(
    /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/,
  );
export const revision = z.number().int().min(1).max(Number.MAX_SAFE_INTEGER);
export const timestamp = z.iso.datetime();
export const shortText = (max = 200) =>
  z.string().superRefine((raw, ctx) => {
    const value = trimOuterWhitespace(raw);
    if (/[\ud800-\udfff]/u.test(raw) || controls.test(value))
      ctx.addIssue({ code: 'custom', message: '请使用有效的单行文字' });
    if (!value) ctx.addIssue({ code: 'custom', message: '请填写此项' });
    if ([...value].length > max)
      ctx.addIssue({ code: 'custom', message: `最多 ${max} 个字符` });
  });
export const bodyText = z.string().superRefine((v, c) => {
  if (controls.test(v) || /[\ud800-\udfff]/u.test(v) || !trimOuterWhitespace(v))
    c.addIssue({ code: 'custom', message: '内容不能为空或包含换行、控制字符' });
  if ([...v].length > 10000)
    c.addIssue({ code: 'custom', message: '每段最多 10000 个字符' });
});
export const month = z
  .string()
  .regex(/^(?!0000)[0-9]{4}-(0[1-9]|1[0-2])$/, '请输入 YYYY-MM 格式的年月')
  .nullable();
