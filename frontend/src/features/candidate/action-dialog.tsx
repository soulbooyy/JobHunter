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
import { evidenceName, type EvidencePair } from '@/entities/evidence/model';
type Props = { onClose: () => void; onChanged: () => void } & (
  | { action: 'retire'; target: EvidencePair }
  | {
      action: 'rename' | 'remove' | 'default';
      target: Resume;
      list: ResumeList;
    }
);
export function CandidateActionDialog(props: Props) {
  const [target, setTarget] = useState(props.target),
    [list, setList] = useState('list' in props ? props.list : undefined),
    [name, setName] = useState(
      'resume_name' in props.target ? props.target.resume_name : '',
    ),
    [latestText, setLatestText] = useState(''),
    [readError, setReadError] = useState(''),
    [rebase, setRebase] = useState(false),
    [dismiss, setDismiss] = useState(false);
  const resume = 'resume_id' in target ? target : undefined,
    evidence = 'evidence_item' in target ? target : undefined;
  const index =
    list?.resumes.findIndex((r) => r.resume_id === resume?.resume_id) ?? -1;
  const isDefault =
    resume?.resume_id === list?.default_resume_selection.default_resume_id;
  const replacement = isDefault
    ? (list?.resumes[index + 1] ?? list?.resumes[index - 1])
    : undefined;
  const blocked = props.action === 'remove' && (list?.resumes.length ?? 0) < 2;
  const title = {
    retire: '移除资料',
    rename: '重命名简历',
    remove: '移除简历',
    default: '设为默认简历',
  }[props.action];
  const command = useCandidateCommand(
    async (request: {
      key: string;
      revision: number;
      selection?: number;
      replacement?: string | null;
      name: string;
      targetId: string;
    }) => {
      const request_id = request.key,
        revision = request.revision;
      if (props.action === 'retire')
        return candidateApi.retireEvidence(request.targetId, {
          request_id,
          revision,
        });
      if (props.action === 'rename')
        return candidateApi.renameResume(request.targetId, {
          request_id,
          revision,
          resume_name: request.name,
        });
      if (props.action === 'default')
        return candidateApi.setDefault({
          request_id,
          revision: request.selection!,
          default_resume_id: request.targetId,
        });
      return candidateApi.removeResume(request.targetId, {
        request_id,
        revision,
        default_resume_selection: { revision: request.selection! },
        replacement_resume_id: request.replacement ?? null,
      });
    },
    async () => {
      if (evidence)
        await candidateApi.evidenceItem(
          evidence.evidence_item.evidence_item_id,
        );
      else await candidateApi.resumes();
      props.onChanged();
      props.onClose();
    },
  );
  async function inspect() {
    try {
      if (evidence) {
        const latest = await candidateApi.evidenceItem(
          evidence.evidence_item.evidence_item_id,
        );
        setLatestText(
          `${evidenceName(latest.evidence_item_version.fields)} · ${latest.evidence_item.status === 'ACTIVE' ? '仍在资料库' : '已移除'}`,
        );
        if (!command.unknown) {
          setTarget(latest);
          setRebase(true);
        }
      } else {
        const latest = await candidateApi.resumes();
        const item = latest.resumes.find(
          (r) => r.resume_id === resume?.resume_id,
        );
        setLatestText(
          item
            ? `${item.resume_name} · 当前默认：${latest.resumes.find((r) => r.resume_id === latest.default_resume_selection.default_resume_id)?.resume_name ?? '无'}`
            : '这份简历已被移除',
        );
        if (!command.unknown && item) {
          setTarget(item);
          setList(latest);
          setRebase(true);
        }
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
    void command.execute({
      key: crypto.randomUUID(),
      revision: resume?.revision ?? evidence!.evidence_item.revision,
      selection: list?.default_resume_selection.revision,
      replacement: replacement?.resume_id ?? null,
      name,
      targetId: resume?.resume_id ?? evidence!.evidence_item.evidence_item_id,
    });
  }
  const close = () => (command.unknown ? setDismiss(true) : props.onClose());
  return (
    <>
      <DirtyGuard
        dirty={
          props.action === 'rename' &&
          name !==
            ('resume_name' in props.target ? props.target.resume_name : '')
        }
        busy={command.busy}
        unknown={command.unknown}
      />
      <Dialog
        title={title}
        description={
          evidence
            ? '移除后不再出现在资料库中；已有简历保留其历史来源。'
            : props.action === 'remove'
              ? '移除后不再出现在我的简历列表中。至少需保留一份简历。'
              : '此操作只修改简历管理信息，不改变简历内容。'
        }
        onClose={close}
        busy={command.busy}
      >
        <div className="mt-5 space-y-4">
          <p className="text-sm font-medium">
            {resume?.resume_name ??
              (evidence && evidenceName(evidence.evidence_item_version.fields))}
          </p>
          {blocked && <p role="alert">无法移除最后一份简历，请先新建简历。</p>}
          {replacement && (
            <p className="text-sm">
              移除后默认简历将更换为：<strong>{replacement.resume_name}</strong>
            </p>
          )}
          {props.action === 'rename' && (
            <FormControl
              label="简历名称"
              value={name}
              onChange={(v) => setName(v ?? '')}
              disabled={command.disabled}
            />
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
              采用当前状态作为操作基准
            </Button>
          )}
          {readError && (
            <p role="alert" className="text-sm text-destructive">
              {readError}
            </p>
          )}
          <div className="flex justify-end gap-2">
            <Button variant="outline" disabled={command.busy} onClick={close}>
              关闭
            </Button>
            <Button
              variant={
                props.action === 'remove' || props.action === 'retire'
                  ? 'destructive'
                  : 'default'
              }
              disabled={
                blocked ||
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
