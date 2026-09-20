import type { ComponentProps } from 'react';
import { cn } from '@/shared/lib/cn';
export const inputClass =
  'h-10 rounded-md border border-border bg-surface px-3 text-sm placeholder:text-text-muted disabled:bg-surface-muted disabled:text-text-muted read-only:bg-surface-muted';
export function Input({ className, ...props }: ComponentProps<'input'>) {
  return (
    <input
      autoComplete="off"
      className={cn(inputClass, className)}
      {...props}
    />
  );
}
