# JobHunter 正式文档编写指导 Spec

## Problem Statement

新的 JobHunter 仓库目前只有九份已完成的 Architecture Grill 决策与设计记录，没有正式产品文档、代码、测试或已实现功能。后续文档将在多个任务和上下文中编写，仅靠重新阅读历史问答容易遗漏决定、误解文档归属，或把早期仍标为 ACCEPTED 但已经被局部替代的条款写回正式文档。

需要把最终有效设计组织成可交接、可检查的文档编写依据，覆盖产品、架构、Contracts、验收、开发和真实进度六类文档。它必须保留来源和覆盖关系，明确哪些已经决定、哪些只决定了架构边界、哪些等待后续 Contract Grill，并避免把设计、示例、研究参考或计划当成当前实现。

## Solution

产出本地文档编写指导 spec，作为后续任务的共同输入。它综合有效决定、划分文档职责、给出任务依赖和交接要求，并使用用户已确认的两个相互关联的验证 seam：

1. **Decision-to-Document Traceability Seam**：最终有效 Grill 决定 → 正式文档，验证 controlling Q-ID、supersession、覆盖、归属及暂缓／排除理由。
2. **Cross-Document Semantic Consistency Seam**：正式文档之间验证职责边界、术语、authority、状态和引用语义一致；同一设计事实不得出现多个冲突 authority。

本文件是编写工作的 spec，不是 JobHunter 产品规范、详细 Contract 或新的第七类正式权威。当前只交付本文件，不创建六类正式文档。后续遵循 Q22／S38.1：编写并评审五份正文，同时规划 Contract 结构与职责 → 独立的详细 Contract Grill → 完成 Contracts 并协调受影响引用 → 正式开发。具体路径、来源和任务交接安排见 Further Notes。

## User Stories

不适用。本工作是已决架构的文档化与跨上下文交接，不新增产品功能，不为适配模板虚构产品 User Stories。文档编写要求集中在 Implementation Decisions，验证集中在 Testing Decisions。

## Implementation Decisions

### 1. 决策解释、术语与基线

- 以九份 Grill 记录为设计输入，按条款解析后续修正；较新决定只覆盖其明确涉及的语义，不使整个早期记录自动失效，也不因早期记录仍为 ACCEPTED 就保留旧机制。先解释覆盖关系，再撰写最终行为，禁止把相互矛盾的历史段落并排当成现行要求。
- 每个有效设计事实保留来源 Q-ID／S-ID、控制性决定和必要的详细模块章节。来源说明中的旧仓库“当前”问题、旧实现完成度和迁移假设不得移植成新仓库事实。已清理的 Q-ID 可作为 supersession 证据，不能补造其原文或恢复其机制。
- Contract Design Inventory 是非规范性设计清单。对象名、示例属性、状态名和概念图不等于完整 Contract；不得逐行翻译为字段定义、接口或数据库表。模块中的示例代码目录、数字、模型配置、部署方式也不得自行升级为已决要求。
- 使用领域原名区分 CandidateProfile、PreferenceSet、EvidenceItemVersion、EvidenceBaselineSnapshot、ResumeVersion、ResumeGroundingSet、RequirementSet、两类 Fit Analysis、ChangeProposal、ApplicationPreparation 及各类审批、执行、应用事件。历史 DeepFitAnalysis 泛称必须按实际语境拆解，不能创建一个新的统一结果权威。
- 本文件的任务编号、主题分组和核对表只是文档编写组织，不新增 Domain 对象、产品要求编号、Contract ID 或业务状态。（Q2–Q5、Q11、Q22、Q26、S24.2、S29.2、S37.1、S38.1）

### 2. 六类正式文档的职责

| 类别 | 应负责的内容 | 与其他类别的边界 |
| --- | --- | --- |
| 产品规范 | 使用者、范围、非线性任务组织、入口、前提、可见结果与失败行为、非目标 | 不复制字段 Contract，不把导航等同于 Domain，不报告实现完成度 |
| 架构 | 系统分层与职责、业务 authority、依赖与数据流、事务／并发／恢复／权限／持久化不变量、Harness 与 Eval 分工 | 不以伪 schema 补齐未定细节，不把设计模块直接当成已实现服务 |
| Contracts | 后续规范性业务／数据／接口边界；当前仅规划文档结构、职责、归属及跨域引用方向 | 详细字段、类型、枚举、状态转换、API payload、数据库 schema、validation error、migration 等等待详细 Contract Grill；不固化文件数量 |
| 验收 | 能力完成需要的可观察行为与证据；正向、负向、并发、失败、恢复和权限边界；Eval 证据的含义 | 验证既定设计，不另创业务 authority；不把测试计划写成已通过，不自行决定发布政策 |
| 开发 | 文档优先顺序、来源与变更纪律、测试优先／Eval 原则、外部研究要求、任务交接和验收证据维护 | 不预选未经接受的首个实现 Slice、固定技术目录、启动脚手架或 CI 发布阈值 |
| 进度 | 真实文档／实现／验证状态、当前任务、缺口、阻塞、下一步及追溯矩阵 | 不承载目标架构正文，不凭文档或文件存在认定功能已实现，不继承旧仓库完成度 |

同一事实可以在产品、架构和验收中出现不同视角的说明，但应标明其权威归属并引用，不能分别定义不同规则。Contracts 完成前使用已决架构和明确的“详细 Contract 待定”边界，不假装规范已存在。Q32 的追溯矩阵属于进度类别；ADR 仅在未来确有独立持久理由时考虑，不新增 overview 类别。（Q2、Q5–Q7、Q11、Q18、Q26、Q32）

### 3. 产品范围与入口

- v1 是单用户、local-first 的个人求职工作区；Profile、Preferences、Evidence、Resume 和应用记录各有身份，不引入统一 Candidate Aggregate、CandidateId、租户层或推测性的 ownership 字段。
- 覆盖岗位导入／采集、确定性 QuickScreen、用户选择、DeepFit、简历优化、投递准备、外部执行与跟踪，但不是强制线性流水线。符合各自前提时能力可独立调用；Advisor 不以已完成 DeepFit 为门槛。
- 五个导航入口为“我的简历、求职资料库、岗位池、求职助手、我的投递”。DeepFit 位于岗位池；投递准备由选岗进入，没有顶层导航；“我的投递”的前往投递导向岗位池。求职助手初期只暴露简历优化对话。
- 岗位池默认平铺列表，可有 Company 聚合只读视图；公司视图不创建 Company Aggregate。采集方向、城市等由用户偏好决定，示例岗位／地区不是产品支持范围或已证明的质量范围。
- Shortlisted／PursuitDecision 不等于筛选通过、一次分析选择、开始准备或真实投递。书签／长期关注是未来独立设计，不能因旧代码存在而保留为 v1 要求。（Q1、Q6、Q8、Q23–Q24、Q53、S5.1、S5.3、S17.1–S17.4、S37.1）

### 4. Job、Preferences、QuickScreen 与采集

- 一个平台的可靠来源身份对应一个 Job；相同身份的语义内容变化创建不可变 JobVersion。当前不做跨平台合并、多 SourceListing canonicalization 或历史记录归并。
- Manual 每次创建独立来源身份；重复 URL 至多提示。缺 JD 可有 Job 根并支持人工记录／跟踪，但没有正式 JobVersion；补齐有效 JD 才产生首个版本。BOSS 自动采集只在完整详情／JD 验证后原子保存 Job 与首个 JobVersion，不保存不完整 BOSS Job。
- 一个全局版本化 PreferenceSet；所有已配置偏好都是硬约束，未设维度不受限，不创造默认偏好或多组 SearchProfiles。临时列表筛选不改 Preferences。
- QuickScreen 只使用岗位／来源元数据、精确偏好版本与筛选策略；确定冲突才拒绝，缺失信息保持不确定。不得从 Q10 的早期描述恢复 RequirementSet、Evidence、Resume 或 ScreeningProfileSnapshot 作为 QuickScreen 输入。
- BOSS 采集先获取列表并筛选；拒绝者不访问详情、不进入 Job 数据集、不保留可还原拒绝岗位的标题／公司／URL／JD。通过或不确定者继续详情获取。CollectionRun 留存运行、访问使用量、聚合拒绝原因和风险审计，不成为另一岗位事实库。
- 日常浏览与偏好变化优先操作本地持久数据；除初始偏好设置触发的约定采集外，后续平台刷新需显式动作。采集冻结开始时的偏好；新偏好立即控制本地展示与未来运行，不改写进行中规则。用户停止保留已提交的部分结果，不自动重采或删除不再匹配的岗位。
- 内容采集时间、最后看到来源、直接验证可用性的含义分开。未变内容只更新观察信息；语义变化才新建版本。陈旧不等于关闭，搜索缺席不证明关闭，关闭需要可靠来源证据且不删历史。缺 JD／新任务可用性是投影，不是统一 Job lifecycle。（Q3、Q12–Q14、Q17、Q27、Q44–Q45、Q48–Q50、Q55–Q56、Q110、Q161、S9.1）

### 5. Profile、共享 Evidence 与简历事实

- CandidateProfile 只负责身份／联系信息，以不可变版本和根 revision 管理；职业事实属于 Workspace 共享 Evidence，求职意向属于 Preferences。联系信息可用于本地渲染；联系信息、身份号码、家庭信息和原始来源文件默认不可见于模型，UI／API 可见性与模型可见性分开。
- Evidence 是经历级事实，例如一段工作或项目；保留原始段落／列表结构，不强行原子化为持久 Assertion。精细 grounding 指向精确 Evidence 版本及其内部位置；引用粒度不决定 Aggregate 粒度。新系统历史引用按原版本的 schema reader 解释，不重写旧引用。
- 每个 EvidenceItem 只有一个当前已保存事实版本；旧版本用于历史，不能任选作新正式任务输入。恢复旧文本创建新时间版本，不回退指针。Baseline 冻结当时的当前事实集合，不是第二份事实库或完整性承诺。
- 上传先产生非权威 ResumeDraft／Profile／Evidence proposals；确定性 Document／Resume parsing 恢复版式、章节、经历和原有结构，LLM 只是可选语义增强，不是从零摄取或拆成原子事实的默认 owner。解析和匹配没有合并 authority。人工审阅与 reconciliation 后 Save 才建立正式版本；原文遗漏的旧经历不自动删除。
- 正式简历所有职业事实必须得到支持或通过用户确认创建／修正事实；模糊未解决内容阻止 Save。用户有权确认自己的事实，不需要额外第三方证明或第二次事实确认。结构、目标表达、展示与职业事实的验证职责分开。
- 正式 Resume 选择完整当前经历，允许选择不同经历、排序和布局，不允许各简历独立选择 bullet 或保留另一份职业正文。正文改动版本化共享 Evidence；纯展示变更不改变职业事实 baseline。Profile 字段显示／隐私选择仍独立，不因完整经历选择而扩展。
- Evidence 保存原子更新事实、当前指针、baseline、所有受影响当前 ResumeVersion 及 grounding；同步已有事实不递归再创建 Evidence 版本。Profile 保存同样原子传播到引用它的当前简历并保留显示选择，但联系信息变化不改变职业 Evidence baseline。历史分析、聊天、已选 Preparation 输入和执行 Snapshot 不随之改写。（Q15、Q19、Q54、Q63–Q64、Q66、Q70–Q75、Q79、Q86、Q96–Q98、Q108、Q113–Q114、Q118–Q119、Q163、S15.1）

### 6. Save、删除、grounding 与派生工作

- Save 本身确认事实；删除 KnowledgeConfirmation、全局完整性确认与相关前置 Gate。我的简历／求职资料库的未保存编辑留在页面，正常离开需 Save／Discard／Cancel，失败 Save 不得伪装成功。我的简历 ResumeDraft 允许崩溃丢失，没有持久恢复或 autosave 保证。
- GroundingSet 是不可变持久派生资产，按实际依赖兼容性判断，而非整个 baseline。同一 ResumeVersion 可有多个精确 GroundingSet，按兼容输入解析，无可变 active GroundingSet 指针；版本祖先关系本身不能证明支持有效。无关事实变化不使 grounding 自动失效；但引用事实已非当前时，不能只给旧 Resume 重绑 GroundingSet 恢复新业务资格，必须使用当前事实的正式新版本。
- Candidate Fit 则绑定完整精确 baseline；职业正文变化使旧分析成为历史／stale，不做未经评估的细粒度增量影响推断。Profile-only 与展示-only 变化不能误伤不依赖它们的 Candidate Fit。
- 删除 Resume 为逻辑移除，不删除共享事实和历史；首份自动为默认，有多份可切换，删除默认须原子选择另一份，不能删除最后一份。旧聊天使用已移除简历时需显式重选。
- 从我的简历移除经历只改变该简历的选择；全局 Delete Evidence 仅由求职资料库发起。全局删除按当前简历是否直接包含 Item 计算影响，确认后原子删除当前资格、更新 baseline／直接受影响简历／grounding／必要派生意图。不建立句子／Claim 语义删除图，不退回旧版本，不更改历史 PDF 或已完成投递。
- 允许保存空资料／简历状态；缺少具体任务所需信息时在模型执行前失败。各功能必填资料矩阵等待 Contract Grill，不能在这里创造统一 Profile 门槛、经历数或恢复完整性确认。
- Prepare 完成校验、冲突处理、revision 检查、影响范围与必要派生任务计算；短 SQLite authority 事务同时提交正式变化及必要的持久派生工作意图。渲染／预览／索引／缓存留在提交后，不使用 MQ，不把网络／模型调用放进此事务。
- 派生生成按当前预览、导出、Preparation 需求触发，不要求每次 Save 预渲染全部格式。后续需求也先持久意图再执行，可复用精确来源与配置兼容工作。执行前跳过过时需求；运行中的安全计算可完成但 stale 输出不得发布为 current。派生失败影响材料就绪，不回滚已保存事实；这不是远程模型／平台调用的重试许可。（Q66、Q70–Q71、Q73、Q75–Q77、Q87、Q93、Q97、Q100、Q108、Q113–Q114、Q118–Q119、Q147、Q151–Q154、Q165–Q166）

### 7. Requirement 依赖与独立 Fit

- RequirementSet 是精确 JobVersion 的不可变持久派生资产；创建与激活分开，验证合格后可自动成为当前默认，旧消费者保留精确引用。采集只保留 JD，不触发解析。
- Application 的共享 EnsureRequirementSet 复用兼容结果，或启动独立 RequirementParse Run。LLM 负责完整精确 JD 的语义提取，确定性代码负责验证；正常一次提取，最多一次验证错误指导的修复。失败不保存不可信依赖，不给部分要求打正式分数。
- 结构验证不证明零语义遗漏；歧义保留不确定，不猜 necessity／logic。真实 JD 测试、人工检查与质量报告仍需要，但 v1 不强制离线人工标注 ParserVersion 发布认证。
- 下游 Candidate Fit、Resume Fit、岗位定向 Advisor 只消费精确 RequirementSet 作为岗位要求，不再次读取完整 JD 重新解释。无可评估 Requirement 在 Fit 前失败，不产生空集合满分，也不增加修复次数。
- 同一精确解析目标使用数据库级 single-flight／claim／CAS 保证有效唯一 producer；owner 支付，waiter 复用且取消仅影响自己的等待。owner 取消／失败／未知结果不会引发自动接管或重新解析；显式 Retry 先查已持久兼容结果。
- DeepFitBatch 先冻结已知选项，再准备依赖，最后冻结完整独立分析请求；不使用占位 RequirementSet，不静默升级选中的版本。派发前重验适用的 QuickScreen 非拒绝、来源／依赖兼容性和权限；调用后的最终校验失败保留真实调用／usage／audit，不发布无效分析。每个 Job 内可分别选择 Candidate Fit 与 Resume Fit；没有兼容保存结果的任务默认勾选，已有兼容结果的默认不勾选，显式重跑新建不可变结果。两者各有身份、Run、失败、历史和重试。
- Candidate Fit 检查当前保存且获准的 Evidence；Resume Fit 只检查精确正式 Resume 及必要 grounding 校验信息，不能借用未表达的 Candidate 事实、另一份 Resume 或 Candidate Fit 结果。两者无前后依赖、Coverage 资产、分差或分数上下界关系。
- v1 两类 Full Context Fit 均为一次结构化评估，最多一次确定性验证错误指导的修复，无自主 Evidence Tool loop；局部修复上限同时受整个 Run 的资源约束。一个任务失败不回滚另一分析或已成功生成的独立 RequirementSet。
- 沿用 MATCHED／PARTIAL／MISSING／UNKNOWN 的已决范围语义：Candidate MISSING 仅限已保存且获准资料未发现支持；Resume MISSING 仅限完整检查该简历获准内容后未发现表达。隐私排除、截断、不可验证或不完整检查应保持 UNKNOWN，不能推断现实无能力。
- 完整性检查针对实际产生 assessments 的 Frame，包括全部必要要求、获准内容纳入、引用解析与输出验证，不能仅凭 FULL_CONTEXT 标签证明 MISSING。Baseline、eligibility、实际 model visibility 是不同边界。
- 不同目标可并行，同目标只允许一个有效进行中的分析；后端也强制。当前展示为最新成功且兼容的结果；失败重跑保留旧兼容成功，stale 结果不能成为 current，不采用并发 Run 的最新用户意图仲裁。
- 模型输出 assessment，版本化确定性 ScorePolicy 推导分数；小项匹配不能抵消关键硬缺口，UNKNOWN 不能机械映射成固定低分，分数仅是排序／展示摘要。原始分析与原始评分／不可评分结果保留；显式重新评分是派生投影而非新语义分析，比较使用共同策略版本，旧 assessment 缺少新策略必要维度时不能猜分。有效分析可以没有可比较总分，不能记零、继承旧分或进入普通数值排序；权重、阈值和表示方式仍待定。（Q10、Q14、Q35、Q40、Q46、Q51、Q58–Q59、Q72、Q76、Q82–Q83、Q110–Q117、Q121、Q142、Q168、Q171、S22.1）

### 8. Advisor、Session 与正式修改

- 同一 ResumeAdvisor Skill 服务普通与 Preparation 入口，统一 ChatSession；每次从 Preparation 进入创建新聊天，传递明确引用／意图，不引入 targeted Session 兼容性机制或第二个 Agent。普通模式不凭岗位方向推断具体 Job。
- Advisor 可选复用当前兼容的 Candidate／Resume Fit 结果，二者都不是前提；逐 Requirement 对比只能是临时优化提示，不持久化为 CoverageAnalysis。一般简历优化不要求具体 Job／RequirementSet；岗位定向优化通过共享 Ensure 获取依赖。
- 讨论／读取上下文遵循当前显式请求、Session 已显式采用对象、来源 Preparation、Workspace 默认的既定规则；默认变化不静默切换已有讨论。没有任何正式简历时在 Run 前给出导入／创建引导。临时聊天文件优化不在 v1。
- **正式 apply 的目标规则单列**：当前指令显式目标，否则 Workspace 默认。不能把讨论上下文的简历优先级当成 apply 授权，也不推断额外 suggestion-source Resume。读取实际目标精确版本，生成该目标自己的 before／after ChangeProposal；不得仅替换 ID 移植 patch 或复制未请求经历。
- 用户刚陈述的 Session 事实可立即用于讨论和 Suggestion，引用可验证的 SessionContextRef／UserTurnRef；它们不是 Evidence，也不自动成为 Memory 或正式 Fit 输入。普通讨论不反复触发 Save 提示；模型不能伪造 Session 来源或确认。
- Advisor 没有 ResumeDraft、持久 working draft 或草稿导出路径。ChangeProposal 是不可编辑、不可独立导出／投递的操作预览，展示目标／版本／默认来源、具体修改、共享事实和其他当前简历影响。一次确认只授权该完整修改；目标、patch 或 revision 变化必须重新预览。
- Proposal 生成／展示结束其 Turn／Run。后续由 Application 验证并执行精确已确认操作，不再调用模型解释同意；不占用旧 Run 等人，也没有第二次草稿 Save。后续对话使用新有界执行。
- 每个 Session 最多一个活跃前台 Turn，新输入排队或显式停止前一 Turn；不同 Session 与合法独立辅助／依赖／后台执行可并行。等待独立 RequirementParse 时同一前台 Turn 保持活跃但释放模型执行容量，保留总 deadline／cancel，不模型轮询、不自动 producer 接管。
- Application 已提交的 mutation result 不因后续回复失败回滚；UI 区分“已保存”与“回复未完成”。同一已确认 Proposal 幂等识别已提交结果，不重复产生版本。流式文字说已保存不是提交证据。
- 删除 Session 原子仲裁 pending Proposal 确认／失效，并取消活跃前台；旧 ID／恢复页面不能重新执行未确认动作。已经提交的正式事实、结果和历史保留。
- 回到 Preparation 是另一显式的 Resume-only CAS 采用动作，保留 Greeting 和其他并发修改；冲突需加载当前状态并显式重新采用，不授权外部执行。（Q24、Q41、Q47、Q52、Q85、Q88–Q89、Q91、Q93–Q94、Q96、Q108、Q128、Q133–Q134、Q138–Q139、Q143–Q144、Q146、Q148–Q149、Q155–Q156、Q158–Q159、Q167、S17.3）

### 9. Preparation、材料、外部执行与跟踪

- Preparation 是可编辑、受 revision／CAS 保护的 Job／channel 准备根，没有每次编辑的不可变历史。它展示／选择正式渲染 Resume，不编辑简历正文。再次进入默认恢复未完成准备，保留选择与手动 Greeting；重复请求不重复创建，多项候选需用户选择，显式新准备／再次真实投递另建链。
- Greeting 属于 Preparation，一个固定通用默认文本，允许手动编辑；不做岗位／公司／简历／Memory 个性化，不调用模型，不创建独立 Aggregate、模板库或版本系统。
- 渲染必须实际可见后才能确认材料。MaterialApproval 绑定用户实际看到的冻结 artifact／hash／来源以及实际 Greeting，不只绑定简历名称或版本。编辑 Greeting 需重新确认；更换材料要验证兼容性，hash 相等也不能绕过当前事实资格。
- 不可变 ExecutionSnapshot 冻结将要使用的精确输入，但不授予执行权。ExecutionApproval 是范围绑定、有期限、单次使用的执行授权，最多被一个 Attempt 消费；MaterialApproval 不可替代它。
- 批量投递只是交互与调度，每个 Job 的准备、Snapshot、Approval、Attempt 和可选真实记录各自独立。部分继续需新的较窄授权；未知外部结果无成功事件且不能自动重试。未派发成员不能标为已失败或已投递。
- ExecutionEvent 描述技术动作／观察；ApplicationEvent 只在可靠渠道回读或明确人工报告建立真实业务事实后产生。点击发送不等于已投递，人工报告不虚构 Executor 历史。
- ApplicationRecord 代表一次真实 Job／channel／account 投递尝试，再投递新建记录。事件追加、去重、区分发生／观察时间，纠正／撤回通过新事件；进度由版本化策略投影，不是第二个可写状态权威。面试先以结构化 ApplicationEvents 表达，不新增 Interview Aggregate。
- Executor 的必要实时身份／可用性检查不得隐式刷新 JobVersion、生成 RequirementSet、更换 Snapshot 或增加 LLM 岗位分析；明确不匹配／关闭则停止，显式刷新／重新准备另走流程。（Q7、Q16、Q21、Q25、Q30–Q31、Q36–Q37、Q42、Q77、Q91、Q146、Q150、Q157、Q162、Q164）

### 10. 平台安全、来源研究与适配器

- Collector、Browser Executor 和未来若实现的 Monitor 在每次平台访问前共用按 platform／account 持久化的 PlatformAccessSafety。容量、风险与操作许可共享，但各 workflow、budget、approval 和恢复责任不合并。
- 普通页面／selector／浏览器故障不自动视为账户风险；可预测容量可按策略恢复，强风险需用户处理并显式恢复，不能靠 cooldown 自动解除、换账号／页签或提高并发绕过。
- BossHunter、boss-zhipin-scraper 和 Resume 优化开源项目只能作为研究／实现输入；第三方来源先验证为 adapter DTO，有明确消费者才进入最小 canonical 边界。第三方数据存在不意味着 model-visible。
- 在详细相关 Contract／渠道验证设计前，研究任务须固定来源 commit、核对许可与维护情况、做 source→adapter→canonical 映射。Grill 中的访问次数、延迟、冷却值与第三方行为不是官方限额或冻结默认值。此次文档编写不补做未授权的新产品／架构决策，也不声称这些研究已完成。（Q3、Q27、Q31、Q36、Q49、Q126、Q160、Q164、S7.1）

### 11. Harness、Tools 与模型调用责任

- 共用 Harness，RequirementParse、CandidateJobFit、ResumeJobFit、ResumeAdvisor 各有静态 Skill Contract；MemoryExtraction 是独立 headless Skill。一个 Run 承载一个有界语义任务，岗位任务绑定一个精确 Job；独立 Fit 不能塞入一个 Run。
- Application 负责依赖准备、batch 编排、完整输入冻结、业务验证与结果保存；Harness 负责执行、Context、权限、预算、取消、恢复和审计，不拥有事实写权。
- ToolRegistry 注册不等于授权；有效 actions 由 Registry、Skill allowlist、Context 策略及当前 runtime permission 共同限定。只暴露 typed scoped Business Actions，没有通用 Shell、SQL、文件、HTTP 或模型自主浏览器操作面。
- 调用前验证 action、参数、对象、scope、Run authority 和所需批准，结果进入 Frame 前重新做隐私／scope admission。模型参数、JD、网页、ToolResult 或引用中的指令不能扩权。Tools 不偷偷扫描聊天猜意图。
- ResumeAdvisor 自己负责优化，不另建 suggest_improvement Tool。已决 job.requirements.read 是纯读取；缺依赖交由 Application EnsureRequirementSet，不在 read 中隐藏模型调用、另一个 Run 或资产创建。其他示例名称不得冻结成完整目录。
- AgentRunRuntime 管理 Run 生命周期／ownership；ModelInvocationRuntime 是所有业务 Provider 调用的唯一执行入口，覆盖主调用、repair、compaction、rescue、MemoryExtraction。ModelGateway 只做 transport adaptation；ToolInvocationRuntime 管理 Tool admission 和 replay。
- SDK／Gateway 无透明 retry 或自动 model／Provider fallback。所有允许的新请求重新计数、预算准入、持久派发与审计。独立 Eval Judge 不是业务调用漏记的例外，而是另一个明确的 Eval 执行责任。（Q47、Q120–Q122、Q126–Q127、Q128、Q135、Q138、Q140、Q142–Q144、Q176、S7.1、S17.4、S22.1）

### 12. Context 精确性、容量与 compaction

- Advisor 主要 LAZY_TOOL：起始控制、当前／近期 Session、获准 Recall、Tool 定义；Preparation 引用不等于已注入业务正文。RequirementParse 与两类 Fit 使用 Application 冻结的 EAGER_EXACT 输入；v1 Fit 无自主 Evidence Tool loop。
- ContextPackage 是不可变初始 scope／policy／input／capability manifest；每次 ModelInvocation 绑定实际发送内容的独立不可变 ContextFrame。后来读取或合法写入返回的精确版本经 admission 追加为 runtime input，不改写历史 Package／Frame。
- 懒读取第一次解析后固定精确版本，后续不跟随 latest；本任务授权写入可明确追加已提交版本，无关并发变化不能静默升级。Q158 的实际 Proposal 流程不会为了确认而保留或复活生成它的旧 Run。
- 预算检查使用实际序列化输入与 control／Tool／output reserves／margin。v1 完整获准输入装不下则调用前明确失败，不裁剪事实、不自动换模型、不启用尚未实现的 RAG；可行的另一独立 Fit 不受牵连。
- Context Engineering 独立于 Memory：先区分 protected exact 与可压缩内容，再 externalize ToolResult、缩减历史窗口、确定性 micro-compaction，仍不足才做有界语义 checkpoint；trigger 与 target 分开但数字待定。
- 正常语义 compaction 是当前 Run 的辅助 Invocation，共享预算／deadline／fencing／恢复，整个 Run 最多一次；明确 Provider size rejection 的 reactive rescue 最多一次。所有 local allowance 仍受总预算约束，步骤推进不能重置次数；timeout／未知结果不能改称 size rejection。
- checkpoint 先验证并持久发布再进入新 Frame，失败保留原可恢复来源。不得以摘要替换 protected 输入或删除完整 Session；旧 LAZY_TOOL result 可外置并按精确版本新读，但不是伪造旧 ToolResult。
- 长期 Memory 直接块不进入 checkpoint，逐 Frame 动态 Recall；v1 不承诺清除真实 assistant 历史中的间接影响。
- 初始排除遵循 UNKNOWN 语义；冻结后 protected EAGER_EXACT 权限撤销则终止该任务，不缩小同一分析继续运行，不再让 repair／Frame／Tool 消费撤销内容或发布新 current Analysis。新 scope 需新任务，历史已传输事实不能撤回。（Q19、Q72、Q80–Q83、Q94、Q121、Q123、Q132、Q134–Q136、Q138–Q139、Q143、Q172、S24.1）

### 13. Budget、Recovery、Storage

- 一个共享 Budget Runtime 服务不同 owner：前台 operation、独立 BackgroundMemoryBudget，Run 还有调用／token／step／deadline 等局部限额。每次收费／受限 Invocation 原子检查与 reserve，结算实际使用；已结算与 outstanding exposure 都从可用量扣除。复用 RequirementSet 不重复计解析费。
- 预算、Provider headroom、运行容量和平台安全不是同一资源。后台提取服从前台优先，合并多个 Turn 不向最后一个 Turn 记账；当前 Run compaction 记当前 Run。金额、阈值、分配、overrun 与 unknown reconciliation 细节留后续。
- 远程调用前持久提交 dispatch intent；完整 response 持久后才能继续本地 parse／validation。intent 后无完整 durable response 属未知结果，即使可能尚未真正发出也不静默重放。已持久 response 可恢复本地处理，不另调模型。
- Run ownership／generation fencing 阻止取消、超时、旧 owner 的迟到写入；startup reconciliation 在持久边界恢复安全工作或结束未知任务并释放目标槽位。释放槽位不等于远程停止或清零成本。显式 Retry 新建 Run，重新准入且保留旧不确定费用。
- LangGraph checkpoint 只恢复流程状态，不是远程动作回执。Tool replay 必须由具体 action 语义证明，不能由名称或通用框架授权。已提交 canonical 结果恢复时按幂等处理，不重复产生资产。
- 四层分别为 Business Durable Assets、受保护 Recovery Payload、轻量 Audit Metadata、最小 Operational Logs／Telemetry；不是四个数据库要求。必要精确 payload 留给活跃恢复依赖；终态历史来源可按独立 retention 清理，留下诚实 availability／hash／lineage，不用当前资产重构冒充旧 Frame。
- 不把 HTTP 秘密、完整 Resume／Evidence／prompt／response 放进普通日志。业务历史不因 payload 清理或聊天清理消失。持久化不等于 model admission，历史可读不等于当前业务资格。
- 流式 deltas 是临时展示，不是正式 Turn、Suggestion、MemoryExtraction source 或提交证据；不强制保存，不拼接到 Retry。前端断线不自动取消健康后端，重连可读最终完整结果。（Q83、Q116、Q122–Q125、Q130、Q132、Q135–Q136、Q140–Q142、Q147、Q156、Q165、S24.2）

### 14. Collaboration Memory

- 区分 Business Authority、持久 Session、Long-term Memory、派生 Memory retrieval；Context Engineering 不属于 Memory 层。Memory 只保存获准的协作偏好、反馈、工作方式及可复用协作学习，不保存职业 USER_FACT、求职搜索偏好或申请事实。
- 事实依据、动作权限和交互风格是三条规则；当前显式指令可覆盖本次交互风格，却不授权改事实或免审批。一次性要求留 Session，不自动成为长期偏好。
- Auto Learning、Recall、显式 View／Add／Edit／Delete／Clear All 三者独立。关闭学习不停止 Recall，关闭 Recall 从下一 Frame 停止 Memory 输入但不删已存条目；管理走确定性校验，不需要 extraction。启用不默认回扫停用期／历史聊天。
- 完成且持久的用户 Turn 产生持久 pending 来源；合并／延迟触发独立后台 Extraction，不依赖 Session-ended、每 Turn 固定调用或进程 timer 作为 authority。提取仅建议，确定性 admission 判断；需可追溯的明确长期用户表达／纠正，assistant 推断、重复行为、summary 本身不够。
- Parse 与 Fits 不读取长期 Memory；Advisor 默认只获准协作偏好／反馈／工作方式，不能因可存 reusable learning 就自动读取该类。未来 General Assistant／面试 Skill 的例子不扩展 v1。
- 遗忘使新 Context 和派生索引不再使用条目，并阻止旧来源自动复活；迟到提取不得覆盖较新的人工管理。之后真实的新长期指令可重新准入，不把人工编辑变成永久锁。
- 失败／未知提取批次与较新来源隔离，不能阻塞后来工作、假记成功推进 cursor 或自动混进新批次；显式 Retry 才处理旧失败范围。未派发的预算等待仍是 pending。
- 删除源 Session 阻止新提取及迟到候选发布，在 dispatch／publish 重新检查；已接受 Memory 生命周期独立。删除不能撤回已发送内容或抹去真实费用／恢复审计。（Q52、Q127–Q131、Q133、Q137、Q139、Q145、Q169–Q170）

### 15. Eval 与观测的正式文档分工

- 架构写清 LangGraph 执行与 self-hosted Langfuse 的选定方向：Langfuse 负责通用 Dataset／Experiment／Evaluator／Score／比较／观测，JobHunter 保留薄 task adapter、真实 Application／Domain／Repository／Harness 路径和 domain-aware checks；不另建通用 Eval 平台或测试专用 Agent。
- 验收写清 outcome、trajectory、Tool、Context、grounding、authorization／safety、reliability、efficiency 各自证明什么。事务、权限、CAS、预算、recovery／fencing 优先确定性测试和受控故障注入，语义质量使用适当人工复核／校准 Judge；引用存在不等于语义支持。
- 每个 Trial 从隔离的不可变 fixture 重建，允许真实测试 DB 提交，但不得写用户 live Workspace 或发生真实招聘平台副作用。冻结 Dataset、business fixture、Scenario events／expectations、Skill／Prompt／Context／Model／Evaluator／Rubric／Runner 配置；缺失或 hash 不符明确不可复现，不回退 latest。
- Dataset 按 Skill 区分 development／holdout，案例保留 positive／negative／boundary／regression 含义，不冻结示例名称或数量。Holdout 若用于定向调优需披露污染。Recorded replay 的确定性机制证据与 live-model 行为证据分别报告；精确输入可复现不承诺远程模型输出相同。Pass@1 表达单次体验，重复 Trial 衡量稳定性而非挑 best-of-N；Trial、Run 内 repair 与用户 Retry 不混计。
- 局部会话问题优先 N+1：冻结历史消息及连贯业务／runtime 边界，只运行下一输入，不重放历史模型／Tool／mutation，也不声称证明了前 N Turn。跨 Turn／Proposal／确认／并发／撤权用薄确定性 Scenario Driver、固定 authored inputs 与逻辑 checkpoint，不用 sleep 或生成式 User Simulator。
- Driver 只能确认实际产生且唯一匹配的 Proposal，通过正式 Application 接口；不得补写 DB、虚构 consent 或帮 Agent 补齐缺失前提。Q158 的生成 Run 结束语义在 Eval 中相同。
- 任务结果与每个 check 的结论分开；预期拒绝可能正确，违规、证据不完整和 evaluator error 不能混为一类。失败 Judge 不抹去有效确定性发现，不漏掉失败／不可评估样本，Q168 无分数不算零。
- Hard Gates 不能被平均质量抵消；质量、稳定性、成本、延迟分别报告，绝对目标与相对回归分别判断。Q117 的 ParserVersion 认证仍暂缓；不冻结 release ladder、默认启用、Trial 数、阈值或全仓 CI 发布政策。
- Judge 是独立 Eval execution／budget／model／rubric，评估已发生结果，不写 Domain、不影响原 Run 成败，不把 Judge 成本混入业务性能。不得声称 Langfuse Judge 自动继承业务 Runtime 的 reserve／fencing 保证。
- Langfuse 只派生观测，本地 canonical 状态决定提交／Invocation 完成／结算／恢复。上传失败不能回滚业务或重放调用。callback 与显式 SDK 同样 export 前脱敏，以 canonical ID 关联包括辅助调用在内的观测，避免重复计数；不另建泛化 Telemetry Port。
- 缺必要证据为 incomplete；若本地 canonical 证据足够，单纯缺 span 不自动使 check 失败。self-hosting 不授权复制全量敏感 payload；evaluator 按任务范围获得证据，Resume Fit Judge 同样不能从 Candidate Knowledge 补事实。
- Agent 输入、evaluation reference、Scenario control 分开；未来 Turn、期待答案、rubric 和历史 Trial 分数不能进入被测 Agent。Judge rubric 是控制，候选输出和 Tool 文本是待评证据，不能改评分规则。
- 允许满足语义／grounding／行为约束的多种正确结果，不把唯一措辞或工具顺序当标准；精确 ID／版本／授权仍严格。Skill-only 与 composed workflow 的执行范围、依赖失败、未执行阶段与成本要分别声明，不作虚假的端到端质量声明。
- 回归保留经复核、保持失败机制的最小脱敏／合成 fixture，原始敏感 payload 生命周期独立；若不可保留可执行 fixture 则明示覆盖缺口。新 evaluator 可重评同一 Trial 的实际留存结果／post-state，不重跑 Agent；缺证据不能静默 fresh execution。
- 普通可比较 Advisor Trial 冻结隔离 Memory／Recall 并控制未脚本化后台学习；Memory 专属 Scenario 显式驱动真实学习，费用／结果独立。关闭学习的实验不能声称测过 Extraction。平台 SDK／部署能力须在后续实际版本上核实，现有研究附录不等于已部署。（S35.1、Q117、Q173–Q187、S37.1）

### 16. Contracts 只规划结构、职责与边界

按真实 authority／消费关系组织候选文档族，以下不是最终文件列表，也不要求一族一文件：

| 候选职责族 | 应承接的已决边界 | 跨族引用方向 |
| --- | --- | --- |
| 共用身份／版本／引用／并发／准入 | 根与版本、精确引用、CAS、幂等、来源、隐私与兼容性原则 | 其他族引用，避免复制出互斥规则 |
| Workspace／Profile／Preferences | 单人范围、默认简历、身份联系与搜索偏好权威 | Resume 引 Profile；collection／QuickScreen 引 Preferences |
| Evidence／导入／baseline | 经历事实、提案与保存、当前版本、删除和快照 | Resume／Candidate Fit 引精确事实；导入 adapter 不越权 |
| Resume／grounding／Proposal | 正式展示、原子同步、讨论来源、目标 patch、确认与 mutation result | 引事实；向材料提供正式版本；Session 失效需协同 |
| Jobs／collection／平台安全 | 来源身份、完整性、版本、筛选、运行与共享访问风险 | Requirements 引 JobVersion；执行访问共用 safety |
| Requirements／Fits／评分与 batch | 共享依赖、独立分析、exact scope、可评分性、结果与编排区别 | 引 Job、Evidence／Resume、Harness 运行，不创建事实 |
| Materials／Preparation／Execution／Application | 渲染、readiness、两种 approval、Snapshot、Attempt、真实事件和进度 | 引正式材料与渠道验证；技术执行不直接写业务进度 |
| Harness／Skill／Invocation／Tools | bounded task、权限、唯一业务模型入口、replay、fencing | 通过 Application Ports 操作；无 Domain authority |
| Context／Session／Memory | 源与实际 Frame、acquisition、compaction、独立记忆控制 | 使用精确业务引用，不改事实或授权 |
| Budget／Recovery／Storage／派生工作 | owner／reserve、持久边界、四层 retention、safe derivative intent | 与 Run／Application 共用边界，不把 safe replay 扩到外部副作用 |
| Eval／observability | fixture／scenario／evidence／judge 分离及派生观测 | 引业务与 runtime 的规范，不成为新的生产 authority |

此阶段只记录各族负责什么、不负责什么、引用谁，以及哪些具体问题等待 Contract Grill。包括被 Grill 点名的现有属性也不得在本轮扩成类型、枚举或 payload。后续 Contract Grill 才确定字段、验证错误、迁移／新系统演化细节等；legacy migration 不因列入待定类型就成为需求。（Q2–Q5、Q11、Q26、S24.2、S29.2、S37.1）

### 17. 开发、验收和真实进度

- 开发文档承接已决的测试优先／TDD、确定性边界测试、真实路径 Eval、Slice 验收与追溯更新原则，不假设测试命令、代码目录、技术栈版本或首个 Slice 已存在／已选定。Grill 对 LangGraph、self-hosted Langfuse、相关 SQLite 事务的明确选择可写为目标，不能外推整个应用技术栈。
- Q32 的将来统一检查入口可规划唯一 ID、引用与必要映射检查，但不声称脚本已存在、已运行或已通过。Q175 未决定的全仓 CI／发布政策保持暂缓；机械文档检查不替代它。
- 正式 Contract 要求以后获得稳定 ID，进度矩阵关联实现、测试／Eval、证据与真实状态。在 Contract 尚未完成时保留 Grill Q-ID 设计追溯及“详细 Contract 待定”，不虚构已发布 Contract ID／实现路径／测试证据。
- 初始产品实现与测试均未开始；已完成的是 Architecture Grill 和记录移交。本文件完成仅意味着文档编写指导已产出。后续文档任务完成、文档评审通过、Contract 完成、产品能力已实现必须分别记载。
- Planned／Deferred 表示目标和有据可查的暂缓；Partial／Implemented 必须有实际实现与验收证据，不可由描述详尽、文件存在或旧系统证据推导。（Q4、Q22、Q26–Q27、Q32、Q117、Q175、S37.1、S38.1）

## Testing Decisions

### 1. 验证对象、先例与证据标准

当前没有可复用的测试套件、实现 seam 或运行结果。可复用的验证依据是原始 Grill 的 Q-ID、模块中的 Verification implications、Eval 设计中的证据边界，以及 Q26／Q32 的追溯原则；它们都是待落地标准，不是通过证明。

本次验证本文件是否足以指导后续编写；后续任务用相同的两个 seam 验证实际正式文档。二者都检查对外可读的文档内容与来源语义，不测试编辑器内部过程，不以关键词命中、字数、Q-ID 出现次数或文件存在代替语义正确。机械检查可以发现漏引、无效锚点和重复 ID，最终是否被错误解释仍需逐条语义复核。

### 2. Decision-to-Document Traceability Seam

**方向：最终有效 Grill 决定 → 正式文档；反向检查文档规则是否有有效来源。**

为每个有效条款维护编写追溯：原始 Q／S、存续语义、控制性 Q／S、局部 supersession、主责文档及章节、其他消费／引用位置、验收对应项、待定或排除理由。文档间共享 Q-ID 不代表可以复制成多套规范。每条记录可以拆成多个存续／替代条款，不能一条一勾而掩盖内部冲突。

检查方法：

1. 以 Further Notes 的来源基线、覆盖索引为入口，回读原记录和相关详细模块，逐条确定最新有效含义；必要时对同一早期记录拆条。
2. 向正式文档定位具体章节／规则／验收项，判断是已写入、仅引用、待详细 Contract、明确非目标、或仅历史维护记录；每个缺口说明原因。
3. 反向检查新增规则：能否定位到有效设计来源或明确的文档组织安排；示例、研究候选和未接受推荐不能成为规范。
4. 验收和进度分别链接预期证明与真实证据，不能把验收计划填写为通过，也不能从待定 Contract 推导已实现。

**通过条件：**所有现存 Q／S 及详细模块的有效内容都有处置；所有产品／架构规则有可追溯来源；局部替代有控制性引用；没有被恢复的 REJECTED／SUPERSEDED 机制；暂缓／排除均有原因和合适归属。Q-ID 的机械完整只是必要条件。

本 spec 的覆盖索引是后续编写入口，不等于完成的正式文档 Traceability Matrix。未来补充实际落点时保持原 Q-ID，不重新编号历史。

### 3. Cross-Document Semantic Consistency Seam

**方向：正式文档 ↔ 正式文档。** 使用上一个 seam 的共同设计事实和 Q-ID 关联同一主题的所有落点，再比较它们表达的含义。

检查以下文档交界：

| 比较位置 | 通过条件 |
| --- | --- |
| 产品 ↔ 架构 | 入口、独立能力、数据前提、权限、用户确认与失败行为相同；导航不创造 Aggregate |
| 架构 ↔ Contract 规划／未来 Contracts | 唯一事实 owner、依赖、输入范围和事务边界一致；规划不伪装为已定 schema；详细 Contract 完成后反查五份正文 |
| 产品／架构 ↔ 验收 | 测试证明最终行为和否定边界，不测试旧机制，不用 Eval 重新定义业务成功 |
| 架构／验收 ↔ 开发 | 测试／实现顺序与职责吻合；禁止隐藏 retry、测试专用 Agent 或未经决定的发布阈值 |
| 所有目标文档 ↔ 进度 | 目标、待定、已编写、已评审、已实现、已验证的含义分开；没有虚假完成声明 |
| 各引用落点 | root／version、历史／current、authority／derived、资格／可读性、状态／投影／事件的含义一致；不把别处的示例当规范 |

**通过条件：**同一设计事实没有冲突 authority；术语同义与不同义均明确；跨文档引用可以找到适用来源；架构边界与验收预期相符；详细未定事项一致标注，不在某个文档暗中定案。未来目标路径尚不存在时显式标注为计划，不伪造可用规范链接。

两个 seam 分别报告结论：引用正确不保证语义一致，文档彼此一致也可能一起写错 Grill。任何一个不通过，都不能以另一个通过抵消。

### 4. 必查语义回归样例

下表是最低检查集，不替代全部记录审阅。检查实际肯定语句与行为语义，允许在“历史／禁止／被替代”说明中出现旧术语，不能粗暴 grep 禁词。

| 易被误写的旧含义 | 最终应表达的语义 | 控制来源 |
| --- | --- | --- |
| QuickScreen 依赖 RequirementSet 或 Candidate 能力快照 | 元数据＋精确偏好／策略；采集不解析 Requirement | Q56、Q110 覆盖 Q8／Q10 等早期输入假设 |
| Manual 与 BOSS 都保存不完整 JobVersion | Manual 可仅根；BOSS 完整后原子创建根与首版本；JobVersion 含义统一 | Q44、Q48–Q49、S9.1 修正 Q17 |
| 上传立即产生正式 Resume | 先 Draft，grounding 完成并原子 Save 后正式版本 | Q70–Q74 覆盖 Q63 导入条款 |
| 旧 ACCEPTED 的 confirmation 字样仍产生完整性 Gate | Save 确认事实，无 KnowledgeConfirmation | Q113 覆盖 Q66／Q72／Q73／Q85／Q97／Q108–Q112 等 |
| Resume 有私有事实／可自由选择历史 Evidence／独立 bullet | 共享当前经历、时间版本、完整经历选择 | Q63、Q108、Q163 |
| 事实改动后手动刷新简历，或只重绑旧 GroundingSet | 原子传播所有受影响当前简历；历史不动，不能重绑救回旧事实的新用资格 | Q108、Q114、Q118–Q119 覆盖 Q64／Q70／Q77／Q87 等局部条款 |
| Advisor 保存持久 working draft，之后 export／apply | 讨论＋Suggestion＋目标 Proposal；一次确认即正式 commit | Q108、Q146、Q148–Q149 覆盖 Q41／Q85／Q94／Q138 等 |
| apply 自动沿用聊天／Preparation 简历或推断 source Resume | 当前指令目标，否则默认；读取目标并为它新建 patch | Q146、Q149 对 Q93 的 scoped override |
| 明确 apply 指令可免具体预览；旧 Run 等确认后继续 | 预览目标／patch／共享影响，一次确认；生成 Run 已结束 | Q146、Q148、Q158 对 Q133／Q134 的 scoped refinement |
| 删除一个简历经历等于全局事实删除 | 我的简历移除选择；资料库全局删除，直接 membership 传播 | Q151、Q153 |
| page Draft crash checkpoint 或 Advisor draft recovery | page 未保存状态可丢；pending Proposal 持久但删除 Session 后不能确认 | Q146、Q166–Q167 |
| 一个 DeepFit Run 计算两轴／Coverage 与分差 | 两类独立 Skill／Run／Analysis、四态各自限域，无分数排序关系 | Q112、Q115、S22.1 |
| 空 Requirement 得到满分；无总分等于失败／零 | 无可用目标在 Fit 前失败；有效 assessment 可无总分 | Q168、Q171 |
| 较新并发分析意图仲裁 current | 同目标串行，最新成功兼容结果；失败保留旧成功 | Q116 |
| Full Context 超限自动 RAG／摘要／换模型 | v1 调用前明确失败；Agentic RAG post-v1 | Q121、Q123、Q132、S24.1 |
| Context 来自存储所以全部默认注入／跟踪 latest | Advisor lazy pinning；headless eager exact；每次 Frame 表示真实可见输入 | Q83、Q94、Q139、Q143 |
| read 缺依赖时暗中解析 | pure read 返回缺依赖；Application 独立 Ensure，owner 支付 | Q142、Q144、Q159 |
| Memory 与 compaction 合一，开关同时控制学与读 | Context 独立；Auto Learning／Recall／管理分开 | Q132、Q139 对 Q127／Q137 的局部修正 |
| 失败 Memory range 自动折入新批／删除源仍能发布 | 旧失败显式重试且不堵后来范围，删源禁止新学习发布 | Q169–Q170 |
| intent 后无 response 可自动重放，SDK 隐藏 retry | outcome unknown，显式新 Run；所有业务调用经 Runtime | Q122、Q135、Q140 |
| 每个 loop 更新 repair／compaction／rescue 次数 | 已决局部上限和 Run 总限额共同约束，不刷新 allowance | Q121、Q135 |
| 自动预渲染每格式；safe derivative 恢复可用于平台／模型 | 必要需求先存意图，过时可跳过；安全派生与远程未知重试分开 | Q147、Q152、Q165 |
| 冻结后撤权删掉输入继续原 Fit | 结束受影响 frozen task，新 scope 必须新任务 | Q172 |
| 只认 ResumeVersion 的材料确认就是执行授权 | 实际可见冻结 artifact／Greeting 确认；ExecutionApproval 独立 | Q30、Q150、Q157 |
| 强风险冷却自动恢复／执行检查隐式刷新 JD | 持久共享 safety、用户恢复；检查与刷新流程分开 | Q160、Q164 |
| Langfuse span 或 Judge 决定业务成功 | 本地 canonical 结果；Judge 独立、受限证据和费用 | Q174、Q176、Q184 |
| Eval unique golden text、N+1 重放历史、全 Dataset 入 Context | 合法语义替代、连贯边界只运行下一步、参考与控制隔离 | Q178、Q180、Q183、Q185 |
| 1／3／5 Trial、统一 release gate 是已决定标准 | 数量、阈值、默认启用、CI 发布政策留后续；Q117 不变 | Q175 覆盖早期 Eval 提案 |
| 旧架构迁移顺序／旧完成度约束新仓库 | 五份正文先评审，后 Contract Grill／Contracts／开发；重新建立真实状态 | Q4、Q22、S37.1、S38.1 |

### 5. 本次交付与未来验收的区分

本次完成条件：默认模板七个章节齐全；用户确认的两个 seam 保留精确名称与各自条件；六类文档有职责与可交接任务；179 条现存 Q／S 可在覆盖索引定位；局部覆盖与排除可追溯；没有详细 Contract 定义或虚构实现；仅生成指定本地 Markdown，原始九份记录不变。

后续每次文档交付应附两项 seam 的实际核对结果、改动位置、尚未关闭的真实问题和下一步。最终五份正文评审必须同时通过两项 seam，才进入详细 Contract Grill；此处的“通过”只证明文档一致，不证明产品、测试、Eval 部署或发布就绪。Contracts 完成后再复核受影响正文、验收和进度。

## Out of Scope

- 此次直接编写六类正式文档、启动 Contract Grill、实现代码／测试／Eval 服务、部署、执行招聘网站访问或外部投递。
- 重新进行 Architecture Grill，接受此前未接受的 Q188–Q192 建议，替用户补选首个 Slice、完整技术栈、实现目录或 bootstrap。
- 提前定义 Contract 字段、类型、枚举、详细状态转换、API payload、数据库 schema、validation error、migration；把 inventory、概念字段、示例数字或代码布局提升为规范。
- 恢复 REJECTED／SUPERSEDED 机制；包括历史 Overlay／可选旧事实、KnowledgeConfirmation、ResumeCoverage、Advisor working draft、旧式 targeted Session、ScreeningProfileSnapshot、持续 Assertion authority、分版本撤回 UI 等。
- 扩展 v1 到跨平台 Job merge、Company／Candidate／Interview 新 Aggregate、多租户、多组 SearchProfile、书签 UI、General Assistant／面试 Skills、个性化 Greeting、动态插件市场、通用 Shell／SQL／HTTP Tools、完整 Candidate Agentic RAG 或复杂 Memory graph／全历史扫描。
- 将未来平台 Monitor 的 safety 约束写成必须实现 Monitor；把平台访问数字视为官方规则；把研究资料写成已核实当前依赖能力。
- 强制旧代码兼容、历史旧库迁移、双运行、旧测试／Eval fixture 必须映射继承。新系统资产的历史可解释性仍是要求，不能与不迁移旧系统混为一谈。
- 冻结 Eval 阈值、Trial 数、默认启用或 release／CI 政策；恢复强制人工标注 ParserVersion 发布认证。
- 发布 GitHub Issue、调用外部 issue tracker、添加 ready-for-agent 标签、修改或清理 Grill 原始记录。

## Further Notes

### A. 输出与来源基线

唯一当前交付路径：`.scratch/document-authoring-spec.md`。本文件保持 to-spec 默认七个二级章节；因用户明确限定文档体系工作，User Stories 不扩写。用户已确认验证方向，并要求拆成这里保留的两个 seam；无需再次就同一验证方案征求确认。

本地来源快照日期为 2026-09-18，九份文档共 8,474 行。决策树现存 179 个独立 Q／S 标识，其中 157 个 Q、22 个 S；缺号反映既有清理，不能补号或推断被删除记录是当前要求。

| 来源 | 路径 | 阅读用途 |
| --- | --- | --- |
| Decision Register | [grill-me-design-tree.md](../docs/design/grill-me-design-tree.md) | 全部 Q／S、后续修正、正式归属与交付顺序 |
| Tool Actions | [tool.md](../docs/design/harness/tool.md) | 纯读／Application Ensure、action 权限、Proposal 与业务写入边界 |
| Context | [context.md](../docs/design/harness/context.md) | acquisition、Package／Frame、pinning、compaction 与保护输入 |
| Memory | [memory.md](../docs/design/harness/memory.md) | 协作记忆、准入、三个控制、后台来源与遗忘 |
| Budget | [budget.md](../docs/design/harness/budget.md) | 多 owner、局部／总限额、原子 reserve、未知费用与容量 |
| Recovery | [recovery.md](../docs/design/harness/recovery.md) | 持久边界、ownership／fencing、retry 与安全派生恢复 |
| Storage | [storage.md](../docs/design/harness/storage.md) | 四层存储、retention、payload availability、历史与当前资格 |
| Eval | [agent-evaluation.md](../docs/design/eval/agent-evaluation.md) | 完整评估设计、Q173–Q187、平台研究与未定细节 |
| 非规范性 inventory | [contract-design-inventory.md](../docs/design/contract/contract-design-inventory.md) | 候选职责、相关对象与后续细节检查，不作 Contract authority |

所有任务先读本文件、Decision Register 的 Purpose／Session State、Q4／Q22／S24.2／S37.1／S38.1，再读主题对应 Q-ID 和详细模块。跨模块语义以相关最终决定核对，不能只读 inventory 或本文件的摘要。若来源在后续任务期间变动，先记录变动及影响再续写，不默默使用旧快照。

### B. 正式输出位置与阶段

以下是后续任务的目标路径，不表示文件已经存在，也不是本次创建清单。

| 输出 | 本轮规划范围／未来任务的目标 |
| --- | --- |
| `docs/spec.md` | 第一阶段正文：产品范围与可见行为 |
| `docs/architecture.md` | 第一阶段正文：最终架构、authority、依赖与不变量，容纳 Contract 文档职责规划 |
| `docs/contracts/*` | 第一阶段只在编写计划／架构中规划结构、职责、边界，不提前写规范性 Contract；详细 Grill 后另行完成 |
| `docs/acceptance.md` | 第一阶段正文：完成所需证据与可观察验收，不伪造测试结果 |
| `docs/development.md` | 第一阶段正文：交付顺序、研发验证纪律、追溯与交接 |
| `docs/progress.md` | 第一阶段正文：从真实新仓库状态建立摘要；随着实际任务更新 |
| `docs/progress/traceability.md` | Q32 已决定的 Progress 类别辅助矩阵；由后续进度任务维护，不新增顶层类别 |

Contract 文件名和数量等待按职责进一步拆分；不创建“临时完整 Contract”绕过后续 Grill。Detailed Contract 完成前，Q32 矩阵可用 Grill 来源承载设计计划并明示 Contract ID 待定；不得将本文件的组织编号当成正式 Contract ID。

### C. 跨上下文任务分工与依赖

以下是文档任务安排，不是新增产品架构决定，也不代表已经创建任务。共同输入为 A 节来源规则；每个任务必须保留两项 seam 的核对证据。

| 任务 | 必读主题／来源 | 输出与责任 | 完成条件与交接 |
| --- | --- | --- | --- |
| W1 产品规范 | Implementation 3–10、14；相应 Q／S；Context／Tool／Memory 的用户边界 | 编写 `docs/spec.md`，覆盖非线性任务、五导航、资料与简历、采集、两类 Fit、Advisor、准备／执行／Tracking、Memory 及非目标 | 用户行为有当前来源；无旧机制、伪字段或实现声明；交接章节→Q-ID、待详细 Contract 的前提和需架构解释的边界 |
| W2 架构与 Contract 结构规划 | 全部九份记录；Implementation 1–17，重点全部 Harness 与 Eval | 编写 `docs/architecture.md`；分配职责、owner、依赖、事务、生命周期机制与 Contract 候选族，不创建 Contract 正文 | 架构与 W1 逐界面对齐；跨域写入／权限／恢复／持久化无冲突 owner；交接 Contract Grill 议题、引用方向及明确排除 |
| W3 验收 | W1／W2 与各模块 Verification implications；Q82、Q117、Q173–Q187 | 编写 `docs/acceptance.md`，从产品和架构行为推导验收、失败／并发／权限／恢复／Eval 证据 | 场景有控制性来源；确定性 tests 与语义 Eval 分开；不擅定阈值／release；交接需求→验收和暂缺详细 Contract 的具体项 |
| W4 开发规则 | W1–W3；Q22／Q26–Q27／Q32／S24.2／S37.1／S38.1；Eval 交付边界 | 编写 `docs/development.md`，明确先文档评审、后 Contract Grill、后实现；测试优先、研究与证据规则 | 不假设 scripts／测试已存在、不定首 Slice 或 CI 发布规则；交接后续任务入口与核对清单 |
| W5 真实进度及矩阵 | W1–W4 实际文件与评审证据；Q4／Q22／Q26／Q32／S38.1；仓库当前状态 | 编写 `docs/progress.md` 与 Q32 矩阵，分清文档完成、Contract 待定、实现未开始、已接受的 post-v1 延期 | 无无证据 Implemented／Partial；目标不作进度正文；条目可回查来源、现存文档与真实证据；交接缺口／阻塞／下一步 |
| W6 五份正文联合复核 | W1–W5、完整覆盖索引和语义回归表，必要时回读九份来源 | 完成两个 seam 的全量复核，修正文档冲突，提供具体可审阅结果供用户评审 | 两项 seam 分别有结论；未定细节明确留给 Contract Grill，不把“待定”当成错误架构或静默补齐；用户评审之后才进入下一阶段 |
| 后续阶段（不在本次执行） | 已评审五份正文、Contract 结构规划、完整来源与待定清单 | 单独详细 Contract Grill → 完成 `docs/contracts/*` → 更新正文／验收／矩阵引用 → 正式开发 | 不重开已决架构来适配旧代码；具体 schemas／error／migration 在这一阶段审议，实施状态由以后真实证据建立 |

W1–W5 是方便分上下文的撰写顺序，不恢复已被 S38.1 替代的 D0–D6 强制流水线。W2 可发现 W1 的职责表述问题并修正，W3／W4 不能为可测试性增设未决业务约束，W5 记录实际状态。若拆成更多任务，必须沿同一职责和来源分工，不能扩展正式文档类别。

每次交接至少提供：本次读取的来源与控制性 Q-ID；实际改动章节及主责／引用关系；逐条覆盖与 supersession 处置；两个 seam 的检查结果；仍待详细 Contract 的问题及来源；真实文档／实现状态；下一任务必读项。可以写在任务完成说明和之后的 Progress／矩阵中，不创建新的长期 authority。下一上下文必须回读实际文件，不能只凭前一条完成摘要继续。

### D. 决策覆盖索引

下表覆盖现存全部 Q／S。它把原记录归入可检索的编写主题；一个源记录的不同条款仍须按 Testing Decisions 拆开检查。控制性 ID 列并非“只读最后一个 ID”，也不是把所有早期决定整体判为无效。具体最终语义见 Implementation Decisions 和原记录。

文档简称：P=产品规范，A=架构，C=Contract 结构／边界规划（详细规范以后），V=验收，D=开发，G=真实进度／矩阵。一个事实的主责按第 2 节区分；列出多个消费文档不创建多个 authority。

| 来源记录（现存） | 有效主题与局部替代处置 | 控制性来源／补充 | 文档消费 |
| --- | --- | --- | --- |
| Q1、Q6 | 非线性任务、导航不等于 Domain；入口采用后续五导航 | S17.2–S17.4 | P、A、V |
| Q2、Q3、Q5、Q11 | 独立最小 canonical Contracts，六类文档，按职责渐进拆分 | S24.2、S38.1 | A、C、D |
| Q4、Q22 | clean-slate 与文档先行；不继承旧代码／完成度／旧顺序 | S37.1、S38.1 | P、A、C、V、D、G |
| Q7、Q18 | eligibility／readiness／progress 分开，各对象最小演化机制 | Q37、Q42 等专门机制 | P、A、C、V、D |
| Q8 | 独立 Profile／Preferences／Evidence／Resume；移除 screening snapshot | Q53–Q56、Q63 | P、A、C |
| Q10、Q14、Q58、Q59 | 独立持久 RequirementSet、验证激活与共享 Ensure；不进 QuickScreen | Q56、Q110–Q111、Q117、Q142、Q171 | P、A、C、V |
| Q12、Q13 | 来源身份 Job；跨平台历史合并 REJECTED | Q12 | P、A、C、D |
| Q15、Q63、Q64 | 共享经历事实、人工 reconciliation；旧导入即正式与 fragment 解释已替代 | Q70–Q75、Q108、Q114、Q163 | P、A、C、V |
| Q16、Q25、Q42 | Candidate 资产／可变 Preparation／冻结执行分离；Greeting 与重入取后续 | Q30、Q150、Q157、Q162 | P、A、C、V、D |
| Q17、Q44、Q48 | Manual 可无 JD 根；BOSS admission 不同，但 JobVersion 语义相同 | Q48、Q49、S9.1 | P、A、C、V |
| Q19、Q72、Q82 | baseline／eligibility／实际可见性、完整性与有限 MISSING；删除 confirmation gate | Q83、Q112–Q115、Q139、Q172 | P、A、C、V、D |
| Q21 | 面试为 ApplicationEvents，不是独立 Aggregate | Q21、Q37 | P、A、C、V |
| Q23 | Pursuit 与一次选择分开；书签未来设计，不保留旧兼容功能 | S37.1 | P、A、C、G |
| Q24 | Advisor 不要求 DeepFit；旧 lineage migration 不保留 | Q58、Q112、Q139、S37.1 | P、A、C、V、G |
| Q26、Q32 | 规范与状态分离、稳定 ID／矩阵／未来检查；无存在即完成 | S37.1、S38.1 | A、C、V、D、G |
| Q27 | 上游研究、版本／许可核对与 adapter 边界 | Q3、Q49 | P、A、C、D、G |
| Q30、Q31 | Snapshot／Approval／Attempt／真实业务事实；回读与人工报告 | Q150、Q157、Q164 | P、A、C、V、D |
| Q35、Q40 | batch 编排独立子任务；先选后依赖再完整 freeze，stale 与撤权 fail-closed | Q110–Q112、Q172、S22.1 | P、A、C、V、D |
| Q36、Q37 | 批量不事务化，技术事件／业务事件分开，非线性追加事件进度 | Q160 | P、A、C、V |
| Q41、Q85 | 对话不隐式写事实；旧 Advisor working draft 全部退出 | Q128、Q133、Q138、Q146、Q148–Q149、Q158 | P、A、C、V |
| Q45、Q55、Q56 | 全局硬偏好、纯确定性筛选、移除冗余 screening authority | Q161 | P、A、C、V、G |
| Q46、Q51 | assessment authority、确定性独立评分与显式 rescore | Q112、Q168 | P、A、C、V |
| Q47、Q52 | 统一 durable Session／bounded Turn；compaction 与等待机制用后续规则 | Q89、Q132、Q139、Q155、Q158–Q159、Q167 | P、A、C、V、D |
| Q49、Q50 | 两阶段采集、聚合审计、freshness／availability；无强风险自动冷却恢复 | Q160–Q161、Q164 | P、A、C、V、D |
| Q53、Q54 | 单用户无 Candidate root；narrow Profile 与隐私 | Q119 | P、A、C、V |
| Q66、Q70、Q71、Q73、Q74 | saved baseline、Draft 后原子 Save、完整 factual grounding；无 confirmation object | Q108、Q113–Q114、Q118–Q119、Q147、Q166 | P、A、C、V、D |
| Q75、Q79、Q86、Q87 | 无持久 Assertions、精确引用及历史 reader、实际依赖 grounding；旧事实不可 rebind 救活 | Q108、Q114 | A、C、V、D |
| Q76、Q77、Q96、Q97、Q98 | 正文事实版本与 current-use；删除／传播不改历史，展示变更区别 | Q108、Q113–Q114、Q118–Q119、Q146、Q151、Q163 | P、A、C、V |
| Q80、Q81、Q83 | Harness Context 策略／逐调用 Frame；retrieval 仅保留 future 边界 | Q121、Q123、Q132、Q136、Q139、S24.1 | A、C、V、D、G |
| Q88、Q89、Q93、Q100 | 默认／讨论选项、统一 Session、逻辑删简历；apply 优先级单列 | Q146、Q149 | P、A、C、V |
| Q91、Q94 | 显式 narrow CAS 回 Preparation，append-only runtime inputs；不保留 Advisor draft | Q108、Q134、Q146、Q158 | P、A、C、V |
| Q108、Q109 | 单当前时间事实，旧 Overlay isolation 分支 REJECTED；working draft 条款被替代 | Q113–Q114、Q146、Q151、Q163 | P、A、C、V |
| Q110、Q111、Q112 | 两阶段 freeze、独立 LLM parse、两 Fit 独立；无 Coverage／分差／上下界 | Q113–Q117、Q142、Q168、Q171 | P、A、C、V |
| Q113、Q114、Q115、Q116、Q117 | Save authority、自动同步、scope-specific 四态、target 串行、parser release Gate 暂缓 | Q118–Q119、Q122、Q168、Q171 | P、A、C、V、D |
| Q118、Q119 | 全受影响 authority 原子提交，Profile 不改职业 baseline | Q147、Q151–Q152 | P、A、C、V、D |
| Q120、Q121、Q126 | 共用 Harness／独立 Skills、typed actions、Full Context，无 v1 RAG／通用执行工具 | Q123、Q127–Q128、Q138–Q139、Q144 | P、A、C、V |
| Q122、Q124、Q125 | durable recovery／fencing、owner reserve／usage、四层存储 | Q130、Q135–Q136、Q140–Q142、Q156 | A、C、V、D |
| Q123 | v1 exact input 超容量前置失败；不静默降级 | Q132、Q172 | P、A、C、V |
| Q127、Q128、Q129、Q130、Q131 | 协作 Memory／受支持用户来源、三条 authority 规则、后台 owner、遗忘不复活 | Q132–Q133、Q139、Q145、Q169–Q170 | P、A、C、V、D |
| Q132、Q134、Q135、Q136 | 独立 Context、合法写后 exact input、Run-wide allowance、active pin vs history | Q139、Q140、Q158 | A、C、V、D |
| Q133、Q138 | Session assertions 可讨论、有真实来源，formal apply 用后续 Proposal 规则 | Q146、Q148–Q149、Q158 | P、A、C、V |
| Q137、Q139 | learning／Recall／management 独立、lazy／eager 分离、Memory 不进 checkpoint | Q143、Q172 | P、A、C、V |
| Q140、Q141、Q142 | 无隐藏 retry、stream 临时、持久 parse single-flight／owner-only cost | Q144、Q156、Q159、Q171 | P、A、C、V |
| Q143、Q144、Q145 | exact lazy pin、pure read／Application Ensure、较新人工 Memory 管理优先 | Q149、Q159 | A、C、V |
| Q146、Q148、Q149 | page-only Draft、actual-target Proposal／一次完整确认，无 source-selection 概念 | Q156、Q158、Q166–Q167 | P、A、C、V |
| Q147、Q152 | authority＋durable intent、post-commit demand-driven 派生 | Q165 | P、A、C、V、D |
| Q150、Q157 | actual viewed material／Greeting 冻结；固定默认与手工编辑，execution approval 独立 | Q30 | P、A、C、V |
| Q151、Q153、Q154 | 资料库逻辑删除／直接 membership；简历 selection-only；空状态与 task prerequisites 分开 | Q163 | P、A、C、V |
| Q155、Q156、Q158、Q159 | 前台串行、已提交结果不依赖 narration、human wait 与 dependency wait 分开 | Q167 | P、A、C、V |
| Q160、Q161、Q162 | 共享持久 safety、冻结采集／最新本地筛选、unfinished Preparation 重入 | Q164 | P、A、C、V |
| Q163、Q164、Q165、Q166、Q167 | 完整经历、执行检查不刷新、过时派生跳过、草稿可丢、Session-delete 原子撤权 | Q170 补充后台源删除 | P、A、C、V |
| Q168、Q169、Q170、Q171、Q172 | 无分数／无目标区分、Memory 失败隔离／删源禁发、protected input 撤权结束 | 各条当前有效 | P、A、C、V |
| Q173、Q174、Q175、Q176、Q177 | 隔离真实路径、派生 telemetry、证据类别不替代 release、独立 Judge、exact fixture/config | S35.1 | A、C、V、D；P 仅质量边界 |
| Q178、Q179、Q180、Q181、Q182 | fixed-input Scenario／N+1、per-check completeness、合法替代、回归留存、output-preserving 重评 | Q183–Q187 | A、C、V、D |
| Q183、Q184、Q185、Q186、Q187 | 连贯边界／task-scoped evaluator／答案控制隔离／实验范围／受控 Memory | 各条当前有效 | A、C、V、D |
| S5.1、S5.3 | 平铺与 Company view，岗位／简历能力入口 | S17.2–S17.3、Q112、Q139 | P、A、C、V |
| S7.1、S17.4、S22.1 | 共用 Harness、独立 Skill、单语义 Run；compaction 为同 Run 辅助 | Q120–Q121、Q127、Q132 | P、A、C、V、D |
| S9.1 | 本地持久 Job 与显式刷新，拒绝 BOSS 不持久 | Q48–Q49、Q160–Q161、Q164 | P、A、C、V |
| S15.1 | 经历级 facts／Full Context First 保留；旧 coverage／confirmation／v1 overflow retrieval 被替代 | Q79、Q98、Q108、Q111–Q113、Q121、Q123、Q163 | P、A、C、V、D |
| S17.1、S17.2、S17.3 | 用户决定搜索范围、五导航、单 Assistant 双入口，非双 Session | Q89、Q139、Q146、Q149 | P、A、C、V |
| S24.1、S24.2 | Agentic RAG post-v1；架构已决不等于详细 Contract 已定 | Q123、Q22、S38.1 | A、C、D、G |
| S25.1、S26.1 | 详细 Harness 记录与 Context／Storage 职责分离；记录不是新 authority | Q125、Q132 | A、C、V、D；记录历史 |
| S27.1、S28.1、S29.1、S29.2、S30.1 | 模块维护、显式清理、Tool／inventory、Memory 文件更名；不转成产品功能或本次修改许可 | Q139；原记录维护历史 | D／来源说明；inventory 仅规划 |
| S35.1 | Langfuse-heavy／JobHunter-thin Eval，真实任务语义 | Q173–Q187 | A、C、V、D；P 质量边界 |
| S37.1、S38.1 | 新仓库重建、九文件输入、文档先行；旧首 Slice／bootstrap 建议未接受 | Q4、Q22 已就地更新 | 全部类别的阶段边界、G 真实状态 |

历史已删除标识只经保留下来的替代关系解释，例如 Q9→Q12、Q57／Q62→Q75、Q65／Q68／Q69→Q112、Q78／Q84→Q113、Q92／Q95／Q99／Q102–Q104／Q106–Q107→Q108、Q101→Q146、Q105→Q151。它们不加入现行覆盖计数，也不要求恢复原记录。REJECTED Q13／Q109 留作排除理由；DEFERRED S24.1 留作 post-v1 范围证据。

### E. 后续待定事项的交接边界

以下只列问题所属后续阶段，不能由文档作者补答：

- 详细 Contract Grill：真实 Profile／Evidence／Job 输入、每功能前提、规范引用语法及验证、Fit target 精确 key、输出／error／status 表示、完整 Tool catalog、command／API payload、审批与 Proposal 生命周期、runtime transitions、事务协议、schema 与新系统历史演化／migration 细节。
- 相关 Contract／策略设计：评分可用性与权重、预算单位／金额／overrun／unknown reconciliation、compaction 与 Memory trigger／range 表示、retention 时长／物理存储／清理协调、render／渠道 payload。保留已决限制，不推导数值默认。
- 研究与实现准备：固定来源 commit 和 source mapping；Langfuse／SDK 实际版本、deployment／worker 能力与脱敏配置验证。已有选型不等于任意版本能力已验证。
- 后续 rollout 工作：Q175 的 Trial 数、阈值、默认启用、CI／release 规则；不得以“Architecture Grill 已闭合”为由假装这些也已经决定。
- 明确延期扩展：Candidate Agentic RAG、正式 annotated parser certification、书签／Pursuit UX、General Assistant／面试能力、跨平台合并、多 Candidate／多租户、全面物理清除与旧数据导入等，按各自源记录单独启动，不能混进本次文档任务。

区分“架构已定但 Contract 表达待细化”“明确延期的能力”“后续研究／rollout 工作”。若无法从后续决定消解某个真实文本冲突，报告具体条款、来源和影响，不默选新机制，也不重新开启整轮 Architecture Grill。
