import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router';
import { RefreshCw } from 'lucide-react';
import { candidateApi } from '@/features/candidate/api';
import { useCandidateCommand } from '@/features/candidate/use-command';
import { CommandFeedback } from '@/features/candidate/command-feedback';
import { ReadView } from '@/features/candidate/read-view';
import {
  kindLabels,
  entryName,
  type ResumeVersion,
} from '@/entities/resume/model';
import { portraitFailureLabels } from '@/entities/profile/model';
import { Button } from '@/shared/ui/button';
import { PageHeader } from '@/shared/ui/page-header';
import { StatePanel } from '@/shared/ui/state-panel';

function sourceEntry(version: ResumeVersion | undefined, entryId: string) {
  if (!version) return undefined;
  for (const section of version.sections) {
    const entry = section.members.find((member) => member.entry_id === entryId);
    if (entry) return { kind: section.kind, entry };
  }
}
const statusText = {
  QUEUED: {
    title: '用户画像已排队',
    description:
      '画像生成尚未完成。重新加载页面只会读取状态，不会重复发起生成。',
  },
  RUNNING: {
    title: '正在生成用户画像',
    description: '当前画像暂不可用。你可以继续编辑简历，保存不会等待生成完成。',
  },
} as const;

export function KnowledgePage() {
  const query = useQuery({
    queryKey: ['candidate', 'portrait'],
    queryFn: candidateApi.portrait,
    gcTime: 0,
  });
  const sourceId = query.data?.state.source_resume_version_id;
  const sourceQuery = useQuery({
    queryKey: ['candidate', 'portrait-source', sourceId],
    queryFn: () => candidateApi.resumeVersion(sourceId!),
    enabled: !!sourceId,
    gcTime: 0,
  });
  const resumes = useQuery({
    queryKey: ['candidate', 'resume-list'],
    queryFn: candidateApi.resumes,
    gcTime: 0,
  });
  const refresh = useCandidateCommand(
    candidateApi.refreshPortrait,
    async () => {
      await query.refetch();
    },
    { message: '用户画像已提交重新生成', variant: 'success' },
  );
  const state = query.data?.state;
  const sourceResume = resumes.data?.resumes.find(
    (resume) => resume.current_resume_version_id === sourceId,
  );
  function requestRefresh() {
    if (!state?.source_resume_version_id) return;
    void refresh.execute({
      request_id: crypto.randomUUID(),
      default_resume_selection: {
        revision: state.default_resume_selection.revision,
      },
      source_resume_version_id: state.source_resume_version_id,
    });
  }
  return (
    <>
      <PageHeader
        title="用户画像"
        description="根据默认简历生成的只读能力索引；每项能力都保留其来源经历。"
        action={
          state?.source_resume_version_id &&
          state.status !== 'EMPTY_SOURCE' && (
            <Button
              variant="outline"
              disabled={refresh.disabled}
              onClick={requestRefresh}
            >
              <RefreshCw size={15} aria-hidden="true" />
              {refresh.busy ? '提交中…' : '重新生成'}
            </Button>
          )
        }
      />
      <CommandFeedback command={refresh} inspect={() => void query.refetch()} />
      <ReadView query={query} label="用户画像">
        {(data) => {
          const current = data.state;
          const editAction = sourceResume ? (
            <Button asChild variant="outline">
              <Link to={`/resumes/${sourceResume.resume_id}/edit`}>
                编辑来源简历
              </Link>
            </Button>
          ) : undefined;
          if (current.status === 'NO_SOURCE')
            return (
              <StatePanel
                title="还没有画像来源"
                description="创建第一份简历后，它会成为默认简历和用户画像来源。"
                action={
                  <Button asChild>
                    <Link to="/resumes/new">新建简历</Link>
                  </Button>
                }
              />
            );
          if (current.status === 'EMPTY_SOURCE')
            return (
              <StatePanel
                title="默认简历还没有经历"
                description="基本信息不会生成能力画像。请先在默认简历中添加一条结构化经历。"
                action={editAction}
              />
            );
          if (current.status === 'QUEUED' || current.status === 'RUNNING')
            return (
              <StatePanel {...statusText[current.status]} action={editAction} />
            );
          if (current.status === 'FAILED')
            return (
              <StatePanel
                title="用户画像暂不可用"
                description={
                  current.failure_code
                    ? portraitFailureLabels[current.failure_code]
                    : '生成未完成，请稍后重试。'
                }
                action={
                  <div className="flex flex-wrap justify-center gap-2">
                    {editAction}
                    <Button
                      disabled={refresh.disabled}
                      onClick={requestRefresh}
                    >
                      重新生成
                    </Button>
                  </div>
                }
              />
            );
          if (!data.portrait)
            return (
              <StatePanel
                title="用户画像暂不可用"
                description="服务没有返回完整的当前画像。"
                action={
                  <Button
                    variant="outline"
                    onClick={() => void query.refetch()}
                  >
                    重新读取
                  </Button>
                }
              />
            );
          return (
            <div className="mt-6 space-y-5">
              <div className="flex flex-wrap items-center justify-between gap-3 rounded-md border border-border bg-surface-muted p-4 text-sm">
                <div>
                  <p className="font-medium">
                    来源：{sourceResume?.resume_name ?? '默认简历'}
                  </p>
                  <p className="mt-1 text-xs text-text-muted">
                    当前画像包含 {data.portrait.profile.entries.length}{' '}
                    项能力；同名能力按来源经历分别保留。
                  </p>
                </div>
                {editAction}
              </div>
              {sourceQuery.isError && (
                <p role="alert" className="text-sm text-destructive">
                  无法读取来源简历详情，能力内容仍保持只读。
                </p>
              )}
              {data.portrait.profile.entries.length ? (
                <div className="grid gap-4 lg:grid-cols-2">
                  {data.portrait.profile.entries.map((profileEntry, index) => {
                    const source = sourceEntry(
                      sourceQuery.data,
                      profileEntry.source_entry_id,
                    );
                    const evidence = profileEntry.evidence_refs
                      .map((reference) =>
                        data.portrait!.evidence.blocks.find(
                          (block) =>
                            block.evidence_id === reference.evidence_id,
                        ),
                      )
                      .filter((item) => item !== undefined);
                    return (
                      <article
                        key={`${profileEntry.source_entry_id}:${index}`}
                        className="rounded-md border border-border p-4"
                      >
                        <h2 className="font-semibold">{profileEntry.name}</h2>
                        <p className="mt-2 text-sm leading-relaxed">
                          {profileEntry.description}
                        </p>
                        <div className="mt-4 border-t border-border-subtle pt-3 text-xs text-text-muted">
                          <p>
                            来源：
                            {source
                              ? `${kindLabels[source.kind]} · ${entryName(source.entry.fields)}`
                              : '来源经历'}
                          </p>
                          {evidence.length > 0 && (
                            <ul className="mt-2 space-y-1">
                              {evidence.map((item) => (
                                <li key={item!.evidence_id}>{item!.text}</li>
                              ))}
                            </ul>
                          )}
                        </div>
                      </article>
                    );
                  })}
                </div>
              ) : (
                <StatePanel
                  title="当前画像没有可展示的能力"
                  description="这不表示候选人缺少能力，只表示当前画像未形成受支持的索引项。"
                  action={editAction}
                />
              )}
            </div>
          );
        }}
      </ReadView>
    </>
  );
}
