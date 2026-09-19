import {
  test,
  expect,
  type Page,
  type APIRequestContext,
} from '@playwright/test';
const base = 'http://127.0.0.1:18765/api/v1/manual-application-entries';
const route = '/job-pool/manual-application-entries';
const sample = {
  company_name: '浏览器验证公司',
  role_title: '前端工程师',
  application_url: 'http://127.0.0.1:18865/destination',
};
async function list(request: APIRequestContext) {
  const r = await request.get(base);
  expect(r.status()).toBe(200);
  return (await r.json()).items as Array<
    typeof sample & { manual_application_entry_id: string; revision: number }
  >;
}
async function seed(request: APIRequestContext) {
  const r = await request.post(base, {
    data: { ...sample, request_id: crypto.randomUUID() },
  });
  expect(r.status()).toBe(200);
  return (await list(request))[0]!;
}
async function edit(page: Page) {
  await page
    .getByRole('button', { name: `${sample.company_name}的更多操作` })
    .click();
  await page.getByRole('menuitem', { name: '编辑', exact: true }).click();
  await expect(
    page.getByRole('textbox', { name: '公司', exact: true }),
  ).toHaveValue(sample.company_name);
}
async function add(page: Page) {
  await page
    .getByRole('button', { name: '添加申请', exact: true })
    .first()
    .click();
  const form = page.getByRole('dialog');
  await form
    .getByRole('textbox', { name: '公司', exact: true })
    .fill(sample.company_name);
  await form
    .getByRole('textbox', { name: '职位名称', exact: true })
    .fill(sample.role_title);
  await form
    .getByRole('textbox', { name: '申请链接', exact: true })
    .fill(sample.application_url);
  await form.getByRole('button', { name: '添加申请', exact: true }).click();
}
test.beforeEach(async ({ request }) => {
  for (const entry of await list(request)) {
    const r = await request.post(
      `${base}/${entry.manual_application_entry_id}/delete`,
      { data: { revision: entry.revision } },
    );
    expect(r.status()).toBe(200);
  }
});
test('create, read, edit, cancel delete, delete and refresh real entries', async ({
  page,
  request,
}) => {
  await page.goto('/job-pool');
  await page
    .getByRole('main')
    .getByRole('link', { name: '手动申请', exact: true })
    .click();
  await expect(
    page.getByRole('heading', { name: '还没有手动申请' }),
  ).toBeVisible();
  await add(page);
  await expect(page.getByRole('dialog')).toHaveCount(0);
  await expect(
    page.getByRole('cell', { name: sample.company_name, exact: true }),
  ).toBeVisible();
  await edit(page);
  await page
    .getByRole('textbox', { name: '职位名称', exact: true })
    .fill('高级前端工程师');
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  expect((await list(request))[0]?.role_title).toBe('高级前端工程师');
  await page.reload();
  await expect(
    page.getByRole('cell', { name: '高级前端工程师', exact: true }),
  ).toBeVisible();
  await page
    .getByRole('button', { name: `${sample.company_name}的更多操作` })
    .click();
  await page.getByRole('menuitem', { name: '删除', exact: true }).click();
  await page
    .getByRole('alertdialog')
    .getByRole('button', { name: '取消' })
    .click();
  expect(await list(request)).toHaveLength(1);
  await page
    .getByRole('button', { name: `${sample.company_name}的更多操作` })
    .click();
  await page.getByRole('menuitem', { name: '删除', exact: true }).click();
  await page
    .getByRole('alertdialog')
    .getByRole('button', { name: '删除', exact: true })
    .click();
  await expect(
    page.getByRole('heading', { name: '还没有手动申请' }),
  ).toBeVisible();
  expect(await list(request)).toHaveLength(0);
});
test('stale edits preserve draft until explicit inspection, rebase and save', async ({
  page,
  request,
}) => {
  const entry = await seed(request);
  await page.goto(route);
  await edit(page);
  await page
    .getByRole('textbox', { name: '职位名称', exact: true })
    .fill('我的未保存修改');
  expect(
    (
      await request.put(`${base}/${entry.manual_application_entry_id}`, {
        data: {
          ...sample,
          role_title: '另一个页面的修改',
          revision: entry.revision,
        },
      })
    ).status(),
  ).toBe(200);
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(
    page.getByText('这条记录已在其他页面发生修改', { exact: true }),
  ).toBeVisible();
  await page.getByRole('button', { name: '检查当前状态' }).click();
  await expect(
    page.getByText('另一个页面的修改', { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole('textbox', { name: '职位名称', exact: true }),
  ).toHaveValue('我的未保存修改');
  expect((await list(request))[0]?.role_title).toBe('另一个页面的修改');
  await page.getByRole('button', { name: '基于当前记录继续编辑' }).click();
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  expect((await list(request))[0]?.role_title).toBe('我的未保存修改');
});
test('lost create response uses identical explicit retry and produces one record', async ({
  page,
  request,
}) => {
  const bodies: unknown[] = [];
  await page.route(
    '**/api/v1/manual-application-entries',
    async (intercepted) => {
      if (intercepted.request().method() === 'POST') {
        bodies.push(intercepted.request().postDataJSON());
        if (bodies.length === 1) {
          await intercepted.fetch();
          await intercepted.abort();
          return;
        }
      }
      await intercepted.continue();
    },
  );
  await page.goto(route);
  await add(page);
  await expect(page.getByText('暂时无法确认操作结果')).toBeVisible();
  expect(bodies).toHaveLength(1);
  expect(await list(request)).toHaveLength(1);
  await page.getByRole('button', { name: '核验这次添加' }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  expect(bodies).toHaveLength(2);
  expect(bodies[0]).toEqual(bodies[1]);
  expect(await list(request)).toHaveLength(1);
});
test('lost delete response is verified as current absence without command replay', async ({
  page,
  request,
}) => {
  await seed(request);
  let deletes = 0;
  await page.route('**/delete', async (intercepted) => {
    deletes++;
    await intercepted.fetch();
    await intercepted.abort();
  });
  await page.goto(route);
  await page
    .getByRole('button', { name: `${sample.company_name}的更多操作` })
    .click();
  await page.getByRole('menuitem', { name: '删除', exact: true }).click();
  await page
    .getByRole('alertdialog')
    .getByRole('button', { name: '删除', exact: true })
    .click();
  await page.getByRole('button', { name: '检查当前状态' }).click();
  await expect(page.getByText(/当前记录已不存在/)).toBeVisible();
  expect(deletes).toBe(1);
  expect(await list(request)).toHaveLength(0);
  await expect(page.getByText('手动申请已删除', { exact: true })).toHaveCount(
    0,
  );
});
test('explicit navigation detaches opener, sends no referrer and changes no entry', async ({
  page,
  request,
}) => {
  const before = await seed(request);
  await page.goto(route);
  const popupPromise = page.waitForEvent('popup');
  await page
    .getByRole('button', { name: `打开 ${sample.company_name} 的申请页面` })
    .click();
  const popup = await popupPromise;
  await popup.waitForURL('http://127.0.0.1:18865/destination');
  expect(await popup.evaluate(() => window.opener === null)).toBe(true);
  expect(await popup.evaluate(() => document.referrer)).toBe('');
  await expect(popup.locator('#received-referrer')).toHaveText('absent');
  await expect(page.getByText('已发起申请页面跳转。')).toBeVisible();
  expect((await list(request))[0]).toEqual(before);
  await popup.close();
});
test('stale URL resolution closes waiting page without visiting destination', async ({
  page,
  request,
}) => {
  const entry = await seed(request);
  await page.goto(route);
  await expect(
    page.getByRole('cell', { name: sample.company_name, exact: true }),
  ).toBeVisible();
  await request.put(`${base}/${entry.manual_application_entry_id}`, {
    data: { ...sample, role_title: '改变版本', revision: entry.revision },
  });
  const destinations: string[] = [];
  page.context().on('request', (r) => {
    if (r.url().startsWith('http://127.0.0.1:18865'))
      destinations.push(r.url());
  });
  await page
    .getByRole('button', { name: `打开 ${sample.company_name} 的申请页面` })
    .click();
  await expect(
    page.getByText(/未发起跳转。这条记录已在其他页面/),
  ).toBeVisible();
  expect(destinations).toHaveLength(0);
});
test('unavailable browsing context does not call resolve or retry', async ({
  page,
  request,
}) => {
  await seed(request);
  await page.addInitScript(() => {
    window.open = () => null;
  });
  let resolves = 0;
  page.on('request', (r) => {
    if (r.url().endsWith('/resolve-url')) resolves++;
  });
  await page.goto(route);
  await page
    .getByRole('button', { name: `打开 ${sample.company_name} 的申请页面` })
    .click();
  await expect(
    page.getByText('无法完成新页面交接，请重新点击后再试。'),
  ).toBeVisible();
  expect(resolves).toBe(0);
});
test('lost update response requires read inspection and never automatically resubmits', async ({
  page,
  request,
}) => {
  await seed(request);
  let updates = 0;
  await page.route(
    '**/api/v1/manual-application-entries/*',
    async (intercepted) => {
      if (intercepted.request().method() === 'PUT') {
        updates++;
        await intercepted.fetch();
        await intercepted.abort();
      } else await intercepted.continue();
    },
  );
  await page.goto(route);
  await edit(page);
  await page
    .getByRole('textbox', { name: '职位名称', exact: true })
    .fill('已提交但响应丢失');
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByText('暂时无法确认操作结果')).toBeVisible();
  await page.getByRole('button', { name: '检查当前状态' }).click();
  await expect(
    page.getByText('已提交但响应丢失', { exact: true }),
  ).toBeVisible();
  expect(updates).toBe(1);
  expect((await list(request))[0]?.revision).toBe(2);
  await expect(
    page.getByRole('button', { name: '保存修改', exact: true }),
  ).toBeDisabled();
});
test('closing the waiting context does not navigate or create a replacement', async ({
  page,
  request,
}) => {
  await seed(request);
  let release!: () => void;
  const gate = new Promise<void>((resolve) => {
    release = resolve;
  });
  await page.route('**/resolve-url', async (intercepted) => {
    await gate;
    await intercepted.continue();
  });
  const destinations: string[] = [];
  page.context().on('request', (r) => {
    if (r.url().startsWith('http://127.0.0.1:18865'))
      destinations.push(r.url());
  });
  await page.goto(route);
  const popupPromise = page.waitForEvent('popup');
  await page
    .getByRole('button', { name: `打开 ${sample.company_name} 的申请页面` })
    .click();
  const popup = await popupPromise;
  await popup.close();
  release();
  await expect(
    page.getByText('新页面已关闭，未发起跳转。请重新点击后再试。'),
  ).toBeVisible();
  expect(page.context().pages()).toHaveLength(1);
  expect(destinations).toHaveLength(0);
});
