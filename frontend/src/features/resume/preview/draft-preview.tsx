import { useEffect, useRef, useState, type ReactNode } from 'react';
import type {
  ResumeDocument,
  TextRun,
  LocalContent,
} from '@/entities/resume/model';
import { headerLabels } from '@/entities/resume/model';
import type { ProfileVersion } from '@/entities/profile/model';
import {
  kindLabels,
  evidenceName,
  degrees,
  type EvidenceVersion,
} from '@/entities/evidence/model';
export function RenderRuns({ runs }: { runs: TextRun[] }) {
  return (
    <>
      {runs.map((r, i) => {
        let text: ReactNode = r.text;
        for (const m of r.marks) {
          if (m.type === 'BOLD') text = <strong>{text}</strong>;
          if (m.type === 'ITALIC') text = <em>{text}</em>;
          if (m.type === 'UNDERLINE') text = <u>{text}</u>;
          if (m.type === 'LINK')
            text = (
              <a
                href={m.url}
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
          <span key={i} className="whitespace-pre-wrap">
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
      {content.map((b, i) =>
        b.type === 'PARAGRAPH' ? (
          <p key={i}>
            <RenderRuns runs={b.runs} />
          </p>
        ) : b.type === 'ORDERED_LIST' ? (
          <ol key={i} className="list-decimal pl-5">
            {b.items.map((item, j) => (
              <li key={j}>
                <RenderRuns runs={item.runs} />
              </li>
            ))}
          </ol>
        ) : (
          <ul key={i} className="list-disc pl-5">
            {b.items.map((item, j) => (
              <li key={j}>
                <RenderRuns runs={item.runs} />
              </li>
            ))}
          </ul>
        ),
      )}
    </div>
  );
}
export function DraftPreview({
  draft,
  profile,
  evidence,
  error,
}: {
  draft: ResumeDocument;
  profile?: ProfileVersion;
  evidence: Record<string, EvidenceVersion>;
  error?: string;
}) {
  const frame = useRef<HTMLDivElement>(null);
  const [scale, setScale] = useState(1);
  useEffect(() => {
    const element = frame.current;
    if (!element) return;
    const observer = new ResizeObserver(([entry]) => {
      if (!entry) return;
      setScale(
        Math.min(
          1,
          Math.max(0.1, entry.contentRect.width / ((210 * 96) / 25.4)),
        ),
      );
    });
    observer.observe(element);
    return () => observer.disconnect();
  }, [profile, error]);
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
      {error || !profile ? (
        <div
          role="alert"
          className="rounded border border-border p-8 text-center text-sm"
        >
          {error ?? '正在读取确切的资料来源…'}
        </div>
      ) : (
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
              {profile.full_name && (
                <h2
                  className="mb-2 text-2xl font-semibold"
                  style={{ color: setting.theme_color }}
                >
                  {profile.full_name}
                </h2>
              )}
              <p>
                {[profile.phone_number, profile.email]
                  .filter(Boolean)
                  .join(' · ')}
              </p>
              {draft.header_presentation.optional_items.length > 0 && (
                <p className="mt-2">
                  {draft.header_presentation.optional_items
                    .map((i) => `${headerLabels[i.kind]}：${i.value}`)
                    .join(' · ')}
                </p>
              )}
            </header>
            {draft.sections
              .filter((s) => s.members.length)
              .map((section) => (
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
                    const source = evidence[member.evidence_item_version_id];
                    if (!source)
                      return (
                        <p key={member.evidence_item_id}>资料来源暂不可用</p>
                      );
                    const f = source.fields;
                    return (
                      <article
                        key={member.evidence_item_id}
                        className="mb-4 break-words"
                      >
                        <div className="mb-1 flex justify-between gap-3 font-semibold">
                          <span>{evidenceName(f)}</span>
                          <span className="font-normal">
                            {'start_month' in f
                              ? `${f.start_month ?? '未知'} — ${f.end_month ?? '至今'}`
                              : 'awarded_month' in f
                                ? f.awarded_month
                                : 'issued_month' in f
                                  ? f.issued_month
                                  : ''}
                          </span>
                        </div>
                        <p className="mb-1">
                          {'role_title' in f
                            ? f.role_title
                            : 'major' in f
                              ? [degrees[f.degree], f.major]
                                  .filter(Boolean)
                                  .join(' · ')
                              : 'awarding_organization' in f
                                ? f.awarding_organization
                                : 'issuing_organization' in f
                                  ? f.issuing_organization
                                  : ''}
                        </p>
                        {'project_url' in f && f.project_url && (
                          <p>
                            <a
                              href={f.project_url}
                              target="_blank"
                              rel="noopener noreferrer"
                              referrerPolicy="no-referrer"
                              className="underline"
                            >
                              {f.project_url}
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
      )}
      <p className="mt-2 text-xs text-text-muted">
        浏览器按可用字体显示。此预览不会自动保存或请求 PDF。
      </p>
    </aside>
  );
}
