import type { ComponentProps } from 'react';
import { cn } from '@/shared/lib/cn';
export function Table({ className, ...props }: ComponentProps<'table'>) {
  return (
    <div className="overflow-x-auto rounded-lg border border-border">
      <table
        className={cn('w-full table-fixed text-left text-[13px]', className)}
        {...props}
      />
    </div>
  );
}
export function TableHeader(props: ComponentProps<'thead'>) {
  return (
    <thead className="bg-surface-muted text-xs text-text-muted" {...props} />
  );
}
export function TableRow({ className, ...props }: ComponentProps<'tr'>) {
  return (
    <tr
      className={cn(
        'h-12 border-t border-border-subtle hover:bg-hover',
        className,
      )}
      {...props}
    />
  );
}
export function TableHead({ className, ...props }: ComponentProps<'th'>) {
  return (
    <th
      scope="col"
      className={cn('h-9 whitespace-nowrap px-4 font-normal', className)}
      {...props}
    />
  );
}
export function TableCell({ className, ...props }: ComponentProps<'td'>) {
  return <td className={cn('px-4', className)} {...props} />;
}
