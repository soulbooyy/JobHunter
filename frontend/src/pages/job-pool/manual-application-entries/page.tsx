import { useRef, useState } from 'react';
import { Link } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import { ChevronRight, Plus, RefreshCw, X } from 'lucide-react';
import type { ManualApplicationEntry } from '@/entities/manual-application-entry/model';
import { EntryList } from '@/features/manual-application-entries/entry-list';
import { EntryFormDialog } from '@/features/manual-application-entries/entry-form-dialog';
import { EditEntryDialog } from '@/features/manual-application-entries/edit-entry-dialog';
import { DeleteEntryDialog } from '@/features/manual-application-entries/delete-entry-dialog';
import { openEntry } from '@/features/manual-application-entries/open-entry';
import { manualApplicationEntriesQuery } from '@/features/manual-application-entries/queries';
import { Button } from '@/shared/ui/button';
import { PageHeader } from '@/shared/ui/page-header';
import { ViewTabs } from '@/shared/ui/view-tabs';
import { jobPoolViews } from '../views';
type Action =
  | { kind: 'create' }
  | { kind: 'edit'; id: string }
  | { kind: 'delete'; entry: ManualApplicationEntry };
export function ManualApplicationEntriesPage() {
  const client = useQueryClient();
  const [action, setAction] = useState<Action>();
  const [message, setMessage] = useState('');
  const [openingId, setOpeningId] = useState<string>();
  const opening = useRef(false);
  function refresh() {
    void client.invalidateQueries({
      queryKey: manualApplicationEntriesQuery.queryKey,
    });
  }
  function done(text: string) {
    setAction(undefined);
    setMessage(text);
    refresh();
  }
  async function navigate(entry: ManualApplicationEntry) {
    if (opening.current) return;
    opening.current = true;
    setOpeningId(entry.manual_application_entry_id);
    setMessage('正在核验申请链接…');
    try {
      setMessage(await openEntry(entry));
    } finally {
      opening.current = false;
      setOpeningId(undefined);
    }
  }
  return (
    <section aria-labelledby="page-title">
      <nav
        aria-label="面包屑"
        className="mb-4 flex items-center gap-2 text-xs text-text-muted"
      >
        <Link to="/job-pool" className="hover:text-foreground">
          岗位池
        </Link>
        <ChevronRight size={12} aria-hidden="true" />
        <span aria-current="page">手动申请</span>
      </nav>
      <PageHeader
        id="page-title"
        title="手动申请"
        description="保存和管理需要手动访问的岗位申请链接。"
        action={
          <Button
            id="add-entry"
            onClick={() => {
              setMessage('');
              setAction({ kind: 'create' });
            }}
          >
            <Plus aria-hidden="true" />
            添加申请
          </Button>
        }
      />
      <ViewTabs
        items={jobPoolViews}
        action={
          <Button variant="ghost" onClick={refresh}>
            <RefreshCw aria-hidden="true" />
            刷新列表
          </Button>
        }
      />
      {message && (
        <div
          role="status"
          className="mb-4 flex items-center justify-between gap-3 rounded-md border border-border bg-surface-muted px-3 py-2 text-sm"
        >
          <p>{message}</p>
          <Button
            variant="ghost"
            className="size-7 shrink-0 px-0"
            aria-label="关闭提示"
            onClick={() => setMessage('')}
          >
            <X aria-hidden="true" />
          </Button>
        </div>
      )}
      <EntryList
        onCreate={() => setAction({ kind: 'create' })}
        onEdit={(entry) =>
          setAction({ kind: 'edit', id: entry.manual_application_entry_id })
        }
        onDelete={(entry) => setAction({ kind: 'delete', entry })}
        onOpen={(entry) => void navigate(entry)}
        openingId={openingId}
      />
      <p className="mt-5 text-xs leading-relaxed text-text-muted">
        若上次操作中断或结果未确认，请先检查列表，避免重复添加。
      </p>
      {action?.kind === 'create' && (
        <EntryFormDialog onClose={() => setAction(undefined)} onSaved={done} />
      )}
      {action?.kind === 'edit' && (
        <EditEntryDialog
          id={action.id}
          onClose={() => setAction(undefined)}
          onSaved={done}
        />
      )}
      {action?.kind === 'delete' && (
        <DeleteEntryDialog
          entry={action.entry}
          onClose={() => {
            setAction(undefined);
            refresh();
          }}
          onDeleted={() => done('手动申请已删除')}
        />
      )}
    </section>
  );
}
