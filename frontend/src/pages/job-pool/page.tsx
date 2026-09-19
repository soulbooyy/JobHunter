import { Link } from 'react-router';
import { ExternalLink } from 'lucide-react';
import { PageHeader } from '@/shared/ui/page-header';
import { Button } from '@/shared/ui/button';
export function JobPoolPage() {
  return (
    <section>
      <PageHeader title="岗位池" description="查看和管理手动申请链接。" />
      <Button asChild className="mt-6">
        <Link to="/job-pool/manual-application-entries">
          <ExternalLink aria-hidden="true" />
          手动申请
        </Link>
      </Button>
    </section>
  );
}
