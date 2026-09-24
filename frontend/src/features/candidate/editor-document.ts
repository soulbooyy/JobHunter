import type { JSONContent } from '@tiptap/core';
import type { EvidenceContent } from '@/entities/evidence/model';
import type { LocalContent, TextRun } from '@/entities/resume/model';
import { trimOuterWhitespace } from '@/shared/lib/unicode-text';
const markNames = {
  BOLD: 'bold',
  ITALIC: 'italic',
  UNDERLINE: 'underline',
  LINK: 'link',
} as const;
function textNodes(runs: TextRun[]): JSONContent[] {
  return runs
    .filter((r) => r.text.length > 0)
    .map((r) => ({
      type: 'text',
      text: r.text,
      marks: r.marks.map((m) => ({
        type: markNames[m.type],
        ...(m.type === 'LINK' ? { attrs: { href: m.url } } : {}),
      })),
    }));
}
export function toEditorDocument(
  value: EvidenceContent | LocalContent,
  rich: boolean,
): JSONContent {
  const paragraph = (item: string | { runs: TextRun[] }): JSONContent => ({
    type: 'paragraph',
    content: textNodes(
      typeof item === 'string' ? [{ text: item, marks: [] }] : item.runs,
    ),
  });
  return {
    type: 'doc',
    content: value.length
      ? value.map((b) =>
          b.type === 'PARAGRAPH'
            ? paragraph(
                rich
                  ? (b as { runs: TextRun[] })
                  : (b as { text: string }).text,
              )
            : {
                type: b.type === 'ORDERED_LIST' ? 'orderedList' : 'bulletList',
                content: b.items.map((item) => ({
                  type: 'listItem',
                  content: [paragraph(item)],
                })),
              },
        )
      : [paragraph('')],
  };
}
function runsFrom(node: JSONContent): TextRun[] {
  return (node.content ?? []).map((n) => {
    if (n.type !== 'text' || typeof n.text !== 'string')
      throw Error('Unsupported editor text');
    const marks: TextRun['marks'] = (n.marks ?? []).map((m) => {
      if (m.type === 'link')
        return { type: 'LINK', url: String(m.attrs?.href ?? '') };
      const type = (
        { bold: 'BOLD', italic: 'ITALIC', underline: 'UNDERLINE' } as const
      )[m.type as 'bold' | 'italic' | 'underline'];
      if (!type) throw Error('Unsupported editor mark');
      return { type };
    });
    // Whitespace typed at a styled caret is a layout separator, never a styled fact.
    return { text: n.text, marks: trimOuterWhitespace(n.text) ? marks : [] };
  });
}
export function fromEditorDocument(
  doc: JSONContent,
  rich: boolean,
): EvidenceContent | LocalContent {
  const output: Array<LocalContent[number] | EvidenceContent[number]> = [];
  for (const b of doc.content ?? []) {
    if (b.type === 'paragraph') {
      const runs = runsFrom(b);
      if (!runs.length) continue; // Empty editor lines are local layout placeholders.
      output.push(
        rich
          ? { type: 'PARAGRAPH', runs }
          : { type: 'PARAGRAPH', text: runs.map((r) => r.text).join('') },
      );
    } else if (b.type === 'bulletList' || b.type === 'orderedList') {
      const entries = (b.content ?? [])
        .map((item) => {
          if (
            item.type !== 'listItem' ||
            item.content?.length !== 1 ||
            item.content[0]?.type !== 'paragraph'
          )
            throw Error('Unsupported nested list');
          return runsFrom(item.content[0]);
        })
        .filter((runs) => runs.length);
      if (!entries.length) continue;
      const type = b.type === 'orderedList' ? 'ORDERED_LIST' : 'UNORDERED_LIST';
      output.push(
        rich
          ? { type, items: entries.map((runs) => ({ runs })) }
          : {
              type,
              items: entries.map((runs) => runs.map((r) => r.text).join('')),
            },
      );
    } else throw Error('Unsupported editor block');
  }
  return output as EvidenceContent | LocalContent;
}
