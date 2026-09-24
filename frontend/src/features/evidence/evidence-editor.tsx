import { useState, useRef, useEffect } from 'react';
import type { components } from '@/shared/api/schema';
import { candidateApi } from '@/features/candidate/api';
import { useCandidateCommand } from '@/features/candidate/use-command';
import { CommandFeedback } from '@/features/candidate/command-feedback';
import { DirtyGuard } from '@/features/candidate/dirty-guard';
import {
  localErrors,
  serverErrors,
  errorAt,
  type Errors,
} from '@/features/candidate/field-errors';
import {
  fieldsByKind,
  fieldLabels,
  kindLabels,
  emptyFields,
  degrees,
  evidenceValues,
  type EvidencePair,
  type EvidenceKind,
  type EvidenceContent,
} from '@/entities/evidence/model';
import { Button } from '@/shared/ui/button';
import { FormControl, FormSection } from '@/shared/ui/form-control';
import { BlockEditor } from '@/features/candidate/block-editor';
import { AlertDialog } from '@/shared/ui/alert-dialog';
export function EvidenceEditor({
  kind,
  initial,
  onClose,
  onSaved,
  embedded = false,
  onState,
}: {
  kind: EvidenceKind;
  initial?: EvidencePair;
  onClose: () => void;
  onSaved: (value: EvidencePair) => void;
  embedded?: boolean;
  onState?: (state: {
    dirty: boolean;
    busy: boolean;
    unknown: boolean;
  }) => void;
}) {
  const allowLeave = useRef(false);
  function leave() {
    allowLeave.current = true;
    onClose();
  }
  const [base, setBase] = useState(initial),
    [fields, setFields] = useState<Record<string, string | null>>(() =>
      initial ? { ...initial.evidence_item_version.fields } : emptyFields(kind),
    ),
    [content, setContent] = useState<EvidenceContent>(() =>
      initial ? structuredClone(initial.evidence_item_version.content) : [],
    ),
    [baseline, setBaseline] = useState(() =>
      JSON.stringify({
        fields: initial?.evidence_item_version.fields ?? emptyFields(kind),
        content: initial?.evidence_item_version.content ?? [],
      }),
    ),
    [errors, setErrors] = useState<Errors>({}),
    [latest, setLatest] = useState<EvidencePair>(),
    [notice, setNotice] = useState(''),
    [discard, setDiscard] = useState(false);
  const command = useCandidateCommand(
    async (
      body:
        | components['schemas']['EvidenceCreate']
        | components['schemas']['EvidenceUpdate'],
    ) =>
      base
        ? candidateApi.saveEvidence(
            base.evidence_item.evidence_item_id,
            body as components['schemas']['EvidenceUpdate'],
          )
        : candidateApi.createEvidence(
            body as components['schemas']['EvidenceCreate'],
          ),
    async (result) => {
      const current = await candidateApi.evidenceItem(
        result.evidence_item.evidence_item_id,
      );
      setBase(current);
      setFields({ ...current.evidence_item_version.fields });
      setContent(current.evidence_item_version.content);
      setBaseline(
        JSON.stringify({
          fields: current.evidence_item_version.fields,
          content: current.evidence_item_version.content,
        }),
      );
      setErrors({});
      onSaved(current);
    },
  );
  const dirty = JSON.stringify({ fields, content }) !== baseline;
  useEffect(() => {
    onState?.({ dirty, busy: command.busy, unknown: command.unknown });
  }, [dirty, command.busy, command.unknown, onState]);
  const disabled = command.disabled || base?.evidence_item.status === 'RETIRED';
  const allErrors = { ...errors, ...serverErrors(command.error) };
  async function save() {
    const parsed = evidenceValues(kind).safeParse({ fields, content });
    if (!parsed.success) {
      setErrors(localErrors(parsed.error));
      return false;
    }
    setErrors({});
    return command.execute(
      base
        ? {
            request_id: crypto.randomUUID(),
            revision: base.evidence_item.revision,
            ...parsed.data,
          }
        : { request_id: crypto.randomUUID(), kind, ...parsed.data },
    );
  }
  async function inspect() {
    if (!base) {
      setNotice('原请求尚未确认；请使用“验证操作结果”，不要重复创建。');
      return;
    }
    try {
      setLatest(
        await candidateApi.evidenceItem(base.evidence_item.evidence_item_id),
      );
      setNotice('');
    } catch {
      setNotice('暂时无法读取最新资料。');
    }
  }
  return (
    <>
      <form
        noValidate
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
        {notice && (
          <p role="alert" className="mt-3 text-sm">
            {notice}
          </p>
        )}
        {base?.evidence_item.status === 'RETIRED' && (
          <p role="alert" className="p-4 text-sm">
            这条资料已被移除；已引用它的简历仍保留历史来源。
          </p>
        )}
        {latest && (
          <div className="my-4 space-y-3 rounded-md border border-border p-4">
            <h3 className="text-sm font-medium">
              最新读取的资料
              {latest.evidence_item.status === 'RETIRED' ? '（已移除）' : ''}
            </h3>
            <dl className="space-y-2 text-sm">
              {Object.entries(latest.evidence_item_version.fields).map(
                ([k, v]) => (
                  <div key={k}>
                    {fieldLabels[k]}：{v ?? '未填写'}
                  </div>
                ),
              )}
            </dl>
            <div className="whitespace-pre-wrap text-sm">
              {latest.evidence_item_version.content.map((b, i) => (
                <p key={i}>
                  {b.type === 'PARAGRAPH' ? b.text : b.items.join(' · ')}
                </p>
              ))}
            </div>
            {!command.unknown && latest.evidence_item.status === 'ACTIVE' && (
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
        <FormSection title="基本信息">
          <div className="grid max-w-3xl gap-5 sm:grid-cols-2">
            {Object.entries(fieldsByKind[kind].shape).map(([key, schema]) => (
              <FormControl
                key={key}
                label={
                  key === 'role_title' && kind === 'WORK_EXPERIENCE'
                    ? '职位名称'
                    : (fieldLabels[key] ?? key)
                }
                value={fields[key] ?? null}
                onChange={(v) => setFields({ ...fields, [key]: v })}
                nullable={schema.isNullable()}
                required={!schema.isNullable()}
                disabled={disabled}
                type={key.endsWith('month') ? 'month' : 'text'}
                options={key === 'degree' ? degrees : undefined}
                error={errorAt(allErrors, 'fields.' + key)}
                help={
                  key === 'end_month'
                    ? '留空表示至今'
                    : key === 'start_month'
                      ? '留空表示开始时间未知'
                      : undefined
                }
              />
            ))}
          </div>
        </FormSection>
        <FormSection title={kindLabels[kind] + '内容'}>
          <p className="text-xs text-text-muted">
            按段落或列表记录事实。内容可为空；不支持文字格式、代码或嵌套列表。
          </p>
          <BlockEditor
            label="资料内容"
            value={content}
            onChange={(v) => setContent(v as EvidenceContent)}
            disabled={disabled}
          />
          {errorAt(allErrors, 'content') && (
            <p role="alert" className="text-sm text-destructive">
              {errorAt(allErrors, 'content')}
            </p>
          )}
        </FormSection>
        <div className="sticky bottom-0 flex justify-end gap-2 border-t border-border bg-surface py-4">
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
            disabled={disabled || command.error?.code === 'REVISION_CONFLICT'}
          >
            {command.busy ? '保存中…' : `保存${kindLabels[kind]}`}
          </Button>
        </div>
      </form>
      {!embedded && (
        <DirtyGuard
          allowLeave={allowLeave}
          dirty={dirty}
          busy={command.busy}
          unknown={command.unknown}
          onSave={save}
        />
      )}{' '}
      {discard && (
        <AlertDialog
          title="放弃当前修改？"
          description={
            command.unknown
              ? '结果仍未知，离开会丢失原请求的核验信息，不会撤销可能已生效的保存。'
              : '未保存的输入将被清除，已保存资料不受影响。'
          }
          onCancel={() => setDiscard(false)}
          action={
            <Button variant="destructive" onClick={leave}>
              放弃修改
            </Button>
          }
        />
      )}
    </>
  );
}
