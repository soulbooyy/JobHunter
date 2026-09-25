import { Fragment, Slice } from '@tiptap/pm/model';
import { useEffect, useState } from 'react';
import { EditorContent, useEditor, useEditorState } from '@tiptap/react';
import { Extension } from '@tiptap/core';
import StarterKit from '@tiptap/starter-kit';
import ListItem from '@tiptap/extension-list-item';
import {
  Bold,
  Italic,
  Underline,
  List,
  ListOrdered,
  Link2,
  Unlink,
  Undo2,
  Redo2,
  RemoveFormatting,
} from 'lucide-react';
import { Button } from '@/shared/ui/button';
import { Dialog } from '@/shared/ui/dialog';
import { FormControl } from '@/shared/ui/form-control';
import { httpUrlIssue } from '@/shared/lib/http-url';
import type { LocalContent } from '@/entities/resume/model';
import {
  LogicalBlockIds,
  toEditorDocument,
  fromEditorDocument,
} from './editor-document';
const FlatListItem = ListItem.extend({
  content: 'paragraph',
  addKeyboardShortcuts() {
    return {
      Enter: () => this.editor.commands.splitListItem(this.name),
      'Shift-Tab': () => this.editor.commands.liftListItem(this.name),
    };
  },
});
const SemanticEnter = Extension.create({
  name: 'semanticEnter',
  addKeyboardShortcuts() {
    return {
      'Shift-Enter': () => this.editor.commands.keyboardShortcut('Enter'),
    };
  },
});
export function BlockEditor({
  value,
  onChange,
  rich = true,
  disabled = false,
  label = '内容',
}: {
  value: LocalContent;
  onChange: (value: LocalContent) => void;
  rich?: boolean;
  disabled?: boolean;
  label?: string;
}) {
  const [link, setLink] = useState<string | null>(null),
    [error, setError] = useState('');
  const editor = useEditor({
    extensions: [
      StarterKit.configure({
        heading: false,
        blockquote: false,
        code: false,
        codeBlock: false,
        hardBreak: false,
        horizontalRule: false,
        strike: false,
        listItem: false,
        trailingNode: false,
        bold: rich ? {} : false,
        italic: rich ? {} : false,
        underline: rich ? {} : false,
        link: rich
          ? {
              openOnClick: false,
              autolink: false,
              linkOnPaste: false,
              HTMLAttributes: {
                rel: 'noopener noreferrer',
                referrerpolicy: 'no-referrer',
              },
            }
          : false,
      }),
      FlatListItem,
      SemanticEnter,
      LogicalBlockIds,
    ],
    content: toEditorDocument(value),
    editable: !disabled,
    enableInputRules: false,
    enablePasteRules: false,
    editorProps: {
      attributes: {
        role: 'textbox',
        'aria-label': label,
        'aria-multiline': 'true',
        class: 'candidate-editor-body',
      },
      handlePaste: (view, event) => {
        // Clipboard markup never becomes a second document format or a hidden link.
        const text = event.clipboardData?.getData('text/plain');
        if (text === undefined) return false;
        event.preventDefault();
        const paragraphs = text
          .replace(/\r\n?/g, '\n')
          .split('\n')
          .map((line) =>
            view.state.schema.nodes.paragraph!.create(
              { blockId: crypto.randomUUID() },
              line ? view.state.schema.text(line) : undefined,
            ),
          );
        const slice = new Slice(Fragment.fromArray(paragraphs), 1, 1);
        view.dispatch(view.state.tr.replaceSelection(slice).scrollIntoView());
        return true;
      },
    },
    onUpdate: ({ editor: current }) => {
      onChange(fromEditorDocument(current.getJSON()));
    },
  });
  const state = useEditorState({
    editor,
    selector: ({ editor: e }) => ({
      bold: e?.isActive('bold'),
      italic: e?.isActive('italic'),
      underline: e?.isActive('underline'),
      bullet: e?.isActive('bulletList'),
      ordered: e?.isActive('orderedList'),
      link: e?.isActive('link'),
      undo: e?.can().undo(),
      redo: e?.can().redo(),
    }),
  });
  useEffect(() => {
    if (editor) editor.setEditable(!disabled);
  }, [editor, disabled]);
  useEffect(() => {
    if (
      editor &&
      JSON.stringify(fromEditorDocument(editor.getJSON())) !==
        JSON.stringify(value)
    )
      editor.commands.setContent(toEditorDocument(value), {
        emitUpdate: false,
      });
  }, [editor, value, rich]);
  if (!editor) return null;
  const commands = [
    {
      name: '撤销',
      Icon: Undo2,
      run: () => editor.chain().focus().undo().run(),
      unavailable: !state?.undo,
    },
    {
      name: '重做',
      Icon: Redo2,
      run: () => editor.chain().focus().redo().run(),
      unavailable: !state?.redo,
    },
    ...(rich
      ? [
          {
            name: '加粗',
            Icon: Bold,
            active: state?.bold,
            run: () => editor.chain().focus().toggleBold().run(),
          },
          {
            name: '斜体',
            Icon: Italic,
            active: state?.italic,
            run: () => editor.chain().focus().toggleItalic().run(),
          },
          {
            name: '下划线',
            Icon: Underline,
            active: state?.underline,
            run: () => editor.chain().focus().toggleUnderline().run(),
          },
        ]
      : []),
    {
      name: '无序列表',
      Icon: List,
      active: state?.bullet,
      run: () => editor.chain().focus().toggleBulletList().run(),
    },
    {
      name: '有序列表',
      Icon: ListOrdered,
      active: state?.ordered,
      run: () => editor.chain().focus().toggleOrderedList().run(),
    },
    ...(rich
      ? [
          {
            name: '链接',
            Icon: Link2,
            active: state?.link,
            run: () => {
              setError('');
              setLink(String(editor.getAttributes('link').href ?? ''));
            },
          },
          {
            name: '移除链接',
            Icon: Unlink,
            unavailable: !state?.link,
            run: () =>
              editor.chain().focus().extendMarkRange('link').unsetLink().run(),
          },
          {
            name: '清除格式',
            Icon: RemoveFormatting,
            run: () => editor.chain().focus().unsetAllMarks().run(),
          },
        ]
      : []),
  ];
  return (
    <div className="w-full min-w-0 overflow-hidden rounded-md border border-border bg-surface focus-within:border-primary/40 focus-within:ring-2 focus-within:ring-primary/10">
      <div
        role="toolbar"
        aria-label={label + '格式'}
        className="flex flex-wrap gap-1 border-b border-border bg-surface-muted/60 p-2"
      >
        {commands.map((c) => (
          <Button
            key={c.name}
            variant="ghost"
            aria-label={c.name}
            title={c.name}
            aria-pressed={'active' in c ? !!c.active : undefined}
            disabled={disabled || ('unavailable' in c && c.unavailable)}
            className={
              'h-9 w-9 px-0 ' +
              ('active' in c && c.active
                ? 'bg-primary/10 text-foreground'
                : 'text-text-muted')
            }
            onMouseDown={(e) => e.preventDefault()}
            onClick={c.run}
          >
            <c.Icon size={16} />
          </Button>
        ))}
      </div>
      <EditorContent editor={editor} />
      {link !== null && (
        <Dialog
          title="编辑链接"
          description="将链接应用到选中文字，或继续输入带链接的文字。"
          onClose={() => setLink(null)}
        >
          <div className="mt-4 space-y-4">
            <FormControl
              label="链接地址"
              value={link}
              onChange={(v) => setLink(v ?? '')}
              error={error}
            />
            <Button
              onClick={() => {
                const issue = httpUrlIssue(link);
                if (issue) {
                  setError(issue);
                  return;
                }
                editor
                  .chain()
                  .focus()
                  .extendMarkRange('link')
                  .setLink({ href: link })
                  .run();
                setLink(null);
              }}
            >
              应用链接
            </Button>
          </div>
        </Dialog>
      )}
    </div>
  );
}
