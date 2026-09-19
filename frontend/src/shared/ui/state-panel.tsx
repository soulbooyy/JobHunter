import type { ReactNode } from 'react';
export function StatePanel({
  title,
  description,
  action,
  error = false,
}: {
  title: string;
  description: string;
  action?: ReactNode;
  error?: boolean;
}) {
  return (
    <section role={error ? 'alert' : 'status'} className="py-20 text-center">
      <h2 className="text-base font-medium">{title}</h2>
      <p className="mt-2 text-sm text-text-muted">{description}</p>
      {action && <div className="mt-5">{action}</div>}
    </section>
  );
}
