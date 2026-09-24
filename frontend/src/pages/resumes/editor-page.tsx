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
    queryFn: async () => ({
      profile: await candidateApi.profile(),
      initial: id ? await candidateApi.resume(id) : undefined,
    }),
    gcTime: 0,
  });
  return (
    <ReadView query={query} label="简历编辑内容">
      {(data) => (
        <ResumeEditor
          key={id ?? 'new'}
          {...data}
          onClose={() => navigate('/resumes')}
        />
      )}
    </ReadView>
  );
}
