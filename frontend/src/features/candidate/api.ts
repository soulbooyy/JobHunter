import { z } from 'zod';
import { api as client } from '@/shared/api/client';
import { apiResult } from '@/shared/api/result';
import type { components } from '@/shared/api/schema';
import { portraitRead, portraitRefreshResult } from '@/entities/profile/model';
import {
  resumePair,
  resumeList,
  resumeVersion,
  resumeResult,
  resumeSelectionResult,
  selectionResult,
} from '@/entities/resume/model';

const options = () => ({ signal: AbortSignal.timeout(15000) });
type S = components['schemas'];
function result<T>(
  operation: Parameters<typeof apiResult>[0],
  schema: z.ZodType<T>,
  write = false,
  requestId?: string,
) {
  return apiResult(
    operation,
    schema.refine(
      (value) =>
        !requestId ||
        (value as { request_id?: string }).request_id === requestId,
    ),
    write,
    'candidate',
  );
}
export const candidateApi = {
  resumes: () =>
    result(() => client.GET('/api/v1/resumes', options()), resumeList),
  resume: (id: string) =>
    result(
      () =>
        client.GET('/api/v1/resumes/{resume_id}', {
          ...options(),
          params: { path: { resume_id: id } },
        }),
      resumePair.refine((value) => value.resume.resume_id === id),
    ),
  resumeVersion: (id: string) =>
    result(
      () =>
        client.GET('/api/v1/resumes/versions/{resume_version_id}', {
          ...options(),
          params: { path: { resume_version_id: id } },
        }),
      resumeVersion.refine((value) => value.resume_version_id === id),
    ),
  createResume: (body: S['ResumeCreate']) =>
    result(
      () => client.POST('/api/v1/resumes', { ...options(), body }),
      resumeSelectionResult,
      true,
      body.request_id,
    ),
  saveResume: (id: string, body: S['ResumeSave']) =>
    result(
      () =>
        client.POST('/api/v1/resumes/{resume_id}/save', {
          ...options(),
          params: { path: { resume_id: id } },
          body,
        }),
      resumeResult.refine((value) => value.resume.resume_id === id),
      true,
      body.request_id,
    ),
  renameResume: (id: string, body: S['ResumeRename']) =>
    result(
      () =>
        client.POST('/api/v1/resumes/{resume_id}/rename', {
          ...options(),
          params: { path: { resume_id: id } },
          body,
        }),
      resumeResult.refine((value) => value.resume.resume_id === id),
      true,
      body.request_id,
    ),
  removeResume: (id: string, body: S['ResumeRemove']) =>
    result(
      () =>
        client.POST('/api/v1/resumes/{resume_id}/remove', {
          ...options(),
          params: { path: { resume_id: id } },
          body,
        }),
      resumeSelectionResult.refine((value) => value.resume.resume_id === id),
      true,
      body.request_id,
    ),
  setDefault: (body: S['SetDefault']) =>
    result(
      () =>
        client.POST('/api/v1/workspace/default-resume/set', {
          ...options(),
          body,
        }),
      selectionResult,
      true,
      body.request_id,
    ),
  portrait: () =>
    result(
      () => client.GET('/api/v1/workspace/portrait', options()),
      portraitRead,
    ),
  refreshPortrait: (body: S['PortraitRefresh']) =>
    result(
      () =>
        client.POST('/api/v1/workspace/portrait/refresh', {
          ...options(),
          body,
        }),
      portraitRefreshResult,
      true,
      body.request_id,
    ),
};
