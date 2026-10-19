# Cognitive Yield Monitor

**An experimental open-source Agent Skill for detecting when an AI conversation is advancing, exploring productively, or repeating itself.**

> AI can keep answering long after a conversation stops moving forward. What if it could notice that—and help you choose a better next step?

[简体中文](README.zh-CN.md) · [Core Skill](SKILL.md) · [Chinese Skill](SKILL.zh-CN.md) · [Evaluation protocol](docs/EXPERIMENT_PROTOCOL.md) · [Launch article (中文)](docs/launch-post.zh-CN.md)

## The idea

Most conversational systems are optimized to respond. Cognitive Yield Monitor adds a small but important question:

**Is the next answer likely to help the user make progress toward their actual goal?**

The goal is not to make conversations shorter at all costs. Emotional support, deliberate practice, creative exploration, and research all have different definitions of progress. Sometimes repetition helps. Sometimes uncertainty is productive. Sometimes a discussion is circling—and should switch methods.

This Skill asks the model to track the user's goal, established insights, unresolved questions, evidence, and recent changes. When a status check would help, it can recommend testing a claim, finding a counterexample, changing frames, making an idea actionable, synthesizing, or continuing deliberately.

## Five conversation states

| State | Meaning |
|---|---|
| **ADVANCING** | A meaningful new insight, evidence item, inference, application, or goal-aligned development appears. |
| **PRODUCTIVE UNCERTAINTY** | There is no settled answer yet, but useful questions, tensions, or distinctions are emerging. |
| **DIMINISHING RETURNS** | Multiple recent substantive turns repeat existing ideas without meaningful new support or progress. |
| **READY TO CLOSE** | The user's stated goal appears sufficiently met. |
| **INSUFFICIENT EVIDENCE** | Available context is too short, ambiguous, or incomplete for a responsible judgment. |

The warning threshold is intentionally conservative. A single repetitive answer is not enough. The Skill should explain what seems repeated, acknowledge uncertainty, and suggest a concrete next move. The user remains in control.

## Quick start

1. Clone or download this repository.
2. Load `SKILL.md` into a host that supports Agent Skills, or adapt it to the host's supported custom-instruction mechanism.
3. In a substantive conversation, ask: **“Evaluate the marginal cognitive return of this conversation so far.”**
4. If the discussion appears to be circling, choose a different operation: test the claim, find a counterexample, define a measurable question, make a decision, or summarize what is actually established.

See [`SKILL.zh-CN.md`](SKILL.zh-CN.md) for the Chinese instructions.

### Compatibility and limitations

Skill support and installation differ by host and product version. Consult the official [OpenAI Skills documentation](https://developers.openai.com/api/docs/guides/tools-skills) and [Anthropic Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

A Skill is an instruction set, **not an autonomous background process**. It cannot silently inspect every future message or access conversation history that the host has not provided. Whether it runs depends on the host loading and following it.

## How it is designed

- **Goal-relative progress:** judge progress against what the user wants, not novelty alone.
- **Evidence before interruption:** repeated wording alone does not prove a loop.
- **Protect productive uncertainty:** an unresolved question can still be getting sharper.
- **Mode-specific safeguards:** do not mistake emotional processing, practice, or divergent brainstorming for waste.
- **User agency:** advise; do not take control or nag after the user chooses to continue.
- **Honest claims:** this is a model judgment, not a scientific measure of cognition.

## Evaluate it instead of just believing it

The repository includes a starter set of qualitative cases and a proposed controlled comparison:

- [Starter evaluation cases](evals/cases.json)
- [Evaluation instructions and reporting template](docs/EXPERIMENT_PROTOCOL.md)
- [Worked examples](references/examples.md)
- [Qualitative rubric](references/rubric.md)

The initial cases are **test fixtures, not benchmark results**. No effectiveness claim should be made until the Skill has been compared against a baseline on matched examples and outputs have been reviewed. Measure false-positive interruptions separately from missed loops.

Run the packaging/data checks with Python 3.9+:

```bash
python scripts/validate_project.py
```

This checks repository structure and evaluation-case format. It does not evaluate model behavior.

## Repository map

- `SKILL.md` / `SKILL.zh-CN.md` — English and Chinese Skill instructions
- `README.md` / `README.zh-CN.md` — project overview
- `references/` — rubric and worked examples
- `evals/` — qualitative starter cases
- `docs/EXPERIMENT_PROTOCOL.md` — proposed controlled evaluation
- `docs/launch-post.zh-CN.md` — Chinese project introduction draft
- `prompts/optional-always-on.md` — optional custom-instruction snippet
- `scripts/validate_project.py` — dependency-free packaging validator

## Roadmap

1. **Test the idea:** run matched baseline-versus-Skill evaluations across different conversation modes.
2. **Study failure modes:** identify premature warnings, missed loops, and cases where the model mistakes uncertainty for stagnation.
3. **Invite outside cases:** collect privacy-scrubbed examples from users and contributors.
4. **Build only if needed:** consider host-specific middleware or a separate monitor agent if evidence shows a prompt-level Skill is insufficient.

## Contributing

The most useful contribution is not simply another feature. It is a case that challenges the design: a false alarm, a missed loop, a valuable repetition, or a conversation where the right answer is “not enough evidence.” See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE).
