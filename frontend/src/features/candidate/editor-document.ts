import { Extension, type JSONContent } from '@tiptap/core';
import { Plugin } from '@tiptap/pm/state';
import { Mapping } from '@tiptap/pm/transform';
import type { Node as ProseMirrorNode } from '@tiptap/pm/model';
import type { LocalContent, TextRun } from '@/entities/resume/model';
import { trimOuterWhitespace } from '@/shared/lib/unicode-text';

const markNames = {
  BOLD: 'bold',
  ITALIC: 'italic',
  UNDERLINE: 'underline',
  LINK: 'link',
} as const;
const markOrder = ['BOLD', 'ITALIC', 'UNDERLINE', 'LINK'] as const;
function canonicalMarks(marks: TextRun['marks']): TextRun['marks'] {
  return [...marks].sort(
    (left, right) =>
      markOrder.indexOf(left.type) - markOrder.indexOf(right.type),
  );
}
function textNodes(runs: TextRun[]): JSONContent[] {
  return runs
    .filter((run) => run.text.length > 0)
    .map((run) => ({
      type: 'text',
      text: run.text,
      marks: canonicalMarks(run.marks).map((mark) => ({
        type: markNames[mark.type],
        ...(mark.type === 'LINK' ? { attrs: { href: mark.url } } : {}),
      })),
    }));
}
export function toEditorDocument(value: LocalContent): JSONContent {
  const paragraph = (blockId: string | null, runs: TextRun[]): JSONContent => ({
    type: 'paragraph',
    attrs: { blockId },
    content: textNodes(runs),
  });
  return {
    type: 'doc',
    content: value.length
      ? value.map((block) =>
          block.type === 'PARAGRAPH'
            ? paragraph(block.block_id, block.runs)
            : {
                type:
                  block.type === 'ORDERED_LIST' ? 'orderedList' : 'bulletList',
                content: block.items.map((item) => ({
                  type: 'listItem',
                  attrs: { blockId: item.block_id },
                  content: [paragraph(null, item.runs)],
                })),
              },
        )
      : [paragraph(null, [])],
  };
}
function runsFrom(node: JSONContent): TextRun[] {
  const runs = (node.content ?? []).map((child) => {
    if (child.type !== 'text' || typeof child.text !== 'string')
      throw Error('Unsupported editor text');
    const marks: TextRun['marks'] = (child.marks ?? []).map((mark) => {
      if (mark.type === 'link')
        return { type: 'LINK', url: String(mark.attrs?.href ?? '') };
      const type = (
        { bold: 'BOLD', italic: 'ITALIC', underline: 'UNDERLINE' } as const
      )[mark.type as 'bold' | 'italic' | 'underline'];
      if (!type) throw Error('Unsupported editor mark');
      return { type };
    });
    return {
      text: child.text,
      marks: trimOuterWhitespace(child.text) ? canonicalMarks(marks) : [],
    };
  });
  return runs.reduce<TextRun[]>((canonical, run) => {
    const previous = canonical.at(-1);
    if (
      previous &&
      JSON.stringify(previous.marks) === JSON.stringify(run.marks)
    )
      previous.text += run.text;
    else canonical.push(structuredClone(run));
    return canonical;
  }, []);
}
function blockId(node: JSONContent): string {
  if (typeof node.attrs?.blockId !== 'string')
    throw Error('Missing editor block identity');
  return node.attrs.blockId;
}
export function fromEditorDocument(doc: JSONContent): LocalContent {
  const output: LocalContent = [];
  for (const block of doc.content ?? []) {
    if (block.type === 'paragraph') {
      const runs = runsFrom(block);
      if (runs.length)
        output.push({ type: 'PARAGRAPH', block_id: blockId(block), runs });
    } else if (block.type === 'bulletList' || block.type === 'orderedList') {
      const items = (block.content ?? [])
        .map((item) => {
          if (
            item.type !== 'listItem' ||
            item.content?.length !== 1 ||
            item.content[0]?.type !== 'paragraph'
          )
            throw Error('Unsupported nested list');
          return { block_id: blockId(item), runs: runsFrom(item.content[0]) };
        })
        .filter((item) => item.runs.length);
      if (items.length)
        output.push({
          type:
            block.type === 'orderedList' ? 'ORDERED_LIST' : 'UNORDERED_LIST',
          items,
        });
    } else throw Error('Unsupported editor block');
  }
  return output;
}

type Unit = { pos: number; id: string | null };
function units(doc: ProseMirrorNode): Unit[] {
  const found: Unit[] = [];
  doc.descendants((node, pos, parent) => {
    if (
      (node.type.name === 'paragraph' && parent?.type.name === 'doc') ||
      node.type.name === 'listItem'
    )
      found.push({
        pos,
        id: typeof node.attrs.blockId === 'string' ? node.attrs.blockId : null,
      });
  });
  return found;
}
function containingUnit(
  doc: ProseMirrorNode,
  rawPosition: number,
): number | null {
  const position = Math.max(0, Math.min(rawPosition, doc.content.size));
  const direct = doc.nodeAt(position);
  if (direct?.type.name === 'listItem') return position;
  const resolved = doc.resolve(position);
  for (let depth = resolved.depth; depth > 0; depth--)
    if (resolved.node(depth).type.name === 'listItem')
      return resolved.before(depth);
  if (direct?.type.name === 'paragraph') return position;
  for (const candidate of [position - 1, position + 1]) {
    if (candidate < 0 || candidate > doc.content.size) continue;
    const node = doc.nodeAt(candidate);
    if (node?.type.name === 'paragraph' || node?.type.name === 'listItem')
      return candidate;
  }
  return null;
}

export const LogicalBlockIds = Extension.create({
  name: 'logicalBlockIds',
  addGlobalAttributes() {
    return [
      {
        types: ['paragraph', 'listItem'],
        attributes: {
          blockId: {
            default: null,
            parseHTML: (element) => element.getAttribute('data-block-id'),
            renderHTML: (attributes) =>
              attributes.blockId ? { 'data-block-id': attributes.blockId } : {},
          },
        },
      },
    ];
  },
  addProseMirrorPlugins() {
    return [
      new Plugin({
        appendTransaction(transactions, oldState, newState) {
          if (!transactions.some((transaction) => transaction.docChanged))
            return null;
          const mapping = new Mapping();
          transactions.forEach((transaction) =>
            mapping.appendMapping(transaction.mapping),
          );
          const transaction = newState.tr;
          const claimed = new Set<number>();
          for (const old of units(oldState.doc)) {
            if (!old.id) continue;
            const target = containingUnit(
              transaction.doc,
              mapping.map(old.pos, -1),
            );
            if (target === null || claimed.has(target)) continue;
            const current = transaction.doc.nodeAt(target)?.attrs.blockId;
            if (typeof current === 'string' && current !== old.id) continue;
            transaction.setNodeAttribute(target, 'blockId', old.id);
            claimed.add(target);
          }
          const nestedParagraphs: number[] = [];
          transaction.doc.descendants((node, pos, parent) => {
            if (
              node.type.name === 'paragraph' &&
              parent?.type.name === 'listItem' &&
              node.attrs.blockId
            )
              nestedParagraphs.push(pos);
          });
          nestedParagraphs.forEach((pos) =>
            transaction.setNodeAttribute(pos, 'blockId', null),
          );
          const seen = new Set<string>();
          for (const unit of units(transaction.doc)) {
            const current = transaction.doc.nodeAt(unit.pos)?.attrs.blockId;
            if (typeof current !== 'string' || seen.has(current)) {
              const id = crypto.randomUUID();
              transaction.setNodeAttribute(unit.pos, 'blockId', id);
              seen.add(id);
            } else seen.add(current);
          }
          return transaction.docChanged ? transaction : null;
        },
      }),
    ];
  },
});
