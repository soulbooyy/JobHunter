import { z } from 'zod';
import { api as client } from '@/shared/api/client';
import { apiResult } from '@/shared/api/result';
import type { components } from '@/shared/api/schema';
import {
  profilePair,
  profileVersion,
  profileResult,
} from '@/entities/profile/model';
import {
  evidencePair,
  evidenceList,
  evidenceExact,
  evidenceResult,
} from '@/entities/evidence/model';
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
      (v) =>
        !requestId || (v as { request_id?: string }).request_id === requestId,
    ),
    write,
    'candidate',
  );
}
export const candidateApi = {
  profile: () =>
    result(() => client.GET('/api/v1/profile', options()), profilePair),
  profileVersion: (id: string) =>
    result(
      () =>
        client.GET('/api/v1/profile/versions/{profile_version_id}', {
          ...options(),
          params: { path: { profile_version_id: id } },
        }),
      profileVersion.refine((v) => v.profile_version_id === id),
    ),
  saveProfile: (body: S['ProfileSave']) =>
    result(
      () => client.POST('/api/v1/profile/save', { ...options(), body }),
      profileResult,
      true,
      body.request_id,
    ),
  evidence: () =>
    result(() => client.GET('/api/v1/evidence-items', options()), evidenceList),
  evidenceItem: (id: string) =>
    result(
      () =>
        client.GET('/api/v1/evidence-items/{evidence_item_id}', {
          ...options(),
          params: { path: { evidence_item_id: id } },
        }),
      evidencePair.refine((v) => v.evidence_item.evidence_item_id === id),
    ),
  evidenceVersion: (id: string) =>
    result(
      () =>
        client.GET(
          '/api/v1/evidence-items/versions/{evidence_item_version_id}',
          { ...options(), params: { path: { evidence_item_version_id: id } } },
        ),
      evidenceExact.refine(
        (v) => v.evidence_item_version.evidence_item_version_id === id,
      ),
    ),
  createEvidence: (body: S['EvidenceCreate']) =>
    result(
      () => client.POST('/api/v1/evidence-items', { ...options(), body }),
      evidenceResult,
      true,
      body.request_id,
    ),
  saveEvidence: (id: string, body: S['EvidenceUpdate']) =>
    result(
      () =>
        client.POST('/api/v1/evidence-items/{evidence_item_id}/save', {
          ...options(),
          params: { path: { evidence_item_id: id } },
          body,
        }),
      evidenceResult.refine((v) => v.evidence_item.evidence_item_id === id),
      true,
      body.request_id,
    ),
  retireEvidence: (id: string, body: S['EvidenceRetire']) =>
    result(
      () =>
        client.POST('/api/v1/evidence-items/{evidence_item_id}/retire', {
          ...options(),
          params: { path: { evidence_item_id: id } },
          body,
        }),
      evidenceResult.refine((v) => v.evidence_item.evidence_item_id === id),
      true,
      body.request_id,
    ),
  resumes: () =>
    result(() => client.GET('/api/v1/resumes', options()), resumeList),
  resume: (id: string) =>
    result(
      () =>
        client.GET('/api/v1/resumes/{resume_id}', {
          ...options(),
          params: { path: { resume_id: id } },
        }),
      resumePair.refine((v) => v.resume.resume_id === id),
    ),
  resumeVersion: (id: string) =>
    result(
      () =>
        client.GET('/api/v1/resumes/versions/{resume_version_id}', {
          ...options(),
          params: { path: { resume_version_id: id } },
        }),
      resumeVersion.refine((v) => v.resume_version_id === id),
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
      resumeResult.refine((v) => v.resume.resume_id === id),
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
      resumeResult.refine((v) => v.resume.resume_id === id),
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
      resumeSelectionResult.refine((v) => v.resume.resume_id === id),
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
};
