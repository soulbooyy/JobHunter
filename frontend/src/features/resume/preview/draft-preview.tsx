import { useEffect, useRef, useState, type ReactNode } from 'react';
import {
  degrees,
  entryName,
  headerLabels,
  kindLabels,
  type LocalContent,
  type ResumeDocument,
  type TextRun,
} from '@/entities/resume/model';

export function RenderRuns({ runs }: { runs: TextRun[] }) {
  return (
    <>
      {runs.map((run, index) => {
        let text: ReactNode = run.text;
        for (const mark of run.marks) {
          if (mark.type === 'BOLD') text = <strong>{text}</strong>;
          if (mark.type === 'ITALIC') text = <em>{text}</em>;
          if (mark.type === 'UNDERLINE') text = <u>{text}</u>;
          if (mark.type === 'LINK')
            text = (
              <a
                href={mark.url}
                target="_blank"
                rel="noopener noreferrer"
                referrerPolicy="no-referrer"
                className="underline"
              >
                {text}
              </a>
            );
        }
        return (
          <span key={index} className="whitespace-pre-wrap">
            {text}
          </span>
        );
      })}
    </>
  );
}
function Body({ content }: { content: LocalContent }) {
  return (
    <div className="space-y-1">
      {content.map((block) =>
        block.type === 'PARAGRAPH' ? (
          <p key={block.block_id}>
            <RenderRuns runs={block.runs} />
          </p>
        ) : block.type === 'ORDERED_LIST' ? (
          <ol
            key={block.items.map((item) => item.block_id).join(':')}
            className="list-decimal pl-5"
          >
            {block.items.map((item) => (
              <li key={item.block_id}>
                <RenderRuns runs={item.runs} />
              </li>
            ))}
          </ol>
        ) : (
          <ul
            key={block.items.map((item) => item.block_id).join(':')}
            className="list-disc pl-5"
          >
            {block.items.map((item) => (
              <li key={item.block_id}>
                <RenderRuns runs={item.runs} />
              </li>
            ))}
          </ul>
        ),
      )}
    </div>
  );
}
export function DraftPreview({ draft }: { draft: ResumeDocument }) {
  const frame = useRef<HTMLDivElement>(null);
  const [scale, setScale] = useState(1);
  useEffect(() => {
    const element = frame.current;
    if (!element) return;
    const observer = new ResizeObserver(([entry]) => {
      if (entry)
        setScale(
          Math.min(
            1,
            Math.max(0.1, entry.contentRect.width / ((210 * 96) / 25.4)),
          ),
        );
    });
    observer.observe(element);
    return () => observer.disconnect();
  }, []);
  const setting = draft.document_presentation;
  const font = {
    SOURCE_HAN_SANS: '"Source Han Sans SC", "PingFang SC", sans-serif',
    HEITI: '"Heiti SC", "PingFang SC", sans-serif',
    SONGTI: '"Songti SC", serif',
    KAITI: '"Kaiti SC", "STKaiti", serif',
  }[setting.font_family];
  return (
    <aside aria-label="简历本地预览" className="min-w-0">
      <div className="mb-3 flex justify-between text-xs text-text-muted">
        <span>A4 草稿预览</span>
        <span>本地更新 · 尚非导出文件</span>
      </div>
      <div
        ref={frame}
        className="overflow-hidden rounded border border-border bg-surface-muted p-3"
      >
        <div
          className="mx-auto min-h-[297mm] w-[210mm] origin-top-left bg-white px-[18mm] py-[16mm] text-black shadow-sm"
          style={{
            zoom: scale,
            fontFamily: font,
            fontSize: `${setting.font_size_pt}pt`,
            lineHeight: `${setting.line_spacing_pt}pt`,
          }}
        >
          <header className="mb-5 text-center">
            {draft.contacts.full_name && (
              <h2
                className="mb-2 text-2xl font-semibold"
                style={{ color: setting.theme_color }}
              >
                {draft.contacts.full_name}
              </h2>
            )}
            <p>
              {[draft.contacts.phone_number, draft.contacts.email]
                .filter(Boolean)
                .join(' · ')}
            </p>
            {draft.header_presentation.optional_items.length > 0 && (
              <p className="mt-2">
                {draft.header_presentation.optional_items
                  .map((item) => `${headerLabels[item.kind]}：${item.value}`)
                  .join(' · ')}
              </p>
            )}
          </header>
          {draft.sections.map((section) => (
            <section key={section.kind} className="mb-5">
              <h3
                className="mb-3 border-b pb-1 font-semibold"
                style={{
                  color: setting.theme_color,
                  borderColor: setting.theme_color,
                }}
              >
                {kindLabels[section.kind]}
              </h3>
              {section.members.map((member) => {
                const fields = member.fields;
                return (
                  <article key={member.entry_id} className="mb-4 break-words">
                    <div className="mb-1 flex justify-between gap-3 font-semibold">
                      <span>{entryName(fields)}</span>
                      <span className="font-normal">
                        {'start_month' in fields
                          ? `${fields.start_month ?? '未知'} — ${fields.end_month ?? '至今'}`
                          : 'awarded_month' in fields
                            ? fields.awarded_month
                            : 'issued_month' in fields
                              ? fields.issued_month
                              : ''}
                      </span>
                    </div>
                    <p className="mb-1">
                      {'role_title' in fields
                        ? fields.role_title
                        : 'major' in fields
                          ? [
                              degrees[fields.degree as keyof typeof degrees],
                              fields.major,
                            ]
                              .filter(Boolean)
                              .join(' · ')
                          : 'awarding_organization' in fields
                            ? fields.awarding_organization
                            : 'issuing_organization' in fields
                              ? fields.issuing_organization
                              : ''}
                    </p>
                    {'project_url' in fields && fields.project_url && (
                      <p>
                        <a
                          href={fields.project_url}
                          target="_blank"
                          rel="noopener noreferrer"
                          referrerPolicy="no-referrer"
                          className="underline"
                        >
                          {fields.project_url}
                        </a>
                      </p>
                    )}
                    <Body content={member.content} />
                  </article>
                );
              })}
            </section>
          ))}
        </div>
      </div>
      <p className="mt-2 text-xs text-text-muted">
        浏览器按可用字体显示。此预览不会自动保存或请求 PDF。
      </p>
    </aside>
  );
}
