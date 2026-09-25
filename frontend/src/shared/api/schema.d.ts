/** Generated from backend OpenAPI. Run npm run api:generate; do not edit. */
export interface paths {
    "/api/v1/manual-application-entries": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** List Entries */
        get: operations["list_entries_api_v1_manual_application_entries_get"];
        put?: never;
        /** Create */
        post: operations["create_api_v1_manual_application_entries_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/manual-application-entries/{manual_application_entry_id}": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Read */
        get: operations["read_api_v1_manual_application_entries__manual_application_entry_id__get"];
        /** Update */
        put: operations["update_api_v1_manual_application_entries__manual_application_entry_id__put"];
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/manual-application-entries/{manual_application_entry_id}/delete": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Delete */
        post: operations["delete_api_v1_manual_application_entries__manual_application_entry_id__delete_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/manual-application-entries/{manual_application_entry_id}/resolve-url": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Resolve */
        post: operations["resolve_api_v1_manual_application_entries__manual_application_entry_id__resolve_url_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/preferences/save": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /**
         * Save
         * @description PRF-012–023: complete canonical Save; null revision requires absence. 1 MiB UTF-8 JSON; duplicate members forbidden; max 1000 raw items per array. Retry preserves the original request and never resets current. Integer-valued numbers admit decimal/exponent spellings without rounding.
         */
        post: operations["save_api_v1_preferences_save_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/preferences": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Current */
        get: operations["current_api_v1_preferences_get"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/preferences/versions/{preference_set_version_id}": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Version */
        get: operations["version_api_v1_preferences_versions__preference_set_version_id__get"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/resumes": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /**
         * Resumes
         * @description Consistent read; no query parameters or request body. Historical exact reads never substitute current versions.
         */
        get: operations["resumes_api_v1_resumes_get"];
        put?: never;
        /**
         * Create Resume
         * @description SAV-018–025: complete closed body, exact JSON numbers, UTF-8 application/json, identity encoding, no query or duplicate object keys. Shared request_id namespace for these six commands. Receipt replay returns the original completion snapshot; read current separately. Limits apply before canonicalization. No network/model/rendering invocation occurs inside the command transaction.
         */
        post: operations["create_resume_api_v1_resumes_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/resumes/versions/{resume_version_id}": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /**
         * Resume Version
         * @description Consistent read; no query parameters or request body. Historical exact reads never substitute current versions.
         */
        get: operations["resume_version_api_v1_resumes_versions__resume_version_id__get"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/resumes/{resume_id}": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /**
         * Resume
         * @description Consistent read; no query parameters or request body. Historical exact reads never substitute current versions.
         */
        get: operations["resume_api_v1_resumes__resume_id__get"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/resumes/{resume_id}/save": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /**
         * Save Resume
         * @description SAV-018–025: complete closed body, exact JSON numbers, UTF-8 application/json, identity encoding, no query or duplicate object keys. Shared request_id namespace for these six commands. Receipt replay returns the original completion snapshot; read current separately. Limits apply before canonicalization. No network/model/rendering invocation occurs inside the command transaction.
         */
        post: operations["save_resume_api_v1_resumes__resume_id__save_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/resumes/{resume_id}/rename": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /**
         * Rename Resume
         * @description SAV-018–025: complete closed body, exact JSON numbers, UTF-8 application/json, identity encoding, no query or duplicate object keys. Shared request_id namespace for these six commands. Receipt replay returns the original completion snapshot; read current separately. Limits apply before canonicalization. No network/model/rendering invocation occurs inside the command transaction.
         */
        post: operations["rename_resume_api_v1_resumes__resume_id__rename_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/resumes/{resume_id}/remove": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /**
         * Remove Resume
         * @description SAV-018–025: complete closed body, exact JSON numbers, UTF-8 application/json, identity encoding, no query or duplicate object keys. Shared request_id namespace for these six commands. Receipt replay returns the original completion snapshot; read current separately. Limits apply before canonicalization. No network/model/rendering invocation occurs inside the command transaction.
         */
        post: operations["remove_resume_api_v1_resumes__resume_id__remove_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/workspace/default-resume/set": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /**
         * Set Default
         * @description SAV-018–025: complete closed body, exact JSON numbers, UTF-8 application/json, identity encoding, no query or duplicate object keys. Shared request_id namespace for these six commands. Receipt replay returns the original completion snapshot; read current separately. Limits apply before canonicalization. No network/model/rendering invocation occurs inside the command transaction.
         */
        post: operations["set_default_api_v1_workspace_default_resume_set_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/workspace/portrait": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /**
         * Portrait
         * @description Consistent read; no query parameters or request body. Historical exact reads never substitute current versions.
         */
        get: operations["portrait_api_v1_workspace_portrait_get"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/v1/workspace/portrait/refresh": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /**
         * Refresh Portrait
         * @description SAV-018–025: complete closed body, exact JSON numbers, UTF-8 application/json, identity encoding, no query or duplicate object keys. Shared request_id namespace for these six commands. Receipt replay returns the original completion snapshot; read current separately. Limits apply before canonicalization. No network/model/rendering invocation occurs inside the command transaction.
         */
        post: operations["refresh_portrait_api_v1_workspace_portrait_refresh_post"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
}
export type webhooks = Record<string, never>;
export interface components {
    schemas: {
        /** BlockEvidenceUnit */
        BlockEvidenceUnit: {
            /** Evidence Id */
            evidence_id: string;
            /** Entry Id */
            entry_id: string;
            /** Block Id */
            block_id: string;
            /** Text */
            text: string;
        };
        /** CandidateEvidenceProjection */
        CandidateEvidenceProjection: {
            /**
             * Schema Version
             * @constant
             */
            schema_version: 1;
            /** Resume Version Id */
            resume_version_id: string;
            /** Extraction Key */
            extraction_key: string;
            /** Entries */
            entries: components["schemas"]["EntryEvidenceUnit"][];
            /** Blocks */
            blocks: components["schemas"]["BlockEvidenceUnit"][];
        };
        /** CandidateProfileProjection */
        CandidateProfileProjection: {
            /**
             * Schema Version
             * @constant
             */
            schema_version: 1;
            /** Resume Version Id */
            resume_version_id: string;
            /** Extraction Key */
            extraction_key: string;
            /** Entries */
            entries: components["schemas"]["ProfileIndexEntry"][];
        };
        /** CityLimited */
        "CityLimited-Input": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /**
             * Value
             * @description PRF-003/004/016: validate every raw item; fixed trim, exact dedup, Unicode code-point sort; no controls, blank or non-scalar text.
             */
            value: string[];
        };
        /** CityLimited */
        "CityLimited-Output": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /** Value */
            value: string[];
        };
        /** CompanyLimited */
        "CompanyLimited-Input": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /**
             * Value
             * @description PRF-003/004/016: validate every raw item; fixed trim, exact dedup, Unicode code-point sort; no controls, blank or non-scalar text.
             */
            value: string[];
        };
        /** CompanyLimited */
        "CompanyLimited-Output": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /** Value */
            value: string[];
        };
        /** Configuration */
        "Configuration-Input": {
            /**
             * Target Job Keywords
             * @description PRF-003/004/016: validate every raw item; fixed trim, exact dedup, Unicode code-point sort; no controls, blank or non-scalar text.
             */
            target_job_keywords: string[];
            /** Accepted Cities */
            accepted_cities: components["schemas"]["Unlimited"] | components["schemas"]["CityLimited-Input"];
            /** Minimum Salary */
            minimum_salary: components["schemas"]["Unlimited"] | components["schemas"]["SalaryLimited"];
            /** Recruitment Types */
            recruitment_types: components["schemas"]["Unlimited"] | components["schemas"]["RecruitmentLimited-Input"];
            /** Excluded Companies */
            excluded_companies: components["schemas"]["Unlimited"] | components["schemas"]["CompanyLimited-Input"];
            /** Max Required Education */
            max_required_education: components["schemas"]["Unlimited"] | components["schemas"]["EducationLimited"];
        };
        /** Configuration */
        "Configuration-Output": {
            /** Target Job Keywords */
            target_job_keywords: string[];
            /** Accepted Cities */
            accepted_cities: components["schemas"]["Unlimited"] | components["schemas"]["CityLimited-Output"];
            /** Minimum Salary */
            minimum_salary: components["schemas"]["Unlimited"] | components["schemas"]["SalaryLimited"];
            /** Recruitment Types */
            recruitment_types: components["schemas"]["Unlimited"] | components["schemas"]["RecruitmentLimited-Output"];
            /** Excluded Companies */
            excluded_companies: components["schemas"]["Unlimited"] | components["schemas"]["CompanyLimited-Output"];
            /** Max Required Education */
            max_required_education: components["schemas"]["Unlimited"] | components["schemas"]["EducationLimited"];
        };
        /** Configured */
        Configured: {
            /**
             * Status
             * @constant
             */
            status: "CONFIGURED";
            preference_set: components["schemas"]["PreferenceSet"];
            current_preference_set_version: components["schemas"]["PreferenceSetVersion"];
        };
        /** ContractError */
        ContractError: {
            /**
             * Code
             * @enum {string}
             */
            code: "RENDER_CONFIGURATION_UNAVAILABLE" | "ARTIFACT_UNAVAILABLE" | "ARTIFACT_INTEGRITY_FAILED" | "INVALID_STATE" | "SOURCE_CONFLICT" | "CAPACITY_EXCEEDED" | "BAD_REQUEST" | "REQUEST_TOO_LARGE" | "VALIDATION_ERROR" | "NOT_FOUND" | "REVISION_CONFLICT" | "REQUEST_CONFLICT" | "ORIGINAL_ENTRY_DELETED" | "REVISION_EXHAUSTED" | "STORAGE_UNAVAILABLE" | "OUTCOME_UNKNOWN" | "INTERNAL_ERROR" | "ACCESS_DENIED";
            /** Message */
            message: string;
            /** Field Errors */
            field_errors: components["schemas"]["FieldError"][];
        };
        /** CreateEntry */
        CreateEntry: {
            /**
             * Company Name
             * @description COM-025/026, MAE-003: scalar text, fixed outer trim; admitted length 1–200; no controls or line separators.
             */
            company_name: string;
            /**
             * Role Title
             * @description COM-025/026, MAE-003: scalar text, fixed outer trim; admitted length 1–200; no controls or line separators.
             */
            role_title: string;
            /**
             * Application Url
             * @description MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors.
             */
            application_url: string;
            /** Request Id */
            request_id: string;
        };
        /** CurrentPortraitState */
        CurrentPortraitState: {
            default_resume_selection: components["schemas"]["DefaultSelection"];
            /** Source Resume Version Id */
            source_resume_version_id: string | null;
            /**
             * Status
             * @enum {string}
             */
            status: "NO_SOURCE" | "EMPTY_SOURCE" | "QUEUED" | "RUNNING" | "READY" | "FAILED";
            /** Build Id */
            build_id: string | null;
            /** Portrait Id */
            portrait_id: string | null;
            /** Failure Code */
            failure_code: ("SOURCE_UNAVAILABLE" | "CONFIGURATION_UNAVAILABLE" | "INPUT_NOT_ADMITTED" | "OUTPUT_INVALID" | "INVOCATION_FAILED" | "OUTCOME_UNKNOWN") | null;
        };
        /** DefaultSelection */
        DefaultSelection: {
            /** Default Resume Id */
            default_resume_id: string | null;
            /** Revision */
            revision: number;
        };
        /** EducationLimited */
        EducationLimited: {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /**
             * Value
             * @enum {string}
             */
            value: "JUNIOR_HIGH_OR_BELOW" | "UPPER_SECONDARY" | "ASSOCIATE" | "BACHELOR" | "MASTER" | "DOCTORATE";
        };
        /** Emphasis */
        Emphasis: {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "BOLD" | "ITALIC" | "UNDERLINE";
        };
        /** EntryEvidenceUnit */
        EntryEvidenceUnit: {
            /** Evidence Id */
            evidence_id: string;
            /** Entry Id */
            entry_id: string;
            /**
             * Kind
             * @enum {string}
             */
            kind: "EDUCATION" | "WORK_EXPERIENCE" | "PROJECT" | "SKILL" | "AWARD" | "CERTIFICATION";
            /** Fields */
            fields: {
                [key: string]: unknown;
            };
            /** Content */
            content: {
                [key: string]: unknown;
            }[];
        };
        /** EvidenceRef */
        EvidenceRef: {
            /** Resume Version Id */
            resume_version_id: string;
            /** Extraction Key */
            extraction_key: string;
            /** Evidence Id */
            evidence_id: string;
        };
        /** ExpectedRevision */
        ExpectedRevision: {
            /** Revision */
            revision: number;
        };
        /** FieldError */
        FieldError: {
            /**
             * Field
             * @description COM-029/034: known fields only; M2 paths use original array indices.
             */
            field: string;
            /**
             * Code
             * @enum {string}
             */
            code: "STRUCTURE_TOO_COMPLEX" | "INVALID_REFERENCE" | "REQUIRED" | "UNKNOWN_FIELD" | "INVALID_TYPE" | "BLANK_VALUE" | "TOO_LONG" | "INVALID_CHARACTERS" | "INVALID_FORMAT" | "OUT_OF_RANGE";
        };
        /** Generation */
        Generation: {
            /**
             * Kind
             * @enum {string}
             */
            kind: "MODEL" | "INCREMENTAL" | "REUSE";
            /** Run Id */
            run_id: string | null;
            /** Reused From Portrait Id */
            reused_from_portrait_id: string | null;
        };
        /** Header */
        "Header-Input": {
            /** Optional Items */
            optional_items: components["schemas"]["HeaderItem-Input"][];
        };
        /** Header */
        "Header-Output": {
            /** Optional Items */
            optional_items: components["schemas"]["HeaderItem-Output"][];
        };
        /** HeaderItem */
        "HeaderItem-Input": {
            /**
             * Kind
             * @enum {string}
             */
            kind: "JOB_SEARCH_STATUS" | "JOB_INTENTION" | "EXPECTED_POSITION" | "EXPECTED_CITY" | "EXPECTED_SALARY" | "HIGHEST_EDUCATION" | "GENDER" | "POLITICAL_AFFILIATION" | "YEARS_OF_EXPERIENCE";
            /**
             * Value
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            value: string;
        };
        /** HeaderItem */
        "HeaderItem-Output": {
            /**
             * Kind
             * @enum {string}
             */
            kind: "JOB_SEARCH_STATUS" | "JOB_INTENTION" | "EXPECTED_POSITION" | "EXPECTED_CITY" | "EXPECTED_SALARY" | "HIGHEST_EDUCATION" | "GENDER" | "POLITICAL_AFFILIATION" | "YEARS_OF_EXPERIENCE";
            /** Value */
            value: string;
        };
        /** Link */
        "Link-Input": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "LINK";
            /**
             * Url
             * @description MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors.
             */
            url: string;
        };
        /** Link */
        "Link-Output": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "LINK";
            /**
             * Url
             * @description MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors.
             */
            url: string;
        };
        /** ListItem */
        "ListItem-Input": {
            /** Block Id */
            block_id: string;
            /** Runs */
            runs: components["schemas"]["TextRun-Input"][];
        };
        /** ListItem */
        "ListItem-Output": {
            /** Block Id */
            block_id: string;
            /** Runs */
            runs: components["schemas"]["TextRun-Output"][];
        };
        /** ManualApplicationEntry */
        ManualApplicationEntry: {
            /** Revision */
            revision: number;
            /** Company Name */
            company_name: string;
            /** Role Title */
            role_title: string;
            /**
             * Application Url
             * @description MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors.
             */
            application_url: string;
            /** Manual Application Entry Id */
            manual_application_entry_id: string;
            /** Created At */
            created_at: string;
            /** Updated At */
            updated_at: string;
        };
        /** ManualApplicationEntryIdentity */
        ManualApplicationEntryIdentity: {
            /** Manual Application Entry Id */
            manual_application_entry_id: string;
        };
        /** ManualApplicationEntryList */
        ManualApplicationEntryList: {
            /** Items */
            items: components["schemas"]["ManualApplicationEntry"][];
        };
        /** ManualApplicationEntryUrl */
        ManualApplicationEntryUrl: {
            /**
             * Application Url
             * @description MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors.
             */
            application_url: string;
        };
        /** NotConfigured */
        NotConfigured: {
            /**
             * Status
             * @constant
             */
            status: "NOT_CONFIGURED";
        };
        /** Paragraph */
        "Paragraph-Input": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "PARAGRAPH";
            /** Block Id */
            block_id: string;
            /** Runs */
            runs: components["schemas"]["TextRun-Input"][];
        };
        /** Paragraph */
        "Paragraph-Output": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "PARAGRAPH";
            /** Block Id */
            block_id: string;
            /** Runs */
            runs: components["schemas"]["TextRun-Output"][];
        };
        /** Portrait */
        Portrait: {
            /** Portrait Id */
            portrait_id: string;
            /**
             * Schema Version
             * @constant
             */
            schema_version: 1;
            /** Resume Version Id */
            resume_version_id: string;
            /** Extraction Key */
            extraction_key: string;
            profile: components["schemas"]["CandidateProfileProjection"];
            evidence: components["schemas"]["CandidateEvidenceProjection"];
            generation: components["schemas"]["Generation"];
            /** Created At */
            created_at: string;
        };
        /** PortraitRead */
        PortraitRead: {
            state: components["schemas"]["CurrentPortraitState"];
            portrait: components["schemas"]["Portrait"] | null;
        };
        /** PortraitRefresh */
        PortraitRefresh: {
            /** Request Id */
            request_id: string;
            default_resume_selection: components["schemas"]["SelectionToken"];
            /** Source Resume Version Id */
            source_resume_version_id: string;
        };
        /** PortraitRefreshResult */
        PortraitRefreshResult: {
            /** Request Id */
            request_id: string;
            /**
             * Outcome
             * @enum {string}
             */
            outcome: "UPDATED" | "UNCHANGED";
            state: components["schemas"]["CurrentPortraitState"];
        };
        /** PreferenceSet */
        PreferenceSet: {
            /** Preference Set Id */
            preference_set_id: string;
            /** Current Preference Set Version Id */
            current_preference_set_version_id: string;
            /** Revision */
            revision: number;
            /** Created At */
            created_at: string;
            /** Updated At */
            updated_at: string;
        };
        /** PreferenceSetVersion */
        PreferenceSetVersion: {
            /** Preference Set Version Id */
            preference_set_version_id: string;
            /** Preference Set Id */
            preference_set_id: string;
            /** Created At */
            created_at: string;
            configuration: components["schemas"]["Configuration-Output"];
        };
        /** Presentation */
        Presentation: {
            /**
             * Font Family
             * @enum {string}
             */
            font_family: "SOURCE_HAN_SANS" | "HEITI" | "SONGTI" | "KAITI";
            /** Font Size Pt */
            font_size_pt: number;
            /** Line Spacing Pt */
            line_spacing_pt: number;
            /** Theme Color */
            theme_color: string;
        };
        /** ProfileContent */
        "ProfileContent-Input": {
            /** Full Name */
            full_name: string | null;
            /** Phone Number */
            phone_number: string | null;
            /** Email */
            email: string | null;
        };
        /** ProfileContent */
        "ProfileContent-Output": {
            /** Full Name */
            full_name: string | null;
            /** Phone Number */
            phone_number: string | null;
            /** Email */
            email: string | null;
        };
        /** ProfileIndexEntry */
        ProfileIndexEntry: {
            /** Source Entry Id */
            source_entry_id: string;
            /** Name */
            name: string;
            /** Description */
            description: string;
            /** Evidence Refs */
            evidence_refs: components["schemas"]["EvidenceRef"][];
        };
        /** RecruitmentLimited */
        "RecruitmentLimited-Input": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /** Value */
            value: ("CAMPUS" | "INTERNSHIP" | "EXPERIENCED" | "PART_TIME")[];
        };
        /** RecruitmentLimited */
        "RecruitmentLimited-Output": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /** Value */
            value: ("CAMPUS" | "INTERNSHIP" | "EXPERIENCED" | "PART_TIME")[];
        };
        /** Resume */
        Resume: {
            /** Resume Id */
            resume_id: string;
            /** Resume Name */
            resume_name: string;
            /**
             * Status
             * @enum {string}
             */
            status: "ACTIVE" | "REMOVED";
            /** Current Resume Version Id */
            current_resume_version_id: string;
            /** Revision */
            revision: number;
            /** Created At */
            created_at: string;
            /** Updated At */
            updated_at: string;
        };
        /** ResumeCreate */
        ResumeCreate: {
            contacts: components["schemas"]["ProfileContent-Input"];
            header_presentation: components["schemas"]["Header-Input"];
            /** Sections */
            sections: components["schemas"]["Section-Input"][];
            document_presentation: components["schemas"]["Presentation"];
            /** Request Id */
            request_id: string;
            /**
             * Resume Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            resume_name: string;
        };
        /** ResumeEntry */
        "ResumeEntry-Input": {
            /** Entry Id */
            entry_id: string;
            /** Fields */
            fields: {
                [key: string]: unknown;
            };
            /** Content */
            content: (components["schemas"]["Paragraph-Input"] | components["schemas"]["RunList-Input"])[];
        };
        /** ResumeEntry */
        "ResumeEntry-Output": {
            /** Entry Id */
            entry_id: string;
            /** Fields */
            fields: {
                [key: string]: unknown;
            };
            /** Content */
            content: (components["schemas"]["Paragraph-Output"] | components["schemas"]["RunList-Output"])[];
        };
        /** ResumeList */
        ResumeList: {
            /** Resumes */
            resumes: components["schemas"]["Resume"][];
            default_resume_selection: components["schemas"]["DefaultSelection"];
        };
        /** ResumePair */
        ResumePair: {
            resume: components["schemas"]["Resume"];
            resume_version: components["schemas"]["ResumeVersion"];
        };
        /** ResumeRemove */
        ResumeRemove: {
            /** Request Id */
            request_id: string;
            /** Revision */
            revision: number;
            default_resume_selection: components["schemas"]["SelectionToken"];
            /** Replacement Resume Id */
            replacement_resume_id: string | null;
        };
        /** ResumeRename */
        ResumeRename: {
            /** Request Id */
            request_id: string;
            /** Revision */
            revision: number;
            /**
             * Resume Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            resume_name: string;
        };
        /** ResumeResult */
        ResumeResult: {
            resume: components["schemas"]["Resume"];
            resume_version: components["schemas"]["ResumeVersion"];
            /** Request Id */
            request_id: string;
            /**
             * Outcome
             * @enum {string}
             */
            outcome: "UPDATED" | "UNCHANGED";
        };
        /** ResumeSave */
        ResumeSave: {
            contacts: components["schemas"]["ProfileContent-Input"];
            header_presentation: components["schemas"]["Header-Input"];
            /** Sections */
            sections: components["schemas"]["Section-Input"][];
            document_presentation: components["schemas"]["Presentation"];
            /** Request Id */
            request_id: string;
            /** Revision */
            revision: number;
        };
        /** ResumeSelectionResult */
        ResumeSelectionResult: {
            resume: components["schemas"]["Resume"];
            resume_version: components["schemas"]["ResumeVersion"];
            /** Request Id */
            request_id: string;
            /**
             * Outcome
             * @enum {string}
             */
            outcome: "CREATED" | "REMOVED" | "UNCHANGED";
            default_resume_selection: components["schemas"]["DefaultSelection"];
        };
        /** ResumeVersion */
        ResumeVersion: {
            contacts: components["schemas"]["ProfileContent-Output"];
            header_presentation: components["schemas"]["Header-Output"];
            /** Sections */
            sections: components["schemas"]["Section-Output"][];
            document_presentation: components["schemas"]["Presentation"];
            /** Resume Version Id */
            resume_version_id: string;
            /** Resume Id */
            resume_id: string;
            /**
             * Schema Version
             * @constant
             */
            schema_version: 2;
            /** Created At */
            created_at: string;
        };
        /** RunList */
        "RunList-Input": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "ORDERED_LIST" | "UNORDERED_LIST";
            /** Items */
            items: components["schemas"]["ListItem-Input"][];
        };
        /** RunList */
        "RunList-Output": {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            type: "ORDERED_LIST" | "UNORDERED_LIST";
            /** Items */
            items: components["schemas"]["ListItem-Output"][];
        };
        /** SalaryLimited */
        SalaryLimited: {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "LIMITED";
            /** Value */
            value: number;
        };
        /** SavePreferences */
        SavePreferences: {
            /** Request Id */
            request_id: string;
            /** Revision */
            revision: number | null;
            configuration: components["schemas"]["Configuration-Input"];
        };
        /** SaveResult */
        SaveResult: {
            /** Preference Set Id */
            preference_set_id: string;
            /** Preference Set Version Id */
            preference_set_version_id: string;
            /** Revision */
            revision: number;
            /**
             * Outcome
             * @enum {string}
             */
            outcome: "CREATED" | "UPDATED" | "UNCHANGED";
        };
        /** Section */
        "Section-Input": {
            /**
             * Kind
             * @enum {string}
             */
            kind: "EDUCATION" | "WORK_EXPERIENCE" | "PROJECT" | "SKILL" | "AWARD" | "CERTIFICATION";
            /** Members */
            members: components["schemas"]["ResumeEntry-Input"][];
        } & (unknown & unknown & unknown & unknown & unknown & unknown);
        /** Section */
        "Section-Output": {
            /**
             * Kind
             * @enum {string}
             */
            kind: "EDUCATION" | "WORK_EXPERIENCE" | "PROJECT" | "SKILL" | "AWARD" | "CERTIFICATION";
            /** Members */
            members: components["schemas"]["ResumeEntry-Output"][];
        };
        /** SelectionResult */
        SelectionResult: {
            /** Request Id */
            request_id: string;
            /**
             * Outcome
             * @enum {string}
             */
            outcome: "UPDATED" | "UNCHANGED";
            default_resume_selection: components["schemas"]["DefaultSelection"];
        };
        /** SelectionToken */
        SelectionToken: {
            /** Revision */
            revision: number;
        };
        /** SetDefault */
        SetDefault: {
            /** Request Id */
            request_id: string;
            /** Revision */
            revision: number;
            /** Default Resume Id */
            default_resume_id: string;
        };
        /** TextRun */
        "TextRun-Input": {
            /** Text */
            text: string;
            /** Marks */
            marks: (components["schemas"]["Emphasis"] | components["schemas"]["Link-Input"])[];
        };
        /** TextRun */
        "TextRun-Output": {
            /** Text */
            text: string;
            /** Marks */
            marks: (components["schemas"]["Emphasis"] | components["schemas"]["Link-Output"])[];
        };
        /** Unlimited */
        Unlimited: {
            /**
             * @description discriminator enum property added by openapi-typescript
             * @enum {string}
             */
            mode: "UNLIMITED";
        };
        /** UpdateEntry */
        UpdateEntry: {
            /** Revision */
            revision: number;
            /**
             * Company Name
             * @description COM-025/026, MAE-003: scalar text, fixed outer trim; admitted length 1–200; no controls or line separators.
             */
            company_name: string;
            /**
             * Role Title
             * @description COM-025/026, MAE-003: scalar text, fixed outer trim; admitted length 1–200; no controls or line separators.
             */
            role_title: string;
            /**
             * Application Url
             * @description MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors.
             */
            application_url: string;
        };
        /** EducationFields */
        EducationFieldsInput: {
            /** Start Month */
            start_month: string | null;
            /** End Month */
            end_month: string | null;
            /**
             * School Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            school_name: string;
            /**
             * Degree
             * @enum {string}
             */
            degree: "SECONDARY_VOCATIONAL" | "HIGH_SCHOOL" | "ASSOCIATE" | "BACHELOR" | "MASTER" | "MBA" | "DOCTORATE";
            /** Major */
            major: string | null;
        };
        /** WorkFields */
        WorkFieldsInput: {
            /** Start Month */
            start_month: string | null;
            /** End Month */
            end_month: string | null;
            /**
             * Company Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            company_name: string;
            /**
             * Role Title
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            role_title: string;
        };
        /** ProjectFields */
        ProjectFieldsInput: {
            /** Start Month */
            start_month: string | null;
            /** End Month */
            end_month: string | null;
            /**
             * Project Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            project_name: string;
            /** Role Title */
            role_title: string | null;
            /** Project Url */
            project_url: string | null;
        };
        /** SkillFields */
        SkillFieldsInput: {
            /**
             * Skill Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            skill_name: string;
        };
        /** AwardFields */
        AwardFieldsInput: {
            /**
             * Award Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            award_name: string;
            /** Awarding Organization */
            awarding_organization: string | null;
            /** Awarded Month */
            awarded_month: string | null;
        };
        /** CertificationFields */
        CertificationFieldsInput: {
            /**
             * Certification Name
             * @description Common fixed outer trim; nonblank scalar single-line text.
             */
            certification_name: string;
            /** Issuing Organization */
            issuing_organization: string | null;
            /** Issued Month */
            issued_month: string | null;
        };
    };
    responses: never;
    parameters: never;
    requestBodies: never;
    headers: never;
    pathItems: never;
}
export type $defs = Record<string, never>;
export interface operations {
    list_entries_api_v1_manual_application_entries_get: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ManualApplicationEntryList"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    create_api_v1_manual_application_entries_post: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["CreateEntry"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ManualApplicationEntryIdentity"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    read_api_v1_manual_application_entries__manual_application_entry_id__get: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                manual_application_entry_id: string;
            };
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ManualApplicationEntry"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    update_api_v1_manual_application_entries__manual_application_entry_id__put: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                manual_application_entry_id: string;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["UpdateEntry"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ManualApplicationEntry"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    delete_api_v1_manual_application_entries__manual_application_entry_id__delete_post: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                manual_application_entry_id: string;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["ExpectedRevision"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ManualApplicationEntryIdentity"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    resolve_api_v1_manual_application_entries__manual_application_entry_id__resolve_url_post: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                manual_application_entry_id: string;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["ExpectedRevision"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ManualApplicationEntryUrl"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    save_api_v1_preferences_save_post: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["SavePreferences"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["SaveResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    current_api_v1_preferences_get: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["Configured"] | components["schemas"]["NotConfigured"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    version_api_v1_preferences_versions__preference_set_version_id__get: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                preference_set_version_id: string;
            };
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["PreferenceSetVersion"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    resumes_api_v1_resumes_get: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumeList"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    create_resume_api_v1_resumes_post: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["ResumeCreate"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumeSelectionResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    resume_version_api_v1_resumes_versions__resume_version_id__get: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                resume_version_id: string;
            };
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumeVersion"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    resume_api_v1_resumes__resume_id__get: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                resume_id: string;
            };
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumePair"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    save_resume_api_v1_resumes__resume_id__save_post: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                resume_id: string;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["ResumeSave"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumeResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    rename_resume_api_v1_resumes__resume_id__rename_post: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                resume_id: string;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["ResumeRename"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumeResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    remove_resume_api_v1_resumes__resume_id__remove_post: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                resume_id: string;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["ResumeRemove"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ResumeSelectionResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    set_default_api_v1_workspace_default_resume_set_post: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["SetDefault"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["SelectionResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    portrait_api_v1_workspace_portrait_get: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["PortraitRead"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
    refresh_portrait_api_v1_workspace_portrait_refresh_post: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["PortraitRefresh"];
            };
        };
        responses: {
            /** @description Successful Response */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["PortraitRefreshResult"];
                };
            };
            /** @description Bad Request */
            400: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Forbidden */
            403: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Not Found */
            404: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Conflict */
            409: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Request Entity Too Large */
            413: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Unprocessable Entity */
            422: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Internal Server Error */
            500: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
            /** @description Service Unavailable */
            503: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["ContractError"];
                };
            };
        };
    };
}
