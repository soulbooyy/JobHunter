import { useContext, type ReactNode } from 'react';
import { createPortal } from 'react-dom';
import { AppHeaderActionsTargetContext } from './app-header-actions-context';

export function AppHeaderActions({ children }: { children: ReactNode }) {
  const target = useContext(AppHeaderActionsTargetContext);
  return target ? createPortal(children, target) : null;
}
