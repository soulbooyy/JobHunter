import { useState, useRef } from 'react';
import { useQuery } from '@tanstack/react-query';
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
  documentFromVersion,
  defaultPresentation,
  resumeDocument,
  headerLabels,
  fonts,
  initializeContent,
  type ResumePair,
  type ResumeDocument,
  type LocalContent,
} from '@/entities/resume/model';
import type { ProfilePair, ProfileVersion } from '@/entities/profile/model';
import {
  kinds,
  kindLabels,
  evidenceName,
  fieldLabels,
  type EvidenceKind,
  type EvidencePair,
  type EvidenceVersion,
} from '@/entities/evidence/model';
import { shortText } from '@/shared/lib/candidate-values';
import { FormControl, FormSection } from '@/shared/ui/form-control';
import { Input, inputClass } from '@/shared/ui/input';
import { Button } from '@/shared/ui/button';
import { Dialog } from '@/shared/ui/dialog';
import { AlertDialog } from '@/shared/ui/alert-dialog';
import { BlockEditor } from '@/features/candidate/block-editor';
import { SourcePicker } from './source-picker';
import { DraftPreview } from '../preview/draft-preview';
import { ProfileEditor } from '@/features/profile/profile-editor';
import { EvidenceEditor } from '@/features/evidence/evidence-editor';
const initialDraft = (
  profile: ProfilePair,
  initial?: ResumePair,
): ResumeDocument =>
  initial
    ? documentFromVersion(initial.resume_version)
    : {
        profile_version_id: profile.profile_version.profile_version_id,
        header_presentation: { optional_items: [] },
        sections: [],
        document_presentation: { ...defaultPresentation },
      };
type SourceChange = { itemId: string; current: EvidencePair };
export function ResumeEditor({
  initial,
  profile,
  onClose,
}: {
  initial?: ResumePair;
  profile: ProfilePair;
  onClose: () => void;
}) {
  const profileClose = useRef<{ close: () => void }>(null);
  const [profileState, setProfileState] = useState({
    dirty: false,
    busy: false,
    unknown: false,
  });
  const allowLeave = useRef(false);
  function leave() {
    allowLeave.current = true;
    onClose();
  }
  const [base, setBase] = useState(initial),
    [draft, setDraft] = useState(() => initialDraft(profile, initial)),
    [name, setName] = useState(initial?.resume.resume_name ?? ''),
    [baseline, setBaseline] = useState(() =>
      JSON.stringify({
        draft: initialDraft(profile, initial),
        name: initial?.resume.resume_name ?? '',
      }),
    ),
    [picker, setPicker] = useState<EvidenceKind>(),
    [createKind, setCreateKind] = useState<EvidenceKind>(),
    [embeddedState, setEmbeddedState] = useState({
      dirty: false,
      busy: false,
      unknown: false,
    }),
    [errors, setErrors] = useState<Errors>({}),
    [latest, setLatest] = useState<ResumePair>(),
    [sourceChange, setSourceChange] = useState<SourceChange>(),
    [profileChange, setProfileChange] = useState<ProfilePair>(),
    [resetExpression, setResetExpression] = useState(false),
    [notice, setNotice] = useState(''),
    [discard, setDiscard] = useState(false),
    [inspecting, setInspecting] = useState(false);
  const refs = draft.sections.flatMap((s) =>
    s.members.map((m) => ({
      id: m.evidence_item_id,
      version: m.evidence_item_version_id,
      kind: s.kind,
    })),
  );
  const sources = useQuery({
    queryKey: [
      'candidate',
      'draft-sources',
      draft.profile_version_id,
      refs.map((r) => r.version).join(','),
    ],
    queryFn: async () => {
      const [p, ...items] = await Promise.all([
        candidateApi.profileVersion(draft.profile_version_id),
        ...refs.map(async (r) => {
          const exact = await candidateApi.evidenceVersion(r.version);
          if (
            exact.evidence_item_version.evidence_item_id !== r.id ||
            exact.kind !== r.kind
          )
            throw Error('source ownership');
          return exact.evidence_item_version;
        }),
      ]);
      return {
        profile: p as ProfileVersion,
        evidence: Object.fromEntries(
          (items as EvidenceVersion[]).map((v) => [
            v.evidence_item_version_id,
            v,
          ]),
        ),
      };
    },
    gcTime: 0,
  });
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
      setNotice(
        current.resume.current_resume_version_id ===
          result.resume.current_resume_version_id
          ? ''
          : '本次保存已确认；现显示后续变更后的当前简历。',
      );
    },
  );
  const dirty = JSON.stringify({ draft, name }) !== baseline;
  const disabled = command.disabled || base?.resume.status === 'REMOVED';
  const allErrors = { ...errors, ...serverErrors(command.error) };
  async function save() {
    const normalized = {
      ...draft,
      sections: draft.sections.filter((s) => s.members.length),
    };
    const parsed = resumeDocument.safeParse(normalized),
      nameParsed = shortText(120).safeParse(name);
    if (!parsed.success || (!base && !nameParsed.success)) {
      setErrors({
        ...(!parsed.success ? localErrors(parsed.error) : {}),
        ...(!base && !nameParsed.success
          ? { resume_name: '请输入 1–120 个字符的简历名称' }
          : {}),
      });
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
          `当前有 ${list.resumes.length} 份简历。此列表不能确认本次创建结果，请验证原请求。`,
        );
      }
    } catch {
      setNotice('暂时无法读取当前简历状态。');
    } finally {
      setInspecting(false);
    }
  }
  async function inspectSource(id: string) {
    setInspecting(true);
    try {
      const current = await candidateApi.evidenceItem(id);
      setSourceChange({ itemId: id, current });
      setResetExpression(false);
    } catch {
      setNotice('无法读取该资料的当前状态，请稍后重试。');
    } finally {
      setInspecting(false);
    }
  }
  async function inspectProfile() {
    setInspecting(true);
    try {
      setProfileState({ dirty: false, busy: false, unknown: false });
      setProfileChange(await candidateApi.profile());
    } catch {
      setNotice('无法读取最新个人信息，请稍后重试。');
    } finally {
      setInspecting(false);
    }
  }
  function updateContent(id: string, content: LocalContent) {
    setDraft((d) => ({
      ...d,
      sections: d.sections.map((s) => ({
        ...s,
        members: s.members.map((m) =>
          m.evidence_item_id === id ? { ...m, content } : m,
        ),
      })),
    }));
  }
  function include(items: EvidencePair[]) {
    setDraft((d) => {
      const sections = structuredClone(d.sections);
      for (const item of items) {
        if (
          sections.some((s) =>
            s.members.some(
              (m) => m.evidence_item_id === item.evidence_item.evidence_item_id,
            ),
          )
        )
          continue;
        let section = sections.find((s) => s.kind === item.evidence_item.kind);
        if (!section) {
          section = { kind: item.evidence_item.kind, members: [] };
          sections.push(section);
        }
        section.members.push({
          evidence_item_id: item.evidence_item.evidence_item_id,
          evidence_item_version_id:
            item.evidence_item_version.evidence_item_version_id,
          content: initializeContent(item.evidence_item_version.content),
        });
      }
      return { ...d, sections };
    });
    setPicker(undefined);
  }
  function remove(id: string) {
    if (command.error?.code === 'SOURCE_CONFLICT') command.reset();
    setDraft((d) => ({
      ...d,
      sections: d.sections.map((s) => ({
        ...s,
        members: s.members.filter((m) => m.evidence_item_id !== id),
      })),
    }));
  }
  function move(kind: EvidenceKind, id: string | undefined, delta: number) {
    setDraft((d) => {
      const sections = structuredClone(d.sections);
      if (id) {
        const members = sections.find((s) => s.kind === kind)!.members;
        const index = members.findIndex((m) => m.evidence_item_id === id);
        const [item] = members.splice(index, 1);
        members.splice(index + delta, 0, item!);
      } else {
        const index = sections.findIndex((s) => s.kind === kind);
        const [section] = sections.splice(index, 1);
        sections.splice(index + delta, 0, section!);
      }
      return { ...d, sections };
    });
  }
  const previousBinding =
    sourceChange &&
    base?.resume_version.sections
      .flatMap((s) => s.members)
      .find((m) => m.evidence_item_id === sourceChange.itemId);
  return (
    <>
      <header className="mb-5 flex items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-semibold">
            {base ? base.resume.resume_name : '新建简历'}
          </h1>
          <p className="mt-2 text-xs text-text-muted">
            编辑本地表达和排版，不会修改知识库中的事实。
          </p>
        </div>
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
              command.error?.code === 'REVISION_CONFLICT' ||
              command.error?.code === 'SOURCE_CONFLICT'
            }
            onClick={() => void save()}
          >
            {command.busy ? '保存中…' : '保存简历'}
          </Button>
        </div>
      </header>
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
        {command.error?.code === 'SOURCE_CONFLICT' && (
          <p>
            请通过“编辑个人信息”或各条经历的“查看资料更新”重新确认来源，然后保存简历。
          </p>
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
              : `${latest.resume_version.sections.reduce((n, s) => n + s.members.length, 0)} 条经历；以下为最新保存的文字。`}
          </p>
          <div className="max-h-52 space-y-2 overflow-y-auto text-sm">
            {latest.resume_version.sections.map((s) => (
              <section key={s.kind}>
                <h3>{kindLabels[s.kind]}</h3>
                {s.members.map((m) => (
                  <div key={m.evidence_item_id}>
                    {m.content.map((b, i) => (
                      <p key={i}>
                        {(b.type === 'PARAGRAPH'
                          ? [b.runs]
                          : b.items.map((i) => i.runs)
                        )
                          .map((r) => r.map((x) => x.text).join(''))
                          .join(' · ')}
                      </p>
                    ))}
                  </div>
                ))}
              </section>
            ))}
          </div>
          {!command.unknown && (
            <div className="flex gap-2">
              <Button
                variant="outline"
                onClick={() => {
                  install(latest);
                  command.reset();
                }}
              >
                放弃修改并加载最新版本
              </Button>
              {latest.resume.status === 'ACTIVE' && (
                <Button
                  onClick={() => {
                    setBase(latest);
                    setLatest(undefined);
                    command.reset();
                  }}
                >
                  基于最新版本继续编辑
                </Button>
              )}
            </div>
          )}
        </div>
      )}
      <div className="mt-5 grid min-w-0 gap-6 xl:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
        <div className="min-w-0">
          {!base && (
            <FormControl
              label="简历名称"
              value={name}
              required
              disabled={disabled}
              onChange={(v) => setName(v ?? '')}
              error={allErrors.resume_name}
            />
          )}
          <FormSection
            title="个人信息"
            action={
              <Button
                variant="outline"
                disabled={disabled || inspecting}
                onClick={() => void inspectProfile()}
              >
                编辑个人信息
              </Button>
            }
          >
            <p className="text-sm">
              {sources.data
                ? [
                    sources.data.profile.full_name,
                    sources.data.profile.phone_number,
                    sources.data.profile.email,
                  ]
                    .filter(Boolean)
                    .join(' · ') || '个人信息未填写'
                : '正在读取个人信息…'}
            </p>
          </FormSection>
          <FormSection title="附加信息">
            <div className="space-y-4">
              {draft.header_presentation.optional_items.map((item, index) => (
                <div key={item.kind} className="flex items-end gap-2">
                  <div className="min-w-0 flex-1">
                    <FormControl
                      label={headerLabels[item.kind]}
                      value={item.value}
                      onChange={(v) =>
                        setDraft({
                          ...draft,
                          header_presentation: {
                            optional_items:
                              draft.header_presentation.optional_items.map(
                                (x, i) =>
                                  i === index ? { ...x, value: v ?? '' } : x,
                              ),
                          },
                        })
                      }
                      disabled={disabled}
                      error={errorAt(
                        allErrors,
                        `header_presentation.optional_items[${index}]`,
                      )}
                    />
                  </div>
                  {([-1, 1] as const).map((direction) => (
                    <Button
                      key={direction}
                      variant="ghost"
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
                          header_presentation: { optional_items: items },
                        });
                      }}
                    >
                      {direction < 0 ? '↑' : '↓'}
                    </Button>
                  ))}
                  <Button
                    variant="ghost"
                    disabled={disabled}
                    onClick={() =>
                      setDraft({
                        ...draft,
                        header_presentation: {
                          optional_items:
                            draft.header_presentation.optional_items.filter(
                              (_, i) => i !== index,
                            ),
                        },
                      })
                    }
                  >
                    移除
                  </Button>
                </div>
              ))}
              <select
                aria-label="添加附加信息"
                className={inputClass}
                value=""
                disabled={disabled}
                onChange={(e) => {
                  const kind = e.target.value as keyof typeof headerLabels;
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
                <option value="">添加信息</option>
                {Object.entries(headerLabels)
                  .filter(
                    ([key]) =>
                      !draft.header_presentation.optional_items.some(
                        (i) => i.kind === key,
                      ),
                  )
                  .map(([k, v]) => (
                    <option key={k} value={k}>
                      {v}
                    </option>
                  ))}
              </select>
            </div>
          </FormSection>
          {draft.sections.map((section, si) => (
            <FormSection
              key={section.kind}
              title={kindLabels[section.kind]}
              action={
                <div className="flex gap-1">
                  <Button
                    variant="ghost"
                    disabled={disabled || si === 0}
                    onClick={() => move(section.kind, undefined, -1)}
                  >
                    上移
                  </Button>
                  <Button
                    variant="ghost"
                    disabled={disabled || si === draft.sections.length - 1}
                    onClick={() => move(section.kind, undefined, 1)}
                  >
                    下移
                  </Button>
                  <Button
                    variant="outline"
                    disabled={disabled}
                    onClick={() => setPicker(section.kind)}
                  >
                    添加经历
                  </Button>
                </div>
              }
            >
              <div className="space-y-5">
                {section.members.map((member, mi) => {
                  const source =
                    sources.data?.evidence[member.evidence_item_version_id];
                  return (
                    <article
                      key={member.evidence_item_id}
                      className="space-y-3 rounded-md border border-border p-3"
                    >
                      <h3 className="text-sm font-semibold">
                        {source ? evidenceName(source.fields) : '正在读取资料…'}
                      </h3>
                      {source && (
                        <p className="text-xs text-text-muted">
                          {Object.entries(source.fields)
                            .filter(
                              ([key, v]) =>
                                v &&
                                [
                                  'role_title',
                                  'major',
                                  'start_month',
                                  'end_month',
                                ].includes(key),
                            )
                            .map(([, v]) => v)
                            .join(' · ')}
                        </p>
                      )}
                      <div className="flex flex-wrap gap-1">
                        <Button
                          variant="ghost"
                          disabled={disabled || inspecting}
                          onClick={() =>
                            void inspectSource(member.evidence_item_id)
                          }
                        >
                          查看资料更新
                        </Button>
                        <Button
                          variant="ghost"
                          disabled={disabled || mi === 0}
                          onClick={() =>
                            move(section.kind, member.evidence_item_id, -1)
                          }
                        >
                          上移
                        </Button>
                        <Button
                          variant="ghost"
                          disabled={
                            disabled || mi === section.members.length - 1
                          }
                          onClick={() =>
                            move(section.kind, member.evidence_item_id, 1)
                          }
                        >
                          下移
                        </Button>
                        <Button
                          variant="ghost"
                          disabled={disabled}
                          onClick={() => remove(member.evidence_item_id)}
                        >
                          从简历中移除
                        </Button>
                      </div>
                      <BlockEditor
                        rich
                        label={kindLabels[section.kind] + '简历内容'}
                        disabled={disabled}
                        value={member.content}
                        onChange={(v) =>
                          updateContent(
                            member.evidence_item_id,
                            v as LocalContent,
                          )
                        }
                      />
                      {errorAt(allErrors, `sections[${si}].members[${mi}]`) && (
                        <p role="alert" className="text-sm text-destructive">
                          {errorAt(allErrors, `sections[${si}].members[${mi}]`)}
                        </p>
                      )}
                    </article>
                  );
                })}
              </div>
            </FormSection>
          ))}
          <FormSection title="添加经历分类">
            <div className="flex flex-wrap gap-2">
              {kinds
                .filter((k) => !draft.sections.some((s) => s.kind === k))
                .map((k) => (
                  <Button
                    key={k}
                    variant="outline"
                    disabled={disabled}
                    onClick={() => setPicker(k)}
                  >
                    添加{kindLabels[k]}
                  </Button>
                ))}
            </div>
          </FormSection>

          {Object.keys(allErrors).length > 0 && (
            <div role="alert" className="my-3 text-sm text-destructive">
              请检查标记的内容。
              {Object.entries(allErrors)
                .filter(
                  ([k]) =>
                    !k.startsWith('sections[') &&
                    !k.startsWith('document_presentation') &&
                    !k.startsWith('header_presentation.optional_items[') &&
                    k !== 'resume_name',
                )
                .map(([k, v]) => (
                  <p key={k}>{v}</p>
                ))}
            </div>
          )}
        </div>
        <div className="min-w-0 xl:sticky xl:top-4 xl:self-start">
          <section aria-label="排版设置" className="mb-4">
            <div className="grid grid-cols-[minmax(90px,1.3fr)_minmax(64px,1fr)_minmax(64px,1fr)_minmax(48px,0.7fr)] items-end gap-2">
              <FormControl
                label="字体"
                value={draft.document_presentation.font_family}
                options={fonts}
                disabled={disabled}
                onChange={(v) =>
                  setDraft({
                    ...draft,
                    document_presentation: {
                      ...draft.document_presentation,
                      font_family: v as keyof typeof fonts,
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
                    onChange={(e) =>
                      setDraft({
                        ...draft,
                        document_presentation: {
                          ...draft.document_presentation,
                          [key]:
                            e.target.value === ''
                              ? NaN
                              : Number(e.target.value),
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
                  onChange={(e) =>
                    setDraft({
                      ...draft,
                      document_presentation: {
                        ...draft.document_presentation,
                        theme_color: e.target.value.toUpperCase(),
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
          <DraftPreview
            draft={draft}
            profile={sources.data?.profile}
            evidence={sources.data?.evidence ?? {}}
            error={
              sources.isError ? '无法读取确切来源，预览暂不可用。' : undefined
            }
          />
          {sources.isError && (
            <Button variant="outline" onClick={() => void sources.refetch()}>
              重试读取来源
            </Button>
          )}
        </div>
      </div>
      <DirtyGuard
        allowLeave={allowLeave}
        dirty={
          dirty ||
          (!!createKind && embeddedState.dirty) ||
          (!!profileChange && profileState.dirty)
        }
        busy={
          command.busy ||
          (!!createKind && embeddedState.busy) ||
          (!!profileChange && profileState.busy)
        }
        unknown={
          command.unknown ||
          (!!createKind && embeddedState.unknown) ||
          (!!profileChange && profileState.unknown)
        }
        onSave={createKind || profileChange ? undefined : save}
      />
      {picker && (
        <SourcePicker
          kind={picker}
          selected={refs.map((r) => r.id)}
          onClose={() => setPicker(undefined)}
          onAdd={include}
          onCreate={() => {
            setCreateKind(picker);
            setPicker(undefined);
          }}
        />
      )}
      {createKind && (
        <Dialog
          wide
          title={`新建${kindLabels[createKind]}`}
          description="先保存到求职资料库，再添加到简历。之后取消简历编辑不会撤销这次资料保存。"
          onClose={() =>
            setNotice('请使用资料表单内的取消按钮，以保护未保存输入。')
          }
        >
          <EvidenceEditor
            embedded
            onState={setEmbeddedState}
            kind={createKind}
            onClose={() => setCreateKind(undefined)}
            onSaved={(value) => {
              if (value.evidence_item.status !== 'ACTIVE') {
                setNotice('创建已确认，但资料随后已被移除，不能新增引用。');
                return;
              }
              include([value]);
              setCreateKind(undefined);
              setNotice('资料已保存到知识库并加入简历草稿；简历尚未保存。');
            }}
          />
        </Dialog>
      )}
      {sourceChange && (
        <Dialog
          wide
          title="重新确认资料来源"
          description="采用最新来源默认保留当前简历中的文字、格式和链接，不会自动验证语义一致性。"
          onClose={() => setSourceChange(undefined)}
        >
          <div className="mt-4 space-y-4">
            <h3 className="font-medium">
              {evidenceName(sourceChange.current.evidence_item_version.fields)}
            </h3>
            <div className="grid gap-4 sm:grid-cols-2">
              {[
                {
                  label: '当前绑定',
                  version:
                    sources.data?.evidence[
                      refs.find((r) => r.id === sourceChange.itemId)?.version ??
                        ''
                    ],
                },
                {
                  label: '最新读取',
                  version: sourceChange.current.evidence_item_version,
                },
              ].map(({ label, version }) => (
                <div
                  key={label}
                  className="rounded border border-border p-3 text-sm"
                >
                  <h4 className="mb-2 font-medium">{label}</h4>
                  {version &&
                    Object.entries(version.fields).map(([k, v]) => (
                      <p key={k}>
                        {fieldLabels[k]}：{v ?? '未填写'}
                      </p>
                    ))}
                  {version?.content.map((b, i) => (
                    <p key={i}>
                      {b.type === 'PARAGRAPH' ? b.text : b.items.join(' · ')}
                    </p>
                  ))}
                </div>
              ))}
            </div>
            {sourceChange.current.evidence_item.status === 'RETIRED' ? (
              <p role="alert">
                该资料已被移除，不能新增或切换为此来源。已发布的原有绑定可以保留。
              </p>
            ) : (
              <label className="flex items-start gap-2 text-sm">
                <input
                  type="checkbox"
                  checked={resetExpression}
                  onChange={(e) => setResetExpression(e.target.checked)}
                />
                使用最新资料内容替换当前简历文字和格式（默认保留）
              </label>
            )}
            <div className="flex flex-wrap justify-end gap-2">
              {previousBinding && (
                <Button
                  variant="outline"
                  onClick={() => {
                    setDraft((d) => ({
                      ...d,
                      sections: d.sections.map((s) => ({
                        ...s,
                        members: s.members.map((m) =>
                          m.evidence_item_id === sourceChange.itemId
                            ? {
                                ...m,
                                evidence_item_version_id:
                                  previousBinding.evidence_item_version_id,
                              }
                            : m,
                        ),
                      })),
                    }));
                    setSourceChange(undefined);
                    command.reset();
                  }}
                >
                  继续使用原先绑定
                </Button>
              )}
              <Button
                variant="outline"
                onClick={() => {
                  remove(sourceChange.itemId);
                  setSourceChange(undefined);
                  command.reset();
                }}
              >
                从简历中移除
              </Button>
              <Button
                disabled={
                  sourceChange.current.evidence_item.status !== 'ACTIVE'
                }
                onClick={() => {
                  const v = sourceChange.current.evidence_item_version;
                  setDraft((d) => ({
                    ...d,
                    sections: d.sections.map((s) => ({
                      ...s,
                      members: s.members.map((m) =>
                        m.evidence_item_id === sourceChange.itemId
                          ? {
                              ...m,
                              evidence_item_version_id:
                                v.evidence_item_version_id,
                              content: resetExpression
                                ? initializeContent(v.content)
                                : m.content,
                            }
                          : m,
                      ),
                    })),
                  }));
                  setSourceChange(undefined);
                  command.reset();
                }}
              >
                采用最新资料
              </Button>
            </div>
          </div>
        </Dialog>
      )}
      {profileChange && (
        <Dialog
          title="编辑个人信息"
          description="保存会更新求职资料库中的个人信息。保存后可应用到当前简历草稿；其他简历不会自动更新，当前简历仍需单独保存。"
          busy={profileState.busy}
          onClose={() => profileClose.current?.close()}
        >
          <div className="mt-5 space-y-4">
            <ProfileEditor
              embedded
              initial={profileChange}
              closeRef={profileClose}
              onState={setProfileState}
              onClose={() => setProfileChange(undefined)}
              onSaved={setProfileChange}
            />
            <div className="border-t border-border pt-4 flex justify-end">
              <Button
                disabled={
                  profileState.dirty ||
                  profileState.busy ||
                  profileState.unknown
                }
                onClick={() => {
                  setDraft((d) => ({
                    ...d,
                    profile_version_id:
                      profileChange.profile_version.profile_version_id,
                  }));
                  setProfileChange(undefined);
                  if (command.error?.code === 'SOURCE_CONFLICT')
                    command.reset();
                  setNotice(
                    '已将保存的个人信息应用到当前简历草稿，请保存简历。',
                  );
                }}
              >
                应用到当前简历
              </Button>
            </div>
          </div>
        </Dialog>
      )}
      {discard && (
        <AlertDialog
          title="离开简历编辑？"
          description={
            command.unknown
              ? '保存结果仍未知，离开会丢失核验信息，不会撤销可能生效的保存。'
              : '未保存的简历修改将丢失。已保存到知识库的新资料会保留。'
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
