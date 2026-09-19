import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { QueryClientProvider } from '@tanstack/react-query';
import { describe, it, expect, vi } from 'vitest';
import { EntryList } from '@/features/manual-application-entries/entry-list';
import { createQueryClient } from '@/app/providers/query-client';

// Inject fetch at the transport seam while retaining the generated-path client.
vi.mock('@/shared/api/client', async () => {
  const { default: createClient } = await import('openapi-fetch');
  return {
    api: createClient({
      baseUrl: window.location.origin,
      fetch: (request) => fetch(request),
    }),
  };
});

function mount() {
  const client = createQueryClient();
  render(
    <QueryClientProvider client={client}>
      <EntryList />
    </QueryClientProvider>,
  );
  return client;
}
function reply(value: unknown, status = 200) {
  return new Response(JSON.stringify(value), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
describe('manual application list boundary', () => {
  it('does not show empty while a read is pending', () => {
    vi.stubGlobal(
      'fetch',
      vi.fn(() => new Promise(() => {})),
    );
    mount();
    expect(screen.getByRole('status')).toHaveTextContent('正在加载');
    expect(screen.queryByText('还没有手动申请')).not.toBeInTheDocument();
  });
  it('shows empty only after a successful empty list response', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(reply({ items: [] })));
    mount();
    expect(await screen.findByText('还没有手动申请')).toBeInTheDocument();
  });
  it.each([
    reply({}, 503),
    reply({}),
    reply({ items: null }),
    reply({ items: [] }, 201),
  ])(
    'keeps failed or malformed reads distinct from empty',
    async (response) => {
      const fetchMock = vi.fn().mockResolvedValue(response);
      vi.stubGlobal('fetch', fetchMock);
      mount();
      expect(await screen.findByRole('alert')).toHaveTextContent('无法加载');
      expect(screen.queryByText('还没有手动申请')).not.toBeInTheDocument();
      expect(fetchMock).toHaveBeenCalledTimes(1);
    },
  );
  it('retries only after the user clicks retry', async () => {
    const fetchMock = vi
      .fn()
      .mockRejectedValueOnce(new TypeError('network'))
      .mockResolvedValueOnce(reply({ items: [] }));
    vi.stubGlobal('fetch', fetchMock);
    mount();
    await screen.findByRole('alert');
    expect(fetchMock).toHaveBeenCalledTimes(1);
    await userEvent.click(screen.getByRole('button', { name: '重试' }));
    expect(await screen.findByText('还没有手动申请')).toBeInTheDocument();
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });
  it('preserves server order and URL spelling without adding direct navigation', async () => {
    const items = ['第二家公司', '第一家公司'].map((company_name, index) => ({
      manual_application_entry_id: `8f395bc2-5dc4-4b9a-8d31-a9e9056072f${index}`,
      company_name,
      role_title: '前端工程师',
      application_url: 'HTTP://Example.test:80/./apply',
      revision: 1,
      created_at: '2026-09-19T10:00:00.000Z',
      updated_at: '2026-09-19T10:00:00.000Z',
    }));
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(reply({ items })));
    mount();
    await waitFor(() => expect(screen.getAllByRole('row')).toHaveLength(3));
    expect(screen.getAllByRole('row')[1]).toHaveTextContent('第二家公司');
    expect(screen.getAllByText('HTTP://Example.test:80/./apply')).toHaveLength(
      2,
    );
    expect(screen.queryByRole('link')).not.toBeInTheDocument();
  });
});
