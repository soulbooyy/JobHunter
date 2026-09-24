import { useState } from 'react';
import { Link } from 'react-router';
import { useQuery } from '@tanstack/react-query';
import { candidateApi } from '@/features/candidate/api';
import { ReadView } from '@/features/candidate/read-view';
import { CandidateActionDialog } from '@/features/candidate/action-dialog';
import type { Resume } from '@/entities/resume/model';
import { Button } from '@/shared/ui/button';
import { PageHeader } from '@/shared/ui/page-header';
import { StatePanel } from '@/shared/ui/state-panel';
export function ResumesPage() {
  const query = useQuery({
    queryKey: ['candidate', 'resume-list'],
    queryFn: candidateApi.resumes,
    gcTime: 0,
  });
  const [action, setAction] = useState<{
    action: 'rename' | 'remove' | 'default';
    target: Resume;
  }>();
  return (
    <>
      <PageHeader
        title="我的简历"
        description="基于求职资料创建不同版本的简历，独立维护表达与排版。"
        action={
          <Button asChild>
            <Link to="/resumes/new">新建简历</Link>
          </Button>
        }
      />
      <ReadView query={query} label="我的简历">
        {(list) => (
          <>
            {list.resumes.length ? (
              <div className="divide-y divide-border-subtle">
                {list.resumes.map((r) => (
                  <article
                    key={r.resume_id}
                    className="group relative flex flex-wrap items-center justify-between gap-4 rounded-md py-6 hover:bg-surface-muted/50"
                  >
                    <div>
                      <h2 className="text-sm font-semibold">
                        <Link
                          to={`/resumes/${r.resume_id}/edit`}
                          className="after:absolute after:inset-0 focus-visible:outline-none focus-visible:after:ring-2 focus-visible:after:ring-primary/40"
                        >
                          {r.resume_name}
                        </Link>
                        {r.resume_id ===
                          list.default_resume_selection.default_resume_id && (
                          <span className="ml-3 rounded border border-border px-2 py-0.5 text-xs font-normal text-text-muted">
                            默认简历
                          </span>
                        )}
                      </h2>
                      <p className="mt-2 text-xs text-text-muted">
                        更新于 {new Date(r.updated_at).toLocaleString('zh-CN')}
                      </p>
                    </div>
                    <div className="relative z-10 flex flex-wrap gap-2">
                      <Button
                        variant="ghost"
                        onClick={() =>
                          setAction({ action: 'rename', target: r })
                        }
                      >
                        重命名
                      </Button>
                      {r.resume_id !==
                        list.default_resume_selection.default_resume_id && (
                        <Button
                          variant="ghost"
                          onClick={() =>
                            setAction({ action: 'default', target: r })
                          }
                        >
                          设为默认
                        </Button>
                      )}
                      <Button
                        variant="ghost"
                        onClick={() =>
                          setAction({ action: 'remove', target: r })
                        }
                      >
                        移除
                      </Button>
                    </div>
                  </article>
                ))}
              </div>
            ) : (
              <StatePanel
                title="还没有简历"
                description="可以先创建空白简历，再选择资料并完善内容。"
                action={
                  <Button asChild>
                    <Link to="/resumes/new">新建简历</Link>
                  </Button>
                }
              />
            )}{' '}
            {action && (
              <CandidateActionDialog
                {...action}
                list={list}
                onClose={() => setAction(undefined)}
                onChanged={() => void query.refetch()}
              />
            )}
          </>
        )}
      </ReadView>
    </>
  );
}
