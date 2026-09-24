import type { ReactNode } from 'react';
import { StatePanel } from '@/shared/ui/state-panel';
import { Button } from '@/shared/ui/button';
import { Skeleton } from '@/shared/ui/skeleton';
export function ReadView<T>({
  query,
  children,
  label,
}: {
  query: {
    isPending: boolean;
    isError: boolean;
    data: T | undefined;
    refetch: () => unknown;
  };
  children: (data: T) => ReactNode;
  label: string;
}) {
  if (query.isPending)
    return (
      <div
        role="status"
        aria-label={`正在加载${label}`}
        className="space-y-4 py-8"
      >
        {[1, 2, 3].map((i) => (
          <Skeleton key={i} className="h-20 w-full" />
        ))}
      </div>
    );
  if (query.isError || !query.data)
    return (
      <StatePanel
        error
        title={`无法加载${label}`}
        description="暂时无法读取已保存内容，请重试。"
        action={
          <Button variant="outline" onClick={() => void query.refetch()}>
            重试
          </Button>
        }
      />
    );
  return children(query.data);
}
