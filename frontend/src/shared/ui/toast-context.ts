import { createContext } from 'react';

export type ToastVariant = 'success' | 'delete' | 'warning';

export type ToastInput = {
  message: string;
  variant: ToastVariant;
  duration?: number;
};

export type ToastApi = {
  show: (toast: ToastInput) => void;
  success: (message: string) => void;
  deleted: (message: string) => void;
  warning: (message: string) => void;
};

export const ToastContext = createContext<ToastApi | undefined>(undefined);
