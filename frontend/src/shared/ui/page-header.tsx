import type { ReactNode } from 'react';
export function PageHeader({
  title,
  description,
  action,
  id,
}: {
  title: string;
  description: string;
  action?: ReactNode;
  id?: string;
}) {
  return (
    <header className="mb-6 flex flex-wrap items-start justify-between gap-4">
      <div>
        <h1 id={id} className="text-2xl font-semibold">
          {title}
        </h1>
        <p className="mt-2 text-sm text-text-muted">{description}</p>
      </div>
      {action}
    </header>
  );
}
