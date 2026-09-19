import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath, URL } from 'node:url';
import { createServer } from 'node:http';
const root = fileURLToPath(new URL('../../', import.meta.url));
const directory = await mkdtemp(join(tmpdir(), 'jobhunter-e2e-'));
const child = spawn(`${root}.venv/bin/python`, ['-m', 'jobhunter.main'], {
  cwd: root,
  env: {
    ...process.env,
    JOBHUNTER_DATA_DIRECTORY: directory,
    JOBHUNTER_PORT: '18765',
    JOBHUNTER_ALLOWED_HOSTS: '127.0.0.1:18765',
    JOBHUNTER_ALLOWED_ORIGINS: 'http://127.0.0.1:15173',
  },
  stdio: 'inherit',
});
const sink = createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  response.end(
    `<!doctype html><html><head><title>Local navigation test</title></head><body><p id="received-referrer">${request.headers.referer ? 'present' : 'absent'}</p></body></html>`,
  );
});
sink.listen(18865, '127.0.0.1');
let stopping = false;
async function stop() {
  if (stopping) return;
  stopping = true;
  sink.close();
  child.kill('SIGTERM');
}
process.on('SIGINT', () => void stop());
process.on('SIGTERM', () => void stop());
child.on('exit', async (code) => {
  sink.close();
  await rm(directory, { recursive: true, force: true });
  process.exit(stopping ? 0 : (code ?? 1));
});
