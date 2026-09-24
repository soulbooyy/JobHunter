import { useState, useEffect, useImperativeHandle, type Ref } from 'react';
import { candidateApi } from '@/features/candidate/api';
import { profileValues, type ProfilePair } from '@/entities/profile/model';
import { useCandidateCommand } from '@/features/candidate/use-command';
import { CommandFeedback } from '@/features/candidate/command-feedback';
import { DirtyGuard } from '@/features/candidate/dirty-guard';
import {
  localErrors,
  serverErrors,
  type Errors,
} from '@/features/candidate/field-errors';
import { FormControl } from '@/shared/ui/form-control';
import { Button } from '@/shared/ui/button';
import { AlertDialog } from '@/shared/ui/alert-dialog';
type Values = {
  full_name: string | null;
  phone_number: string | null;
  email: string | null;
};
const values = (p: ProfilePair): Values => ({
  full_name: p.profile_version.full_name,
  phone_number: p.profile_version.phone_number,
  email: p.profile_version.email,
});
export function ProfileEditor({
  initial,
  onClose,
  onSaved,
  embedded = false,
  onState,
  closeRef,
}: {
  initial: ProfilePair;
  onClose: () => void;
  onSaved?: (p: ProfilePair) => void;
  embedded?: boolean;
  onState?: (s: { dirty: boolean; busy: boolean; unknown: boolean }) => void;
  closeRef?: Ref<{ close: () => void }>;
}) {
  const [base, setBase] = useState(initial),
    [draft, setDraft] = useState(() => values(initial)),
    [saved, setSaved] = useState(() => JSON.stringify(values(initial))),
    [errors, setErrors] = useState<Errors>({}),
    [latest, setLatest] = useState<ProfilePair>(),
    [notice, setNotice] = useState(''),
    [discard, setDiscard] = useState(false);
  const command = useCandidateCommand(candidateApi.saveProfile, async () => {
    const current = await candidateApi.profile();
    setBase(current);
    setDraft(values(current));
    setSaved(JSON.stringify(values(current)));
    setLatest(undefined);
    setErrors({});
    onSaved?.(current);
  });
  async function inspect() {
    try {
      setLatest(await candidateApi.profile());
      setNotice('');
    } catch {
      setNotice('暂时无法读取当前个人信息，请重试。');
    }
  }
  async function save() {
    const parsed = profileValues.safeParse(draft);
    if (!parsed.success) {
      setErrors(localErrors(parsed.error));
      return false;
    }
    setErrors({});
    return command.execute({
      request_id: crypto.randomUUID(),
      revision: base.profile.revision,
      ...parsed.data,
    });
  }
  const dirty = JSON.stringify(draft) !== saved;
  useEffect(() => {
    onState?.({
      dirty: dirty || command.confirmed,
      busy: command.busy,
      unknown: command.unknown,
    });
  }, [dirty, command.confirmed, command.busy, command.unknown, onState]);
  useImperativeHandle(closeRef, () => ({
    close: () => {
      if (!command.busy) {
        if (dirty || command.unknown) setDiscard(true);
        else onClose();
      }
    },
  }));
  const allErrors = { ...errors, ...serverErrors(command.error) };
  return (
    <>
      <form
        noValidate
        className="space-y-5"
        onSubmit={(e) => {
          e.preventDefault();
          void save();
        }}
      >
        <CommandFeedback command={command} inspect={() => void inspect()}>
          {command.error?.code === 'REVISION_CONFLICT' && (
            <Button variant="outline" onClick={() => void inspect()}>
              查看最新内容
            </Button>
          )}
        </CommandFeedback>
        {notice && <p role="alert">{notice}</p>}
        {latest && (
          <div className="space-y-3 rounded-md border border-border p-4">
            <p className="text-sm font-medium">最新读取的个人信息</p>
            <dl className="text-sm">
              {Object.entries(values(latest)).map(([k, v]) => (
                <div key={k}>
                  {
                    { full_name: '姓名', phone_number: '电话', email: '邮箱' }[
                      k as keyof Values
                    ]
                  }
                  ：{v ?? '未填写'}
                </div>
              ))}
            </dl>
            {!command.unknown && (
              <Button
                variant="outline"
                onClick={() => {
                  setBase(latest);
                  setLatest(undefined);
                  command.reset();
                }}
              >
                基于最新内容继续编辑
              </Button>
            )}
          </div>
        )}
        <div className="max-w-xl space-y-5">
          {(['full_name', 'phone_number', 'email'] as const).map((key) => (
            <FormControl
              key={key}
              label={
                { full_name: '姓名', phone_number: '电话', email: '邮箱' }[key]
              }
              value={draft[key]}
              nullable
              disabled={command.disabled}
              onChange={(v) => setDraft({ ...draft, [key]: v })}
              error={allErrors[key]}
              help="选填；清空后保存将移除此项内容。"
            />
          ))}
        </div>
        <p className="text-xs text-text-muted">
          保存个人信息不会自动替换已有简历中的个人信息。
        </p>
        <div className="flex justify-end gap-2">
          <Button
            variant="outline"
            disabled={command.busy}
            onClick={() =>
              dirty || command.unknown ? setDiscard(true) : onClose()
            }
          >
            取消
          </Button>
          <Button
            type="submit"
            disabled={
              command.disabled || command.error?.code === 'REVISION_CONFLICT'
            }
          >
            保存个人信息
          </Button>
        </div>
      </form>
      {!embedded && (
        <DirtyGuard
          dirty={dirty}
          busy={command.busy}
          unknown={command.unknown}
          onSave={save}
        />
      )}
      {discard && (
        <AlertDialog
          title="放弃当前修改？"
          description={
            command.unknown
              ? '结果仍未知，离开将丢失原请求核验信息，不会撤销可能生效的保存。'
              : '未保存的个人信息修改将被清除。'
          }
          onCancel={() => setDiscard(false)}
          action={
            <Button variant="destructive" onClick={onClose}>
              放弃修改
            </Button>
          }
        />
      )}
    </>
  );
}
