import { render, screen, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it } from 'vitest';
import { ToastProvider } from '@/shared/ui/toast';
import { useToast } from '@/shared/ui/use-toast';

function Harness() {
  const toast = useToast();
  return (
    <>
      <button onClick={() => toast.success('修改已保存')}>显示修改</button>
      <button onClick={() => toast.deleted('记录已删除')}>显示删除</button>
      <button onClick={() => toast.warning('请检查输入')}>显示警告</button>
    </>
  );
}

describe('shared toast feedback', () => {
  it('uses the shared top notification surface for all three semantic variants', async () => {
    render(
      <ToastProvider>
        <Harness />
      </ToastProvider>,
    );

    await userEvent.click(screen.getByRole('button', { name: '显示修改' }));
    await userEvent.click(screen.getByRole('button', { name: '显示删除' }));
    await userEvent.click(screen.getByRole('button', { name: '显示警告' }));

    const region = screen.getByLabelText('通知');
    const statuses = within(region).getAllByRole('status');
    expect(statuses[0]).toHaveTextContent('修改已保存');
    expect(statuses[0]).toHaveClass('bg-toast-success-background');
    expect(statuses[1]).toHaveTextContent('记录已删除');
    expect(statuses[1]).toHaveClass('bg-toast-delete-background');
    expect(within(region).getByRole('alert')).toHaveClass(
      'bg-toast-warning-background',
    );

    await userEvent.click(within(statuses[0]!).getByRole('button'));
    expect(screen.queryByText('修改已保存')).not.toBeInTheDocument();
  });
});
