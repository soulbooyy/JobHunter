import { useQuery } from '@tanstack/react-query';
import { Dialog } from '@/shared/ui/dialog';
import { StatePanel } from '@/shared/ui/state-panel';
import { Button } from '@/shared/ui/button';
import { Skeleton } from '@/shared/ui/skeleton';
import { entryApi } from './api';
import { EntryFormDialog } from './entry-form-dialog';
export function EditEntryDialog({
  id,
  onClose,
  onSaved,
}: {
  id: string;
  onClose: () => void;
  onSaved: (message: string) => void;
}) {
  const query = useQuery({
    queryKey: ['manual-application-entry', id],
    queryFn: () => entryApi.read(id),
    staleTime: 0,
    gcTime: 0,
  });
  if (query.data && !query.isFetching && !query.isError)
    return (
      <EntryFormDialog
        initial={query.data}
        onClose={onClose}
        onSaved={onSaved}
      />
    );
  return (
    <Dialog
      title="编辑手动申请"
      description="读取当前已保存的记录。"
      onClose={onClose}
    >
      {query.isError ? (
        <StatePanel
          error
          title="无法读取这条记录"
          description="记录可能已不存在，或暂时无法读取。"
          action={
            <Button
              onClick={() => void query.refetch()}
              disabled={query.isFetching}
            >
              重试
            </Button>
          }
        />
      ) : (
        <div role="status" className="space-y-6 py-6">
          <span className="sr-only">正在读取</span>
          <Skeleton className="h-10" />
          <Skeleton className="h-10" />
          <Skeleton className="h-10" />
        </div>
      )}
    </Dialog>
  );
}
