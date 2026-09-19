# JobHunter Design System v1

> Status: FROZEN\
> Version: 1.0\
> Design anchor: Manual Applications\
> Primary implementation target: React + TypeScript + Tailwind CSS + shadcn/ui + Radix UI\
> Primary UI language: Simplified Chinese\
>
> JobHunter Design System v1 defines the shared visual and interaction language for the JobHunter frontend.
>
> New pages must reuse this system rather than inventing page-specific visual patterns.
>
> The approved Manual Applications designs are the visual reference implementation for v1.

---

# 1. Design System Authority

## 1.1 Responsibility

This document owns shared frontend visual and interaction rules, including:

- application shell;
- sidebar navigation;
- page hierarchy;
- typography;
- colors;
- spacing;
- border and radius;
- buttons;
- forms;
- tables;
- dialogs;
- destructive actions;
- empty states;
- loading states;
- error states;
- conflict states;
- uncertain-operation states;
- interaction feedback.

This document does **not** define product behavior or business authority.

Product behavior must come from the relevant:

- Product Specification;
- Architecture;
- Contract;
- API reference;
- Acceptance criteria.

A Stitch design must not create new product behavior merely because a visual element appears in a generated screen.

---

## 1.2 Authority order

When sources appear to disagree, use this order:

1. Product / Contract / API documents — business behavior and available capabilities.
2. `docs/ui/DESIGN.md` — shared visual and interaction system.
3. Approved Stitch screens — page-specific visual reference.
4. Stitch-generated implementation code — optional implementation reference only.

Stitch-generated code is not architectural authority.

---

## 1.3 Design anchor

The following Manual Applications states established Design System v1:

- populated list;
- add dialog;
- edit dialog;
- inline validation;
- delete confirmation;
- successful empty state;
- loading skeleton;
- load error;
- revision conflict;
- uncertain mutation outcome.

Future pages should inherit their visual language.

---

# 2. Product Character

JobHunter is a:

- single-user;
- local-first;
- AI-assisted;
- personal job-search workspace;
- desktop productivity tool.

It is **not**:

- a recruiting website;
- an ATS;
- a CRM;
- an enterprise admin template;
- a marketing SaaS dashboard;
- an AI showcase.

The interface should feel closer to:

- Linear;
- Codex;
- GitHub productivity tooling;
- modern developer workspaces.

---

# 3. Core Design Principles

## 3.1 Information before decoration

Information hierarchy must come primarily from:

- typography;
- spacing;
- alignment;
- grouping;
- subtle surface changes.

Do not add decorative elements merely to make a page look richer.

---

## 3.2 Tool before marketing

Prefer:

- tables;
- compact controls;
- contextual dialogs;
- restrained navigation;
- dense but readable layouts.

Avoid:

- hero sections;
- promotional banners;
- oversized cards;
- decorative statistics;
- colorful dashboards.

---

## 3.3 Reuse before specialization

If an existing Design System component can represent a new screen, reuse it.

Do not create page-specific variants of:

- buttons;
- inputs;
- dialogs;
- tables;
- navigation active states;
- empty states;
- error states;

unless the existing pattern is genuinely insufficient.

---

## 3.4 Business state must be real

Do not invent visual states unsupported by the product.

Examples of prohibited invented UI:

- application status when no such status exists;
- AI score when no analysis exists;
- fake synchronization state;
- fake job metadata;
- persistent “pending verification” badges derived from transient UI state.

---

## 3.5 Calm failure handling

Failure and uncertainty should be visible but not dramatic.

Prefer:

- localized feedback;
- restrained warning surfaces;
- clear recovery actions;
- preserved user input.

Avoid:

- full-screen failures;
- large red banners;
- dramatic warning illustrations;
- alarming language.

---

# 4. Language and Copy

## 4.1 UI language

All ordinary user-visible interface text should use:

**Simplified Chinese**

Exceptions:

- `JobHunter`;
- URLs;
- proper nouns normally written in English;
- unavoidable technical notation.

Do not mix ordinary English UI labels into Chinese screens.

---

## 4.2 Tone

Copy should be:

- concise;
- neutral;
- calm;
- professional;
- natural;
- developer-tool-like.

Prefer:

- `保存修改`
- `查看最新版本`
- `重试`
- `打开申请页面`

Avoid verbose enterprise copy such as:

- `请点击此处进行重新加载操作`
- `系统检测到当前数据版本已发生变化`

Avoid recruiting-marketing copy such as:

- `立即投递`
- `发现好机会`
- `AI 帮你拿 Offer`
- `提升求职成功率`

---

## 4.3 Error wording

Do not expose backend codes directly in ordinary UI.

Do not show:

- `REVISION_CONFLICT`
- `OUTCOME_UNKNOWN`
- `VALIDATION_ERROR`
- HTTP status codes;
- internal field names;
- database terminology.

Translate behavior into natural user-facing Chinese.

---

# 5. Application Shell

## 5.1 Structure

Desktop layout:

```text
┌──────────────── Sidebar ────────────────┬───────────────────────────────┐
│                                        │ Workspace Top Bar             │
│ Navigation                             ├───────────────────────────────┤
│                                        │ Main Content                  │
│                                        │                               │
│                                        │                               │
└────────────────────────────────────────┴───────────────────────────────┘
````

Primary regions:

1. Sidebar
2. Workspace Top Bar
3. Main Content Area

---

## 5.2 Desktop-first

v1 is desktop-first.

The primary design target is a laptop / desktop workspace.

Do not distort desktop information density merely to simulate a mobile-first application.

Responsive behavior may be added later without redefining desktop patterns.

---

# 6. Sidebar

## 6.1 General character

Sidebar should be:

* compact;
* quiet;
* monochrome;
* easy to scan;
* visually stable.

Avoid:

* oversized icons;
* colorful category blocks;
* heavy shadows;
* card-style navigation.

---

## 6.2 Current navigation language

Current Chinese navigation labels include:

* 我的简历
* 求职资料库
* 岗位池

  * 手动申请
* 求职助手
* 我的申请

Actual navigation availability must follow Product scope.

---

## 6.3 Primary and secondary navigation share one system

Primary and secondary navigation items must use the **same active and hover language**.

Secondary navigation must not look like a separate design system.

Hierarchy is expressed through:

* indentation;
* alignment;
* parent / child grouping;
* expand / collapse behavior.

---

## 6.4 Secondary navigation

Example:

```text
岗位池
    手动申请
```

Use indentation to communicate hierarchy.

Do **not** use:

* gray + black double vertical lines;
* multiple active indicators;
* heavy nested borders.

---

## 6.5 Active state

For both primary and secondary navigation items:

* subtle light-gray rounded background;
* dark foreground text;
* slightly increased font weight;
* background covers the full clickable row;
* no heavy shadow;
* no decorative treatment.

Preferred approach:

**background highlight only**

Avoid a vertical active bar.

If a future context genuinely requires an indicator, use at most one very thin subtle accent line.

---

## 6.6 Hover state

Hover state:

* lighter gray than active;
* no extra border;
* no decorative line;
* subtle transition only.

---

## 6.7 Unselected state

Unselected secondary items:

* transparent background;
* standard foreground / muted foreground;
* indentation communicates hierarchy.

---

## 6.8 Expand / collapse

Parent navigation may use a compact chevron.

Chevron should:

* align precisely with the row;
* use the same visual weight as other sidebar icons;
* not dominate the item.

---

## 6.9 Icons

Sidebar icons must share:

* same visual size;
* same stroke weight;
* same outline style;
* same alignment;
* same visual rhythm.

Do not use colorful icons.

Secondary navigation items may have their own icon.

For Manual Applications, appropriate metaphors include:

* external-link;
* link;
* form;
* send;
* cursor-click;
* file-check.

The icon must not be more visually dominant than other navigation icons.

---

## 6.10 Sidebar footer

A local workspace status area may appear at the bottom of the Sidebar when relevant.

Example visual language:

```text
● 本地工作区
  Local SQLite DB
```

Keep this secondary and compact.

Do not turn it into a large status card.

---

# 7. Workspace Top Bar

The top bar provides workspace context and a small number of global controls.

Characteristics:

* compact height;
* thin bottom border;
* neutral background;
* minimal actions.

Example context:

```text
workspace / jobhunter-core
```

Do not overload the top bar.

---

## 7.1 Keyboard shortcut hints

JobHunter Design System v1 does **not** display visible keyboard shortcut hints.

Do not show:

* `⌘ K`;
* `Ctrl K`;
* keycaps;
* shortcut badges;
* command-key labels.

Keyboard shortcuts may be implemented later without visible v1 UI.

---

# 8. Main Content Area

## 8.1 Width

Use a wide productivity-workspace content region.

Typical useful content width:

approximately `1200–1400px`, depending on viewport.

Do not artificially constrain data-heavy pages to narrow marketing-page widths.

---

## 8.2 Whitespace

Open whitespace is acceptable.

Do not fill unused workspace with:

* metrics;
* decorative cards;
* suggestions;
* tutorials;
* fake activity feeds.

Whitespace is part of the restrained visual language.

---

# 9. Breadcrumb

Breadcrumb provides lightweight context.

Example:

```text
岗位池 / 手动申请
```

Style:

* small;
* muted;
* visually secondary.

Breadcrumb must not compete with:

* page title;
* secondary tabs;
* primary action.

---

# 10. Page Header

Standard structure:

```text
Page Title                         Primary Action
Description
```

Example:

```text
手动申请                           + 添加申请
保存和管理需要手动访问的岗位申请链接。
```

---

## 10.1 Title

Recommended visual range:

* 24–28px;
* semibold;
* strong foreground.

Do not use oversized marketing typography.

---

## 10.2 Description

Recommended:

* 13–14px;
* muted foreground;
* concise.

---

## 10.3 Primary action

Place the primary page action toward the right side of the header.

Keep it visually clear but compact.

---

# 11. Secondary View Navigation

Use text-style tabs for sibling views.

Example:

```text
岗位列表    手动申请
              ━━━
```

Active state:

* stronger foreground;
* slightly increased font weight;
* thin underline.

Inactive:

* muted foreground;
* no filled background.

Avoid:

* pill tabs;
* large segmented controls;
* card-style tabs.

---

# 12. Typography

Use a modern sans-serif interface stack with high-quality Simplified Chinese rendering.

Requirements:

* clear hierarchy;
* compact but readable line-height;
* no decorative Chinese fonts;
* no unnecessary letter spacing.

Recommended hierarchy:

| Role               | Approximate size |
| ------------------ | ---------------: |
| Page title         |          24–28px |
| Dialog title       |          18–20px |
| Section heading    |          16–18px |
| Body / table       |          13–14px |
| Label              |          12–14px |
| Metadata / caption |          12–13px |

These are visual ranges, not strict pixel contracts.

---

## 12.1 Weight hierarchy

Use font weight sparingly.

Typical hierarchy:

* page / dialog title: semibold;
* company / primary row label: medium / semibold;
* normal content: regular;
* metadata: regular + muted color.

Avoid bolding multiple columns in one table row.

---

# 13. Color System

## 13.1 General palette

The interface is primarily:

* white;
* near-white;
* neutral gray;
* dark neutral text.

The system should remain mostly monochrome.

---

## 13.2 Semantic color roles

Use semantic tokens rather than arbitrary page-specific colors.

Required roles:

```text
background
foreground

surface
surface-muted

border
border-subtle

text-muted

primary
primary-foreground

hover
active

destructive
destructive-foreground

notice-background
notice-border
notice-accent

error
focus
```

Exact implementation values should be mapped consistently in the frontend theme.

---

## 13.3 Primary action

Primary actions use a strong neutral / black treatment.

Avoid saturated brand colors for ordinary primary actions in v1.

---

## 13.4 Destructive red

Destructive red is reserved primarily for irreversible actions.

Examples:

* Delete button;
* destructive menu item.

Use restrained red rather than high-saturation scarlet.

---

## 13.5 Exception notice tone

Revision Conflict and Outcome Unknown use a softer warning surface than destructive actions.

Use:

* very light muted red / rose / dusty-red background;
* soft low-saturation red border;
* muted red icon or accent;
* mostly neutral-dark body text.

Severity hierarchy:

```text
Destructive action
    ↓ stronger red

Conflict / Outcome Unknown notice
    ↓ muted dusty-red / rose surface

Ordinary neutral information
    ↓ grayscale
```

Do not make conflict / uncertainty surfaces as visually strong as Delete.

---

# 14. Borders

Use subtle `1px` borders.

Primary uses:

* table boundaries;
* input boundaries;
* dialog surfaces;
* separators;
* inline notice surfaces.

Avoid thick borders.

---

# 15. Radius

Use restrained rounding.

Typical range:

`6–10px`

Suggested behavior:

* buttons: compact radius;
* inputs: 6–8px;
* table container: approximately 8px;
* dialogs: approximately 8px.

Avoid excessively rounded SaaS-style pills and cards.

---

# 16. Shadows

Normal surfaces should use little or no shadow.

Use subtle elevation primarily for:

* Dialog;
* AlertDialog;
* menus.

Avoid:

* large soft card shadows;
* glowing shadows;
* layered marketing elevation.

---

# 17. Spacing

Use an approximately `8px` spacing rhythm.

Common relationships:

```text
4px   micro spacing
8px   compact spacing
12px  small separation
16px  standard component gap
24px  section-level gap
32px+ major structural spacing
```

These are implementation guides rather than strict contracts.

---

# 18. Buttons

## 18.1 Primary button

Characteristics:

* black / strong neutral background;
* light foreground;
* compact;
* approximately 32–36px height;
* restrained radius.

Example:

```text
+ 添加申请
```

Do not make ordinary primary buttons into large marketing CTAs.

---

## 18.2 Secondary button

Use:

* white / neutral background;
* subtle border or ghost treatment;
* dark foreground.

Example:

```text
取消
```

---

## 18.3 Destructive button

Use muted destructive red.

Example:

```text
删除
```

Do not make the entire surrounding Dialog destructive red.

---

## 18.4 Loading button

During an active operation:

* keep button width stable;
* optionally show small spinner;
* disable repeated submission.

Example:

```text
保存中…
```

Avoid layout shift.

---

## 18.5 Disabled

Disabled controls should remain readable.

Do not reduce opacity so aggressively that labels become difficult to understand.

---

# 19. Form System

## 19.1 Layout

Default form pattern:

```text
Label
Input
Inline error if needed
```

Use a single-column layout for ordinary compact Dialog forms.

---

## 19.2 Inputs

Recommended:

* 36–40px height;
* subtle border;
* neutral surface;
* 6–8px radius;
* clear focus state;
* dark entered text;
* muted placeholder.

Avoid:

* floating labels;
* filled Material Design fields;
* underline-only fields.

---

## 19.3 Labels

Labels should be:

* small;
* medium weight;
* dark neutral.

---

## 19.4 Required fields

Required fields use a small `*` beside the label.

Example:

```text
公司 *
职位名称 *
申请链接 *
```

The form may also show the approved subtle required helper:

```text
* 为必填项
```

Use the same header pattern across Add and Edit.

Do not write:

```text
公司（必填）
职位名称（必填）
```

on every field.

---

# 20. Validation

## 20.1 Field validation

Field validation is local to the field.

Pattern:

```text
公司 *

[ invalid input ]

请输入公司名称
```

Use:

* subtle error-colored input border;
* small error message;
* approximately 4–6px spacing below input.

---

## 20.2 Error icons

Small error icons may be used, but should not dominate.

Do not add warning icons to every field if text alone is sufficient.

---

## 20.3 Preserve user input

Validation errors must not:

* clear the form;
* restore previous values;
* close the dialog.

The user's entered content remains visible.

---

## 20.4 Error copy

Examples:

```text
请输入公司名称
请输入职位名称
请输入申请链接
请输入有效的 HTTP 或 HTTPS 链接
内容过长，请缩短后重试
```

Keep errors specific and actionable.

---

## 20.5 Form-level errors

Non-field-specific issues may appear above the form in a compact inline surface.

Do not use large banners for ordinary form errors.

---

# 21. Dialog

## 21.1 Standard form Dialog

Recommended width:

approximately `460–520px`.

Characteristics:

* centered;
* restrained overlay;
* subtle shadow;
* compact layout;
* approximately 8px radius.

---

## 21.2 Header pattern

Example:

```text
编辑手动申请
保存公司、职位和申请链接，方便之后继续访问。
* 为必填项
```

Add and Edit must share the same header structure.

Only semantic text should differ.

---

## 21.3 Close button

A normal form Dialog may use a subtle top-right close button.

---

## 21.4 Footer

Actions align bottom-right.

Typical order:

```text
取消    保存修改
```

---

# 22. Add / Edit Reuse

Create and Edit should reuse the same Form/Dialog component whenever possible.

Example:

```text
Add
Title: 添加手动申请
Primary: 添加申请

Edit
Title: 编辑手动申请
Primary: 保存修改
```

Do not create different visual systems for Add and Edit.

---

# 23. AlertDialog

Use AlertDialog for irreversible confirmations.

Example:

```text
删除这条手动申请？

删除后，这条记录将被永久移除，无法恢复.

取消    删除
```

---

## 23.1 AlertDialog characteristics

* smaller than ordinary form Dialog;
* approximately 380–440px;
* compact;
* one confirmation step;
* no unnecessary form input.

---

## 23.2 Close behavior

Prefer explicit actions rather than an additional visible close button.

---

## 23.3 Destructive context

Optional contextual identity may be shown:

```text
OpenAI · 软件工程师
```

Do not expose technical metadata.

---

## 23.4 No fake Undo

If the product has no restore capability:

do not show:

* Undo;
* Restore;
* Trash;
* Recycle Bin.

---

# 24. Dropdown Menu

Use a compact overflow menu for secondary row actions.

Trigger:

```text
···
```

Example actions:

```text
打开申请页面
编辑
────────
删除
```

Delete should be visually destructive.

Avoid placing multiple large action buttons directly in every table row.

---

# 25. Tables

## 25.1 General style

Tables should feel similar to developer productivity tools.

Use:

* compact rows;
* subtle separators;
* weak header background;
* thin outer border;
* restrained radius;
* no heavy shadow;
* no zebra striping.

---

## 25.2 Information hierarchy

Example hierarchy:

1. primary entity label;
2. normal content;
3. muted secondary content;
4. metadata;
5. actions.

Do not give every column equal visual emphasis.

---

## 25.3 URLs

URLs should be visually quiet.

Prefer presentation such as:

```text
jobs.bytedance.com / experienced/position/...
```

rather than visually dominant full links.

The underlying actual saved URL must remain intact.

Do not silently normalize or rewrite the business value.

---

## 25.4 Action column

Action headers must remain on one line.

Do not allow:

```text
操
作
```

Use sufficient fixed width for compact action columns.

---

# 26. Empty State

## 26.1 Meaning

Empty State represents:

**successful data load with zero records**

It must never be used to mask:

* loading;
* backend failure;
* storage failure;
* unknown state.

---

## 26.2 Structure

Standard pattern:

```text
Title

Description

[ Primary Action ]
```

Example:

```text
还没有手动申请

保存你想稍后继续访问的岗位申请链接。

[ 添加申请 ]
```

---

## 26.3 Positioning

Place the state relatively near the upper content area.

Do not perfectly center it vertically in the entire viewport.

Typical relationship:

```text
secondary tabs
↓
60–100px space
↓
empty state
```

---

## 26.4 Decoration

Prefer text-first states.

Do not use:

* large illustrations;
* mascots;
* decorative AI graphics;
* onboarding cards.

---

# 27. Loading State

## 27.1 Scope

Loading should be localized to the data region.

Keep:

* App Shell;
* navigation;
* Page Header;
* tabs;

stable.

---

## 27.2 Skeleton

Use table-shaped skeletons for table content.

Keep:

* table header;
* column positions;
* row height;
* table border;
* table radius.

This reduces layout shift.

---

## 27.3 Skeleton visual treatment

Use:

* very light neutral gray;
* low contrast;
* compact blocks;
* subtle radius.

Avoid:

* bright shimmer;
* strong pulse;
* colorful loading effects.

---

## 27.4 No full-page spinner

Do not replace the workspace with:

```text
正在加载...
```

or a centered blocking spinner.

---

# 28. Load Error State

## 28.1 Meaning

Load Error means data could not currently be read.

It must not imply:

* zero data;
* deletion;
* data loss.

---

## 28.2 Structure

Example:

```text
无法加载手动申请

暂时无法读取已保存的手动申请，请重试。

[ 重试 ]
```

---

## 28.3 Composition

Load Error and Empty State should share similar spatial composition.

Difference comes from meaning, copy, and recovery action.

Do not create an entirely separate layout system.

---

## 28.4 Technical details

Do not expose raw backend failures in ordinary UI.

---

# 29. Revision Conflict Pattern

Revision Conflict represents a known concurrent change.

Core rules:

1. keep Dialog open;
2. preserve dirty input;
3. do not automatically overwrite;
4. do not automatically retry;
5. allow user to inspect latest saved state;
6. require explicit user decision.

---

## 29.1 Copy pattern

Example:

```text
这条记录已在其他页面发生修改

你当前输入的内容已保留。请查看最新版本后再决定是否保存。
```

---

## 29.2 Visual treatment

Use the Design System exception notice:

* very light muted dusty-red / rose background;
* soft low-saturation red border;
* muted red accent / icon;
* neutral-dark text.

Do not use strong destructive red.

---

## 29.3 Latest saved version

The latest saved state may appear in a compact read-only section.

Do not turn it into a second editable form.

---

## 29.4 User decision

Possible actions include:

```text
基于最新版本继续编辑
放弃当前修改
```

Exact behavior must follow the relevant business Contract.

Do not invent automatic merging.

---

# 30. Outcome Unknown Pattern

Outcome Unknown represents a mutation whose final result cannot currently be confirmed.

It is neither known success nor known failure.

Core rules:

1. preserve user input;
2. do not claim success;
3. do not claim failure;
4. do not silently retry;
5. verify current saved state;
6. transition to known patterns after verification.

---

## 30.1 Copy pattern

Example:

```text
暂时无法确认操作结果

无法确认刚才的修改是否已经保存。
请先检查当前记录，再决定是否重试。

[ 检查当前状态 ]
```

---

## 30.2 Visual treatment

Use the same exception-notice family as Revision Conflict:

* muted dusty-red / rose tint;
* soft border;
* restrained accent.

Do not make it equal in severity to Delete.

---

## 30.3 Save button

While the result remains unknown, normal save must not immediately submit again.

The primary recovery action is verification.

---

## 30.4 Verification loading

Use:

```text
检查中…
```

with a small spinner if necessary.

Do not hide the user's current input.

---

# 31. Interaction Feedback

## 31.1 Hover

Hover should be:

* subtle;
* neutral;
* predictable.

Do not use flashy transitions.

---

## 31.2 Focus

Keyboard focus must remain clearly visible.

Use a restrained focus ring consistent with the neutral palette.

---

## 31.3 Success

Use small toast feedback when useful.

Examples:

```text
手动申请已添加
修改已保存
手动申请已删除
```

Avoid celebratory visuals.

---

## 31.4 Errors

Prefer feedback closest to the source:

* field error → inline;
* form problem → form-level notice;
* page load failure → page content state;
* destructive confirmation → AlertDialog.

---

# 32. Icons

Use a consistent minimalist outline icon family.

Requirements:

* consistent stroke width;
* consistent bounding size;
* precise alignment;
* no colorful icon system;
* no decorative iconography.

Icons support meaning; they do not define the visual hierarchy.

---

# 33. Animation

JobHunter v1 should use minimal animation.

Permitted:

* subtle hover transition;
* dialog opening / closing;
* small spinner;
* lightweight menu transitions.

Avoid:

* large motion;
* 3D;
* parallax;
* animated gradients;
* decorative micro-animation.

---

# 34. Accessibility

Implementation should preserve:

* visible focus states;
* keyboard navigation;
* sufficient contrast;
* semantic labels;
* accessible Dialog focus management;
* accessible error association;
* adequate clickable targets.

Visual minimalism must not reduce interaction clarity.

---

# 35. shadcn/ui Mapping

Prefer existing shadcn/ui primitives where appropriate.

Typical mapping:

| JobHunter Pattern          | Preferred primitive                          |
| -------------------------- | -------------------------------------------- |
| Primary / Secondary Button | `Button`                                     |
| Text field                 | `Input`                                      |
| Form Dialog                | `Dialog`                                     |
| Destructive confirmation   | `AlertDialog`                                |
| Row overflow               | `DropdownMenu`                               |
| Table                      | `Table`                                      |
| View navigation            | custom lightweight Tabs / navigation pattern |
| Tooltip                    | `Tooltip`                                    |
| Loading                    | `Skeleton`                                   |
| Toast                      | project toast implementation                 |
| Supporting sheet           | `Sheet` when genuinely appropriate           |

Do not rebuild Radix primitives unnecessarily.

---

# 36. Component Reuse Expectations

Shared components should be preferred for recurring patterns.

Likely reusable components include:

```text
AppShell
Sidebar
SidebarItem
WorkspaceTopBar
Breadcrumb
PageHeader
ViewTabs
EmptyState
LoadErrorState
InlineNotice
FormField
```

Do not prematurely create abstractions that have only one concrete use.

Generalize after a stable repeated pattern exists.

---

# 37. Page-Specific Design Rules

Page-specific behavior belongs outside this global Design System.

Recommended structure:

```text
docs/ui/
├── DESIGN.md
└── pages/
    ├── manual-applications.md
    ├── job-pool.md
    ├── resumes.md
    └── ...
```

A page document should describe:

* purpose;
* approved Stitch screens;
* page-specific information hierarchy;
* page-specific business constraints;
* applicable Contract/API references.

It should reference this file rather than duplicate global visual rules.

---

# 38. Stitch Usage

Approved Stitch designs are visual references.

When generating or editing pages in Stitch:

1. Follow JobHunter Design System v1.
2. Do not create new business capabilities.
3. Reuse existing patterns.
4. Keep all ordinary UI text in Simplified Chinese.
5. Do not introduce keyboard shortcut hints.
6. Keep Sidebar navigation consistent with this specification.

When Stitch produces an inconsistent local pattern, update the page to match this Design System rather than creating a second pattern.

---

# 39. Codex Implementation Rules

Before implementing or modifying frontend UI, Codex should:

1. read this file;
2. read the relevant page design document;
3. inspect the approved Stitch design through Stitch MCP when visual detail is needed;
4. read the relevant Product / Contract / API documents for behavior;
5. reuse existing components before creating new UI primitives.

Stitch screens are visual references.

They are not business authority.

---

# 40. Stitch-Generated Code

Stitch-generated frontend code may be used as:

* visual implementation reference;
* layout reference;
* spacing reference;
* typography reference;
* styling reference.

It should not automatically become the production frontend architecture.

Prefer rebuilding the approved design using the JobHunter project's:

* React architecture;
* feature boundaries;
* shared components;
* shadcn/ui primitives;
* API layer;
* error and recovery semantics.

Avoid copying page-generated code wholesale if it creates:

* duplicated UI components;
* hard-coded style systems;
* page-specific primitives;
* duplicated Radix functionality;
* incorrect business behavior.

---

# 41. Visual Review

A frontend implementation should be compared against its approved Stitch design.

Review:

* overall hierarchy;
* Sidebar;
* spacing;
* typography;
* column widths;
* border strength;
* radius;
* dialog dimensions;
* state positioning;
* button hierarchy;
* empty / loading / error consistency.

Do not treat “functionally works” as complete visual acceptance.

---

# 42. Prohibited Generic Patterns

Unless later explicitly accepted, do not introduce:

* marketing hero sections;
* colorful KPI dashboards;
* excessive cards;
* gradients;
* glassmorphism;
* 3D visuals;
* large company-logo layouts;
* decorative AI sparkles;
* status badges without real business states;
* oversized rounded containers;
* large shadows;
* fake analytics;
* visual clutter used only to fill empty space.

---

# 43. Change Control

JobHunter Design System v1 is frozen.

A new page should not modify this system merely because Stitch generates a different pattern.

Change the Design System only when:

1. an existing rule cannot support a legitimate product requirement;
2. a new reusable pattern has been validated;
3. the change improves multiple pages rather than one isolated design;
4. the change does not conflict with settled Product / Contract behavior.

When such a change occurs:

* update this document;
* increment the Design System version when appropriate;
* reconcile affected Stitch pages;
* reconcile shared frontend components.

---

# 44. Current Frozen Decisions

The following decisions are explicitly frozen in v1:

* Developer-tool visual direction.
* Desktop-first workspace.
* Neutral grayscale foundation.
* Compact black primary actions.
* Fixed left Sidebar.
* Primary and secondary Sidebar navigation share one active/hover system.
* Secondary hierarchy is expressed through indentation.
* No gray + black double-line selection treatment.
* Secondary navigation items may have their own icons.
* No visible keyboard shortcut hints.
* Breadcrumb is visually weak.
* Page Header is compact.
* Secondary views use text tabs + underline.
* Data-heavy content prefers tables over cards.
* Row actions use overflow menus.
* Add / Edit reuse the same Dialog/Form system.
* Required fields use `*`.
* Validation is inline and preserves input.
* Delete uses compact AlertDialog and no fake Undo.
* Empty State is text-first.
* Loading is localized skeleton content.
* Load failure is distinct from empty data.
* Revision Conflict preserves dirty input.
* Outcome Unknown never guesses success or failure.
* Conflict / uncertainty notices use restrained muted-red / dusty-rose surfaces.
* Destructive red is stronger than exception-notice red.
* No decorative visual content merely to make pages less empty.

---

# 45. Design System Summary

JobHunter Design System v1 should feel:

**quiet**

**precise**

**dense**

**professional**

**technical**

**predictable**

**restrained**

The desired result is a mature personal productivity workspace for technical job seekers.

It should look like a tool the user can comfortably keep open every day — not a recruiting portal, marketing site, or generic enterprise dashboard.
