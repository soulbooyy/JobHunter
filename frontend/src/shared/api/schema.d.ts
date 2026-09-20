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
}
export type webhooks = Record<string, never>;
export interface components {
    schemas: {
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
            code: "BAD_REQUEST" | "REQUEST_TOO_LARGE" | "VALIDATION_ERROR" | "NOT_FOUND" | "REVISION_CONFLICT" | "REQUEST_CONFLICT" | "ORIGINAL_ENTRY_DELETED" | "REVISION_EXHAUSTED" | "STORAGE_UNAVAILABLE" | "OUTCOME_UNKNOWN" | "INTERNAL_ERROR" | "ACCESS_DENIED";
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
            code: "REQUIRED" | "UNKNOWN_FIELD" | "INVALID_TYPE" | "BLANK_VALUE" | "TOO_LONG" | "INVALID_CHARACTERS" | "INVALID_FORMAT" | "OUT_OF_RANGE";
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
}
