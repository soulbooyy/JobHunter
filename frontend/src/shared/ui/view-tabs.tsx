import { NavLink } from 'react-router';
import type { ReactNode } from 'react';
import { cn } from '@/shared/lib/cn';
export function ViewTabs({
  items,
  action,
  label = '岗位池视图',
}: {
  items: ReadonlyArray<{ to: string; label: string }>;
  action?: ReactNode;
  label?: string;
}) {
  return (
    <div className="mb-5 flex items-center justify-between gap-3 border-b border-border text-sm">
      <nav aria-label={label} className="flex gap-5">
        {items.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end
            className={({ isActive }) =>
              cn(
                'border-b-2 px-1 pb-3',
                isActive
                  ? 'border-primary font-medium'
                  : 'border-transparent text-text-muted hover:text-foreground',
              )
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
      {action}
    </div>
  );
}
