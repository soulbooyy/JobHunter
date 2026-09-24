import { createBrowserRouter, Navigate, Link } from 'react-router';
import { AppLayout } from '@/app/layout/app-layout';
export const router = createBrowserRouter([
  {
    element: <AppLayout />,
    hydrateFallbackElement: (
      <div role="status" className="p-8 text-sm text-text-muted">
        正在加载页面…
      </div>
    ),
    children: [
      {
        path: '/candidate-knowledge',
        lazy: async () => ({
          Component: (await import('@/pages/candidate-knowledge/page'))
            .KnowledgePage,
        }),
      },
      {
        path: '/candidate-knowledge/profile',
        lazy: async () => ({
          Component: (await import('@/pages/candidate-knowledge/profile-page'))
            .ProfilePage,
        }),
      },
      {
        path: '/candidate-knowledge/evidence/new/:kind',
        lazy: async () => ({
          Component: (await import('@/pages/candidate-knowledge/evidence-page'))
            .EvidencePage,
        }),
      },
      {
        path: '/candidate-knowledge/evidence/:id/edit',
        lazy: async () => ({
          Component: (await import('@/pages/candidate-knowledge/evidence-page'))
            .EvidencePage,
        }),
      },
      {
        path: '/resumes',
        lazy: async () => ({
          Component: (await import('@/pages/resumes/page')).ResumesPage,
        }),
      },
      {
        path: '/resumes/new',
        lazy: async () => ({
          Component: (await import('@/pages/resumes/editor-page'))
            .ResumeEditorPage,
        }),
      },
      {
        path: '/resumes/:id/edit',
        lazy: async () => ({
          Component: (await import('@/pages/resumes/editor-page'))
            .ResumeEditorPage,
        }),
      },
      { index: true, element: <Navigate to="/job-pool" replace /> },
      {
        path: '/job-pool/preferences',
        lazy: async () => ({
          Component: (await import('@/pages/job-pool/preferences/page'))
            .PreferencesPage,
        }),
      },
      {
        path: '/job-pool',
        lazy: async () => ({
          Component: (await import('@/pages/job-pool/page')).JobPoolPage,
        }),
      },
      {
        path: '/job-pool/manual-application-entries',
        lazy: async () => ({
          Component: (
            await import('@/pages/job-pool/manual-application-entries/page')
          ).ManualApplicationEntriesPage,
        }),
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
