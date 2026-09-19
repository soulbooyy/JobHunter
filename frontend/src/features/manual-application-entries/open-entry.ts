import type { ManualApplicationEntry } from '@/entities/manual-application-entry/model';
import { entryApi } from './api';
import { ApiFailure, failureMessage } from '@/shared/api/result';
const waitingDocument =
  '<!doctype html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="referrer" content="no-referrer"><title>正在准备申请页面 · JobHunter</title></head><body style="font-family:system-ui,sans-serif;padding:32px;color:#202024"><h1 style="font-size:20px">正在准备申请页面</h1><p>正在核验当前保存的申请链接，请稍候。</p></body></html>';
export async function openEntry(
  entry: ManualApplicationEntry,
): Promise<string> {
  // Synchronous user activation first. Do not use noopener here: some browsers
  // return null even on success. Detach the opener before any external navigation.
  let waiting: Window | null = null;
  let ownedDocument: Document | undefined;
  let waitingUrl: string | undefined;
  try {
    waiting = window.open('about:blank', '_blank');
    if (!waiting || waiting.closed)
      return '无法完成新页面交接，请重新点击后再试。';
    waiting.opener = null;
    if (waiting.opener !== null) throw new Error('Could not detach opener');
    waiting.document.open();
    waiting.document.write(waitingDocument);
    waiting.document.close();
    ownedDocument = waiting.document;
    waitingUrl = waiting.location.href;
    const { application_url } = await entryApi.resolve(
      entry.manual_application_entry_id,
      entry.revision,
    );
    if (waiting.closed) return '新页面已关闭，未发起跳转。请重新点击后再试。';
    // A user-navigated context is no longer ours to replace.
    if (
      waiting.document !== ownedDocument ||
      waiting.location.href !== waitingUrl
    )
      return '新页面已发生变化，未替换其内容。请重新点击后再试。';
    waiting.opener = null;
    const link = waiting.document.createElement('a');
    link.href = application_url;
    link.rel = 'noreferrer noopener';
    link.referrerPolicy = 'no-referrer';
    link.textContent = '打开申请页面';
    waiting.document.body.append(link);
    link.click();
    return '已发起申请页面跳转。';
  } catch (error) {
    try {
      if (
        waiting &&
        !waiting.closed &&
        waiting.document === ownedDocument &&
        waiting.location.href === waitingUrl
      )
        waiting.close();
    } catch {
      /* Do not touch user-navigated contexts. */
    }
    return error instanceof ApiFailure
      ? `未发起跳转。${failureMessage(error)}`
      : '无法完成新页面交接，未确认发起跳转。请重新点击后再试。';
  }
}
