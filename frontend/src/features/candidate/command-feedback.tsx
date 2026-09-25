import type { ReactNode } from 'react';
import { Button } from '@/shared/ui/button';
import { InlineNotice } from '@/shared/ui/inline-notice';
import { failureMessage, fieldErrorMessage } from '@/shared/api/result';
import type { CommandState } from './use-command';
export function CommandFeedback({
  command,
  inspect,
  children,
}: {
  command: CommandState;
  inspect?: () => void;
  children?: ReactNode;
}) {
  return (
    <div className="space-y-3">
      {command.message && <InlineNotice title={command.message} />}
      {command.unknown ? (
        <InlineNotice title="暂时无法确认操作结果">
          <p>
            输入和原请求仍保留。读取当前内容不能确认之前的操作结果；验证会使用原请求重试。
          </p>
          {command.error?.kind !== 'unknown' && (
            <p>
              {command.error && failureMessage(command.error)}
              这不能证明先前操作未生效。
            </p>
          )}
          <div className="flex gap-2">
            <Button
              disabled={command.busy}
              onClick={() => void command.execute()}
            >
              {command.busy ? '检查中…' : '验证操作结果'}
            </Button>
            {inspect && (
              <Button
                variant="outline"
                disabled={command.busy}
                onClick={inspect}
              >
                查看当前状态
              </Button>
            )}
          </div>
        </InlineNotice>
      ) : (
        command.error && (
          <InlineNotice title={failureMessage(command.error)}>
            {command.error.fields.length > 0 && (
              <ul>
                {command.error.fields.map((f, i) => (
                  <li key={i}>{fieldErrorMessage(f)}</li>
                ))}
              </ul>
            )}
            {children}
          </InlineNotice>
        )
      )}
      {command.confirmed && (
        <Button
          variant="outline"
          disabled={command.busy}
          onClick={() => void command.refresh()}
        >
          重新读取当前状态
        </Button>
      )}
    </div>
  );
}
