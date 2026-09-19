import { useRef, useState } from 'react';
import type { ManualApplicationEntry } from '@/entities/manual-application-entry/model';
import { ApiFailure, failureMessage } from '@/shared/api/result';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import { Button } from '@/shared/ui/button';
import { InlineNotice } from '@/shared/ui/inline-notice';
import { SavedEntrySummary } from './saved-entry-summary';
import { entryApi } from './api';
export function DeleteEntryDialog({
  entry,
  onClose,
  onDeleted,
}: {
  entry: ManualApplicationEntry;
  onClose: () => void;
  onDeleted: () => void;
}) {
  const [target, setTarget] = useState(entry);
  const [phase, setPhase] = useState<'confirm' | 'verify' | 'missing'>(
    'confirm',
  );
  const [notice, setNotice] = useState('');
  const [latest, setLatest] = useState<ManualApplicationEntry>();
  const [busy, setBusy] = useState(false);
  const locked = useRef(false);
  async function remove() {
    if (locked.current || phase !== 'confirm') return;
    locked.current = true;
    setBusy(true);
    setNotice('');
    try {
      await entryApi.delete(
        target.manual_application_entry_id,
        target.revision,
      );
      onDeleted();
    } catch (error) {
      const f =
        error instanceof ApiFailure
          ? error
          : new ApiFailure('unknown', 'OUTCOME_UNKNOWN');
      setPhase(
        f.code === 'NOT_FOUND'
          ? 'missing'
          : f.kind === 'unknown' || f.code === 'REVISION_CONFLICT'
            ? 'verify'
            : 'confirm',
      );
      setNotice(
        f.kind === 'unknown'
          ? '暂时无法确认删除结果。请先检查当前状态。'
          : failureMessage(f),
      );
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  async function inspect() {
    if (locked.current) return;
    locked.current = true;
    setBusy(true);
    try {
      setLatest(await entryApi.read(target.manual_application_entry_id));
      setNotice('当前记录仍存在。请查看内容，再决定是否重新确认删除。');
    } catch (error) {
      const f = error as ApiFailure;
      setNotice(
        f.code === 'NOT_FOUND'
          ? '当前记录已不存在；这不代表可以还原先前操作的全部经过。'
          : failureMessage(f),
      );
      if (f.code === 'NOT_FOUND') setPhase('missing');
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  return (
    <AlertDialog
      title="删除这条手动申请？"
      description="删除后，这条记录将被永久移除，无法恢复。"
      onCancel={onClose}
      busy={busy}
      cancelLabel={phase === 'confirm' ? '取消' : '关闭并检查列表'}
      action={
        phase === 'confirm' ? (
          <Button
            variant="destructive"
            disabled={busy}
            onClick={() => void remove()}
          >
            {busy ? '删除中…' : '删除'}
          </Button>
        ) : null
      }
    >
      <p className="rounded-md border border-border bg-surface-muted px-3 py-2 text-sm break-words">
        {target.company_name} · {target.role_title}
      </p>
      {notice && (
        <InlineNotice title={notice}>
          {phase === 'verify' && (
            <Button
              variant="outline"
              onClick={() => void inspect()}
              disabled={busy}
            >
              {busy ? '检查中…' : '检查当前状态'}
            </Button>
          )}
        </InlineNotice>
      )}
      {latest && (
        <>
          <SavedEntrySummary entry={latest} />
          <Button
            variant="outline"
            disabled={busy}
            onClick={() => {
              setTarget(latest);
              setLatest(undefined);
              setPhase('confirm');
              setNotice('请再次确认删除当前显示的记录。');
            }}
          >
            使用当前记录重新确认删除
          </Button>
        </>
      )}
    </AlertDialog>
  );
}
