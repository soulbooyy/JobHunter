import { X } from 'lucide-react';
import { Button } from './button';
import { Input } from './input';
export function TagInput({
  id,
  label,
  values,
  pending,
  onPending,
  onAdd,
  onRemove,
  disabled,
  invalid,
  describedBy,
}: {
  id: string;
  label: string;
  values: string[];
  pending: string;
  onPending: (value: string) => void;
  onAdd: () => void;
  onRemove: (index: number) => void;
  disabled?: boolean;
  invalid?: boolean;
  describedBy?: string;
}) {
  return (
    <div className="space-y-3">
      <div className="flex max-w-xl gap-2">
        <Input
          id={id}
          aria-label={label}
          aria-invalid={invalid}
          aria-describedby={describedBy}
          disabled={disabled}
          value={pending}
          onChange={(e) => onPending(e.target.value)}
          className={`min-w-0 flex-1 ${invalid ? 'border-error' : ''}`}
          placeholder={`输入${label}`}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.nativeEvent.isComposing) {
              e.preventDefault();
              onAdd();
            }
          }}
        />
        <Button
          variant="outline"
          disabled={disabled}
          aria-label={`添加${label}`}
          onClick={onAdd}
        >
          添加
        </Button>
      </div>
      {values.length > 0 && (
        <ul aria-label={`${label}已添加项`} className="flex flex-wrap gap-2">
          {values.map((value, index) => (
            <li
              key={`${index}-${value}`}
              className="inline-flex max-w-full items-center gap-1 rounded border border-border bg-surface-muted pl-2 text-xs"
            >
              <span className="break-all">{value}</span>
              <button
                type="button"
                disabled={disabled}
                aria-label={`移除${label}第 ${index + 1} 项：${value}`}
                onClick={() => onRemove(index)}
                className="rounded p-2 hover:bg-hover disabled:opacity-40"
              >
                <X size={12} aria-hidden="true" />
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
