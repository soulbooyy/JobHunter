import {
  fieldLabels,
  recruitmentLabels,
  educationLabels,
  type CurrentPreferences,
  type PreferenceField,
} from './model';
export function SavedPreferences({ current }: { current: CurrentPreferences }) {
  if (current.status === 'NOT_CONFIGURED')
    return <p className="text-sm">当前尚未配置搜索偏好。</p>;
  const configuration = current.current_preference_set_version.configuration;
  const value = (field: PreferenceField) => {
    const choice = configuration[field];
    if (Array.isArray(choice)) return choice.join(' · ');
    if (choice.mode === 'UNLIMITED') return '不限';
    if (
      field === 'recruitment_types' &&
      configuration.recruitment_types.mode === 'LIMITED'
    )
      return configuration.recruitment_types.value
        .map((v) => recruitmentLabels[v])
        .join(' · ');
    if (
      field === 'max_required_education' &&
      configuration.max_required_education.mode === 'LIMITED'
    )
      return educationLabels[configuration.max_required_education.value];
    if (field === 'minimum_salary') return `${choice.value} 元 / 月`;
    return Array.isArray(choice.value)
      ? choice.value.join(' · ')
      : String(choice.value);
  };
  return (
    <div className="rounded-md border border-border p-4">
      <h2 className="mb-3 text-sm font-semibold">最新读取的保存配置</h2>
      <dl className="grid gap-3 text-sm xl:grid-cols-2">
        {(Object.keys(fieldLabels) as PreferenceField[]).map((field) => (
          <div
            key={field}
            className="flex min-w-0 justify-between gap-5 border-b border-border-subtle pb-2"
          >
            <dt className="shrink-0 text-text-muted">{fieldLabels[field]}</dt>
            <dd className="break-all text-right">{value(field)}</dd>
          </div>
        ))}
      </dl>
      <p className="mt-3 text-xs text-text-muted">
        这是一次读取时的已保存状态；不能据此判断先前请求的结果，也不保证之后未发生变化。
      </p>
    </div>
  );
}
