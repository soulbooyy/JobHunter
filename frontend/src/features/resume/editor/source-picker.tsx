import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { candidateApi } from '@/features/candidate/api';
import { ReadView } from '@/features/candidate/read-view';
import { Dialog } from '@/shared/ui/dialog';
import { Input } from '@/shared/ui/input';
import { Button } from '@/shared/ui/button';
import {
  evidenceName,
  kindLabels,
  type EvidenceKind,
  type EvidencePair,
} from '@/entities/evidence/model';
export function SourcePicker({
  kind,
  selected,
  onClose,
  onAdd,
  onCreate,
}: {
  kind: EvidenceKind;
  selected: string[];
  onClose: () => void;
  onAdd: (items: EvidencePair[]) => void;
  onCreate: () => void;
}) {
  const query = useQuery({
      queryKey: ['candidate', 'picker', kind],
      queryFn: candidateApi.evidence,
      gcTime: 0,
    }),
    [chosen, setChosen] = useState<string[]>([]),
    [search, setSearch] = useState(''),
    [busy, setBusy] = useState(false),
    [error, setError] = useState('');
  async function add() {
    if (busy) return;
    setBusy(true);
    try {
      const items = await Promise.all(
        chosen.map(async (id) => {
          const projection = query.data!.evidence_items.find(
            (i) => i.evidence_item.evidence_item_id === id,
          )!;
          const exact = await candidateApi.evidenceVersion(
            projection.current_evidence_item_version_id,
          );
          if (
            exact.evidence_item_version.evidence_item_id !== id ||
            exact.kind !== kind
          )
            throw Error('source mismatch');
          return {
            evidence_item: projection.evidence_item,
            evidence_item_version: exact.evidence_item_version,
          };
        }),
      );
      onAdd(items);
    } catch {
      setError('无法读取所选资料的完整内容，请重试。');
    } finally {
      setBusy(false);
    }
  }
  return (
    <Dialog
      title={`添加${kindLabels[kind]}`}
      description="选择已有资料，首次添加会将来源内容复制为简历中的本地表达。"
      onClose={onClose}
      busy={busy}
    >
      <div className="mt-4 space-y-4">
        <Input
          aria-label="搜索可选资料"
          placeholder="搜索资料名称"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <ReadView query={query} label="可选资料">
          {(data) => (
            <div className="max-h-80 space-y-2 overflow-y-auto">
              {data.evidence_items
                .filter(
                  (i) =>
                    i.evidence_item.kind === kind &&
                    evidenceName(i.fields).includes(search),
                )
                .map((i) => {
                  const id = i.evidence_item.evidence_item_id;
                  return (
                    <label
                      key={id}
                      className="flex items-center gap-3 rounded border border-border p-3 text-sm"
                    >
                      <input
                        type="checkbox"
                        disabled={busy || selected.includes(id)}
                        checked={selected.includes(id) || chosen.includes(id)}
                        onChange={(e) =>
                          setChosen(
                            e.target.checked
                              ? [...chosen, id]
                              : chosen.filter((v) => v !== id),
                          )
                        }
                      />
                      {evidenceName(i.fields)}
                      {selected.includes(id) && (
                        <span className="ml-auto text-xs text-text-muted">
                          已添加
                        </span>
                      )}
                    </label>
                  );
                })}
              {!data.evidence_items.some(
                (i) => i.evidence_item.kind === kind,
              ) && (
                <p className="py-5 text-center text-sm text-text-muted">
                  暂无此类资料
                </p>
              )}
            </div>
          )}
        </ReadView>
        {error && (
          <p role="alert" className="text-sm text-destructive">
            {error}
          </p>
        )}
        <div className="flex flex-wrap justify-between gap-3">
          <Button variant="outline" disabled={busy} onClick={onCreate}>
            新建{kindLabels[kind]}
          </Button>
          <Button
            disabled={busy || chosen.length === 0}
            onClick={() => void add()}
          >
            添加到简历 ({chosen.length})
          </Button>
        </div>
      </div>
    </Dialog>
  );
}
