import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { candidateApi } from '@/features/candidate/api';
import { ReadView } from '@/features/candidate/read-view';
import { ProfileEditor } from '@/features/profile/profile-editor';
import { PageHeader } from '@/shared/ui/page-header';
import { Button } from '@/shared/ui/button';
import { ViewTabs } from '@/shared/ui/view-tabs';
import { knowledgeViews } from './views';
export function ProfilePage() {
  const [editing, setEditing] = useState(false);
  const query = useQuery({
    queryKey: ['candidate', 'profile'],
    queryFn: candidateApi.profile,
    gcTime: 0,
  });
  return (
    <>
      <PageHeader
        title={editing ? '编辑个人信息' : '个人信息'}
        description="维护姓名、电话和邮箱；简历会引用确切的已保存版本。"
        action={
          !editing && (
            <Button
              variant="outline"
              disabled={!query.data}
              onClick={() => setEditing(true)}
            >
              编辑个人信息
            </Button>
          )
        }
      />
      <ViewTabs label="求职资料库视图" items={knowledgeViews} />
      <div className="mt-5">
        <ReadView query={query} label="个人信息">
          {(p) =>
            editing ? (
              <ProfileEditor
                initial={p}
                onClose={() => {
                  setEditing(false);
                  void query.refetch();
                }}
              />
            ) : (
              <div className="max-w-2xl divide-y divide-border-subtle">
                {(['full_name', 'phone_number', 'email'] as const).map((k) => (
                  <div
                    key={k}
                    className="grid grid-cols-[120px_1fr] py-5 text-sm"
                  >
                    <span className="text-text-muted">
                      {
                        {
                          full_name: '姓名',
                          phone_number: '电话',
                          email: '邮箱',
                        }[k]
                      }
                    </span>
                    <span>{p.profile_version[k] ?? '未填写'}</span>
                  </div>
                ))}
              </div>
            )
          }
        </ReadView>
      </div>
    </>
  );
}
