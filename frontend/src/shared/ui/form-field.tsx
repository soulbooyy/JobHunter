import { useId, type ComponentProps } from 'react';
import { cn } from '@/shared/lib/cn';
export function FormField({
  label,
  error,
  className,
  ...props
}: ComponentProps<'input'> & { label: string; error?: string }) {
  const id = useId();
  return (
    <div>
      <label htmlFor={id} className="mb-2 block text-sm font-medium">
        {label}
        <span className="ml-1 text-error" aria-hidden="true">
          *
        </span>
      </label>
      <input
        id={id}
        aria-required="true"
        aria-invalid={!!error}
        aria-describedby={error ? `${id}-error` : undefined}
        className={cn(
          'h-10 w-full rounded-md border border-border bg-surface px-3 text-sm placeholder:text-text-muted read-only:bg-surface-muted',
          error && 'border-error',
          className,
        )}
        autoComplete="off"
        {...props}
      />
      {error && (
        <p id={`${id}-error`} className="mt-1 text-xs text-error">
          {error}
        </p>
      )}
    </div>
  );
}
