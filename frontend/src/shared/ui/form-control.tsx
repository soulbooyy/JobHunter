import { useId, type ReactNode } from 'react';
import { Input, inputClass } from './input';
export function FormControl({
  label,
  value,
  onChange,
  nullable = false,
  required = false,
  type = 'text',
  error,
  disabled = false,
  options,
  help,
}: {
  label: string;
  value: string | null;
  onChange: (v: string | null) => void;
  nullable?: boolean;
  required?: boolean;
  type?: string;
  error?: string;
  disabled?: boolean;
  options?: Record<string, string>;
  help?: string;
}) {
  const id = useId();
  return (
    <div className="space-y-2">
      <label htmlFor={id} className="block text-sm font-medium">
        {label}
        {required && <span className="ml-1 text-destructive">*</span>}
      </label>
      <div className="flex items-center gap-2">
        {options ? (
          <select
            id={id}
            className={inputClass + ' w-full min-w-0'}
            value={value ?? ''}
            onChange={(e) => onChange(e.target.value)}
            disabled={disabled}
            aria-invalid={!!error}
            aria-describedby={error ? id + '-error' : undefined}
          >
            <option value="">请选择</option>
            {Object.entries(options).map(([v, l]) => (
              <option key={v} value={v}>
                {l}
              </option>
            ))}
          </select>
        ) : (
          <Input
            className="w-full min-w-0"
            id={id}
            type={type}
            value={value ?? ''}
            disabled={disabled}
            required={required}
            aria-invalid={!!error}
            aria-describedby={error ? id + '-error' : undefined}
            onChange={(e) =>
              onChange(
                nullable && e.target.value === '' ? null : e.target.value,
              )
            }
          />
        )}
      </div>
      {help && <p className="text-xs text-text-muted">{help}</p>}
      {error && (
        <p id={id + '-error'} className="text-xs text-destructive">
          {error}
        </p>
      )}
    </div>
  );
}
export function FormSection({
  title,
  children,
  action,
}: {
  title: string;
  children: ReactNode;
  action?: ReactNode;
}) {
  return (
    <section className="space-y-4 border-b border-border-subtle py-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <h2 className="text-sm font-semibold">{title}</h2>
        {action}
      </div>
      {children}
    </section>
  );
}
