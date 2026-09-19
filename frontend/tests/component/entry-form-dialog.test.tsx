import { render, screen, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, it, expect, vi } from 'vitest';
import { EntryFormDialog } from '@/features/manual-application-entries/entry-form-dialog';
import { DeleteEntryDialog } from '@/features/manual-application-entries/delete-entry-dialog';
import { entryApi } from '@/features/manual-application-entries/api';
import { ApiFailure } from '@/shared/api/result';
vi.mock('@/features/manual-application-entries/api', () => ({
  entryApi: {
    create: vi.fn(),
    read: vi.fn(),
    update: vi.fn(),
    delete: vi.fn(),
  },
}));
const entry = {
  manual_application_entry_id: '8f395bc2-5dc4-4b9a-8d31-a9e9056072f1',
  company_name: '原公司',
  role_title: '原岗位',
  application_url: 'HTTP://Example.test:80/./apply',
  revision: 1,
  created_at: '2026-09-19T10:00:00.000Z',
  updated_at: '2026-09-19T10:00:00.000Z',
};
async function fill() {
  await userEvent.type(screen.getByRole('textbox', { name: '公司' }), '公司');
  await userEvent.type(
    screen.getByRole('textbox', { name: '职位名称' }),
    '岗位',
  );
  await userEvent.type(
    screen.getByRole('textbox', { name: '申请链接' }),
    'https://example.test',
  );
}
beforeEach(() => vi.resetAllMocks());
describe('shared create/edit dialog', () => {
  it('validates inline without posting or clearing input', async () => {
    render(<EntryFormDialog onClose={vi.fn()} onSaved={vi.fn()} />);
    await userEvent.type(
      screen.getByRole('textbox', { name: '公司' }),
      '我的公司',
    );
    await userEvent.click(screen.getByRole('button', { name: '添加申请' }));
    expect(await screen.findByText('请输入职位名称')).toBeInTheDocument();
    expect(screen.getByRole('textbox', { name: '公司' })).toHaveValue(
      '我的公司',
    );
    expect(entryApi.create).not.toHaveBeenCalled();
  });
  it('reuses exact uncertain create request, even after a rejected verification', async () => {
    vi.mocked(entryApi.create)
      .mockRejectedValueOnce(new ApiFailure('unknown', 'OUTCOME_UNKNOWN'))
      .mockRejectedValueOnce(new ApiFailure('rejected', 'STORAGE_UNAVAILABLE'))
      .mockResolvedValueOnce({
        manual_application_entry_id: entry.manual_application_entry_id,
      });
    vi.mocked(entryApi.read).mockResolvedValue(entry);
    const saved = vi.fn();
    render(<EntryFormDialog onClose={vi.fn()} onSaved={saved} />);
    await fill();
    await userEvent.click(screen.getByRole('button', { name: '添加申请' }));
    await screen.findByText('暂时无法确认操作结果');
    expect(entryApi.create).toHaveBeenCalledTimes(1);
    expect(screen.getByRole('button', { name: '添加申请' })).toBeDisabled();
    await userEvent.click(screen.getByRole('button', { name: '核验这次添加' }));
    await waitFor(() => expect(entryApi.create).toHaveBeenCalledTimes(2));
    expect(screen.getByRole('button', { name: '添加申请' })).toBeDisabled();
    expect(saved).not.toHaveBeenCalled();
    await userEvent.click(screen.getByRole('button', { name: '核验这次添加' }));
    await waitFor(() => expect(saved).toHaveBeenCalledTimes(1));
    const calls = vi.mocked(entryApi.create).mock.calls;
    expect(calls[0]?.[0]).toEqual(calls[1]?.[0]);
    expect(calls[0]?.[0]).toEqual(calls[2]?.[0]);
  });
  it('keeps dirty edit input and requires explicit rebasing plus another Save', async () => {
    vi.mocked(entryApi.update)
      .mockRejectedValueOnce(new ApiFailure('rejected', 'REVISION_CONFLICT'))
      .mockResolvedValue({ ...entry, role_title: '我的修改', revision: 3 });
    vi.mocked(entryApi.read).mockResolvedValue({
      ...entry,
      role_title: '其他页面的修改',
      revision: 2,
    });
    render(
      <EntryFormDialog initial={entry} onClose={vi.fn()} onSaved={vi.fn()} />,
    );
    await userEvent.clear(screen.getByRole('textbox', { name: '职位名称' }));
    await userEvent.type(
      screen.getByRole('textbox', { name: '职位名称' }),
      '我的修改',
    );
    await userEvent.click(screen.getByRole('button', { name: '保存修改' }));
    await screen.findByText('这条记录已在其他页面发生修改');
    await userEvent.click(screen.getByRole('button', { name: '检查当前状态' }));
    await screen.findByText('其他页面的修改');
    expect(screen.getByRole('textbox', { name: '职位名称' })).toHaveValue(
      '我的修改',
    );
    expect(entryApi.update).toHaveBeenCalledTimes(1);
    await userEvent.click(
      screen.getByRole('button', { name: '基于当前记录继续编辑' }),
    );
    expect(entryApi.update).toHaveBeenCalledTimes(1);
    await userEvent.click(screen.getByRole('button', { name: '保存修改' }));
    await waitFor(() => expect(entryApi.update).toHaveBeenCalledTimes(2));
    expect(vi.mocked(entryApi.update).mock.calls[1]?.[1]).toMatchObject({
      revision: 2,
      role_title: '我的修改',
    });
  });
  it('reads after an unknown edit without replaying', async () => {
    vi.mocked(entryApi.update).mockRejectedValue(
      new ApiFailure('unknown', 'OUTCOME_UNKNOWN'),
    );
    vi.mocked(entryApi.read).mockResolvedValue({ ...entry, revision: 2 });
    const saved = vi.fn();
    render(
      <EntryFormDialog initial={entry} onClose={vi.fn()} onSaved={saved} />,
    );
    await userEvent.click(screen.getByRole('button', { name: '保存修改' }));
    await screen.findByText('暂时无法确认操作结果');
    await userEvent.click(screen.getByRole('button', { name: '检查当前状态' }));
    await screen.findByRole('region', { name: '当前已保存的记录' });
    expect(entryApi.update).toHaveBeenCalledTimes(1);
    expect(saved).not.toHaveBeenCalled();
  });
  it('does not clear server-rejected fields or treat a confirmed save plus failed read as unknown', async () => {
    vi.mocked(entryApi.create)
      .mockRejectedValueOnce(
        new ApiFailure('rejected', 'VALIDATION_ERROR', [
          { field: 'application_url', code: 'INVALID_FORMAT' },
        ]),
      )
      .mockResolvedValueOnce({
        manual_application_entry_id: entry.manual_application_entry_id,
      });
    vi.mocked(entryApi.read).mockRejectedValue(
      new ApiFailure('read', 'READ_FAILED'),
    );
    const saved = vi.fn();
    render(<EntryFormDialog onClose={vi.fn()} onSaved={saved} />);
    await fill();
    await userEvent.click(screen.getByRole('button', { name: '添加申请' }));
    await screen.findByText('请输入有效的 HTTP 或 HTTPS 链接');
    expect(screen.getByRole('textbox', { name: '申请链接' })).toHaveValue(
      'https://example.test',
    );
    await userEvent.click(screen.getByRole('button', { name: '添加申请' }));
    await waitFor(() => expect(saved).toHaveBeenCalledTimes(1));
  });
  it('requires explicit discard before losing dirty input', async () => {
    const close = vi.fn();
    render(<EntryFormDialog onClose={close} onSaved={vi.fn()} />);
    await fill();
    await userEvent.click(screen.getByRole('button', { name: '关闭弹窗' }));
    const confirmation = await screen.findByRole('alertdialog');
    expect(close).not.toHaveBeenCalled();
    await userEvent.click(
      within(confirmation).getByRole('button', { name: '继续保留' }),
    );
    expect(screen.getByRole('textbox', { name: '公司' })).toHaveValue('公司');
  });
});
describe('delete verification', () => {
  it('checks absence after an unknown delete without claiming confirmed deletion', async () => {
    vi.mocked(entryApi.delete).mockRejectedValue(
      new ApiFailure('unknown', 'OUTCOME_UNKNOWN'),
    );
    vi.mocked(entryApi.read).mockRejectedValue(
      new ApiFailure('read', 'NOT_FOUND'),
    );
    const deleted = vi.fn();
    render(
      <DeleteEntryDialog entry={entry} onClose={vi.fn()} onDeleted={deleted} />,
    );
    await userEvent.click(screen.getByRole('button', { name: '删除' }));
    await userEvent.click(
      await screen.findByRole('button', { name: '检查当前状态' }),
    );
    await screen.findByText(/当前记录已不存在/);
    expect(entryApi.delete).toHaveBeenCalledTimes(1);
    expect(deleted).not.toHaveBeenCalled();
  });
});
