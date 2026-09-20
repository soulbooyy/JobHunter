import { TagInput } from '@/shared/ui/tag-input';
import { Input, inputClass } from '@/shared/ui/input';
import { Button } from '@/shared/ui/button';
import {
  fieldLabels,
  recruitmentLabels,
  educationLabels,
  type PreferenceDraft,
  type PreferenceField,
  type TagField,
  type Recruitment,
  type Education,
} from './model';
export type FieldMessages = Partial<Record<PreferenceField, string[]>>;
const help: Record<PreferenceField, string> = {
  target_job_keywords:
    '用于描述你希望收集的目标岗位。逐项添加，逗号不会拆分为多个关键词。',
  accepted_cities: '限制后续岗位收集的工作城市，不会自动包含相邻城市。',
  minimum_salary: '人民币税前基础月薪，不包含奖金、股票或额外月份薪资。',
  recruitment_types: '选择可以接受的招聘类型。',
  excluded_companies:
    '后续岗位收集时排除这些公司；使用完整名称，不进行模糊匹配。',
  max_required_education: '限制岗位要求的最高学历门槛，不代表你的个人学历。',
};
export function PreferencesFields({
  draft,
  onChange,
  onAdd,
  errors,
  disabled,
}: {
  draft: PreferenceDraft;
  onChange: (draft: PreferenceDraft) => void;
  onAdd: (field: TagField) => void;
  errors: FieldMessages;
  disabled: boolean;
}) {
  function tags(field: TagField) {
    return (
      <TagInput
        id={`pref-${field}`}
        label={fieldLabels[field]}
        values={draft[field]}
        pending={draft.pending[field]}
        disabled={
          disabled ||
          (field !== 'target_job_keywords' && draft.unlimited[field])
        }
        invalid={!!errors[field]?.length}
        describedBy={`pref-${field}-help${errors[field]?.length ? ` pref-${field}-error` : ''}`}
        onPending={(value) =>
          onChange({ ...draft, pending: { ...draft.pending, [field]: value } })
        }
        onAdd={() => onAdd(field)}
        onRemove={(index) =>
          onChange({
            ...draft,
            [field]: draft[field].filter((_, i) => i !== index),
          })
        }
      />
    );
  }
  return (
    <div>
      {(Object.keys(fieldLabels) as PreferenceField[]).map((field) => {
        const inactive =
          disabled ||
          (field !== 'target_job_keywords' && draft.unlimited[field]);
        const description = `pref-${field}-help${errors[field]?.length ? ` pref-${field}-error` : ''}`;
        return (
          <section
            key={field}
            aria-labelledby={`pref-${field}-label`}
            className="border-b border-border-subtle py-6 first:pt-2"
          >
            <div className="mb-3 flex items-start justify-between gap-5">
              <div>
                <label
                  id={`pref-${field}-label`}
                  htmlFor={
                    field === 'recruitment_types' ? undefined : `pref-${field}`
                  }
                  className="text-sm font-semibold"
                >
                  {fieldLabels[field]}
                  {field === 'target_job_keywords' && (
                    <span className="ml-1 text-error" aria-hidden="true">
                      *
                    </span>
                  )}
                </label>
                <p
                  id={`pref-${field}-help`}
                  className="mt-1 text-xs leading-relaxed text-text-muted"
                >
                  {help[field]}
                </p>
              </div>
              {field !== 'target_job_keywords' && (
                <label className="flex shrink-0 cursor-pointer items-center gap-2 text-sm text-text-muted">
                  <input
                    type="checkbox"
                    aria-label={`${fieldLabels[field]}不限`}
                    checked={draft.unlimited[field]}
                    disabled={disabled}
                    onChange={(e) =>
                      onChange({
                        ...draft,
                        unlimited: {
                          ...draft.unlimited,
                          [field]: e.target.checked,
                        },
                      })
                    }
                    className="size-4 accent-primary"
                  />
                  不限
                </label>
              )}
            </div>
            {(field === 'target_job_keywords' ||
              field === 'accepted_cities' ||
              field === 'excluded_companies') &&
              tags(field)}
            {field === 'minimum_salary' && (
              <div className="flex items-center gap-3">
                <Input
                  id={`pref-${field}`}
                  className={`w-48 ${errors[field]?.length ? 'border-error' : ''}`}
                  inputMode="numeric"
                  value={draft.salary}
                  onChange={(e) =>
                    onChange({ ...draft, salary: e.target.value })
                  }
                  disabled={inactive}
                  aria-invalid={!!errors[field]?.length}
                  aria-describedby={description}
                  placeholder="例如：15000"
                />
                <span className="text-xs text-text-muted">元 / 月</span>
              </div>
            )}
            {field === 'recruitment_types' && (
              <div
                role="group"
                tabIndex={-1}
                aria-labelledby={`pref-${field}-label`}
                aria-describedby={description}
                aria-invalid={!!errors[field]?.length}
                id={`pref-${field}`}
                className="flex flex-wrap gap-2"
              >
                {(Object.keys(recruitmentLabels) as Recruitment[]).map(
                  (value) => (
                    <Button
                      key={value}
                      variant={
                        draft.recruitment_types.includes(value)
                          ? 'default'
                          : 'outline'
                      }
                      aria-pressed={draft.recruitment_types.includes(value)}
                      disabled={inactive}
                      onClick={() =>
                        onChange({
                          ...draft,
                          recruitment_types: draft.recruitment_types.includes(
                            value,
                          )
                            ? draft.recruitment_types.filter((v) => v !== value)
                            : [...draft.recruitment_types, value],
                        })
                      }
                    >
                      {recruitmentLabels[value]}
                    </Button>
                  ),
                )}
              </div>
            )}
            {field === 'max_required_education' && (
              <select
                id={`pref-${field}`}
                className={`${inputClass} w-64 max-w-full ${errors[field]?.length ? 'border-error' : ''}`}
                value={draft.education}
                onChange={(e) =>
                  onChange({
                    ...draft,
                    education: e.target.value as Education | '',
                  })
                }
                disabled={inactive}
                aria-invalid={!!errors[field]?.length}
                aria-describedby={description}
              >
                <option value="">请选择学历要求</option>
                {(Object.keys(educationLabels) as Education[]).map((value) => (
                  <option key={value} value={value}>
                    {educationLabels[value]}
                  </option>
                ))}
              </select>
            )}
            {!!errors[field]?.length && (
              <div
                id={`pref-${field}-error`}
                className="mt-2 space-y-1 text-xs text-error"
              >
                {errors[field]?.map((error, index) => (
                  <p key={index}>{error}</p>
                ))}
              </div>
            )}
          </section>
        );
      })}
    </div>
  );
}
