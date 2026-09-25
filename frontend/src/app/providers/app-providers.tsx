import { useState, type ReactNode } from 'react';
import { QueryClientProvider } from '@tanstack/react-query';
import { ToastProvider } from '@/shared/ui/toast';
import { createQueryClient } from './query-client';
export function AppProviders({ children }: { children: ReactNode }) {
  const [client] = useState(createQueryClient);
  return (
    <ToastProvider>
      <QueryClientProvider client={client}>{children}</QueryClientProvider>
    </ToastProvider>
  );
}
