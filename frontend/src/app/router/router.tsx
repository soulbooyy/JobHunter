import { createBrowserRouter, Navigate, Link } from 'react-router';
import { AppLayout } from '@/app/layout/app-layout';
import { JobPoolPage } from '@/pages/job-pool/page';
import { ManualApplicationEntriesPage } from '@/pages/job-pool/manual-application-entries/page';
export const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      { index: true, element: <Navigate to="/job-pool" replace /> },
      { path: '/job-pool', element: <JobPoolPage /> },
      {
        path: '/job-pool/manual-application-entries',
        element: <ManualApplicationEntriesPage />,
      },
      {
        path: '*',
        element: (
          <section className="space-y-4">
            <h1 className="text-2xl font-semibold">找不到此页面</h1>
            <Link to="/job-pool" className="underline">
              返回岗位池
            </Link>
          </section>
        ),
      },
    ],
  },
]);
