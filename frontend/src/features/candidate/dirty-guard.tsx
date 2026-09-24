import { useBlocker } from 'react-router';
import { useEffect, type RefObject } from 'react';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import { Button } from '@/shared/ui/button';
export function DirtyGuard({
  dirty,
  busy,
  unknown = false,
  onSave,
  allowLeave,
}: {
  allowLeave?: RefObject<boolean>;
  dirty: boolean;
  busy: boolean;
  unknown?: boolean;
  onSave?: () => Promise<boolean>;
}) {
  const blocker = useBlocker(
    ({ currentLocation, nextLocation }) =>
      !allowLeave?.current &&
      (dirty || busy || unknown) &&
      currentLocation.pathname !== nextLocation.pathname,
  );
  useEffect(() => {
    if (!dirty && !busy && !unknown) return;
    const warn = (e: BeforeUnloadEvent) => e.preventDefault();
    window.addEventListener('beforeunload', warn);
    return () => window.removeEventListener('beforeunload', warn);
  }, [dirty, busy, unknown]);
  if (blocker.state !== 'blocked') return null;
  return (
    <AlertDialog
      title="离开当前页面？"
      description={
        unknown
          ? '操作结果尚未确认。离开会丢失本次请求的核验信息，不会撤销可能已生效的操作。'
          : '当前修改尚未保存。请选择保存后离开，或放弃本地修改。'
      }
      busy={busy}
      cancelLabel="继续编辑"
      onCancel={() => blocker.reset()}
      action={
        <>
          <Button
            variant="outline"
            disabled={busy}
            onClick={() => blocker.proceed()}
          >
            放弃并离开
          </Button>
          {onSave && !unknown && (
            <Button
              disabled={busy}
              onClick={async () => {
                if (await onSave()) blocker.proceed();
              }}
            >
              保存后离开
            </Button>
          )}
        </>
      }
    />
  );
}
