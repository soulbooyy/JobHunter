import { Link } from 'react-router';
import { useQuery } from '@tanstack/react-query';
import { ChevronRight } from 'lucide-react';
import { PageHeader } from '@/shared/ui/page-header';
import { ViewTabs } from '@/shared/ui/view-tabs';
import { StatePanel } from '@/shared/ui/state-panel';
import { Skeleton } from '@/shared/ui/skeleton';
import { Button } from '@/shared/ui/button';
import { PreferencesEditor } from '@/features/preferences/preferences-editor';
import { preferencesQuery } from '@/features/preferences/api';
import { jobPoolViews } from '../views';
export function PreferencesPage() {
  const query = useQuery(preferencesQuery);
  return (
    <section aria-labelledby="preferences-title">
      <nav
        aria-label="面包屑"
        className="mb-4 flex items-center gap-2 text-xs text-text-muted"
      >
        <Link to="/job-pool" className="hover:text-foreground">
          岗位池
        </Link>
        <ChevronRight size={12} aria-hidden="true" />
        <span aria-current="page">搜索偏好</span>
      </nav>
      <PageHeader
        id="preferences-title"
        title="搜索偏好"
        description="设置后续岗位收集使用的搜索条件。"
      />
      <ViewTabs items={jobPoolViews} />
      {query.isPending ? (
        <div role="status" aria-label="正在加载搜索偏好" className="space-y-8">
          {Array.from({ length: 6 }, (_, i) => (
            <div
              key={i}
              className="space-y-3 border-b border-border-subtle pb-6"
            >
              <Skeleton className="h-4 w-28" />
              <Skeleton className="h-3 w-60" />
              <Skeleton className="h-10 max-w-xl" />
            </div>
          ))}
        </div>
      ) : query.isError ? (
        <StatePanel
          error
          title="无法加载搜索偏好"
          description="暂时无法读取当前搜索偏好，无法判断是否已经配置。请重试。"
          action={
            <Button
              variant="outline"
              onClick={() => void query.refetch()}
              disabled={query.isFetching}
            >
              {query.isFetching ? '读取中…' : '重试'}
            </Button>
          }
        />
      ) : (
        <PreferencesEditor initial={query.data} />
      )}
    </section>
  );
}
