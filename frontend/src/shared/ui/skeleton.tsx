import type { ComponentProps } from 'react';
import { cn } from '@/shared/lib/cn';
export function Skeleton({ className, ...props }: ComponentProps<'div'>) {
  return (
    <div
      aria-hidden="true"
      className={cn('h-3 rounded bg-active', className)}
      {...props}
    />
  );
}
