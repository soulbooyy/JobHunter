import { useState } from 'react';
import { useNavigate, useParams } from 'react-router';
import { useQuery } from '@tanstack/react-query';
import { candidateApi } from '@/features/candidate/api';
import { ReadView } from '@/features/candidate/read-view';
import { EvidenceEditor } from '@/features/evidence/evidence-editor';
import {
  kinds,
  kindLabels,
  type EvidenceKind,
} from '@/entities/evidence/model';
import { PageHeader } from '@/shared/ui/page-header';
import { StatePanel } from '@/shared/ui/state-panel';
export function EvidencePage() {
  const [created, setCreated] = useState(false);
  const { id, kind } = useParams(),
    navigate = useNavigate();
  const query = useQuery({
    queryKey: ['candidate', 'evidence', id],
    queryFn: () => candidateApi.evidenceItem(id!),
    enabled: !!id,
    gcTime: 0,
  });
  const close = () => navigate('/candidate-knowledge');
  if (!id && !kinds.includes(kind as EvidenceKind))
    return (
      <StatePanel
        title="找不到此资料类型"
        description="请从资料库选择资料类型。"
      />
    );
  return (
    <>
      <PageHeader
        title={
          id || created
            ? '编辑经历资料'
            : `添加${kindLabels[kind as EvidenceKind]}`
        }
        description="保存到资料库后，可在简历中选择引用。"
      />
      {id ? (
        <ReadView query={query} label="经历资料">
          {(p) => (
            <EvidenceEditor
              key={p.evidence_item.evidence_item_id}
              kind={p.evidence_item.kind}
              initial={p}
              onClose={close}
              onSaved={() => setCreated(true)}
            />
          )}
        </ReadView>
      ) : (
        <EvidenceEditor
          key={kind}
          kind={kind as EvidenceKind}
          onClose={close}
          onSaved={() => setCreated(true)}
        />
      )}
    </>
  );
}
