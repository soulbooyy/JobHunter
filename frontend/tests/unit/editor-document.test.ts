import { describe, it, expect } from 'vitest';
import {
  toEditorDocument,
  fromEditorDocument,
} from '@/features/candidate/editor-document';
describe('semantic editor document boundary', () => {
  it('round trips paragraphs, lists and combined marks without HTML transport', () => {
    const value = [
      {
        type: 'PARAGRAPH' as const,
        runs: [{ text: '<b>literal</b>', marks: [] }],
      },
      {
        type: 'UNORDERED_LIST' as const,
        items: [
          {
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
    expect(fromEditorDocument(toEditorDocument(value, true), true)).toEqual(
      value,
    );
  });
  it('omits empty editing lines while retaining explicit nonempty content', () => {
    expect(
      fromEditorDocument(
        { type: 'doc', content: [{ type: 'paragraph' }] },
        true,
      ),
    ).toEqual([]);
    expect(
      fromEditorDocument(
        {
          type: 'doc',
          content: [
            {
              type: 'paragraph',
              content: [{ type: 'text', text: '  keep  ' }],
            },
          ],
        },
        true,
      ),
    ).toEqual([{ type: 'PARAGRAPH', runs: [{ text: '  keep  ', marks: [] }] }]);
  });
  it('keeps plain knowledge list semantics', () => {
    const value = [{ type: 'ORDERED_LIST' as const, items: ['one', 'two'] }];
    expect(fromEditorDocument(toEditorDocument(value, false), false)).toEqual(
      value,
    );
  });
});
