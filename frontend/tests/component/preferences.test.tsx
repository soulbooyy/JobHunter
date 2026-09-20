import { beforeEach, describe, expect, it, vi } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { createMemoryRouter, Link, RouterProvider } from 'react-router';
import { QueryClientProvider } from '@tanstack/react-query';
import { createQueryClient } from '@/app/providers/query-client';
import { PreferencesEditor } from '@/features/preferences/preferences-editor';
import { PreferencesPage } from '@/pages/job-pool/preferences/page';
import { preferencesApi } from '@/features/preferences/api';
import { ApiFailure } from '@/shared/api/result';
import { current, saved } from '../fixtures/preferences';
import type { CurrentPreferences } from '@/features/preferences/model';
vi.mock('@/features/preferences/api', () => ({
  preferencesApi: { current: vi.fn(), save: vi.fn() },
  preferencesQuery: {
    queryKey: ['preferences'],
    queryFn: () => preferencesApi.current(),
    retry: false,
  },
}));
function mount(initial: CurrentPreferences = current(), page = false) {
  const router = createMemoryRouter([
    {
      path: '/',
      element: (
        <>
          <Link to="/away">离开</Link>
          {page ? <PreferencesPage /> : <PreferencesEditor initial={initial} />}
        </>
      ),
    },
    { path: '/away', element: <p>其他页面</p> },
  ]);
  render(
    <QueryClientProvider client={createQueryClient()}>
      <RouterProvider router={router} />
    </QueryClientProvider>,
  );
  return router;
}
const salary = () => screen.getByRole('textbox', { name: '最低月薪' });
const save = () =>
  userEvent.click(screen.getByRole('button', { name: '保存修改' }));
beforeEach(() => vi.resetAllMocks());
describe('Preferences editor recovery and controls', () => {
  it('requires all first-save choices and focuses an error summary', async () => {
    mount({ status: 'NOT_CONFIGURED' });
    expect(
      screen.getByRole('checkbox', { name: '排除公司不限' }),
    ).toBeChecked();
    expect(screen.getByRole('textbox', { name: '排除公司' })).toBeDisabled();
    await userEvent.click(screen.getByRole('button', { name: '保存偏好' }));
    expect(preferencesApi.save).not.toHaveBeenCalled();
    await waitFor(() => expect(screen.getByRole('alert')).toHaveFocus());
    expect(
      screen.getByRole('textbox', { name: '目标岗位关键词' }),
    ).toHaveAttribute('aria-invalid', 'true');
  });
  it('requires adding pending chip text; preserves comma and IME entry', async () => {
    mount();
    const input = screen.getByRole('textbox', { name: '目标岗位关键词' });
    await userEvent.type(input, 'Java,Python');
    await save();
    expect(await screen.findByText(/输入框中还有未添加/)).toBeVisible();
    expect(preferencesApi.save).not.toHaveBeenCalled();
    await userEvent.click(
      screen.getByRole('button', { name: '添加目标岗位关键词' }),
    );
    expect(screen.getByText('Java,Python')).toBeVisible();
    expect(
      screen.getByRole('button', {
        name: '移除目标岗位关键词第 2 项：Java,Python',
      }),
    ).toBeVisible();
  });
  it('disables inactive inputs, retains unsaved concrete value and omits it from Save', async () => {
    mount();
    await userEvent.click(
      screen.getByRole('checkbox', { name: '最低月薪不限' }),
    );
    expect(salary()).toBeDisabled();
    await userEvent.click(
      screen.getByRole('checkbox', { name: '最低月薪不限' }),
    );
    expect(salary()).toHaveValue('15000');
    await userEvent.click(
      screen.getByRole('checkbox', { name: '最低月薪不限' }),
    );
    vi.mocked(preferencesApi.save).mockRejectedValue(
      new ApiFailure('rejected', 'STORAGE_UNAVAILABLE'),
    );
    await save();
    expect(
      vi.mocked(preferencesApi.save).mock.calls[0]?.[0].configuration
        .minimum_salary,
    ).toEqual({ mode: 'UNLIMITED' });
  });
  it('retains original request after uncertainty and later definite rejection', async () => {
    mount();
    vi.mocked(preferencesApi.save)
      .mockRejectedValueOnce(new ApiFailure('unknown', 'OUTCOME_UNKNOWN'))
      .mockRejectedValueOnce(new ApiFailure('rejected', 'REVISION_CONFLICT'))
      .mockResolvedValueOnce(saved);
    vi.mocked(preferencesApi.current).mockResolvedValue(current(2));
    await userEvent.clear(salary());
    await userEvent.type(salary(), '20000');
    await save();
    await screen.findByText('暂时无法确认保存结果');
    expect(salary()).toBeDisabled();
    await userEvent.click(screen.getByRole('button', { name: '查看当前配置' }));
    await screen.findByText('最新读取的保存配置');
    expect(preferencesApi.save).toHaveBeenCalledTimes(1);
    expect(screen.getByRole('button', { name: '保存修改' })).toBeDisabled();
    await userEvent.click(screen.getByRole('button', { name: '验证保存结果' }));
    await screen.findByText(/这不能证明先前的保存没有生效/);
    await userEvent.click(screen.getByRole('button', { name: '验证保存结果' }));
    await screen.findByText('搜索偏好已保存。');
    const calls = vi.mocked(preferencesApi.save).mock.calls;
    expect(calls).toHaveLength(3);
    expect(calls[1]?.[0]).toEqual(calls[0]?.[0]);
    expect(calls[2]?.[0]).toEqual(calls[0]?.[0]);
  });
  it('preserves draft through conflict inspection and requires explicit rebase plus save', async () => {
    mount();
    vi.mocked(preferencesApi.save)
      .mockRejectedValueOnce(new ApiFailure('rejected', 'REVISION_CONFLICT'))
      .mockResolvedValueOnce({ ...saved, revision: 3 });
    vi.mocked(preferencesApi.current).mockResolvedValue(
      current(2, ['他处修改']),
    );
    await userEvent.clear(salary());
    await userEvent.type(salary(), '20000');
    await save();
    await screen.findByText('搜索偏好已在其他页面发生修改');
    await userEvent.click(screen.getByRole('button', { name: '查看最新配置' }));
    await screen.findByText('他处修改');
    expect(salary()).toHaveValue('20000');
    expect(preferencesApi.save).toHaveBeenCalledTimes(1);
    await userEvent.click(
      screen.getByRole('button', { name: '基于最新配置继续编辑' }),
    );
    expect(salary()).toHaveValue('20000');
    await save();
    await waitFor(() => expect(preferencesApi.save).toHaveBeenCalledTimes(2));
    const calls = vi.mocked(preferencesApi.save).mock.calls;
    expect(calls[1]?.[0].revision).toBe(2);
    expect(calls[1]?.[0].request_id).not.toBe(calls[0]?.[0].request_id);
  });
  it('does not reclassify a confirmed save when its follow-up read fails', async () => {
    mount();
    vi.mocked(preferencesApi.save).mockResolvedValue(saved);
    vi.mocked(preferencesApi.current)
      .mockRejectedValueOnce(new ApiFailure('read', 'READ_FAILED'))
      .mockResolvedValueOnce(current(2));
    await save();
    await screen.findByText(/本次保存已确认，但暂时无法读取/);
    expect(screen.queryByText('暂时无法确认保存结果')).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: '保存修改' })).toBeDisabled();
    await userEvent.click(
      screen.getByRole('button', { name: '重新读取当前配置' }),
    );
    await screen.findByText('搜索偏好已保存。');
    expect(preferencesApi.save).toHaveBeenCalledTimes(1);
  });
  it('labels historical replay success separately from newly read current state', async () => {
    mount();
    vi.mocked(preferencesApi.save).mockResolvedValue(saved);
    vi.mocked(preferencesApi.current).mockResolvedValue(
      current(3, ['更新的配置']),
    );
    await save();
    await screen.findByText(/当前配置已发生后续变化/);
    expect(screen.getByText('更新的配置')).toBeVisible();
  });
  it('only discards an uncertain request in place after a successful current read', async () => {
    mount();
    vi.mocked(preferencesApi.save).mockRejectedValue(
      new ApiFailure('unknown', 'OUTCOME_UNKNOWN'),
    );
    vi.mocked(preferencesApi.current)
      .mockRejectedValueOnce(new ApiFailure('read', 'READ_FAILED'))
      .mockResolvedValueOnce(current(3, ['最新配置']));
    await save();
    await screen.findByText('暂时无法确认保存结果');
    await userEvent.click(screen.getByRole('button', { name: '取消' }));
    await userEvent.click(screen.getByRole('button', { name: '放弃并继续' }));
    await screen.findByText(
      '无法读取当前配置。原请求仍保留，请稍后重试或验证保存结果。',
    );
    expect(screen.getByRole('button', { name: '保存修改' })).toBeDisabled();
    await userEvent.click(screen.getByRole('button', { name: '取消' }));
    await userEvent.click(screen.getByRole('button', { name: '放弃并继续' }));
    await screen.findByText('最新配置');
    expect(screen.getByRole('button', { name: '保存修改' })).toBeEnabled();
    expect(preferencesApi.save).toHaveBeenCalledTimes(1);
  });
  it('maps original item index errors without clearing the input', async () => {
    mount();
    vi.mocked(preferencesApi.save).mockRejectedValue(
      new ApiFailure('rejected', 'VALIDATION_ERROR', [
        { field: 'configuration.target_job_keywords[0]', code: 'TOO_LONG' },
      ]),
    );
    await save();
    await screen.findByText('第 1 项：内容过长，请缩短后重试');
    expect(screen.getByText('工程师')).toBeVisible();
  });
  it('blocks navigation with unsaved input and supports cancel or explicit discard', async () => {
    mount();
    await userEvent.type(salary(), '0');
    await userEvent.click(screen.getByRole('link', { name: '离开' }));
    await screen.findByRole('alertdialog');
    await userEvent.click(screen.getByRole('button', { name: '继续编辑' }));
    expect(salary()).toHaveValue('150000');
    await userEvent.click(screen.getByRole('link', { name: '离开' }));
    await userEvent.click(screen.getByRole('button', { name: '放弃并继续' }));
    await screen.findByText('其他页面');
  });
});
describe('Preferences read presentation', () => {
  it('keeps loading distinct from unconfigured', () => {
    vi.mocked(preferencesApi.current).mockReturnValue(new Promise(() => {}));
    mount(current(), true);
    expect(
      screen.getByRole('status', { name: '正在加载搜索偏好' }),
    ).toBeVisible();
    expect(screen.queryByText('尚未配置搜索偏好')).not.toBeInTheDocument();
  });
  it('keeps read failure distinct from empty and retries only explicitly', async () => {
    vi.mocked(preferencesApi.current)
      .mockRejectedValueOnce(new ApiFailure('read', 'READ_FAILED'))
      .mockResolvedValueOnce({ status: 'NOT_CONFIGURED' });
    mount(current(), true);
    await screen.findByText('无法加载搜索偏好');
    expect(preferencesApi.current).toHaveBeenCalledTimes(1);
    await userEvent.click(screen.getByRole('button', { name: '重试' }));
    await screen.findByText('尚未配置搜索偏好');
    expect(preferencesApi.current).toHaveBeenCalledTimes(2);
  });
});
