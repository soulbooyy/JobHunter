import { useRef, useState } from 'react';
import { ApiFailure } from '@/shared/api/result';
export function useCandidateCommand<T, R>(
  send: (request: T) => Promise<R>,
  after: (result: R) => Promise<void>,
) {
  const pending = useRef<T | undefined>(undefined),
    receipt = useRef<R | undefined>(undefined),
    locked = useRef(false);
  const [busy, setBusy] = useState(false),
    [unknown, setUnknown] = useState(false),
    [confirmed, setConfirmed] = useState(false),
    [error, setError] = useState<ApiFailure>(),
    [message, setMessage] = useState('');
  async function read(result: R) {
    try {
      await after(result);
      setConfirmed(false);
      setMessage('操作已确认。');
    } catch {
      setConfirmed(true);
      setMessage('操作已确认，但暂时无法读取当前状态。请重新读取后再编辑。');
    }
  }
  async function execute(request?: T) {
    if (locked.current || confirmed || (unknown && request !== undefined))
      return false;
    const retry = request === undefined;
    const value = retry ? pending.current : structuredClone(request);
    if (value === undefined) return false;
    pending.current = value;
    locked.current = true;
    setBusy(true);
    setError(undefined);
    setMessage('');
    try {
      const result = await send(value);
      receipt.current = result;
      pending.current = undefined;
      setUnknown(false);
      setConfirmed(true);
      await read(result);
      return true;
    } catch (e) {
      const failure =
        e instanceof ApiFailure
          ? e
          : new ApiFailure('unknown', 'OUTCOME_UNKNOWN');
      setError(failure);
      setUnknown(retry || failure.kind === 'unknown');
      return false;
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  async function refresh() {
    if (locked.current || receipt.current === undefined) return;
    locked.current = true;
    setBusy(true);
    try {
      await read(receipt.current);
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  function reset() {
    if (unknown || locked.current || confirmed) return;
    setError(undefined);
    setMessage('');
  }
  return {
    busy,
    unknown,
    confirmed,
    error,
    message,
    execute,
    refresh,
    reset,
    disabled: busy || unknown || confirmed,
  };
}
export type CommandState = Pick<
  ReturnType<typeof useCandidateCommand>,
  'busy' | 'unknown' | 'confirmed' | 'error' | 'message' | 'refresh'
> & { execute: () => Promise<boolean> };
