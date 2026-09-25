import { useRef, useState } from 'react';
import type { components } from '@/shared/api/schema';
import { candidateApi } from '@/features/candidate/api';
import { useCandidateCommand } from '@/features/candidate/use-command';
import { CommandFeedback } from '@/features/candidate/command-feedback';
import { DirtyGuard } from '@/features/candidate/dirty-guard';
import {
  errorAt,
  localErrors,
  serverErrors,
  type Errors,
} from '@/features/candidate/field-errors';
import {
  copyResumeEntry,
  defaultPresentation,
  degrees,
  documentFromVersion,
  entryName,
  fieldLabels,
  fieldsByKind,
  fonts,
  headerLabels,
  kindLabels,
  kinds,
  newResumeEntry,
  resumeDocument,
  type LocalContent,
  type ResumeDocument,
  type ResumeKind,
  type ResumePair,
} from '@/entities/resume/model';
import { shortText } from '@/shared/lib/candidate-values';
import { cn } from '@/shared/lib/cn';
import { FormControl, FormSection } from '@/shared/ui/form-control';
import { Input, inputClass } from '@/shared/ui/input';
import { Button } from '@/shared/ui/button';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import { useToast } from '@/shared/ui/use-toast';
import { AppHeaderActions } from '@/app/layout/app-header-actions';
import { BlockEditor } from '@/features/candidate/block-editor';
import { DraftPreview } from '../preview/draft-preview';

const initialDocument = (initial?: ResumePair): ResumeDocument =>
  initial
    ? documentFromVersion(initial.resume_version)
    : {
        contacts: { full_name: null, phone_number: null, email: null },
        header_presentation: { optional_items: [] },
        sections: [],
        document_presentation: { ...defaultPresentation },
      };

export function ResumeEditor({
  initial,
  onClose,
}: {
  initial?: ResumePair;
  onClose: () => void;
}) {
  const toast = useToast();
  const allowLeave = useRef(false);
  const [base, setBase] = useState(initial);
  const [draft, setDraft] = useState(() => initialDocument(initial));
  const [name, setName] = useState(initial?.resume.resume_name ?? '');
  const [baseline, setBaseline] = useState(() =>
    JSON.stringify({
      draft: initialDocument(initial),
      name: initial?.resume.resume_name ?? '',
    }),
  );
  const [errors, setErrors] = useState<Errors>({});
  const [latest, setLatest] = useState<ResumePair>();
  const [notice, setNotice] = useState('');
  const [discard, setDiscard] = useState(false);
  const [inspecting, setInspecting] = useState(false);

  function leave() {
    allowLeave.current = true;
    onClose();
  }
  function install(pair: ResumePair) {
    const next = documentFromVersion(pair.resume_version);
    setBase(pair);
    setDraft(next);
    setName(pair.resume.resume_name);
    setBaseline(JSON.stringify({ draft: next, name: pair.resume.resume_name }));
    setErrors({});
    setLatest(undefined);
  }
  const command = useCandidateCommand(
    async (
      body:
        | components['schemas']['ResumeCreate']
        | components['schemas']['ResumeSave'],
    ) =>
      base
        ? candidateApi.saveResume(
            base.resume.resume_id,
            body as components['schemas']['ResumeSave'],
          )
        : candidateApi.createResume(
            body as components['schemas']['ResumeCreate'],
          ),
    async (result) => {
      const current = await candidateApi.resume(result.resume.resume_id);
      install(current);
      setNotice('');
      if (
        current.resume.current_resume_version_id !==
        result.resume.current_resume_version_id
      )
        return {
          message: '本次保存已确认；当前页面已显示随后保存的新版本。',
          variant: 'warning' as const,
        };
    },
    {
      message: base ? '简历修改已保存' : '简历已创建',
      variant: 'success',
    },
  );
  const dirty = JSON.stringify({ draft, name }) !== baseline;
  const disabled = command.disabled || base?.resume.status === 'REMOVED';
  const allErrors = { ...errors, ...serverErrors(command.error) };

  async function save() {
    const normalized = {
      ...draft,
      sections: draft.sections.filter((section) => section.members.length),
    };
    const parsed = resumeDocument.safeParse(normalized);
    const nameParsed = shortText(120).safeParse(name);
    if (!parsed.success || (!base && !nameParsed.success)) {
      setErrors({
        ...(!parsed.success ? localErrors(parsed.error) : {}),
        ...(!base && !nameParsed.success
          ? { resume_name: '请输入 1–120 个字符的简历名称' }
          : {}),
      });
      toast.warning('请检查标记的内容。');
      return false;
    }
    setErrors({});
    return command.execute(
      base
        ? {
            request_id: crypto.randomUUID(),
            revision: base.resume.revision,
            ...parsed.data,
          }
        : {
            request_id: crypto.randomUUID(),
            resume_name: name,
            ...parsed.data,
          },
    );
  }
  async function inspect() {
    setInspecting(true);
    try {
      if (base) setLatest(await candidateApi.resume(base.resume.resume_id));
      else {
        const list = await candidateApi.resumes();
        setNotice(
          `当前有 ${list.resumes.length} 份简历。列表不能确认本次创建结果，请使用原请求核验。`,
        );
      }
    } catch {
      setNotice('暂时无法读取当前简历状态。');
    } finally {
      setInspecting(false);
    }
  }
  function addEntry(kind: ResumeKind) {
    setDraft((current) => {
      const sections = structuredClone(current.sections);
      let section = sections.find((item) => item.kind === kind);
      if (!section) {
        section = { kind, members: [] };
        sections.push(section);
      }
      section.members.push(newResumeEntry(kind));
      return { ...current, sections };
    });
  }
  function updateEntry(
    entryId: string,
    update: (
      entry: ResumeDocument['sections'][number]['members'][number],
    ) => ResumeDocument['sections'][number]['members'][number],
  ) {
    setDraft((current) => ({
      ...current,
      sections: current.sections.map((section) => ({
        ...section,
        members: section.members.map((entry) =>
          entry.entry_id === entryId ? update(entry) : entry,
        ),
      })),
    }));
  }
  function removeEntry(entryId: string) {
    setDraft((current) => ({
      ...current,
      sections: current.sections.flatMap((section) => {
        const members = section.members.filter(
          (entry) => entry.entry_id !== entryId,
        );
        return members.length ? [{ ...section, members }] : [];
      }),
    }));
  }
  function move(kind: ResumeKind, entryId: string | undefined, delta: number) {
    setDraft((current) => {
      const sections = structuredClone(current.sections);
      if (entryId) {
        const members = sections.find(
          (section) => section.kind === kind,
        )!.members;
        const index = members.findIndex((entry) => entry.entry_id === entryId);
        const [entry] = members.splice(index, 1);
        members.splice(index + delta, 0, entry!);
      } else {
        const index = sections.findIndex((section) => section.kind === kind);
        const [section] = sections.splice(index, 1);
        sections.splice(index + delta, 0, section!);
      }
      return { ...current, sections };
    });
  }
  return (
    <>
      <AppHeaderActions>
        <div className="flex gap-2">
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
            disabled={
              disabled ||
              inspecting ||
              command.error?.code === 'REVISION_CONFLICT'
            }
            onClick={() => void save()}
          >
            {command.busy ? '保存中…' : '保存简历'}
          </Button>
        </div>
      </AppHeaderActions>
      <CommandFeedback command={command} inspect={() => void inspect()}>
        {command.error?.code === 'REVISION_CONFLICT' && (
          <Button
            disabled={inspecting}
            variant="outline"
            onClick={() => void inspect()}
          >
            查看最新版本
          </Button>
        )}
      </CommandFeedback>
      {notice && (
        <p
          role="status"
          className="my-4 rounded border border-border bg-surface-muted p-3 text-sm"
        >
          {notice}
        </p>
      )}
      {base?.resume.status === 'REMOVED' && (
        <p role="alert" className="my-4 text-sm">
          这份简历已被移除，不能继续保存。
          <Button variant="outline" onClick={leave}>
            返回我的简历
          </Button>
        </p>
      )}
      {latest && (
        <div className="my-4 space-y-3 rounded-md border border-border p-4">
          <h2 className="font-medium">
            最新保存内容：{latest.resume.resume_name}
          </h2>
          <p className="text-sm">
            {latest.resume.status === 'REMOVED'
              ? '这份简历已被移除'
              : `${latest.resume_version.sections.reduce((sum, section) => sum + section.members.length, 0)} 条经历。你的当前草稿仍保留。`}
          </p>
          {!command.unknown && (
            <div className="flex gap-2">
              <Button
                variant="outline"
                onClick={() => {
                  install(latest);
                  command.reset();
                }}
              >
                放弃草稿并加载最新版本
              </Button>
              {latest.resume.status === 'ACTIVE' && (
                <Button
                  onClick={() => {
                    setBase(latest);
                    setLatest(undefined);
                    command.reset();
                  }}
                >
                  保留草稿并基于最新版本保存
                </Button>
              )}
            </div>
          )}
        </div>
      )}
      <div className="grid min-w-0 gap-6 xl:h-[calc(100vh-7.5rem)] xl:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
        <div className="min-w-0 xl:flex xl:min-h-0 xl:flex-col">
          <section
            role="region"
            aria-label="简历模块"
            className="sticky top-0 z-10 mb-3 rounded-md border border-border bg-surface p-3 xl:shrink-0"
          >
            <h2 className="sr-only">添加简历模块</h2>
            <div className="flex flex-wrap gap-2">
              {kinds.map((kind) => (
                <Button
                  key={kind}
                  variant="outline"
                  aria-label={`添加${kindLabels[kind]}`}
                  disabled={disabled}
                  onClick={() => addEntry(kind)}
                >
                  <span aria-hidden="true">＋</span>
                  {kindLabels[kind]}
                </Button>
              ))}
            </div>
          </section>
          <div
            role="region"
            aria-label="简历编辑内容"
            className="min-w-0 xl:min-h-0 xl:flex-1 xl:overflow-y-auto xl:pr-2"
          >
            {!base && (
              <div className="mb-4 min-w-0 px-1 pt-1">
                <FormControl
                  label="简历名称"
                  value={name}
                  required
                  disabled={disabled}
                  onChange={(value) => setName(value ?? '')}
                  error={allErrors.resume_name}
                />
              </div>
            )}
            <FormSection title="基本信息">
              <p className="text-xs text-text-muted">
                基本信息只属于当前简历，不会同步到其他简历。
              </p>
              <div className="grid grid-cols-[repeat(auto-fit,minmax(130px,1fr))] gap-3">
                {(
                  [
                    ['full_name', '姓名', 'text'],
                    ['phone_number', '电话', 'tel'],
                    ['email', '邮箱', 'email'],
                  ] as const
                ).map(([key, label, type]) => (
                  <FormControl
                    key={key}
                    label={label}
                    value={draft.contacts[key]}
                    nullable
                    compact
                    type={type}
                    disabled={disabled}
                    onChange={(value) =>
                      setDraft({
                        ...draft,
                        contacts: { ...draft.contacts, [key]: value },
                      })
                    }
                    error={errorAt(allErrors, `contacts.${key}`)}
                  />
                ))}
                {draft.header_presentation.optional_items.map((item, index) => (
                  <div key={item.kind} className="min-w-0 space-y-1">
                    <FormControl
                      label={headerLabels[item.kind]}
                      value={item.value}
                      compact
                      disabled={disabled}
                      onChange={(value) =>
                        setDraft({
                          ...draft,
                          header_presentation: {
                            optional_items:
                              draft.header_presentation.optional_items.map(
                                (current, currentIndex) =>
                                  currentIndex === index
                                    ? { ...current, value: value ?? '' }
                                    : current,
                              ),
                          },
                        })
                      }
                      error={errorAt(
                        allErrors,
                        `header_presentation.optional_items[${index}]`,
                      )}
                    />
                    <div className="flex justify-end gap-1">
                      {([-1, 1] as const).map((direction) => (
                        <Button
                          key={direction}
                          variant="ghost"
                          className="size-7 px-0"
                          aria-label={`${direction < 0 ? '上移' : '下移'}${headerLabels[item.kind]}`}
                          disabled={
                            disabled ||
                            index + direction < 0 ||
                            index + direction >=
                              draft.header_presentation.optional_items.length
                          }
                          onClick={() => {
                            const items = [
                              ...draft.header_presentation.optional_items,
                            ];
                            [items[index], items[index + direction]] = [
                              items[index + direction]!,
                              items[index]!,
                            ];
                            setDraft({
                              ...draft,
                              header_presentation: {
                                optional_items: items,
                              },
                            });
                          }}
                        >
                          {direction < 0 ? '↑' : '↓'}
                        </Button>
                      ))}
                      <Button
                        variant="ghost"
                        className="size-7 px-0"
                        aria-label={`移除${headerLabels[item.kind]}`}
                        disabled={disabled}
                        onClick={() =>
                          setDraft({
                            ...draft,
                            header_presentation: {
                              optional_items:
                                draft.header_presentation.optional_items.filter(
                                  (_, currentIndex) => currentIndex !== index,
                                ),
                            },
                          })
                        }
                      >
                        ×
                      </Button>
                    </div>
                  </div>
                ))}
                <label className="block space-y-1 text-xs font-medium">
                  <span className="block">添加信息项</span>
                  <select
                    aria-label="添加信息项"
                    className={cn(inputClass, 'h-9 w-full min-w-0 px-2')}
                    value=""
                    disabled={
                      disabled ||
                      draft.header_presentation.optional_items.length ===
                        Object.keys(headerLabels).length
                    }
                    onChange={(event) => {
                      const kind = event.target
                        .value as keyof typeof headerLabels;
                      if (kind)
                        setDraft({
                          ...draft,
                          header_presentation: {
                            optional_items: [
                              ...draft.header_presentation.optional_items,
                              { kind, value: '' },
                            ],
                          },
                        });
                    }}
                  >
                    <option value="">＋ 信息项</option>
                    {Object.entries(headerLabels)
                      .filter(
                        ([key]) =>
                          !draft.header_presentation.optional_items.some(
                            (item) => item.kind === key,
                          ),
                      )
                      .map(([key, label]) => (
                        <option key={key} value={key}>
                          {label}
                        </option>
                      ))}
                  </select>
                </label>
              </div>
            </FormSection>
            {draft.sections.map((section, sectionIndex) => (
              <FormSection
                key={section.kind}
                title={kindLabels[section.kind]}
                action={
                  <div className="flex flex-wrap gap-1">
                    <Button
                      variant="ghost"
                      disabled={disabled || sectionIndex === 0}
                      onClick={() => move(section.kind, undefined, -1)}
                    >
                      上移分类
                    </Button>
                    <Button
                      variant="ghost"
                      disabled={
                        disabled || sectionIndex === draft.sections.length - 1
                      }
                      onClick={() => move(section.kind, undefined, 1)}
                    >
                      下移分类
                    </Button>
                  </div>
                }
              >
                <div className="space-y-5">
                  {section.members.map((entry, entryIndex) => (
                    <article
                      key={entry.entry_id}
                      className="space-y-4 rounded-md border border-border p-4"
                    >
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <h3 className="text-sm font-semibold">
                          {entryName(entry.fields) ||
                            `未命名${kindLabels[section.kind]}`}
                        </h3>
                        <div className="flex flex-wrap gap-1">
                          <Button
                            variant="ghost"
                            disabled={disabled || entryIndex === 0}
                            onClick={() =>
                              move(section.kind, entry.entry_id, -1)
                            }
                          >
                            上移
                          </Button>
                          <Button
                            variant="ghost"
                            disabled={
                              disabled ||
                              entryIndex === section.members.length - 1
                            }
                            onClick={() =>
                              move(section.kind, entry.entry_id, 1)
                            }
                          >
                            下移
                          </Button>
                          <Button
                            variant="ghost"
                            disabled={disabled}
                            onClick={() =>
                              setDraft((current) => ({
                                ...current,
                                sections: current.sections.map((item) =>
                                  item.kind === section.kind
                                    ? {
                                        ...item,
                                        members: item.members.flatMap(
                                          (candidate) =>
                                            candidate.entry_id ===
                                            entry.entry_id
                                              ? [
                                                  candidate,
                                                  copyResumeEntry(candidate),
                                                ]
                                              : [candidate],
                                        ),
                                      }
                                    : item,
                                ),
                              }))
                            }
                          >
                            复制
                          </Button>
                          <Button
                            variant="ghost"
                            disabled={disabled}
                            onClick={() => removeEntry(entry.entry_id)}
                          >
                            移除
                          </Button>
                        </div>
                      </div>
                      <div className="grid gap-4 sm:grid-cols-2">
                        {Object.entries(fieldsByKind[section.kind].shape).map(
                          ([key, schema]) => (
                            <FormControl
                              key={key}
                              label={
                                key === 'role_title' &&
                                section.kind === 'WORK_EXPERIENCE'
                                  ? '职位名称'
                                  : (fieldLabels[key] ?? key)
                              }
                              value={
                                (entry.fields as Record<string, string | null>)[
                                  key
                                ] ?? null
                              }
                              nullable={schema.isNullable()}
                              required={!schema.isNullable()}
                              disabled={disabled}
                              type={key.endsWith('month') ? 'month' : 'text'}
                              options={key === 'degree' ? degrees : undefined}
                              onChange={(value) =>
                                updateEntry(entry.entry_id, (current) => ({
                                  ...current,
                                  fields: {
                                    ...current.fields,
                                    [key]: value,
                                  },
                                }))
                              }
                              error={errorAt(
                                allErrors,
                                `sections[${sectionIndex}].members[${entryIndex}].fields.${key}`,
                              )}
                              help={
                                key === 'end_month'
                                  ? '留空表示至今'
                                  : key === 'start_month'
                                    ? '留空表示开始时间未知'
                                    : undefined
                              }
                            />
                          ),
                        )}
                      </div>
                      <BlockEditor
                        label={`${kindLabels[section.kind]}简历内容`}
                        disabled={disabled}
                        value={entry.content}
                        onChange={(content: LocalContent) =>
                          updateEntry(entry.entry_id, (current) => ({
                            ...current,
                            content,
                          }))
                        }
                      />
                      {errorAt(
                        allErrors,
                        `sections[${sectionIndex}].members[${entryIndex}]`,
                      ) && (
                        <p role="alert" className="text-sm text-destructive">
                          {errorAt(
                            allErrors,
                            `sections[${sectionIndex}].members[${entryIndex}]`,
                          )}
                        </p>
                      )}
                    </article>
                  ))}
                </div>
              </FormSection>
            ))}
          </div>
        </div>
        <div className="min-w-0 xl:flex xl:min-h-0 xl:flex-col">
          <section aria-label="排版设置" className="mb-4 xl:shrink-0">
            <div className="grid grid-cols-[minmax(90px,1.3fr)_minmax(64px,1fr)_minmax(64px,1fr)_minmax(48px,0.7fr)] items-end gap-2">
              <FormControl
                label="字体"
                value={draft.document_presentation.font_family}
                options={fonts}
                disabled={disabled}
                onChange={(value) =>
                  setDraft({
                    ...draft,
                    document_presentation: {
                      ...draft.document_presentation,
                      font_family: value as keyof typeof fonts,
                    },
                  })
                }
              />
              {(['font_size_pt', 'line_spacing_pt'] as const).map((key) => (
                <label key={key} className="block space-y-2 text-sm">
                  <span className="block font-medium">
                    {key === 'font_size_pt' ? '字号（磅）' : '行高（磅）'}
                  </span>
                  <Input
                    className="w-full min-w-0 px-2"
                    type="number"
                    step="0.5"
                    value={
                      Number.isFinite(draft.document_presentation[key])
                        ? draft.document_presentation[key]
                        : ''
                    }
                    disabled={disabled}
                    onChange={(event) =>
                      setDraft({
                        ...draft,
                        document_presentation: {
                          ...draft.document_presentation,
                          [key]:
                            event.target.value === ''
                              ? NaN
                              : Number(event.target.value),
                        },
                      })
                    }
                  />
                </label>
              ))}
              <label className="block space-y-2 text-sm">
                <span className="block font-medium">主题颜色</span>
                <Input
                  className="w-full min-w-0 px-2"
                  type="color"
                  aria-label="主题颜色"
                  value={draft.document_presentation.theme_color}
                  disabled={disabled}
                  onChange={(event) =>
                    setDraft({
                      ...draft,
                      document_presentation: {
                        ...draft.document_presentation,
                        theme_color: event.target.value.toUpperCase(),
                      },
                    })
                  }
                />
              </label>
            </div>
            {errorAt(allErrors, 'document_presentation') && (
              <p role="alert" className="text-sm text-destructive">
                {errorAt(allErrors, 'document_presentation')}
              </p>
            )}
          </section>
          <div
            role="region"
            aria-label="简历预览内容"
            className="min-w-0 xl:min-h-0 xl:flex-1 xl:overflow-y-auto xl:pr-2"
          >
            <DraftPreview draft={draft} />
          </div>
        </div>
      </div>
      <DirtyGuard
        allowLeave={allowLeave}
        dirty={dirty}
        busy={command.busy}
        unknown={command.unknown}
        onSave={save}
      />
      {discard && (
        <AlertDialog
          title="离开简历编辑？"
          description={
            command.unknown
              ? '保存结果仍未知，离开会丢失核验信息，不会撤销可能生效的保存。'
              : '未保存的简历修改将丢失。'
          }
          onCancel={() => setDiscard(false)}
          action={
            <>
              <Button variant="outline" onClick={leave}>
                放弃并离开
              </Button>
              {!command.unknown && (
                <Button
                  onClick={async () => {
                    if (await save()) leave();
                  }}
                >
                  保存后离开
                </Button>
              )}
            </>
          }
        />
      )}
    </>
  );
}
