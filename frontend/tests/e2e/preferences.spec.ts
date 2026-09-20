import {
  test,
  expect,
  type APIRequestContext,
  type Page,
} from '@playwright/test';
import { configuration } from '../fixtures/preferences';
const endpoint = 'http://127.0.0.1:18765/api/v1/preferences';
const route = '/job-pool/preferences';
async function current(request: APIRequestContext) {
  const r = await request.get(endpoint);
  expect(r.status()).toBe(200);
  return r.json();
}
async function seed(request: APIRequestContext, keyword = '工程师') {
  const old = await current(request);
  const r = await request.post(`${endpoint}/save`, {
    data: {
      request_id: crypto.randomUUID(),
      revision:
        old.status === 'CONFIGURED' ? old.preference_set.revision : null,
      configuration: { ...configuration, target_job_keywords: [keyword] },
    },
  });
  expect(r.status()).toBe(200);
  return current(request);
}
async function salary(page: Page, value: string) {
  await page
    .getByRole('textbox', { name: '最低月薪', exact: true })
    .fill(value);
}
test('first configuration saves all six choices, reloads and admits canonical no-op', async ({
  page,
  request,
}) => {
  expect((await current(request)).status).toBe('NOT_CONFIGURED');
  await page.goto(route);
  await expect(page.getByText('尚未配置搜索偏好')).toBeVisible();
  await page
    .getByRole('textbox', { name: '目标岗位关键词', exact: true })
    .fill('AI Agent,后端');
  await page
    .getByRole('button', { name: '添加目标岗位关键词', exact: true })
    .click();
  for (const name of [
    '接受城市',
    '最低月薪',
    '招聘类型',
    '排除公司',
    '最高学历要求',
  ])
    await page
      .getByRole('checkbox', { name: `${name}不限`, exact: true })
      .check();
  await page.getByRole('button', { name: '保存偏好', exact: true }).click();
  await expect(
    page.getByText('搜索偏好已保存。', { exact: true }),
  ).toBeVisible();
  const initial = await current(request);
  expect(initial.preference_set.revision).toBe(1);
  expect(
    initial.current_preference_set_version.configuration.target_job_keywords,
  ).toEqual(['AI Agent,后端']);
  expect(
    initial.current_preference_set_version.configuration.minimum_salary,
  ).toEqual({ mode: 'UNLIMITED' });
  const exact = await request.get(
    `${endpoint}/versions/${initial.preference_set.current_preference_set_version_id}`,
  );
  expect(exact.status()).toBe(200);
  expect(await exact.json()).toEqual(initial.current_preference_set_version);
  await page.reload();
  await expect(page.getByText('AI Agent,后端', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByText('保存已确认，配置内容没有变化。')).toBeVisible();
  expect(await current(request)).toEqual(initial);
});
test('invalid controls and unadded text cannot silently save or disappear', async ({
  page,
  request,
}) => {
  await seed(request);
  await page.goto(route);
  await salary(page, '1.5e4');
  await page
    .getByRole('textbox', { name: '目标岗位关键词', exact: true })
    .fill('还没添加');
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByText('请输入 1–300000 之间的整数')).toBeVisible();
  await expect(page.getByText(/输入框中还有未添加/)).toBeVisible();
  await expect(
    page.getByRole('textbox', { name: '目标岗位关键词', exact: true }),
  ).toHaveValue('还没添加');
  expect(
    (await current(request)).current_preference_set_version.configuration
      .minimum_salary.value,
  ).toBe(15000);
});
test('concurrent Save preserves draft until explicit inspection and rebase', async ({
  page,
  request,
}) => {
  await seed(request);
  await page.goto(route);
  await salary(page, '20000');
  const newer = await seed(request, '另一个页面的配置');
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByText('搜索偏好已在其他页面发生修改')).toBeVisible();
  await page.getByRole('button', { name: '查看最新配置' }).click();
  await expect(
    page.getByText('另一个页面的配置', { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole('textbox', { name: '最低月薪', exact: true }),
  ).toHaveValue('20000');
  expect((await current(request)).preference_set.revision).toBe(
    newer.preference_set.revision,
  );
  await page.getByRole('button', { name: '基于最新配置继续编辑' }).click();
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(
    page.getByText('搜索偏好已保存。', { exact: true }),
  ).toBeVisible();
  const result = await current(request);
  expect(result.preference_set.revision).toBe(
    newer.preference_set.revision + 1,
  );
  expect(
    result.current_preference_set_version.configuration.minimum_salary.value,
  ).toBe(20000);
});
test('lost Save response retries identical request and does not restore historical current', async ({
  page,
  request,
}) => {
  await seed(request);
  const bodies: unknown[] = [];
  await page.route('**/preferences/save', async (r) => {
    bodies.push(r.request().postDataJSON());
    if (bodies.length === 1) {
      await r.fetch();
      await r.abort();
    } else await r.continue();
  });
  await page.goto(route);
  await salary(page, '25000');
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByText('暂时无法确认保存结果')).toBeVisible();
  expect(
    (await current(request)).current_preference_set_version.configuration
      .minimum_salary.value,
  ).toBe(25000);
  const newer = await seed(request, '后续已经保存的配置');
  await page.getByRole('button', { name: '查看当前配置' }).click();
  await expect(
    page.getByText('后续已经保存的配置', { exact: true }),
  ).toBeVisible();
  expect(bodies).toHaveLength(1);
  await expect(
    page.getByRole('button', { name: '保存修改', exact: true }),
  ).toBeDisabled();
  await page.getByRole('button', { name: '验证保存结果' }).click();
  await expect(
    page.getByText(/本次保存已确认；当前配置已发生后续变化/),
  ).toBeVisible();
  expect(bodies).toHaveLength(2);
  expect(bodies[0]).toEqual(bodies[1]);
  expect(await current(request)).toEqual(newer);
  await expect(
    page.getByRole('textbox', { name: '最低月薪', exact: true }),
  ).toHaveValue('15000');
});
test('confirmed Save remains successful when the follow-up read is unavailable', async ({
  page,
  request,
}) => {
  await seed(request);
  let committed = false;
  let failures = 0;
  let writes = 0;
  await page.route('**/preferences/save', async (r) => {
    writes++;
    const response = await r.fetch();
    committed = true;
    await r.fulfill({ response });
  });
  await page.route('**/api/v1/preferences', async (r) => {
    if (committed && failures++ === 0) await r.abort();
    else await r.continue();
  });
  await page.goto(route);
  await salary(page, '18000');
  await page.getByRole('button', { name: '保存修改', exact: true }).click();
  await expect(page.getByText(/本次保存已确认，但暂时无法读取/)).toBeVisible();
  await expect(page.getByText('暂时无法确认保存结果')).toHaveCount(0);
  await page.getByRole('button', { name: '重新读取当前配置' }).click();
  await expect(
    page.getByText('搜索偏好已保存。', { exact: true }),
  ).toBeVisible();
  expect(writes).toBe(1);
});
test('dirty navigation stays until explicit discard and does not change saved preferences', async ({
  page,
  request,
}) => {
  const before = await seed(request);
  await page.goto(route);
  await salary(page, '18000');
  await page
    .getByRole('navigation', { name: '岗位池视图' })
    .getByRole('link', { name: '手动申请' })
    .click();
  await expect(page.getByRole('alertdialog')).toBeVisible();
  await page.getByRole('button', { name: '继续编辑' }).click();
  await expect(
    page.getByRole('textbox', { name: '最低月薪', exact: true }),
  ).toHaveValue('18000');
  await page
    .getByRole('navigation', { name: '岗位池视图' })
    .getByRole('link', { name: '手动申请' })
    .click();
  await page.getByRole('button', { name: '放弃并继续' }).click();
  await expect(page).toHaveURL(/manual-application-entries$/);
  expect(await current(request)).toEqual(before);
});
