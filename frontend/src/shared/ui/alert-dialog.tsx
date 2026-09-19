import * as Alert from '@radix-ui/react-alert-dialog';
import { useRef, type ReactNode } from 'react';
import { Button } from './button';
export function AlertDialog({
  title,
  description,
  children,
  onCancel,
  action,
  busy = false,
  cancelLabel = '取消',
}: {
  title: string;
  description: string;
  children?: ReactNode;
  onCancel: () => void;
  action: ReactNode;
  busy?: boolean;
  cancelLabel?: string;
}) {
  const trigger = useRef(document.activeElement as HTMLElement | null);
  return (
    <Alert.Root
      open
      onOpenChange={(open) => {
        if (!open && !busy) onCancel();
      }}
    >
      <Alert.Portal>
        <Alert.Overlay className="fixed inset-0 z-50 bg-black/20" />
        <Alert.Content
          onCloseAutoFocus={(e) => {
            e.preventDefault();
            if (trigger.current?.isConnected) trigger.current.focus();
            else document.getElementById('add-entry')?.focus();
          }}
          className="fixed left-1/2 top-1/2 z-[60] max-h-[90vh] w-[calc(100%-32px)] max-w-[420px] -translate-x-1/2 -translate-y-1/2 overflow-y-auto rounded-lg border border-border bg-surface p-5 shadow-lg"
        >
          <Alert.Title className="text-lg font-semibold">{title}</Alert.Title>
          <Alert.Description className="mt-2 text-sm leading-relaxed text-text-muted">
            {description}
          </Alert.Description>
          {children && <div className="mt-4 space-y-4">{children}</div>}
          <div className="mt-6 flex flex-wrap justify-end gap-2">
            <Alert.Cancel asChild>
              <Button variant="outline" disabled={busy} onClick={onCancel}>
                {cancelLabel}
              </Button>
            </Alert.Cancel>
            {action}
          </div>
        </Alert.Content>
      </Alert.Portal>
    </Alert.Root>
  );
}
