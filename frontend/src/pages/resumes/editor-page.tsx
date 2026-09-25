import { useParams, useNavigate } from 'react-router';
import { useQuery } from '@tanstack/react-query';
import { candidateApi } from '@/features/candidate/api';
import { ReadView } from '@/features/candidate/read-view';
import { ResumeEditor } from '@/features/resume/editor/resume-editor';
export function ResumeEditorPage() {
  const { id } = useParams(),
    navigate = useNavigate();
  const query = useQuery({
    queryKey: ['candidate', 'editor', id ?? 'new'],
    queryFn: () => candidateApi.resume(id!),
    enabled: !!id,
    gcTime: 0,
  });
  if (!id)
    return <ResumeEditor key="new" onClose={() => navigate('/resumes')} />;
  return (
    <ReadView query={query} label="简历编辑内容">
      {(initial) => (
        <ResumeEditor
          key={id ?? 'new'}
          initial={initial ?? undefined}
          onClose={() => navigate('/resumes')}
        />
      )}
    </ReadView>
  );
}
