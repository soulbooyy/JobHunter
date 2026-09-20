import { useEffect, useRef, useState } from 'react';
import { useBlocker } from 'react-router';
import { Button } from '@/shared/ui/button';
import { InlineNotice } from '@/shared/ui/inline-notice';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import {
  ApiFailure,
  failureMessage,
  fieldErrorMessage,
} from '@/shared/api/result';
import { trimOuterWhitespace } from '@/shared/lib/unicode-text';
import { preferencesApi } from './api';
import { PreferencesFields, type FieldMessages } from './preferences-fields';
import { SavedPreferences } from './saved-preferences';
import {
  configurationSchema,
  configurationFromDraft,
  draftFromCurrent,
  fieldLabels,
  textIssue,
  type CurrentPreferences,
  type PreferenceField,
  type PreferenceDraft,
  type SavePreferences,
  type SaveResult,
  type TagField,
} from './model';
type Phase = 'editing' | 'conflict' | 'unknown' | 'confirmed';
export function PreferencesEditor({
  initial,
}: {
  initial: CurrentPreferences;
}) {
  const [base, setBase] = useState(initial);
  const [draft, setDraft] = useState(() => draftFromCurrent(initial));
  const [baseline, setBaseline] = useState(() =>
    JSON.stringify(draftFromCurrent(initial)),
  );
  const [phase, setPhase] = useState<Phase>('editing');
  const [busy, setBusy] = useState(false);
  const locked = useRef(false);
  const pendingRequest = useRef<SavePreferences | undefined>(undefined);
  const confirmedResult = useRef<SaveResult | undefined>(undefined);
  const [latest, setLatest] = useState<CurrentPreferences>();
  const [errors, setErrors] = useState<FieldMessages>({});
  const [notice, setNotice] = useState('');
  const [message, setMessage] = useState('');
  const [discard, setDiscard] = useState(false);
  const summary = useRef<HTMLDivElement>(null);
  const dirty = JSON.stringify(draft) !== baseline;
  const needsWarning = dirty || phase === 'unknown' || busy;
  const blocker = useBlocker(
    ({ currentLocation, nextLocation }) =>
      needsWarning && currentLocation.pathname !== nextLocation.pathname,
  );
  useEffect(() => {
    if (!needsWarning) return;
    const warn = (event: BeforeUnloadEvent) => {
      event.preventDefault();
    };
    window.addEventListener('beforeunload', warn);
    return () => window.removeEventListener('beforeunload', warn);
  }, [needsWarning]);
  function install(current: CurrentPreferences) {
    const next = draftFromCurrent(current);
    setBase(current);
    setDraft(next);
    setBaseline(JSON.stringify(next));
    setErrors({});
    setLatest(undefined);
    setPhase('editing');
  }
  function change(next: PreferenceDraft) {
    if (locked.current || phase === 'unknown' || phase === 'confirmed') return;
    setDraft(next);
    setMessage('');
  }
  function add(field: TagField) {
    if (locked.current || phase === 'unknown' || phase === 'confirmed') return;
    const raw = draft.pending[field];
    let error = textIssue(raw, field === 'excluded_companies' ? 200 : 100);
    const value = trimOuterWhitespace(raw);
    const values = draft[field];
    const max =
      field === 'target_job_keywords'
        ? 20
        : field === 'accepted_cities'
          ? 50
          : 200;
    if (!error && !values.includes(value) && values.length >= max)
      error = `最多添加 ${max} 项`;
    if (error) {
      setErrors({ ...errors, [field]: [error] });
      return;
    }
    change({
      ...draft,
      [field]: values.includes(value) ? values : [...values, value],
      pending: { ...draft.pending, [field]: '' },
    });
    setErrors({ ...errors, [field]: undefined });
  }
  function showErrors(next: FieldMessages) {
    setErrors(next);
    setTimeout(() => summary.current?.focus(), 0);
  }
  async function readAfterSuccess(result: SaveResult) {
    try {
      const current = await preferencesApi.current();
      // Save acknowledgements can refer to history. Never label the replay's content current.
      if (current.status !== 'CONFIGURED')
        throw new ApiFailure('read', 'READ_FAILED');
      const matches =
        current.preference_set.current_preference_set_version_id ===
          result.preference_set_version_id &&
        current.preference_set.revision === result.revision &&
        current.preference_set.preference_set_id === result.preference_set_id;
      install(current);
      setNotice('');
      setMessage(
        matches
          ? result.outcome === 'UNCHANGED'
            ? '保存已确认，配置内容没有变化。'
            : '搜索偏好已保存。'
          : '本次保存已确认；当前配置已发生后续变化，现显示最新读取的配置。',
      );
    } catch {
      setMessage('本次保存已确认。');
      setNotice('本次保存已确认，但暂时无法读取当前配置。请重新读取后再编辑。');
    }
  }
  async function submit(replay = false) {
    if (locked.current || (!replay && phase !== 'editing')) return;
    let request: SavePreferences;
    if (replay) {
      if (!pendingRequest.current || phase !== 'unknown') return;
      request = pendingRequest.current;
    } else {
      const parsed = configurationSchema.safeParse(
        configurationFromDraft(draft),
      );
      const issues: FieldMessages = {};
      if (!parsed.success)
        for (const issue of parsed.error.issues) {
          const field = issue.path[0] as PreferenceField;
          if (field in fieldLabels) {
            const index = issue.path.find((p) => typeof p === 'number');
            (issues[field] ??= []).push(
              `${typeof index === 'number' ? `第 ${index + 1} 项：` : ''}${issue.message}`,
            );
          }
        }
      for (const field of [
        'target_job_keywords',
        'accepted_cities',
        'excluded_companies',
      ] as TagField[]) {
        if (
          (field === 'target_job_keywords' || !draft.unlimited[field]) &&
          draft.pending[field] !== ''
        )
          (issues[field] ??= []).push(
            '输入框中还有未添加的内容，请添加或清空后再保存。',
          );
      }
      if (!parsed.success || Object.keys(issues).length) {
        showErrors(issues);
        return;
      }
      request = {
        request_id: crypto.randomUUID(),
        revision:
          base.status === 'CONFIGURED' ? base.preference_set.revision : null,
        configuration: parsed.data,
      };
      pendingRequest.current = request;
    }
    locked.current = true;
    setBusy(true);
    setNotice('');
    setMessage('');
    setErrors({});
    try {
      const result = await preferencesApi.save(request);
      confirmedResult.current = result;
      pendingRequest.current = undefined;
      setPhase('confirmed');
      setBaseline(JSON.stringify(draft));
      setMessage('本次保存已确认，正在读取当前配置…');
      await readAfterSuccess(result);
    } catch (error) {
      const failure =
        error instanceof ApiFailure
          ? error
          : new ApiFailure('unknown', 'OUTCOME_UNKNOWN');
      if (replay || failure.kind === 'unknown') {
        setPhase('unknown');
        if (failure.kind !== 'unknown')
          setNotice(
            `这次核验未完成：${failureMessage(failure)}这不能证明先前的保存没有生效。`,
          );
      } else if (failure.code === 'REVISION_CONFLICT') {
        setPhase('conflict');
        setLatest(undefined);
      } else {
        setNotice(failureMessage(failure));
        const messages: FieldMessages = {};
        for (const field of failure.fields) {
          const key = /^configuration\.([a-z_]+)/.exec(
            field.field,
          )?.[1] as PreferenceField;
          if (key && key in fieldLabels) {
            const index = /\[(\d+)\]/.exec(field.field)?.[1];
            (messages[key] ??= []).push(
              `${index ? `第 ${Number(index) + 1} 项：` : ''}${fieldErrorMessage(field)}`,
            );
          }
        }
        if (Object.keys(messages).length) showErrors(messages);
      }
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  async function inspect() {
    if (locked.current) return;
    locked.current = true;
    setBusy(true);
    setNotice('');
    try {
      setLatest(await preferencesApi.current());
    } catch {
      setNotice('暂时无法读取最新配置。你的输入仍保留，请稍后重试。');
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  async function refreshConfirmed() {
    if (locked.current || !confirmedResult.current) return;
    locked.current = true;
    setBusy(true);
    try {
      await readAfterSuccess(confirmedResult.current);
    } finally {
      locked.current = false;
      setBusy(false);
    }
  }
  async function abandon() {
    if (locked.current) return;
    if (phase === 'unknown' && blocker.state !== 'blocked') {
      locked.current = true;
      setBusy(true);
      try {
        install(await preferencesApi.current());
      } catch {
        setNotice('无法读取当前配置。原请求仍保留，请稍后重试或验证保存结果。');
        setDiscard(false);
        return;
      } finally {
        locked.current = false;
        setBusy(false);
      }
    } else {
      install(latest ?? base);
    }
    pendingRequest.current = undefined;
    setNotice('');
    setMessage('已放弃本地修改。这不会撤销已生效的保存。');
    setDiscard(false);
    if (blocker.state === 'blocked') blocker.proceed();
  }
  return (
    <>
      <form
        noValidate
        onSubmit={(e) => {
          e.preventDefault();
          void submit();
        }}
        className="space-y-5"
      >
        {base.status === 'NOT_CONFIGURED' && phase !== 'confirmed' && (
          <div className="rounded-md border border-border bg-surface-muted p-4 text-sm">
            <h2 className="font-medium">尚未配置搜索偏好</h2>
            <p className="mt-1 text-text-muted">
              完整保存后，这些条件将用于后续岗位收集；保存不会启动收集。
            </p>
          </div>
        )}
        {base.status === 'CONFIGURED' && (
          <p className="text-xs text-text-muted">
            已配置 · 上次读取的更新时间：
            <time dateTime={base.preference_set.updated_at}>
              {new Date(base.preference_set.updated_at).toLocaleString('zh-CN')}
            </time>
          </p>
        )}
        {message && (
          <p
            role="status"
            className="rounded-md border border-border bg-surface-muted p-3 text-sm"
          >
            {message}
          </p>
        )}
        {phase === 'conflict' && (
          <InlineNotice title="搜索偏好已在其他页面发生修改">
            <p>
              你当前未保存的修改已保留。请查看最新保存配置后，再决定如何继续。
            </p>
            <Button
              variant="outline"
              disabled={busy}
              onClick={() => void inspect()}
            >
              {busy ? '检查中…' : '查看最新配置'}
            </Button>
          </InlineNotice>
        )}
        {phase === 'unknown' && (
          <InlineNotice title="暂时无法确认保存结果">
            <p>
              刚才尝试保存的内容已保留。验证将使用原请求重试，不会自动采用新的版本或开始新的保存。
            </p>
            <div className="flex flex-wrap gap-2">
              <Button disabled={busy} onClick={() => void submit(true)}>
                {busy ? '检查中…' : '验证保存结果'}
              </Button>
              <Button
                variant="outline"
                disabled={busy}
                onClick={() => void inspect()}
              >
                查看当前配置
              </Button>
            </div>
          </InlineNotice>
        )}
        {notice && (
          <InlineNotice title={notice}>
            {phase === 'confirmed' && (
              <Button
                variant="outline"
                disabled={busy}
                onClick={() => void refreshConfirmed()}
              >
                {busy ? '读取中…' : '重新读取当前配置'}
              </Button>
            )}
          </InlineNotice>
        )}
        {latest && (
          <div className="space-y-3">
            <SavedPreferences current={latest} />
            {phase === 'conflict' && (
              <div className="flex flex-wrap justify-end gap-2">
                <Button
                  variant="outline"
                  disabled={busy}
                  onClick={() => setDiscard(true)}
                >
                  放弃当前修改
                </Button>
                <Button
                  disabled={busy}
                  onClick={() => {
                    setBase(latest);
                    setLatest(undefined);
                    setPhase('editing');
                    setNotice(
                      '已采用最新配置作为保存基准。你的输入保持不变，请检查后再明确保存。',
                    );
                  }}
                >
                  基于最新配置继续编辑
                </Button>
              </div>
            )}
          </div>
        )}
        {Object.values(errors).some((items) => items?.length) && (
          <div
            ref={summary}
            tabIndex={-1}
            role="alert"
            className="rounded-md border border-notice-border bg-notice-background p-3 text-sm"
          >
            <p className="font-medium">部分配置需要修改</p>
            <ul className="mt-2 flex flex-wrap gap-x-4 gap-y-1">
              {(Object.keys(errors) as PreferenceField[])
                .filter((field) => errors[field]?.length)
                .map((field) => (
                  <li key={field}>
                    <a
                      className="underline"
                      href={`#pref-${field}`}
                      onClick={(e) => {
                        e.preventDefault();
                        document.getElementById(`pref-${field}`)?.focus();
                      }}
                    >
                      {fieldLabels[field]}
                    </a>
                  </li>
                ))}
            </ul>
          </div>
        )}
        <PreferencesFields
          draft={draft}
          onChange={change}
          onAdd={add}
          errors={errors}
          disabled={busy || phase === 'unknown' || phase === 'confirmed'}
        />
        <div className="sticky bottom-0 flex flex-wrap items-center justify-between gap-3 border-t border-border bg-surface py-4">
          <p className="max-w-xl text-xs leading-relaxed text-text-muted">
            {phase === 'unknown'
              ? '保存结果尚不明确，已暂停新的提交。'
              : phase === 'conflict'
                ? '请查看最新配置并明确选择保存基准。'
                : dirty
                  ? '有未保存的修改。保存不会启动岗位收集，也不会筛选已有岗位。'
                  : '搜索偏好仅用于后续岗位收集。'}
          </p>
          <div className="flex gap-2">
            <Button
              variant="outline"
              disabled={busy || (!dirty && phase === 'editing')}
              onClick={() => setDiscard(true)}
            >
              取消
            </Button>
            <Button type="submit" disabled={busy || phase !== 'editing'}>
              {busy
                ? '处理中…'
                : base.status === 'NOT_CONFIGURED'
                  ? '保存偏好'
                  : '保存修改'}
            </Button>
          </div>
        </div>
        <p className="text-xs leading-relaxed text-text-muted">
          页面关闭后不会保留未保存输入或待核验请求。若上次操作中断，请先核对当前保存配置；当前内容不能证明先前请求的结果。
        </p>
      </form>
      {(discard || blocker.state === 'blocked') && (
        <AlertDialog
          title={busy ? '正在处理保存请求' : '放弃本地输入？'}
          description={
            phase === 'unknown'
              ? '保存结果仍未确认。离开或放弃后将丢失本次请求的核验信息；这不会撤销可能已生效的保存。'
              : '未保存的输入将被清除；已保存配置不会被删除。'
          }
          busy={busy}
          cancelLabel="继续编辑"
          onCancel={() => {
            setDiscard(false);
            if (blocker.state === 'blocked') blocker.reset();
          }}
          action={
            <Button variant="destructive" disabled={busy} onClick={abandon}>
              放弃并继续
            </Button>
          }
        />
      )}
    </>
  );
}
