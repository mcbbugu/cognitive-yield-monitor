# Starter evaluation set

`cases.json` contains compact scenario summaries with expected qualitative states and rationales. It is a starting point for human review, not a validated benchmark.

## Suggested use

1. Give each scenario to a model with the Skill disabled and enabled, keeping the prompt and available context as similar as possible.
2. Ask the model to return a state, brief rationale, confidence, and (if relevant) a proposed notice.
3. Have reviewers who do not know which condition produced an answer rate correctness, usefulness, and interruption risk.
4. Report false-positive warnings separately from missed loops. Include disagreement and ambiguous cases rather than hiding them in one aggregate score.
5. Add examples across languages, conversation lengths, and modes such as emotional support, tutoring, brainstorming, research, and decision support.

Do not infer real-world effectiveness from passing the repository validator. The validator checks packaging and data shape only.