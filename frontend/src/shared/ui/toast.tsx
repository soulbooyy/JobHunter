import {
  useCallback,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react';
import { CheckCircle2, CircleAlert, Trash2, X } from 'lucide-react';
import { cn } from '@/shared/lib/cn';
import {
  ToastContext,
  type ToastApi,
  type ToastInput,
  type ToastVariant,
} from './toast-context';

type ToastRecord = ToastInput & { id: number };

const styles: Record<ToastVariant, string> = {
  success:
    'border-toast-success-border bg-toast-success-background text-toast-success-accent',
  delete:
    'border-toast-delete-border bg-toast-delete-background text-toast-delete-accent',
  warning:
    'border-toast-warning-border bg-toast-warning-background text-toast-warning-accent',
};

const icons = {
  success: CheckCircle2,
  delete: Trash2,
  warning: CircleAlert,
} satisfies Record<ToastVariant, typeof CheckCircle2>;

let nextToastId = 0;

function ToastItem({
  toast,
  dismiss,
}: {
  toast: ToastRecord;
  dismiss: (id: number) => void;
}) {
  const Icon = icons[toast.variant];
  const [paused, setPaused] = useState(false);

  // Resetting the timer after hover/focus guarantees time to finish reading.
  useEffect(() => {
    if (paused) return;
    const timer = window.setTimeout(
      () => dismiss(toast.id),
      toast.duration ?? (toast.variant === 'warning' ? 7000 : 5000),
    );
    return () => window.clearTimeout(timer);
  }, [dismiss, paused, toast.duration, toast.id, toast.variant]);

  return (
    <div
      role={toast.variant === 'warning' ? 'alert' : 'status'}
      aria-atomic="true"
      className={cn(
        'toast-enter pointer-events-auto flex min-h-12 w-full items-start gap-3 rounded-md border px-4 py-3 text-sm shadow-lg sm:w-auto sm:min-w-80 sm:max-w-xl',
        styles[toast.variant],
      )}
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
      onFocusCapture={() => setPaused(true)}
      onBlurCapture={(event) => {
        if (!event.currentTarget.contains(event.relatedTarget))
          setPaused(false);
      }}
    >
      <Icon className="mt-0.5 size-4 shrink-0" aria-hidden="true" />
      <p className="min-w-0 flex-1 leading-5 text-foreground">
        {toast.message}
      </p>
      <button
        type="button"
        className="-mr-1 flex size-6 shrink-0 items-center justify-center rounded-sm text-current hover:bg-black/5"
        aria-label="关闭提示"
        onClick={() => dismiss(toast.id)}
      >
        <X className="size-4" aria-hidden="true" />
      </button>
    </div>
  );
}

export function ToastProvider({ children }: { children: ReactNode }) {
  const [toasts, setToasts] = useState<ToastRecord[]>([]);
  const dismiss = useCallback((id: number) => {
    setToasts((current) => current.filter((toast) => toast.id !== id));
  }, []);
  const show = useCallback((toast: ToastInput) => {
    const id = ++nextToastId;
    setToasts((current) => [...current.slice(-2), { ...toast, id }]);
  }, []);
  const value = useMemo<ToastApi>(
    () => ({
      show,
      success: (message) => show({ message, variant: 'success' }),
      deleted: (message) => show({ message, variant: 'delete' }),
      warning: (message) => show({ message, variant: 'warning' }),
    }),
    [show],
  );

  return (
    <ToastContext value={value}>
      {children}
      <div
        aria-label="通知"
        className="pointer-events-none fixed inset-x-4 top-4 z-100 flex flex-col items-center gap-2"
      >
        {toasts.map((toast) => (
          <ToastItem key={toast.id} toast={toast} dismiss={dismiss} />
        ))}
      </div>
    </ToastContext>
  );
}
