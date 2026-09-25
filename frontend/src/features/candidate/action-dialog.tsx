import { useState } from 'react';
import { DirtyGuard } from './dirty-guard';
import { Dialog } from '@/shared/ui/dialog';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import { Button } from '@/shared/ui/button';
import { FormControl } from '@/shared/ui/form-control';
import { shortText } from '@/shared/lib/candidate-values';
import { useCandidateCommand } from './use-command';
import { CommandFeedback } from './command-feedback';
import { candidateApi } from './api';
import type { ResumeList, Resume } from '@/entities/resume/model';

type Props = {
  action: 'rename' | 'remove' | 'default';
  target: Resume;
  list: ResumeList;
  onClose: () => void;
  onChanged: () => void;
};
function suggestedReplacement(list: ResumeList, target: Resume) {
  if (list.default_resume_selection.default_resume_id !== target.resume_id)
    return null;
  const index = list.resumes.findIndex(
    (resume) => resume.resume_id === target.resume_id,
  );
  return (
    list.resumes[index + 1]?.resume_id ??
    list.resumes[index - 1]?.resume_id ??
    null
  );
}
export function CandidateActionDialog(props: Props) {
  const [target, setTarget] = useState(props.target);
  const [list, setList] = useState(props.list);
  const [name, setName] = useState(props.target.resume_name);
  const [replacementId, setReplacementId] = useState(() =>
    suggestedReplacement(props.list, props.target),
  );
  const [latestText, setLatestText] = useState('');
  const [readError, setReadError] = useState('');
  const [rebase, setRebase] = useState(false);
  const [dismiss, setDismiss] = useState(false);
  const isDefault =
    target.resume_id === list.default_resume_selection.default_resume_id;
  const replacement = list.resumes.find(
    (resume) => resume.resume_id === replacementId,
  );
  const title = {
    rename: '重命名简历',
    remove: '移除简历',
    default: '设为默认简历',
  }[props.action];
  const command = useCandidateCommand(
    async (request: {
      key: string;
      revision: number;
      selection: number;
      replacement: string | null;
      name: string;
      targetId: string;
    }) => {
      if (props.action === 'rename')
        return candidateApi.renameResume(request.targetId, {
          request_id: request.key,
          revision: request.revision,
          resume_name: request.name,
        });
      if (props.action === 'default')
        return candidateApi.setDefault({
          request_id: request.key,
          revision: request.selection,
          default_resume_id: request.targetId,
        });
      return candidateApi.removeResume(request.targetId, {
        request_id: request.key,
        revision: request.revision,
        default_resume_selection: { revision: request.selection },
        replacement_resume_id: request.replacement,
      });
    },
    async () => {
      await candidateApi.resumes();
      props.onChanged();
      props.onClose();
    },
    {
      message: {
        rename: '简历名称已修改',
        remove: '简历已移除',
        default: '默认简历已更新',
      }[props.action],
      variant: props.action === 'remove' ? 'delete' : 'success',
    },
  );
  async function inspect() {
    try {
      const latest = await candidateApi.resumes();
      const item = latest.resumes.find(
        (resume) => resume.resume_id === target.resume_id,
      );
      setLatestText(
        item
          ? `${item.resume_name} · 当前默认：${latest.resumes.find((resume) => resume.resume_id === latest.default_resume_selection.default_resume_id)?.resume_name ?? '无'}`
          : '这份简历已被移除',
      );
      setList(latest);
      if (!command.unknown && item) {
        setTarget(item);
        setRebase(true);
      }
      setReadError('');
    } catch {
      setReadError('无法读取最新状态，请重试。');
    }
  }
  function submit() {
    if (props.action === 'rename' && !shortText(120).safeParse(name).success) {
      setReadError('简历名称需为 1–120 个字符的单行文字');
      return;
    }
    if (
      props.action === 'remove' &&
      isDefault &&
      list.resumes.length > 1 &&
      !replacement
    ) {
      setReadError('请选择移除后的默认简历');
      return;
    }
    setReadError('');
    void command.execute({
      key: crypto.randomUUID(),
      revision: target.revision,
      selection: list.default_resume_selection.revision,
      replacement:
        props.action === 'remove' && isDefault ? replacementId : null,
      name,
      targetId: target.resume_id,
    });
  }
  const close = () => (command.unknown ? setDismiss(true) : props.onClose());
  return (
    <>
      <DirtyGuard
        dirty={
          (props.action === 'rename' && name !== props.target.resume_name) ||
          (props.action === 'remove' &&
            replacementId !== suggestedReplacement(props.list, props.target))
        }
        busy={command.busy}
        unknown={command.unknown}
      />
      <Dialog
        title={title}
        description={
          props.action === 'remove'
            ? isDefault
              ? list.resumes.length === 1
                ? '这是最后一份简历。移除后将没有默认简历，用户画像来源也会清空。'
                : '请选择移除后作为默认来源的简历。系统不会替你更换选择。'
              : '移除后不再出现在我的简历列表中，其他简历不受影响。'
            : props.action === 'default'
              ? '默认简历将成为用户画像来源；切换不会修改任何简历内容。'
              : '重命名只修改列表名称，不改变简历内容。'
        }
        onClose={close}
        busy={command.busy}
      >
        <div className="mt-5 space-y-4">
          <p className="text-sm font-medium">{target.resume_name}</p>
          {props.action === 'rename' && (
            <FormControl
              label="简历名称"
              value={name}
              onChange={(value) => setName(value ?? '')}
              disabled={command.disabled}
            />
          )}
          {props.action === 'remove' &&
            isDefault &&
            list.resumes.length > 1 && (
              <label className="block space-y-2 text-sm">
                <span className="block font-medium">移除后的默认简历</span>
                <select
                  className="h-10 w-full rounded-md border border-border bg-surface px-3"
                  value={replacementId ?? ''}
                  disabled={command.disabled}
                  onChange={(event) => setReplacementId(event.target.value)}
                >
                  {!replacementId && (
                    <option value="" disabled>
                      请选择默认简历
                    </option>
                  )}
                  {replacementId && !replacement && (
                    <option value={replacementId}>原选择已不可用</option>
                  )}
                  {list.resumes
                    .filter((resume) => resume.resume_id !== target.resume_id)
                    .map((resume) => (
                      <option key={resume.resume_id} value={resume.resume_id}>
                        {resume.resume_name}
                      </option>
                    ))}
                </select>
              </label>
            )}
          <CommandFeedback command={command} inspect={() => void inspect()}>
            {command.error?.code === 'REVISION_CONFLICT' && (
              <Button variant="outline" onClick={() => void inspect()}>
                查看最新状态
              </Button>
            )}
          </CommandFeedback>
          {latestText && (
            <p className="rounded border border-border p-3 text-sm">
              {latestText}
            </p>
          )}
          {rebase && !command.unknown && (
            <Button
              variant="outline"
              onClick={() => {
                command.reset();
                setRebase(false);
              }}
            >
              使用当前状态继续
            </Button>
          )}
          {readError && (
            <p role="alert" className="text-sm text-destructive">
              {readError}
            </p>
          )}
          {replacement && props.action === 'remove' && (
            <p className="text-sm">
              将改为默认：<strong>{replacement.resume_name}</strong>
            </p>
          )}
          <div className="flex justify-end gap-2">
            <Button variant="outline" disabled={command.busy} onClick={close}>
              关闭
            </Button>
            <Button
              variant={props.action === 'remove' ? 'destructive' : 'default'}
              disabled={
                command.disabled ||
                rebase ||
                command.error?.code === 'REVISION_CONFLICT' ||
                command.error?.code === 'INVALID_STATE' ||
                command.error?.code === 'REQUEST_CONFLICT'
              }
              onClick={submit}
            >
              {title}
            </Button>
          </div>
        </div>
      </Dialog>
      {dismiss && (
        <AlertDialog
          title="停止核验并关闭？"
          description="操作结果仍未确认。关闭会丢失原请求信息，不会撤销可能已生效的操作。"
          onCancel={() => setDismiss(false)}
          action={
            <Button variant="destructive" onClick={props.onClose}>
              仍然关闭
            </Button>
          }
        />
      )}
    </>
  );
}
