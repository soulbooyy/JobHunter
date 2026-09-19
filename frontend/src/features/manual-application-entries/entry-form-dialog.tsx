import { useEffect, useRef, useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import type { ManualApplicationEntry } from '@/entities/manual-application-entry/model';
import {
  ApiFailure,
  failureMessage,
  fieldErrorMessage,
} from '@/shared/api/result';
import { Dialog } from '@/shared/ui/dialog';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import { Button } from '@/shared/ui/button';
import { FormField } from '@/shared/ui/form-field';
import { InlineNotice } from '@/shared/ui/inline-notice';
import { entryApi, type CreateEntry } from './api';
import {
  entryFields,
  fieldLabels,
  entryFormSchema,
  type EntryFormValues,
  type EntryField,
} from './validation';
import { SavedEntrySummary } from './saved-entry-summary';

type Phase = 'editing' | 'unknown' | 'conflict' | 'missing';
export function EntryFormDialog({
  initial,
  onClose,
  onSaved,
}: {
  initial?: ManualApplicationEntry;
  onClose: () => void;
  onSaved: (message: string) => void;
}) {
  const [base, setBase] = useState(initial);
  const [phase, setPhase] = useState<Phase>('editing');
  const [notice, setNotice] = useState('');
  const [latest, setLatest] = useState<ManualApplicationEntry>();
  const [busy, setBusy] = useState(false);
  const [discard, setDiscard] = useState(false);
  const locked = useRef(false);
  const pendingCreate = useRef<CreateEntry | undefined>(undefined);
  const form = useForm<EntryFormValues>({
    resolver: zodResolver(entryFormSchema),
    defaultValues: {
      company_name: initial?.company_name ?? '',
      role_title: initial?.role_title ?? '',
      application_url: initial?.application_url ?? '',
    },
  });
  const needsWarning = form.formState.isDirty || phase === 'unknown';
  useEffect(() => {
    if (!needsWarning && !busy) return;
    const warn = (event: BeforeUnloadEvent) => {
      event.preventDefault();
    };
    window.addEventListener('beforeunload', warn);
    return () => window.removeEventListener('beforeunload', warn);
  }, [needsWarning, busy]);
  function close() {
    if (locked.current) return;
    if (needsWarning) setDiscard(true);
    else onClose();
  }
  function applyFailure(error: unknown, wasUncertain: boolean) {
    const failure =
      error instanceof ApiFailure
        ? error
        : new ApiFailure('unknown', 'OUTCOME_UNKNOWN');
    if (failure.kind === 'unknown' || wasUncertain) {
      setPhase('unknown');
      setNotice(
        failure.kind === 'unknown'
          ? ''
          : `本次核验未完成：${failureMessage(failure)}这不能证明先前的添加没有生效。`,
      );
    } else {
      setPhase(
        failure.code === 'REVISION_CONFLICT'
          ? 'conflict'
          : failure.code === 'NOT_FOUND'
            ? 'missing'
            : 'editing',
      );
      setNotice(
        ['REVISION_CONFLICT', 'NOT_FOUND'].includes(failure.code)
          ? ''
          : failureMessage(failure),
      );
      for (const field of failure.fields)
        if (entryFields.includes(field.field as EntryField))
          form.setError(
            field.field as EntryField,
            { type: 'server', message: fieldErrorMessage(field) },
            { shouldFocus: true },
          );
    }
  }
  async function save(values: EntryFormValues, replay = false) {
    if (locked.current || (!replay && phase !== 'editing')) return;
    locked.current = true;
    setBusy(true);
    setNotice('');
    setLatest(undefined);
    const wasUncertain = phase === 'unknown';
    try {
      if (base) {
        await entryApi.update(base.manual_application_entry_id, {
          ...values,
          revision: base.revision,
        });
        onSaved('修改已保存');
      } else {
        if (!replay)
          pendingCreate.current = {
            ...values,
            request_id: crypto.randomUUID(),
          };
        const command = pendingCreate.current;
        if (!command) return;
        const result = await entryApi.create(command);
        // A confirmed write stays confirmed even if its follow-up read fails.
        try {
          await entryApi.read(result.manual_application_entry_id);
        } catch {
          /* List refresh exposes current read availability. */
        }
        onSaved(
          replay
            ? '已确认添加对应的记录，请查看当前保存内容。'
            : '手动申请已添加',
        );
      }
    } catch (error) {
      applyFailure(error, wasUncertain);
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  async function inspect() {
    if (!base || locked.current) return;
    locked.current = true;
    setBusy(true);
    setNotice('');
    try {
      setLatest(await entryApi.read(base.manual_application_entry_id));
    } catch (error) {
      const f = error as ApiFailure;
      setNotice(failureMessage(f));
      if (f.code === 'NOT_FOUND') setPhase('missing');
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  return (
    <>
      <Dialog
        title={initial ? '编辑手动申请' : '添加手动申请'}
        description="保存公司、职位和申请链接，方便之后继续访问。"
        onClose={close}
        busy={busy}
      >
        <p className="mt-2 text-xs text-text-muted">* 为必填项</p>
        <form
          noValidate
          onSubmit={(event) => {
            void form.handleSubmit((values) => save(values))(event);
          }}
          className="mt-5 space-y-4"
        >
          {phase !== 'editing' && (
            <InlineNotice
              title={
                phase === 'unknown'
                  ? '暂时无法确认操作结果'
                  : phase === 'conflict'
                    ? '这条记录已在其他页面发生修改'
                    : '这条记录已不存在'
              }
            >
              <p>
                {phase === 'unknown'
                  ? '无法确认刚才的操作是否已保存。你的输入已保留，请先核验，再决定下一步。'
                  : phase === 'conflict'
                    ? '你当前输入的内容已保留。请查看最新记录后再决定是否保存。'
                    : '输入仍保留在这里，不会自动重新创建记录。'}
              </p>
              {phase !== 'missing' && (
                <Button
                  variant="outline"
                  disabled={busy}
                  onClick={() => {
                    if (base) void inspect();
                    else if (pendingCreate.current)
                      void save(pendingCreate.current, true);
                  }}
                >
                  {busy ? '检查中…' : base ? '检查当前状态' : '核验这次添加'}
                </Button>
              )}
            </InlineNotice>
          )}
          {notice && <InlineNotice title={notice} />}
          {latest && (
            <>
              <SavedEntrySummary entry={latest} />
              <Button
                variant="outline"
                disabled={busy}
                onClick={() => {
                  setBase(latest);
                  setLatest(undefined);
                  setPhase('editing');
                  setNotice(
                    '已采用当前记录作为保存基准；你的输入保持不变，请检查后明确保存。',
                  );
                }}
              >
                基于当前记录继续编辑
              </Button>
            </>
          )}
          {entryFields.map((field) => (
            <FormField
              key={field}
              label={fieldLabels[field]}
              {...form.register(field)}
              error={form.formState.errors[field]?.message}
              readOnly={busy || phase === 'unknown'}
              placeholder={
                field === 'application_url' ? 'https://…' : undefined
              }
              spellCheck={false}
            />
          ))}
          <div className="flex justify-end gap-2 pt-2">
            <Button variant="outline" disabled={busy} onClick={close}>
              取消
            </Button>
            <Button
              type="submit"
              disabled={
                busy || phase !== 'editing' || form.formState.isSubmitting
              }
            >
              {busy ? '处理中…' : initial ? '保存修改' : '添加申请'}
            </Button>
          </div>
        </form>
      </Dialog>
      {discard && (
        <AlertDialog
          title={
            phase === 'unknown' ? '关闭前请保留核验机会' : '放弃未保存的输入？'
          }
          description={
            phase === 'unknown'
              ? '关闭后将丢失本页保留的请求信息。请先检查列表，避免重复添加；关闭并不代表刚才的操作失败。'
              : '关闭后，这些未保存的输入将被丢弃。'
          }
          onCancel={() => setDiscard(false)}
          cancelLabel="继续保留"
          action={
            <Button variant="destructive" onClick={onClose}>
              放弃输入并关闭
            </Button>
          }
        />
      )}
    </>
  );
}
