const whitespace =
  '\u0009-\u000d\u0020\u0085\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000';
const edgeWhitespace = new RegExp(`^[${whitespace}]+|[${whitespace}]+$`, 'gu');
export const anywhereWhitespace = new RegExp(`[${whitespace}]`, 'u');
// COM-026 explicitly defines these control characters for rejection.
// eslint-disable-next-line no-control-regex
export const controls = /[\u0000-\u001f\u007f-\u009f\u2028\u2029]/u;
export function trimOuterWhitespace(value: string) {
  return value.replace(edgeWhitespace, '');
}
