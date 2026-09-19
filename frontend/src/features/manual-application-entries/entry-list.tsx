import { useQuery } from '@tanstack/react-query';
import {
  MoreHorizontal,
  ExternalLink,
  Pencil,
  Trash2,
  RefreshCw,
} from 'lucide-react';
import type { ManualApplicationEntry } from '@/entities/manual-application-entry/model';
import { Button } from '@/shared/ui/button';
import { StatePanel } from '@/shared/ui/state-panel';
import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableCell,
} from '@/shared/ui/table';
import { Skeleton } from '@/shared/ui/skeleton';
import {
  DropdownMenu,
  MenuItem,
  MenuSeparator,
} from '@/shared/ui/dropdown-menu';
import { manualApplicationEntriesQuery } from './queries';
const columns = ['公司', '岗位', '申请链接', '更新时间', '操作'];
const dateFormat = new Intl.DateTimeFormat('zh-CN', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
});
type Props = {
  onCreate?: () => void;
  onEdit?: (entry: ManualApplicationEntry) => void;
  onDelete?: (entry: ManualApplicationEntry) => void;
  onOpen?: (entry: ManualApplicationEntry) => void;
  openingId?: string;
};
export function EntryList({
  onCreate,
  onEdit,
  onDelete,
  onOpen,
  openingId,
}: Props = {}) {
  const query = useQuery(manualApplicationEntriesQuery);
  if (query.isError)
    return (
      <StatePanel
        error
        title="无法加载手动申请"
        description="暂时无法读取已保存的手动申请，请重试。"
        action={
          <Button
            variant="outline"
            disabled={query.isFetching}
            onClick={() => void query.refetch()}
          >
            <RefreshCw aria-hidden="true" />
            {query.isFetching ? '正在重试…' : '重试'}
          </Button>
        }
      />
    );
  if (query.isSuccess && query.data.length === 0)
    return (
      <StatePanel
        title="还没有手动申请"
        description="保存你想稍后继续访问的岗位申请链接。"
        action={onCreate && <Button onClick={onCreate}>添加申请</Button>}
      />
    );
  return (
    <div aria-busy={query.isPending}>
      {query.isPending && (
        <span role="status" className="sr-only">
          正在加载手动申请
        </span>
      )}
      <Table className="min-w-[700px]">
        <caption className="sr-only">已保存的手动申请</caption>
        <colgroup>
          <col className="w-[17%]" />
          <col className="w-[23%]" />
          <col className="w-[34%]" />
          <col className="w-[18%]" />
          <col className="w-[8%]" />
        </colgroup>
        <TableHeader>
          <tr>
            {columns.map((label) => (
              <TableHead
                key={label}
                className={label === '操作' ? 'text-right' : undefined}
              >
                {label}
              </TableHead>
            ))}
          </tr>
        </TableHeader>
        <tbody>
          {query.isPending
            ? Array.from({ length: 5 }, (_, i) => (
                <TableRow key={i} aria-hidden="true">
                  {columns.map((label) => (
                    <TableCell key={label}>
                      <Skeleton className="w-3/4" />
                    </TableCell>
                  ))}
                </TableRow>
              ))
            : query.data?.map((entry) => (
                <TableRow key={entry.manual_application_entry_id}>
                  <TableCell
                    className="truncate font-medium"
                    title={entry.company_name}
                  >
                    {entry.company_name}
                  </TableCell>
                  <TableCell className="truncate" title={entry.role_title}>
                    {entry.role_title}
                  </TableCell>
                  <TableCell
                    className="truncate text-text-muted"
                    title={entry.application_url}
                  >
                    {onOpen ? (
                      <button
                        type="button"
                        className="block max-w-full truncate text-left hover:underline disabled:opacity-50"
                        onClick={() => onOpen(entry)}
                        disabled={
                          openingId === entry.manual_application_entry_id
                        }
                        aria-label={`打开 ${entry.company_name} 的申请页面`}
                      >
                        {entry.application_url}
                      </button>
                    ) : (
                      entry.application_url
                    )}
                  </TableCell>
                  <TableCell className="text-xs text-text-muted">
                    <time dateTime={entry.updated_at} title={entry.updated_at}>
                      {dateFormat.format(new Date(entry.updated_at))}
                    </time>
                  </TableCell>
                  <TableCell className="text-right">
                    {onEdit && onDelete && onOpen && (
                      <DropdownMenu
                        trigger={
                          <Button
                            variant="ghost"
                            className="size-8 px-0"
                            aria-label={`${entry.company_name}的更多操作`}
                            disabled={!!openingId}
                          >
                            <MoreHorizontal aria-hidden="true" />
                          </Button>
                        }
                      >
                        <MenuItem onSelect={() => onOpen(entry)}>
                          <ExternalLink size={14} aria-hidden="true" />
                          打开申请页面
                        </MenuItem>
                        <MenuItem onSelect={() => onEdit(entry)}>
                          <Pencil size={14} aria-hidden="true" />
                          编辑
                        </MenuItem>
                        <MenuSeparator />
                        <MenuItem destructive onSelect={() => onDelete(entry)}>
                          <Trash2 size={14} aria-hidden="true" />
                          删除
                        </MenuItem>
                      </DropdownMenu>
                    )}
                  </TableCell>
                </TableRow>
              ))}
        </tbody>
      </Table>
    </div>
  );
}
