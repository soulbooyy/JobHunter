import { useState } from 'react';
import { Link } from 'react-router';
import { useQuery } from '@tanstack/react-query';
import { ChevronDown, ChevronUp, Plus } from 'lucide-react';
import { candidateApi } from '@/features/candidate/api';
import { ReadView } from '@/features/candidate/read-view';
import { CandidateActionDialog } from '@/features/candidate/action-dialog';
import {
  evidenceName,
  kinds,
  kindLabels,
  type EvidenceKind,
  type EvidenceProjection,
  type EvidencePair,
} from '@/entities/evidence/model';
import { PageHeader } from '@/shared/ui/page-header';
import { StatePanel } from '@/shared/ui/state-panel';
import { ViewTabs } from '@/shared/ui/view-tabs';
import { Input } from '@/shared/ui/input';
import { Button } from '@/shared/ui/button';
import { Dialog } from '@/shared/ui/dialog';
import { knowledgeViews } from './views';
function EvidenceRow({
  item,
  onRetire,
}: {
  item: EvidenceProjection;
  onRetire: (p: EvidencePair) => void;
}) {
  const [open, setOpen] = useState(false);
  const detail = useQuery({
    queryKey: [
      'candidate',
      'evidence-version',
      item.current_evidence_item_version_id,
    ],
    queryFn: () =>
      candidateApi.evidenceVersion(item.current_evidence_item_version_id),
    enabled: open,
    gcTime: 0,
  });
  return (
    <article className="border-b border-border-subtle py-5">
      <div className="flex items-center justify-between gap-3">
        <button
          type="button"
          className="flex min-w-0 flex-1 items-center gap-3 text-left"
          aria-expanded={open}
          onClick={() => setOpen(!open)}
        >
          {open ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          <div>
            <h3 className="break-words text-sm font-semibold">
              {evidenceName(item.fields)}
            </h3>
            <p className="mt-1 text-xs text-text-muted">
              {Object.entries(item.fields)
                .filter(
                  ([k, v]) =>
                    v &&
                    [
                      'role_title',
                      'major',
                      'start_month',
                      'end_month',
                      'degree',
                    ].includes(k),
                )
                .map(([, v]) => v)
                .join(' · ')}
            </p>
          </div>
        </button>
        <Button variant="ghost" asChild>
          <Link
            to={`/candidate-knowledge/evidence/${item.evidence_item.evidence_item_id}/edit`}
          >
            编辑
          </Link>
        </Button>
        <Button
          variant="ghost"
          onClick={async () => {
            setOpen(true);
            const result = await detail.refetch();
            if (result.data)
              onRetire({
                evidence_item: item.evidence_item,
                evidence_item_version: result.data.evidence_item_version,
              });
          }}
        >
          移除
        </Button>
      </div>
      {open && (
        <div className="mt-4 pl-7">
          <ReadView query={detail} label="资料内容">
            {(d) => (
              <div className="space-y-2 break-words text-sm leading-relaxed">
                {d.evidence_item_version.content.length === 0 ? (
                  <p className="text-text-muted">未添加详细内容</p>
                ) : (
                  d.evidence_item_version.content.map((b, i) =>
                    b.type === 'PARAGRAPH' ? (
                      <p key={i}>{b.text}</p>
                    ) : b.type === 'ORDERED_LIST' ? (
                      <ol key={i} className="list-decimal pl-5">
                        {b.items.map((s, j) => (
                          <li key={j}>{s}</li>
                        ))}
                      </ol>
                    ) : (
                      <ul key={i} className="list-disc pl-5">
                        {b.items.map((s, j) => (
                          <li key={j}>{s}</li>
                        ))}
                      </ul>
                    ),
                  )
                )}
              </div>
            )}
          </ReadView>
        </div>
      )}
    </article>
  );
}
export function KnowledgePage() {
  const query = useQuery({
    queryKey: ['candidate', 'evidence-list'],
    queryFn: candidateApi.evidence,
    gcTime: 0,
  });
  const [kind, setKind] = useState<EvidenceKind>('WORK_EXPERIENCE'),
    [search, setSearch] = useState(''),
    [choose, setChoose] = useState(false),
    [retire, setRetire] = useState<EvidencePair>();
  return (
    <>
      <PageHeader
        title="求职资料库"
        description="统一维护经历事实，供不同简历选择和引用。"
        action={
          <Button onClick={() => setChoose(true)}>
            <Plus size={15} />
            添加资料
          </Button>
        }
      />
      <ViewTabs label="求职资料库视图" items={knowledgeViews} />
      <div
        className="mt-5 flex flex-wrap gap-2"
        role="group"
        aria-label="资料分类"
      >
        {kinds.map((k) => (
          <Button
            key={k}
            variant="outline"
            className={k === kind ? 'bg-surface-muted font-medium' : ''}
            aria-pressed={k === kind}
            onClick={() => setKind(k)}
          >
            {kindLabels[k]}
            {query.data &&
              ` ${query.data.evidence_items.filter((i) => i.evidence_item.kind === k).length}`}
          </Button>
        ))}
      </div>
      <div className="mt-5 flex flex-wrap justify-between gap-3">
        <Input
          aria-label="搜索经历资料"
          className="w-full sm:w-80"
          placeholder="搜索当前分类的名称、组织或角色"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <Button variant="outline" asChild>
          <Link to={`/candidate-knowledge/evidence/new/${kind}`}>
            添加{kindLabels[kind]}
          </Link>
        </Button>
      </div>
      <ReadView query={query} label="经历资料">
        {(data) => {
          const items = data.evidence_items.filter(
            (i) =>
              i.evidence_item.kind === kind &&
              Object.values(i.fields).some(
                (v) =>
                  typeof v === 'string' &&
                  v.toLocaleLowerCase().includes(search.toLocaleLowerCase()),
              ),
          );
          return items.length ? (
            <div className="mt-4">
              {items.map((i) => (
                <EvidenceRow
                  key={i.evidence_item.evidence_item_id}
                  item={i}
                  onRetire={setRetire}
                />
              ))}
            </div>
          ) : (
            <StatePanel
              title={
                search
                  ? '没有找到匹配资料'
                  : data.evidence_items.length
                    ? `还没有${kindLabels[kind]}`
                    : '还没有经历资料'
              }
              description={
                search
                  ? '请尝试其他搜索内容。'
                  : '添加已确认的经历事实，之后可在简历中引用。'
              }
              action={
                search ? (
                  <Button variant="outline" onClick={() => setSearch('')}>
                    清除搜索
                  </Button>
                ) : (
                  <Button onClick={() => setChoose(true)}>添加资料</Button>
                )
              }
            />
          );
        }}
      </ReadView>
      {choose && (
        <Dialog
          title="添加资料"
          description="选择需要添加的资料类型。"
          onClose={() => setChoose(false)}
        >
          <div className="mt-5 grid grid-cols-2 gap-3">
            {kinds.map((k) => (
              <Button key={k} variant="outline" asChild>
                <Link to={`/candidate-knowledge/evidence/new/${k}`}>
                  {kindLabels[k]}
                </Link>
              </Button>
            ))}
          </div>
        </Dialog>
      )}
      {retire && (
        <CandidateActionDialog
          action="retire"
          target={retire}
          onClose={() => setRetire(undefined)}
          onChanged={() => void query.refetch()}
        />
      )}
    </>
  );
}
