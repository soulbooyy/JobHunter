import { test, expect, type APIRequestContext } from '@playwright/test';
const api = 'http://127.0.0.1:18765/api/v1';
async function get(request: APIRequestContext, path: string) {
  const r = await request.get(api + path);
  expect(r.status()).toBe(200);
  return r.json();
}
async function post(request: APIRequestContext, path: string, body: object) {
  const r = await request.post(api + path, {
    data: { request_id: crypto.randomUUID(), ...body },
  });
  expect(r.status()).toBe(200);
  return r.json();
}
async function evidence(request: APIRequestContext, name = '测试项目') {
  return post(request, '/evidence-items', {
    kind: 'PROJECT',
    fields: {
      project_name: name,
      role_title: null,
      project_url: null,
      start_month: null,
      end_month: null,
    },
    content: [{ type: 'PARAGRAPH', text: '原始事实' }],
  });
}
async function resume(
  request: APIRequestContext,
  name = '测试简历',
  source?: Awaited<ReturnType<typeof evidence>>,
) {
  const p = await get(request, '/profile');
  return post(request, '/resumes', {
    resume_name: name,
    profile_version_id: p.profile_version.profile_version_id,
    header_presentation: { optional_items: [] },
    sections: source
      ? [
          {
            kind: 'PROJECT',
            members: [
              {
                evidence_item_id: source.evidence_item.evidence_item_id,
                evidence_item_version_id:
                  source.evidence_item_version.evidence_item_version_id,
                content: [
                  {
                    type: 'PARAGRAPH',
                    runs: [{ text: '本地简历表达', marks: [] }],
                  },
                ],
              },
            ],
          },
        ]
      : [],
    document_presentation: {
      font_family: 'HEITI',
      font_size_pt: 12,
      line_spacing_pt: 18,
      theme_color: '#1F2937',
    },
  });
}
test('Profile save, Evidence create and local filter use the real backend', async ({
  page,
  request,
}) => {
  await page.goto('/candidate-knowledge/profile');
  await page.getByRole('button', { name: '编辑个人信息', exact: true }).click();
  await page
    .getByRole('textbox', { name: '姓名', exact: true })
    .fill('前端验证用户');
  await page.getByRole('button', { name: '保存个人信息', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  expect((await get(request, '/profile')).profile_version.full_name).toBe(
    '前端验证用户',
  );
  await page.goto('/candidate-knowledge/evidence/new/PROJECT');
  await page.getByRole('textbox', { name: /项目名称/ }).fill('浏览器项目');
  await page
    .getByRole('textbox', { name: '资料内容', exact: true })
    .fill('可复用的事实');
  await page.getByRole('button', { name: '保存项目经历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  await page.goto('/candidate-knowledge');
  await page.getByRole('button', { name: /^项目经历/ }).click();
  await page.getByRole('textbox', { name: '搜索经历资料' }).fill('浏览器项目');
  await page.getByRole('button', { name: /浏览器项目/ }).click();
  await expect(page.getByText('可复用的事实', { exact: true })).toBeVisible();
});
test('new Resume initializes exact source content and local changes never update Evidence', async ({
  page,
  request,
}) => {
  const source = await evidence(request, '可选来源');
  await page.goto('/resumes/new');
  await page.getByRole('textbox', { name: /简历名称/ }).fill('浏览器创建简历');
  await page.getByRole('button', { name: '添加项目经历', exact: true }).click();
  await page.getByRole('checkbox', { name: '可选来源' }).check();
  await page.getByRole('button', { name: '添加到简历 (1)' }).click();
  const text = page.getByRole('textbox', {
    name: '项目经历简历内容',
    exact: true,
  });
  await expect(text).toHaveText('原始事实');
  await text.fill('独立简历文字');
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  const items = await get(request, '/resumes');
  const root = items.resumes.find(
    (r: { resume_name: string }) => r.resume_name === '浏览器创建简历',
  );
  const saved = await get(request, `/resumes/${root.resume_id}`);
  expect(
    saved.resume_version.sections[0].members[0].content[0].runs[0].text,
  ).toBe('独立简历文字');
  expect(
    (
      await get(
        request,
        `/evidence-items/${source.evidence_item.evidence_item_id}`,
      )
    ).evidence_item_version.content[0].text,
  ).toBe('原始事实');
  await page.reload();
});
test('source adoption preserves local expression and old retired references remain usable', async ({
  page,
  request,
}) => {
  const source = await evidence(request, '历史来源');
  const original = await resume(request, '来源采用测试', source);
  await page.goto(`/resumes/${original.resume.resume_id}/edit`);
  await expect(
    page.getByRole('textbox', { name: '项目经历简历内容', exact: true }),
  ).toHaveText('本地简历表达');
  const updated = await post(
    request,
    `/evidence-items/${source.evidence_item.evidence_item_id}/save`,
    {
      revision: source.evidence_item.revision,
      fields: {
        ...source.evidence_item_version.fields,
        project_name: '已更新来源',
      },
      content: [{ type: 'PARAGRAPH', text: '新的事实' }],
    },
  );
  await page.getByRole('button', { name: '查看资料更新', exact: true }).click();
  await page.getByRole('button', { name: '采用最新资料', exact: true }).click();
  await expect(
    page.getByRole('textbox', { name: '项目经历简历内容', exact: true }),
  ).toHaveText('本地简历表达');
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  const saved = await get(request, `/resumes/${original.resume.resume_id}`);
  expect(
    saved.resume_version.sections[0].members[0].evidence_item_version_id,
  ).toBe(updated.evidence_item_version.evidence_item_version_id);
  await post(
    request,
    `/evidence-items/${source.evidence_item.evidence_item_id}/retire`,
    { revision: updated.evidence_item.revision },
  );
  await page
    .getByRole('textbox', { name: '项目经历简历内容', exact: true })
    .fill('保留历史来源的修改');
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(
    page.getByRole('textbox', { name: '项目经历简历内容', exact: true }),
  ).toHaveText('保留历史来源的修改');
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
});
test('lost Profile response retries identical command after another current change', async ({
  page,
  request,
}) => {
  const bodies: unknown[] = [];
  await page.route('**/profile/save', async (route) => {
    bodies.push(route.request().postDataJSON());
    if (bodies.length === 1) {
      await route.fetch();
      await route.abort();
    } else await route.continue();
  });
  await page.goto('/candidate-knowledge/profile');
  await page.getByRole('button', { name: '编辑个人信息', exact: true }).click();
  await page
    .getByRole('textbox', { name: '姓名', exact: true })
    .fill('未知请求姓名');
  await page.getByRole('button', { name: '保存个人信息', exact: true }).click();
  await expect(
    page.getByText('暂时无法确认操作结果', { exact: true }),
  ).toBeVisible();
  const current = await get(request, '/profile');
  await post(request, '/profile/save', {
    revision: current.profile.revision,
    full_name: '后来保存的姓名',
    phone_number: null,
    email: null,
  });
  await page.getByRole('button', { name: '查看当前状态', exact: true }).click();
  await expect(page.getByText(/后来保存的姓名/)).toBeVisible();
  expect(bodies.length).toBe(1);
  await page.getByRole('button', { name: '验证操作结果', exact: true }).click();
  await expect(
    page.getByRole('textbox', { name: '姓名', exact: true }),
  ).toHaveValue('后来保存的姓名');
  expect(bodies[0]).toEqual(bodies[1]);
});
test('Resume conflict retains draft and requires explicit rebase', async ({
  page,
  request,
}) => {
  const source = await evidence(request);
  const r = await resume(request, '冲突测试', source);
  await page.goto(`/resumes/${r.resume.resume_id}/edit`);
  await page
    .getByRole('textbox', { name: '项目经历简历内容', exact: true })
    .fill('保留草稿');
  await post(request, `/resumes/${r.resume.resume_id}/rename`, {
    revision: r.resume.revision,
    resume_name: '其他页面重命名',
  });
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await page.getByRole('button', { name: '查看最新版本', exact: true }).click();
  await expect(
    page.getByRole('textbox', { name: '项目经历简历内容', exact: true }),
  ).toHaveText('保留草稿');
  await page
    .getByRole('button', { name: '基于最新版本继续编辑', exact: true })
    .click();
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
});
test('default Resume removal shows exact replacement and publishes selection atomically', async ({
  page,
  request,
}) => {
  const r = await resume(request, '将移除的默认简历');
  await resume(request, '候选替代简历');
  const list = await get(request, '/resumes');
  await post(request, '/workspace/default-resume/set', {
    revision: list.default_resume_selection.revision,
    default_resume_id: r.resume.resume_id,
  });
  await page.goto('/resumes');
  const row = page.getByRole('article').filter({
    has: page.getByRole('link', { name: '将移除的默认简历', exact: true }),
  });
  await row.getByRole('button', { name: '移除', exact: true }).click();
  await expect(page.getByText(/移除后默认简历将更换为/)).toBeVisible();
  await page
    .getByRole('dialog')
    .getByRole('button', { name: '移除简历', exact: true })
    .click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  expect(
    (await get(request, '/resumes')).default_resume_selection.default_resume_id,
  ).not.toBe(r.resume.resume_id);
});
test('newly created Knowledge survives discarding the Resume draft', async ({
  page,
  request,
}) => {
  await page.goto('/resumes/new');
  await page.getByRole('textbox', { name: /简历名称/ }).fill('不保存的草稿');
  await page.getByRole('button', { name: '添加技能', exact: true }).click();
  await page.getByRole('button', { name: '新建技能', exact: true }).click();
  await page
    .getByRole('textbox', { name: /技能名称/ })
    .fill('独立持久化的技能');
  await page.getByRole('button', { name: '保存技能', exact: true }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  await page.getByRole('button', { name: '取消', exact: true }).click();
  await page.getByRole('button', { name: '放弃并离开', exact: true }).click();
  await expect(page).toHaveURL(/\/resumes$/);
  expect(
    (await get(request, '/evidence-items')).evidence_items.some(
      (i: { fields: { skill_name?: string } }) =>
        i.fields.skill_name === '独立持久化的技能',
    ),
  ).toBe(true);
});

for (const [kind, label, fields] of [
  [
    'WORK_EXPERIENCE',
    '工作经历',
    { 公司名称: '表单验证公司', 职位名称: '前端工程师' },
  ],
  ['EDUCATION', '教育经历', { 学校名称: '表单验证大学' }],
  ['SKILL', '技能', { 技能名称: 'TypeScript' }],
  ['AWARD', '奖项', { 奖项名称: '表单验证奖项' }],
  ['CERTIFICATION', '证书', { 证书名称: '表单验证证书' }],
] as const) {
  test(`${kind} shared form saves exact kind and nullable fields`, async ({
    page,
    request,
  }) => {
    await page.goto(`/candidate-knowledge/evidence/new/${kind}`);
    for (const [field, value] of Object.entries(fields))
      await page.getByRole('textbox', { name: new RegExp(field) }).fill(value);
    if (kind === 'EDUCATION')
      await page
        .getByRole('combobox', { name: /学历/ })
        .selectOption('BACHELOR');
    await page
      .getByRole('button', { name: `保存${label}`, exact: true })
      .click();
    await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
    const list = await get(request, '/evidence-items');
    const item = list.evidence_items.find(
      (i: {
        evidence_item: { kind: string };
        fields: Record<string, unknown>;
      }) =>
        i.evidence_item.kind === kind &&
        Object.values(i.fields).includes(Object.values(fields)[0]),
    );
    expect(item).toBeTruthy();
  });
}

test('rich text marks and optional Header order survive canonical save', async ({
  page,
  request,
}) => {
  const source = await evidence(request, '格式验证来源');
  const r = await resume(request, '格式验证简历', source);
  await page.goto(`/resumes/${r.resume.resume_id}/edit`);
  const text = page.getByRole('textbox', {
    name: '项目经历简历内容',
    exact: true,
  });
  await text.fill('本地简历表达');
  await text.press('ControlOrMeta+A');
  await page.getByRole('button', { name: '加粗', exact: true }).click();
  await page
    .getByRole('combobox', { name: '添加附加信息' })
    .selectOption('EXPECTED_CITY');
  await page
    .getByRole('textbox', { name: '期望城市', exact: true })
    .fill('上海');
  await page
    .getByRole('combobox', { name: '添加附加信息' })
    .selectOption('EXPECTED_POSITION');
  await page
    .getByRole('textbox', { name: '期望职位', exact: true })
    .fill('前端开发');
  await page.getByRole('button', { name: '上移期望职位', exact: true }).click();
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  const current = await get(request, `/resumes/${r.resume.resume_id}`);
  expect(
    current.resume_version.sections[0].members[0].content[0].runs[0].marks,
  ).toEqual([{ type: 'BOLD' }]);
  expect(
    current.resume_version.header_presentation.optional_items.map(
      (i: { kind: string }) => i.kind,
    ),
  ).toEqual(['EXPECTED_POSITION', 'EXPECTED_CITY']);
});

test('a source retired after selection rejects the entire new Resume until explicit removal', async ({
  page,
  request,
}) => {
  const source = await evidence(request, '保存前移除的来源');
  await page.goto('/resumes/new');
  await page.getByRole('textbox', { name: /简历名称/ }).fill('来源冲突验证');
  await page.getByRole('button', { name: '添加项目经历', exact: true }).click();
  await page.getByRole('checkbox', { name: /保存前移除的来源/ }).check();
  await page
    .getByRole('button', { name: '添加到简历 (1)', exact: true })
    .click();
  await expect(
    page.getByRole('textbox', { name: '项目经历简历内容', exact: true }),
  ).toHaveText('原始事实');
  await post(
    request,
    `/evidence-items/${source.evidence_item.evidence_item_id}/retire`,
    { revision: source.evidence_item.revision },
  );
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(
    page.getByText('引用的资料已变化，请重新确认资料来源。', { exact: true }),
  ).toBeVisible();
  expect(
    (await get(request, '/resumes')).resumes.some(
      (r: { resume_name: string }) => r.resume_name === '来源冲突验证',
    ),
  ).toBe(false);
  await expect(
    page.getByRole('textbox', { name: '项目经历简历内容', exact: true }),
  ).toHaveText('原始事实');
  await page.getByRole('button', { name: '从简历中移除', exact: true }).click();
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
});

test('Resume opens by name and edits Profile in a local modal before explicit adoption', async ({
  page,
  request,
}) => {
  const r = await resume(request, '直接点击进入的简历');
  await page.goto('/resumes');
  await expect(
    page.getByRole('link', { name: '编辑', exact: true }),
  ).toHaveCount(0);
  await page
    .getByRole('link', { name: '直接点击进入的简历', exact: true })
    .click();
  await page.getByRole('button', { name: '编辑个人信息', exact: true }).click();
  const dialog = page.getByRole('dialog', {
    name: '编辑个人信息',
    exact: true,
  });
  await expect(dialog).toBeVisible();
  await expect(page).toHaveURL(
    new RegExp(`/resumes/${r.resume.resume_id}/edit$`),
  );
  await dialog
    .getByRole('textbox', { name: '姓名', exact: true })
    .fill('弹窗保存用户');
  await expect(
    dialog.getByRole('button', { name: '应用到当前简历', exact: true }),
  ).toBeDisabled();
  await dialog
    .getByRole('button', { name: '保存个人信息', exact: true })
    .click();
  await expect(dialog.getByText('操作已确认。', { exact: true })).toBeVisible();
  const profile = await get(request, '/profile');
  expect(profile.profile_version.full_name).toBe('弹窗保存用户');
  expect(
    (await get(request, `/resumes/${r.resume.resume_id}`)).resume_version
      .profile_version_id,
  ).toBe(r.resume_version.profile_version_id);
  await dialog
    .getByRole('button', { name: '应用到当前简历', exact: true })
    .click();
  await expect(dialog).toHaveCount(0);
  await expect(
    page
      .getByRole('complementary', { name: '简历本地预览' })
      .getByText('弹窗保存用户'),
  ).toBeVisible();
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  expect(
    (await get(request, `/resumes/${r.resume.resume_id}`)).resume_version
      .profile_version_id,
  ).toBe(profile.profile_version.profile_version_id);
});

test('single visual editor inherits caret marks, toggles whole-line lists and persists them', async ({
  page,
  request,
}) => {
  const source = await evidence(request, '连续输入来源');
  const r = await resume(request, '连续输入验证', source);
  await page.goto(`/resumes/${r.resume.resume_id}/edit`);
  const text = page.getByRole('textbox', {
    name: '项目经历简历内容',
    exact: true,
  });
  await expect(text).toHaveCount(1);
  await text.fill('dddd');
  await page.getByRole('button', { name: '加粗', exact: true }).click();
  await page.getByRole('button', { name: '斜体', exact: true }).click();
  await text.pressSequentially('aaaa');
  await expect(text.locator('strong em, em strong').first()).toHaveText('aaaa');
  for (let i = 0; i < 6; i++) await text.press('ArrowLeft');
  await expect(
    page.getByRole('button', { name: '加粗', exact: true }),
  ).toHaveAttribute('aria-pressed', 'false');
  await text.pressSequentially('x');
  await text.press('Shift+ArrowLeft');
  await page.getByRole('button', { name: '无序列表', exact: true }).click();
  await expect(text.locator('ul > li')).toHaveText('ddxddaaaa');
  await page.getByRole('button', { name: '有序列表', exact: true }).click();
  await expect(text.locator('ol > li')).toHaveText('ddxddaaaa');
  await expect(text.locator('ul')).toHaveCount(0);
  for (let i = 0; i < 10; i++) await text.press('ArrowRight', { delay: 20 });
  await expect(
    page.getByRole('button', { name: '加粗', exact: true }),
  ).toHaveAttribute('aria-pressed', 'true');
  await text.press('Enter');
  await text.pressSequentially('second');
  await expect(text.locator('ol > li')).toHaveCount(2);

  const settings = page.getByRole('region', { name: '排版设置' });
  const rects = await settings
    .locator('select,input')
    .evaluateAll((nodes) => nodes.map((n) => n.getBoundingClientRect().top));
  expect(Math.max(...rects) - Math.min(...rects)).toBeLessThan(5);
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('操作已确认。', { exact: true })).toBeVisible();
  const saved = await get(request, `/resumes/${r.resume.resume_id}`);
  expect(saved.resume_version.sections[0].members[0].content).toEqual([
    {
      type: 'ORDERED_LIST',
      items: [
        {
          runs: [
            { text: 'ddxdd', marks: [] },
            { text: 'aaaa', marks: [{ type: 'BOLD' }, { type: 'ITALIC' }] },
          ],
        },
        {
          runs: [
            { text: 'second', marks: [{ type: 'BOLD' }, { type: 'ITALIC' }] },
          ],
        },
      ],
    },
  ]);
  await page.reload();
  await expect(text.locator('strong em, em strong').first()).toHaveText('aaaa');
});
