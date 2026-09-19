import type { ReactNode } from 'react';
export function InlineNotice({
  title,
  children,
}: {
  title: string;
  children?: ReactNode;
}) {
  return (
    <div
      role="alert"
      className="space-y-2 rounded-md border border-notice-border bg-notice-background p-3 text-sm"
    >
      <p className="font-medium">{title}</p>
      {children && (
        <div className="space-y-3 leading-relaxed text-text-muted">
          {children}
        </div>
      )}
    </div>
  );
}
