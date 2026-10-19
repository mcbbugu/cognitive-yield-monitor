# Cognitive Yield Monitor

**A lightweight Agent Skill for noticing when an AI conversation is progressing, circling, or sitting in productive uncertainty.**

> Don't just ask an AI to keep answering. Help it notice whether the next answer is likely to add something useful.

[简体中文说明](README.zh-CN.md)

## Why this exists

Conversational AI is good at continuing. It is less consistently good at saying, with reasons, that a discussion is repeating itself—or that it is too early to call a messy exploration unproductive.

Cognitive Yield Monitor adds a conservative reflection step. It tracks the user's goal, established insights, open questions, and recent progress, then recommends a next move when useful: test a claim, seek a counterexample, change frames, operationalize an idea, synthesize, or continue deliberately.

This is an **experimental conversation Skill**, not a scientific instrument and not an autonomous background monitor.

## Design principles

- **Progress over verbosity:** a longer answer is not automatically a more valuable answer.
- **Goal-relative value:** emotional support, practice, creative exploration, and research require different standards.
- **Evidence before interruption:** repeated wording alone is not enough to trigger a warning.
- **Protect productive uncertainty:** early-stage ideas can be messy before a useful concept emerges.
- **Advisory, not controlling:** the user decides whether to continue.
- **Honest limits:** the model must not claim to monitor hidden or unavailable context.

## Repository contents

- `SKILL.md` — core Agent Skill instructions
- `SKILL.zh-CN.md` — Chinese version
- `README.md` / `README.zh-CN.md` — bilingual project overview
- `references/rubric.md` — evaluation rubric and state definitions
- `references/examples.md` — worked examples
- `prompts/optional-always-on.md` — optional custom-instruction snippet
- `evals/cases.json` — starter qualitative evaluation set
- `scripts/validate_project.py` — dependency-free structure/data validation
- `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`

## Quick start

1. Download or clone this directory.
2. Load `SKILL.md` into an Agent Skills-compatible host, or adapt its instructions to your host's custom-instructions mechanism.
3. Start with a long or substantive discussion. You can also explicitly ask: **“Evaluate the marginal cognitive return of this conversation so far.”**
4. If the monitor flags repetition, ask it to test the core claim, find a counterexample, turn the idea into a research question, or summarize what's actually established.

### Host compatibility

Agent Skills use a directory with a `SKILL.md` manifest and optional supporting resources. Support and installation steps vary by host and product version. See the official docs for [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills) and [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

For Claude Code, install the directory under a location discovered by your setup, such as `~/.claude/skills/cognitive-yield-monitor/`. For other hosts, use their supported skill upload or skill-directory mechanism. If a host only supports custom instructions, `prompts/optional-always-on.md` is a starting point, not a guarantee of automatic execution.

**Important:** A loaded Skill is an instruction set, not a daemon. It cannot independently inspect every future message unless the host invokes it and provides the relevant conversation context.

## What it evaluates

| Dimension | Question |
|---|---|
| Information | Did we add facts, evidence, or a useful distinction? |
| Conceptual | Did a genuinely new frame or model emerge? |
| Inferential | Did reasoning move forward or resolve a tension? |
| Empirical | Did we identify something testable or verifiable? |
| Practical | Did we improve a decision or produce something usable? |
| Goal-fit | Did the exchange advance what the user actually wanted? |

These are lenses, not an objective universal score. A conversation may be valuable without being novel—for example, deliberate practice or emotional support.

## The five states

- `ADVANCING` — a meaningful new contribution appears.
- `PRODUCTIVE UNCERTAINTY` — the discussion is messy, but new tensions or questions are emerging.
- `DIMINISHING RETURNS` — several recent substantive turns mainly restate existing ideas without new support or progress.
- `READY TO CLOSE` — the user's goal appears adequately met.
- `INSUFFICIENT EVIDENCE` — there is not enough context for a reliable judgment.

A visible warning should be conservative. It should name what repeated, explain what is missing, and suggest a concrete next move. It must not shame users or repeatedly interrupt them after they choose to continue.

## Try it

See [`references/examples.md`](references/examples.md) for examples of repetition, productive uncertainty, practice, and emotional support. The initial evaluation set is in [`evals/cases.json`](evals/cases.json).

Validate the repository structure with Python 3.9+ (no third-party dependencies):

```bash
python scripts/validate_project.py
```

This validates package structure and evaluation-case format. It does **not** measure model quality or run an LLM-based benchmark.

## Current scope and roadmap

### v0.1

- Portable Skill instructions
- Chinese and English documentation
- Conservative state definitions and mode-specific safeguards
- Example conversations and a starter evaluation set
- Dependency-free structural validator

### Possible next steps

- Run blind comparisons with and without the Skill across several models.
- Add an LLM-as-judge evaluation protocol with human review and disagreement reporting.
- Measure false-positive interruptions separately from missed repetition.
- Build a host-specific middleware or independent monitor agent only if users show that a prompt-level Skill is insufficient.

## Contributing

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md). Especially useful contributions include counterexamples where the monitor interrupted too early, cases where it failed to detect a loop, and evaluations across different conversation types.

## License

MIT. See [`LICENSE`](LICENSE).
