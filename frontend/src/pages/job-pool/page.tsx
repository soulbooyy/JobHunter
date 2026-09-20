import { Link } from 'react-router';
import { ExternalLink } from 'lucide-react';
import { PageHeader } from '@/shared/ui/page-header';
import { Button } from '@/shared/ui/button';
export function JobPoolPage() {
  return (
    <section>
      <PageHeader
        title="岗位池"
        description="查看和管理手动申请链接与搜索偏好。"
      />
      <Button asChild className="mt-6">
        <Link to="/job-pool/manual-application-entries">
          <ExternalLink aria-hidden="true" />
          手动申请
        </Link>
      </Button>
      <Button asChild variant="outline" className="ml-3 mt-6">
        <Link to="/job-pool/preferences">搜索偏好</Link>
      </Button>
    </section>
  );
}
