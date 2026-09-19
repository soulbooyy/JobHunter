import { fileURLToPath, URL } from 'node:url';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';

// Keep ports fixed: the backend admits this exact browser origin.
export default defineConfig(({ mode }) => ({
  plugins: [react(), tailwindcss()],
  resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } },
  server: {
    host: '127.0.0.1',
    port: 5173,
    strictPort: true,
    proxy: {
      '/api': {
        target:
          mode === 'e2e'
            ? 'http://127.0.0.1:18765'
            : process.env.JOBHUNTER_API_TARGET || 'http://127.0.0.1:8765',
        changeOrigin: true,
      },
    },
  },
  preview: {
    host: '127.0.0.1',
    port: 4173,
    strictPort: true,
    proxy: {
      '/api': {
        target:
          mode === 'e2e'
            ? 'http://127.0.0.1:18765'
            : process.env.JOBHUNTER_API_TARGET || 'http://127.0.0.1:8765',
        changeOrigin: true,
      },
    },
  },
}));
