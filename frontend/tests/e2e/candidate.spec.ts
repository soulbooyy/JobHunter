import { test, expect, type APIRequestContext } from '@playwright/test';

const api = 'http://127.0.0.1:18765/api/v1';
const presentation = {
  font_family: 'HEITI',
  font_size_pt: 12,
  line_spacing_pt: 18,
  theme_color: '#1F2937',
};

async function get(request: APIRequestContext, path: string) {
  const response = await request.get(api + path);
  expect(response.status()).toBe(200);
  return response.json();
}

async function post(
  request: APIRequestContext,
  path: string,
  body: Record<string, unknown>,
) {
  const response = await request.post(api + path, {
    data: { request_id: crypto.randomUUID(), ...body },
  });
  expect(response.status()).toBe(200);
  return response.json();
}

async function createResume(
  request: APIRequestContext,
  name: string,
  withEntry = true,
) {
  const entryId = crypto.randomUUID();
  const blockId = crypto.randomUUID();
  const result = await post(request, '/resumes', {
    resume_name: name,
    contacts: {
      full_name: `${name}用户`,
      phone_number: null,
      email: null,
    },
    header_presentation: { optional_items: [] },
    sections: withEntry
      ? [
          {
            kind: 'PROJECT',
            members: [
              {
                entry_id: entryId,
                fields: {
                  project_name: `${name}项目`,
                  role_title: null,
                  project_url: null,
                  start_month: null,
                  end_month: null,
                },
                content: [
                  {
                    type: 'PARAGRAPH',
                    block_id: blockId,
                    runs: [{ text: `${name}正文`, marks: [] }],
                  },
                ],
              },
            ],
          },
        ]
      : [],
    document_presentation: presentation,
  });
  return { ...result, entryId, blockId };
}

async function removeAllResumes(request: APIRequestContext) {
  for (;;) {
    const list = await get(request, '/resumes');
    if (!list.resumes.length) return;
    const target = list.resumes[0];
    const isDefault =
      target.resume_id === list.default_resume_selection.default_resume_id;
    await post(request, `/resumes/${target.resume_id}/remove`, {
      revision: target.revision,
      default_resume_selection: {
        revision: list.default_resume_selection.revision,
      },
      replacement_resume_id: isDefault
        ? (list.resumes[1]?.resume_id ?? null)
        : null,
    });
  }
}

test.beforeEach(async ({ request }) => {
  await removeAllResumes(request);
});

test('creates an independent Resume and edits only its owned data', async ({
  page,
  request,
}) => {
  await page.goto('/resumes/new');
  const editor = page.getByRole('region', { name: '简历编辑内容' });
  const nameInput = page.getByRole('textbox', { name: /简历名称/ });
  const headerActions = page.getByLabel('页面操作');
  await expect(
    headerActions.getByRole('button', { name: '取消', exact: true }),
  ).toBeVisible();
  await expect(
    headerActions.getByRole('button', { name: '保存简历', exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole('heading', { name: '新建简历', exact: true }),
  ).toHaveCount(0);
  await expect(page.getByRole('combobox', { name: '字体' })).toHaveValue(
    'SOURCE_HAN_SANS',
  );
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(
    page.getByLabel('通知').getByText('请检查标记的内容。', { exact: true }),
  ).toBeVisible();
  await expect(editor.getByText('请检查标记的内容。')).toHaveCount(0);
  await nameInput.focus();
  const [editorBox, nameBox] = await Promise.all([
    editor.boundingBox(),
    nameInput.boundingBox(),
  ]);
  expect(nameBox!.x).toBeGreaterThanOrEqual(editorBox!.x + 3);
  expect(nameBox!.x + nameBox!.width).toBeLessThanOrEqual(
    editorBox!.x + editorBox!.width - 3,
  );
  expect(
    await editor.evaluate(
      (element) => element.scrollWidth <= element.clientWidth,
    ),
  ).toBe(true);
  await page.getByRole('button', { name: '关闭提示' }).click();
  await nameInput.fill('前端独立简历');
  await page
    .getByRole('textbox', { name: '姓名', exact: true })
    .fill('独立姓名');
  await expect(
    page.getByRole('heading', { name: '基本信息', exact: true }),
  ).toBeVisible();
  const basicCard = page
    .getByRole('heading', { name: '基本信息', exact: true })
    .locator('..')
    .locator('..');
  expect(
    await basicCard.evaluate((element) => ({
      borderStyle: getComputedStyle(element).borderTopStyle,
      backgroundColor: getComputedStyle(element).backgroundColor,
    })),
  ).toEqual({ borderStyle: 'solid', backgroundColor: 'rgb(255, 255, 255)' });
  const basicFields = await basicCard
    .getByRole('textbox')
    .evaluateAll((inputs) =>
      inputs.slice(0, 3).map((input) => {
        const rectangle = input.getBoundingClientRect();
        return { top: rectangle.top, height: rectangle.height };
      }),
    );
  expect(
    Math.max(...basicFields.map((field) => field.top)) -
      Math.min(...basicFields.map((field) => field.top)),
  ).toBeLessThan(5);
  expect(basicFields.every((field) => field.height <= 36)).toBe(true);
  await page
    .getByRole('combobox', { name: '添加信息项', exact: true })
    .selectOption('EXPECTED_CITY');
  await page
    .getByRole('textbox', { name: '期望城市', exact: true })
    .fill('上海');
  await page.getByRole('button', { name: '添加项目经历', exact: true }).click();
  await page.getByRole('textbox', { name: /项目名称/ }).fill('前端项目');
  await page
    .getByRole('textbox', { name: '项目经历简历内容', exact: true })
    .fill('独立正文');

  const modules = page.getByRole('region', { name: '简历模块' });
  const preview = page.getByRole('region', { name: '简历预览内容' });
  await page.getByRole('button', { name: '添加技能', exact: true }).click();
  const skillHeading = editor.getByRole('heading', {
    name: '技能',
    exact: true,
  });
  const skillSection = skillHeading.locator('..').locator('..');
  await skillSection.getByRole('button', { name: '移除', exact: true }).click();
  await expect(skillHeading).toHaveCount(0);
  await expect(
    page.getByRole('button', { name: '添加技能', exact: true }),
  ).toBeVisible();

  const moduleTop = (await modules.boundingBox())!.y;
  expect(moduleTop).toBeLessThan(110);
  const saveBox = await headerActions
    .getByRole('button', { name: '保存简历', exact: true })
    .boundingBox();
  expect(saveBox!.y + saveBox!.height).toBeLessThan(moduleTop);
  const scrollState = await editor.evaluate((element) => {
    element.scrollTop = element.scrollHeight;
    return {
      overflowY: getComputedStyle(element).overflowY,
      hasOverflow: element.scrollHeight > element.clientHeight,
    };
  });
  expect(scrollState).toEqual({ overflowY: 'auto', hasOverflow: true });
  expect((await modules.boundingBox())!.y).toBe(moduleTop);
  expect(
    await preview.evaluate((element) => ({
      overflowY: getComputedStyle(element).overflowY,
      hasOverflow: element.scrollHeight > element.clientHeight,
    })),
  ).toEqual({ overflowY: 'auto', hasOverflow: true });

  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('简历已创建', { exact: true })).toBeVisible();

  const list = await get(request, '/resumes');
  const first = list.resumes.find(
    (resume: { resume_name: string }) => resume.resume_name === '前端独立简历',
  );
  const firstSaved = await get(request, `/resumes/${first.resume_id}`);
  expect(firstSaved.resume_version.contacts.full_name).toBe('独立姓名');
  expect(firstSaved.resume_version.header_presentation.optional_items).toEqual([
    { kind: 'EXPECTED_CITY', value: '上海' },
  ]);
  expect(
    firstSaved.resume_version.sections[0].members[0].entry_id,
  ).toBeTruthy();
  expect(
    firstSaved.resume_version.sections[0].members[0].content[0].block_id,
  ).toBeTruthy();

  const second = await createResume(request, '另一份简历');
  await page.goto(`/resumes/${first.resume_id}/edit`);
  await page
    .getByRole('textbox', { name: '姓名', exact: true })
    .fill('修改后姓名');
  await page
    .getByRole('textbox', { name: '项目经历简历内容', exact: true })
    .fill('修改后正文');
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText('简历修改已保存', { exact: true })).toBeVisible();

  const untouched = await get(request, `/resumes/${second.resume.resume_id}`);
  expect(untouched.resume_version.contacts.full_name).toBe('另一份简历用户');
  expect(
    untouched.resume_version.sections[0].members[0].content[0].runs[0].text,
  ).toBe('另一份简历正文');
});

test('preserves logical IDs through editing, list conversion, split, merge and duplicate', async ({
  page,
  request,
}) => {
  const created = await createResume(request, '稳定标识简历');
  await page.goto(`/resumes/${created.resume.resume_id}/edit`);
  const editor = page.getByRole('textbox', {
    name: '项目经历简历内容',
    exact: true,
  });
  await editor.click();
  await editor.press('ControlOrMeta+A');
  await page.getByRole('button', { name: '无序列表', exact: true }).click();
  await expect(editor.locator('li')).toHaveAttribute(
    'data-block-id',
    created.blockId,
  );
  await editor.locator('li').evaluate((item) => {
    const range = document.createRange();
    range.selectNodeContents(item);
    range.collapse(false);
    const selection = window.getSelection();
    selection?.removeAllRanges();
    selection?.addRange(range);
  });
  await editor.press('Enter');
  await editor.pressSequentially('第二行');
  await expect(editor.locator('li')).toHaveCount(2);
  const secondId = await editor
    .locator('li')
    .nth(1)
    .getAttribute('data-block-id');
  expect(secondId).toBeTruthy();
  expect(secondId).not.toBe(created.blockId);

  await editor
    .locator('li')
    .nth(1)
    .evaluate((item) => {
      const paragraph = item.querySelector('p') ?? item;
      const range = document.createRange();
      range.selectNodeContents(paragraph);
      range.collapse(true);
      const selection = window.getSelection();
      selection?.removeAllRanges();
      selection?.addRange(range);
    });
  await editor.press('Backspace');
  await expect(editor.locator('li')).toHaveCount(1);
  await expect(editor.locator('li')).toHaveAttribute(
    'data-block-id',
    created.blockId,
  );
  await editor.press('ControlOrMeta+z');
  await expect(editor.locator('li')).toHaveCount(2);
  await expect(editor.locator('li').nth(1)).toHaveAttribute(
    'data-block-id',
    secondId!,
  );
  await editor.press('ControlOrMeta+Shift+z');
  await expect(editor.locator('li')).toHaveCount(1);
  await expect(editor.locator('li')).toHaveAttribute(
    'data-block-id',
    created.blockId,
  );
  await editor.press('ControlOrMeta+z');
  await expect(editor.locator('li').nth(1)).toHaveAttribute(
    'data-block-id',
    secondId!,
  );

  const firstSave = page.waitForResponse(
    (response) =>
      response.url().endsWith(`/resumes/${created.resume.resume_id}/save`) &&
      response.request().method() === 'POST',
  );
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await firstSave;
  let saved = await get(request, `/resumes/${created.resume.resume_id}`);
  expect(saved.resume_version.sections[0].members[0].content[0].items).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ block_id: created.blockId }),
      expect.objectContaining({ block_id: secondId }),
    ]),
  );

  await editor.click();
  await editor.press('ControlOrMeta+A');
  await editor.evaluate((element) => {
    const clipboard = new DataTransfer();
    clipboard.setData('text/plain', '粘贴第一行\n粘贴第二行');
    element.dispatchEvent(
      new ClipboardEvent('paste', {
        bubbles: true,
        cancelable: true,
        clipboardData: clipboard,
      }),
    );
  });
  await expect(editor.locator(':scope > p')).toHaveCount(2);
  const pastedIds = await editor
    .locator(':scope > p')
    .evaluateAll((paragraphs) =>
      paragraphs.map((paragraph) => paragraph.getAttribute('data-block-id')),
    );
  expect(new Set(pastedIds).size).toBe(2);
  expect(pastedIds).not.toContain(created.blockId);
  expect(pastedIds).not.toContain(secondId);

  await page.getByRole('button', { name: '复制', exact: true }).click();
  const secondSave = page.waitForResponse(
    (response) =>
      response.url().endsWith(`/resumes/${created.resume.resume_id}/save`) &&
      response.request().method() === 'POST',
  );
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await secondSave;
  saved = await get(request, `/resumes/${created.resume.resume_id}`);
  const [original, duplicate] = saved.resume_version.sections[0].members;
  expect(original.entry_id).toBe(created.entryId);
  expect(duplicate.entry_id).not.toBe(original.entry_id);
  expect(
    original.content.map((block: { block_id: string }) => block.block_id),
  ).toEqual(pastedIds);
  expect(
    duplicate.content.map((block: { block_id: string }) => block.block_id),
  ).not.toEqual(pastedIds);
});

test('default removal preselects next, allows an explicit replacement and removes the final Resume', async ({
  page,
  request,
}) => {
  const first = await createResume(request, '第一份');
  const second = await createResume(request, '第二份');
  const third = await createResume(request, '第三份');
  let list = await get(request, '/resumes');
  await post(request, '/workspace/default-resume/set', {
    revision: list.default_resume_selection.revision,
    default_resume_id: second.resume.resume_id,
  });

  await page.goto('/resumes');
  const row = page.getByRole('article').filter({
    has: page.getByRole('link', { name: '第二份', exact: true }),
  });
  await row.getByRole('button', { name: '移除', exact: true }).click();
  const replacement = page.getByRole('combobox', {
    name: '移除后的默认简历',
  });
  await expect(replacement).toHaveValue(third.resume.resume_id);
  await replacement.selectOption(first.resume.resume_id);
  await page
    .getByRole('dialog')
    .getByRole('button', { name: '移除简历', exact: true })
    .click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  list = await get(request, '/resumes');
  expect(list.default_resume_selection.default_resume_id).toBe(
    first.resume.resume_id,
  );

  await removeAllResumes(request);
  const final = await createResume(request, '最后一份');
  await page.reload();
  const finalRow = page.getByRole('article').filter({
    has: page.getByRole('link', { name: '最后一份', exact: true }),
  });
  await finalRow.getByRole('button', { name: '移除', exact: true }).click();
  await expect(page.getByText(/这是最后一份简历/)).toBeVisible();
  await page
    .getByRole('dialog')
    .getByRole('button', { name: '移除简历', exact: true })
    .click();
  await expect(page.getByText('还没有简历', { exact: true })).toBeVisible();
  expect(final.resume.resume_id).toBeTruthy();
  expect((await get(request, '/workspace/portrait')).state.status).toBe(
    'NO_SOURCE',
  );
});

test('save conflict and uncertain response preserve the Resume draft', async ({
  page,
  request,
}) => {
  const created = await createResume(request, '冲突恢复简历');
  await page.goto(`/resumes/${created.resume.resume_id}/edit`);
  const editor = page.getByRole('textbox', {
    name: '项目经历简历内容',
    exact: true,
  });
  await editor.fill('必须保留的冲突草稿');
  await post(request, `/resumes/${created.resume.resume_id}/rename`, {
    revision: created.resume.revision,
    resume_name: '其他页面重命名',
  });
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(page.getByText(/已在其他页面发生修改/)).toBeVisible();
  await expect(editor).toHaveText('必须保留的冲突草稿');
  await page.getByRole('button', { name: '查看最新版本', exact: true }).click();
  await page
    .getByRole('button', { name: '保留草稿并基于最新版本保存', exact: true })
    .click();

  const bodies: unknown[] = [];
  await page.route(
    `**/resumes/${created.resume.resume_id}/save`,
    async (route) => {
      bodies.push(route.request().postDataJSON());
      if (bodies.length === 1) {
        await route.fetch();
        await route.abort();
      } else {
        await route.continue();
      }
    },
  );
  await page.getByRole('button', { name: '保存简历', exact: true }).click();
  await expect(
    page.getByText('暂时无法确认操作结果', { exact: true }),
  ).toBeVisible();
  await expect(editor).toHaveText('必须保留的冲突草稿');
  await page.getByRole('button', { name: '查看当前状态', exact: true }).click();
  await expect(editor).toHaveText('必须保留的冲突草稿');
  await page.getByRole('button', { name: '验证操作结果', exact: true }).click();
  await expect(page.getByText('简历修改已保存', { exact: true })).toBeVisible();
  expect(bodies[0]).toEqual(bodies[1]);
  const saved = await get(request, `/resumes/${created.resume.resume_id}`);
  expect(
    saved.resume_version.sections[0].members[0].content[0].runs[0].text,
  ).toBe('必须保留的冲突草稿');
});

test('portrait exposes no-source, empty and queued states and refreshes only explicitly', async ({
  page,
  request,
}) => {
  await page.goto('/candidate-knowledge');
  await expect(page.getByText('还没有画像来源', { exact: true })).toBeVisible();

  const empty = await createResume(request, '空来源', false);
  await page.reload();
  await expect(
    page.getByText('默认简历还没有经历', { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole('link', { name: '编辑来源简历' }),
  ).toHaveAttribute('href', `/resumes/${empty.resume.resume_id}/edit`);

  const populated = await createResume(request, '画像来源');
  const list = await get(request, '/resumes');
  await post(request, '/workspace/default-resume/set', {
    revision: list.default_resume_selection.revision,
    default_resume_id: populated.resume.resume_id,
  });
  let refreshCalls = 0;
  await page.route('**/workspace/portrait/refresh', async (route) => {
    refreshCalls += 1;
    await route.continue();
  });
  await page.reload();
  await expect(page.getByText('用户画像已排队', { exact: true })).toBeVisible();
  expect(refreshCalls).toBe(0);
  await page.reload();
  expect(refreshCalls).toBe(0);
  await page.getByRole('button', { name: '重新生成', exact: true }).click();
  await expect(
    page.getByText('用户画像已提交重新生成', { exact: true }),
  ).toBeVisible();
  expect(refreshCalls).toBe(1);
  expect((await get(request, '/workspace/portrait')).state.status).toBe(
    'QUEUED',
  );
});

test('Resume list opens by name and has no separate edit affordance', async ({
  page,
  request,
}) => {
  const created = await createResume(request, '点击名称编辑');
  await page.goto('/resumes');
  await expect(
    page.getByRole('link', { name: '编辑', exact: true }),
  ).toHaveCount(0);
  await page.getByRole('link', { name: '点击名称编辑', exact: true }).click();
  await expect(page).toHaveURL(
    new RegExp(`/resumes/${created.resume.resume_id}/edit$`),
  );
  await expect(
    page.getByRole('textbox', { name: '姓名', exact: true }),
  ).toHaveValue('点击名称编辑用户');
});
