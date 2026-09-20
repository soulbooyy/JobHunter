import { execFileSync } from 'node:child_process';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { fileURLToPath, URL } from 'node:url';
import openapiTS, { astToString } from 'openapi-typescript';

// Import the real route composition without starting storage or a listener.
const root = fileURLToPath(new URL('../../', import.meta.url));
const schema = JSON.parse(
  execFileSync(
    `${root}.venv/bin/python`,
    [
      '-c',
      [
        'import json',
        'from jobhunter.bootstrap.container import create_app',
        'print(json.dumps(create_app(None).openapi()))',
      ].join('\n'),
    ],
    { cwd: root, encoding: 'utf8' },
  ),
);
// Only the currently consumed Manual Applications and Preferences APIs is exposed to the frontend.
schema.paths = Object.fromEntries(
  Object.entries(schema.paths).filter(
    ([path]) =>
      path.startsWith('/api/v1/manual-application-entries') ||
      path.startsWith('/api/v1/preferences'),
  ),
);
const needed = new Set();
function collect(value) {
  if (!value || typeof value !== 'object') return;
  if (
    typeof value.$ref === 'string' &&
    value.$ref.startsWith('#/components/schemas/')
  ) {
    const name = value.$ref.split('/').at(-1);
    if (!needed.has(name)) {
      needed.add(name);
      collect(schema.components.schemas[name]);
    }
  }
  for (const child of Object.values(value)) collect(child);
}
collect(schema.paths);
schema.components.schemas = Object.fromEntries(
  Object.entries(schema.components.schemas).filter(([name]) =>
    needed.has(name),
  ),
);
const output = new URL('../src/shared/api/schema.d.ts', import.meta.url);
const source = astToString(await openapiTS(schema));
const generated = `/** Generated from backend OpenAPI. Run npm run api:generate; do not edit. */\n${source}`;
if (process.argv.includes('--check')) {
  if ((await readFile(output, 'utf8')) !== generated) {
    throw new Error(
      'API types have drifted. Run npm run api:generate and review the change.',
    );
  }
  console.log('Application API types match backend OpenAPI.');
} else {
  await mkdir(new URL('../src/shared/api/', import.meta.url), {
    recursive: true,
  });
  await writeFile(output, generated);
  console.log('Generated Application API types.');
}
