# Cognitive Yield Monitor｜认知收益监测器

**一个用于识别 AI 对话是在取得进展、陷入重复，还是处于生产性不确定状态的 Agent Skill。**

> 不要只让 AI 一直回答。也要帮助它判断，下一次回答是否可能带来真正有价值的新东西。

[English README](README.md)

## 为什么做这个项目？

对话式 AI 很擅长继续回答，却不总是擅长判断：讨论是否正在重复，或者看似混乱的探索是否仍在孕育新概念。

Cognitive Yield Monitor 在对话中加入一层审慎的反思：围绕用户目标、已有洞察、未解决问题和最近几轮的实际进展做检查；必要时建议下一步，例如验证证据、寻找反例、切换视角、把想法变成可操作方案，或整理收束。

这是一个**实验性的对话 Skill**，不是科学测量工具，也不是自主运行的后台监控器。

## 设计原则

- **关注进展，而非字数：** 回答更长，不等于认知收益更高。
- **收益取决于目标：** 情绪支持、刻意练习、创意探索和研究讨论，不能用同一套标准评价。
- **先看证据，再提醒：** 仅仅措辞重复，不足以触发警告。
- **保护生产性不确定：** 新想法成熟之前，探索可能暂时显得混乱。
- **提供建议，不接管选择：** 是否继续由用户决定。
- **诚实说明边界：** 不声称监控模型无法访问的上下文。

## 项目文件

- `SKILL.md` — 英文核心 Skill
- `SKILL.zh-CN.md` — 中文核心 Skill
- `README.md` / `README.zh-CN.md` — 中英文项目说明
- `references/rubric.md` — 评估标准和状态定义
- `references/examples.md` — 对话示例
- `prompts/optional-always-on.md` — 可选的自定义指令片段
- `evals/cases.json` — 初始评测集
- `scripts/validate_project.py` — 无第三方依赖的结构校验脚本
- `LICENSE`、`CHANGELOG.md`、`CONTRIBUTING.md`

## 快速开始

1. 下载或克隆本项目。
2. 将 `SKILL.md` 加载到支持 Agent Skills 的工具，或根据平台支持的自定义指令方式进行适配。
3. 在一场持续时间较长或内容较深入的讨论中使用。也可以直接问：**“请评估目前这场讨论的边际认知收益。”**
4. 如果系统发现重复，可以让它验证核心判断、寻找反例、把想法转化为研究问题，或总结哪些结论已经成立。

### 平台兼容性

Agent Skills 通常使用包含 `SKILL.md` 的目录，并可附带参考材料。不同平台和产品版本的安装方式有所区别。请参考 [OpenAI Skills 文档](https://developers.openai.com/api/docs/guides/tools-skills) 与 [Anthropic Agent Skills 文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)。

Claude Code 可将目录安装到当前配置能发现的路径，例如 `~/.claude/skills/cognitive-yield-monitor/`。其他平台请使用其支持的技能上传或目录机制。如果平台只支持自定义指令，可参考 `prompts/optional-always-on.md`；这不保证它会自动在每轮执行。

**重要边界：** Skill 是指令集合，不是后台常驻程序。除非宿主平台主动调用它并提供相应上下文，否则它不能独立观察之后的每一条消息。

## 评估维度

| 维度 | 要问的问题 |
|---|---|
| 信息增量 | 是否增加了事实、证据或有用区分？ |
| 概念增量 | 是否产生了真正不同的理解框架？ |
| 推理进展 | 推理是否前进，或解决了一个矛盾？ |
| 实证价值 | 是否提出可验证或可证伪的内容？ |
| 实践价值 | 是否改进决策或产出了可用成果？ |
| 目标契合度 | 是否推进了用户真正想完成的事情？ |

这些是判断视角，不是客观、通用的分数。刻意练习或情绪支持可能不追求新颖，但仍然非常有价值。

## 五种状态

- `ADVANCING`：出现了有意义的新贡献。
- `PRODUCTIVE UNCERTAINTY`：尚无结论，但新的问题、张力或区分正在出现。
- `DIMINISHING RETURNS`：最近多轮实质内容主要在重述已有观点，没有新的证据或进展。
- `READY TO CLOSE`：用户的目标看起来已经得到充分满足。
- `INSUFFICIENT EVIDENCE`：上下文不足，无法可靠判断。

可见提醒必须审慎。它应说明什么内容正在重复、缺少什么进展，并给出具体的下一步建议。不能羞辱用户；用户明确选择继续后，也不能反复唠叨。

## 试用与校验

对话示例见 [`references/examples.md`](references/examples.md)，初始测试集见 [`evals/cases.json`](evals/cases.json)。

使用 Python 3.9+ 运行结构校验（不需要第三方依赖）：

```bash
python scripts/validate_project.py
```

它会检查项目结构与测试数据格式，但**不会**衡量模型判断质量，也不会运行基于大模型的评测。

## 后续路线

- 在多个模型上对比启用和未启用 Skill 的效果。
- 增加带人工复核与分歧记录的 LLM 评判流程。
- 分别衡量误报（过早打断）与漏报（没有发现重复）。
- 只有在真实用户反馈表明提示词式 Skill 不够时，再开发平台专用中间件或独立监测 Agent。

## 参与贡献

请参阅 [`CONTRIBUTING.md`](CONTRIBUTING.md)。欢迎提交系统过早打断的反例、未发现循环的案例，以及不同对话类型下的评测。

## 许可证

MIT，详情见 [`LICENSE`](LICENSE)。
