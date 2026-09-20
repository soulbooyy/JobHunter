import {
  BriefcaseBusiness,
  ExternalLink,
  SlidersHorizontal,
  Terminal,
} from 'lucide-react';
import { NavLink, Outlet } from 'react-router';
import { cn } from '@/shared/lib/cn';

export function AppLayout() {
  const navClass = ({ isActive }: { isActive: boolean }) =>
    cn(
      'flex h-9 items-center gap-2 rounded-md px-3 text-sm transition-colors hover:bg-hover',
      isActive ? 'bg-active font-medium text-foreground' : 'text-text-muted',
    );
  return (
    <div className="min-h-screen bg-background text-foreground">
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-2 focus:z-50 focus:bg-surface focus:p-2"
      >
        跳转到主要内容
      </a>
      <aside
        aria-label="主导航"
        className="fixed inset-y-0 left-0 flex w-48 flex-col border-r border-border bg-surface lg:w-60"
      >
        <div className="flex h-12 items-center gap-2 border-b border-border-subtle px-4 font-semibold">
          <Terminal size={16} aria-hidden="true" />
          JobHunter
        </div>
        <nav className="space-y-1 p-2">
          <NavLink to="/job-pool" end className={navClass}>
            <BriefcaseBusiness size={16} aria-hidden="true" />
            岗位池
          </NavLink>
          <div className="pl-4">
            <NavLink
              to="/job-pool/manual-application-entries"
              className={navClass}
            >
              <ExternalLink size={16} aria-hidden="true" />
              手动申请
            </NavLink>
            <NavLink to="/job-pool/preferences" className={navClass}>
              <SlidersHorizontal size={16} aria-hidden="true" />
              搜索偏好
            </NavLink>
          </div>
        </nav>
        <div className="mt-auto border-t border-border-subtle px-4 py-3 text-xs text-text-muted">
          本地工作区
        </div>
      </aside>
      <div className="ml-48 lg:ml-60">
        <header className="flex h-12 items-center gap-2 border-b border-border px-6 text-xs text-text-muted">
          <span>工作区</span>
          <span aria-hidden="true">/</span>
          <span className="text-foreground">JobHunter</span>
        </header>
        <main
          id="main-content"
          tabIndex={-1}
          className="mx-auto max-w-[1400px] px-6 py-6 lg:px-8"
        >
          <Outlet />
        </main>
      </div>
    </div>
  );
}
