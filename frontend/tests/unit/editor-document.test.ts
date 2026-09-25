import { describe, it, expect } from 'vitest';
import {
  fromEditorDocument,
  toEditorDocument,
} from '@/features/candidate/editor-document';

describe('semantic editor document boundary', () => {
  it('round trips stable IDs, paragraphs, lists and marks without HTML transport', () => {
    const value = [
      {
        type: 'PARAGRAPH' as const,
        block_id: '11111111-1111-4111-8111-111111111111',
        runs: [{ text: '<b>literal</b>', marks: [] }],
      },
      {
        type: 'UNORDERED_LIST' as const,
        items: [
          {
            block_id: '22222222-2222-4222-8222-222222222222',
            runs: [
              {
                text: 'formatted',
                marks: [{ type: 'BOLD' as const }, { type: 'ITALIC' as const }],
              },
            ],
          },
        ],
      },
    ];
    expect(fromEditorDocument(toEditorDocument(value))).toEqual(value);
  });
  it('omits an empty placeholder but never invents an identity for content', () => {
    expect(
      fromEditorDocument({
        type: 'doc',
        content: [{ type: 'paragraph', attrs: { blockId: null } }],
      }),
    ).toEqual([]);
    expect(() =>
      fromEditorDocument({
        type: 'doc',
        content: [
          {
            type: 'paragraph',
            content: [{ type: 'text', text: 'content' }],
          },
        ],
      }),
    ).toThrow('Missing editor block identity');
  });
  it('preserves literal spaces and their logical identity', () => {
    expect(
      fromEditorDocument({
        type: 'doc',
        content: [
          {
            type: 'paragraph',
            attrs: {
              blockId: '33333333-3333-4333-8333-333333333333',
            },
            content: [{ type: 'text', text: '  keep  ' }],
          },
        ],
      }),
    ).toEqual([
      {
        type: 'PARAGRAPH',
        block_id: '33333333-3333-4333-8333-333333333333',
        runs: [{ text: '  keep  ', marks: [] }],
      },
    ]);
  });
  it('canonicalizes mark order and merges adjacent equivalent runs', () => {
    expect(
      fromEditorDocument({
        type: 'doc',
        content: [
          {
            type: 'paragraph',
            attrs: {
              blockId: '44444444-4444-4444-8444-444444444444',
            },
            content: [
              {
                type: 'text',
                text: 'first',
                marks: [{ type: 'italic' }, { type: 'bold' }],
              },
              {
                type: 'text',
                text: 'second',
                marks: [{ type: 'bold' }, { type: 'italic' }],
              },
            ],
          },
        ],
      }),
    ).toEqual([
      {
        type: 'PARAGRAPH',
        block_id: '44444444-4444-4444-8444-444444444444',
        runs: [
          {
            text: 'firstsecond',
            marks: [{ type: 'BOLD' }, { type: 'ITALIC' }],
          },
        ],
      },
    ]);
  });
});
