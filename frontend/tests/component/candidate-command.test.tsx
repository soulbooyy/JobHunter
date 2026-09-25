import { act, renderHook } from '@testing-library/react';
import type { ReactNode } from 'react';
import { describe, it, expect, vi } from 'vitest';
import { useCandidateCommand } from '@/features/candidate/use-command';
import { ApiFailure } from '@/shared/api/result';
import { ToastProvider } from '@/shared/ui/toast';

const wrapper = ({ children }: { children: ReactNode }) => (
  <ToastProvider>{children}</ToastProvider>
);

describe('Candidate command recovery', () => {
  it('keeps the original request after unknown and later rejection, without automatic retry', async () => {
    const send = vi
      .fn()
      .mockRejectedValueOnce(new ApiFailure('unknown', 'OUTCOME_UNKNOWN'))
      .mockRejectedValueOnce(new ApiFailure('rejected', 'REVISION_CONFLICT'))
      .mockResolvedValue({ id: 'receipt' });
    const after = vi.fn().mockResolvedValue(undefined);
    const { result } = renderHook(
      () =>
        useCandidateCommand(send, after, {
          message: '操作成功',
        }),
      { wrapper },
    );
    const body = {
      request_id: 'original',
      revision: 3,
      fields: { name: 'original' },
    };
    await act(async () => {
      await result.current.execute(body);
    });
    body.fields.name = 'changed';
    expect(result.current.unknown).toBe(true);
    await act(async () => {
      await result.current.execute({ ...body, request_id: 'new' });
    });
    expect(send).toHaveBeenCalledTimes(1);
    await act(async () => {
      await result.current.execute();
    });
    expect(result.current.unknown).toBe(true);
    expect(after).not.toHaveBeenCalled();
    await act(async () => {
      await result.current.execute();
    });
    expect(send.mock.calls.map((c) => c[0])).toEqual(
      Array(3).fill({
        request_id: 'original',
        revision: 3,
        fields: { name: 'original' },
      }),
    );
    expect(result.current.unknown).toBe(false);
    expect(after).toHaveBeenCalledTimes(1);
  });
  it('confirmed writes stay confirmed when current read fails; refresh never sends again', async () => {
    const send = vi.fn().mockResolvedValue({ id: 'receipt' });
    const after = vi
      .fn()
      .mockRejectedValueOnce(new Error('read unavailable'))
      .mockResolvedValue(undefined);
    const { result } = renderHook(
      () =>
        useCandidateCommand(send, after, {
          message: '操作成功',
        }),
      { wrapper },
    );
    await act(async () => {
      await result.current.execute({ request_id: 'one' });
    });
    expect(result.current.confirmed).toBe(true);
    expect(result.current.unknown).toBe(false);
    await act(async () => {
      await result.current.execute({ request_id: 'two' });
    });
    expect(send).toHaveBeenCalledTimes(1);
    await act(async () => {
      await result.current.refresh();
    });
    expect(after).toHaveBeenCalledTimes(2);
    expect(send).toHaveBeenCalledTimes(1);
    expect(result.current.disabled).toBe(false);
  });
});
