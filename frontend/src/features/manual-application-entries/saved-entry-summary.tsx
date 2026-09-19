import type { ManualApplicationEntry } from '@/entities/manual-application-entry/model';
import { entryFields, fieldLabels } from './validation';
export function SavedEntrySummary({
  entry,
}: {
  entry: ManualApplicationEntry;
}) {
  return (
    <section
      aria-label="当前已保存的记录"
      className="rounded-md border border-border bg-surface-muted p-3 text-sm"
    >
      <h3 className="mb-2 font-medium">当前已保存的记录</h3>
      <dl className="space-y-2">
        {entryFields.map((field) => (
          <div key={field}>
            <dt className="text-xs text-text-muted">{fieldLabels[field]}</dt>
            <dd className="mt-1 break-all whitespace-pre-wrap">
              {entry[field]}
            </dd>
          </div>
        ))}
      </dl>
      <p className="mt-3 text-xs text-text-muted">
        这里只显示当前记录，不能还原期间发生的所有修改。
      </p>
    </section>
  );
}
