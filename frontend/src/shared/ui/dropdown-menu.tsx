import * as Menu from '@radix-ui/react-dropdown-menu';
import type { ReactNode } from 'react';
import { cn } from '@/shared/lib/cn';
export function DropdownMenu({
  trigger,
  children,
}: {
  trigger: ReactNode;
  children: ReactNode;
}) {
  return (
    <Menu.Root>
      <Menu.Trigger asChild>{trigger}</Menu.Trigger>
      <Menu.Portal>
        <Menu.Content
          align="end"
          sideOffset={4}
          className="z-30 min-w-40 rounded-md border border-border bg-surface p-1 shadow-md"
        >
          {children}
        </Menu.Content>
      </Menu.Portal>
    </Menu.Root>
  );
}
export function MenuItem({
  children,
  onSelect,
  destructive = false,
}: {
  children: ReactNode;
  onSelect: () => void;
  destructive?: boolean;
}) {
  return (
    <Menu.Item
      onSelect={onSelect}
      className={cn(
        'flex cursor-pointer items-center gap-2 rounded px-2 py-2 text-sm outline-none data-[highlighted]:bg-hover',
        destructive && 'text-destructive',
      )}
    >
      {children}
    </Menu.Item>
  );
}
export function MenuSeparator() {
  return <Menu.Separator className="my-1 h-px bg-border-subtle" />;
}
