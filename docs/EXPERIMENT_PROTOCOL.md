# Evaluation Protocol: Does the Skill Help?

This is a proposed evaluation, not a report of completed experiments.

## Research question

When given the same conversation context, does Cognitive Yield Monitor improve a model's ability to distinguish genuine stagnation from productive uncertainty and goal-relevant repetition—without increasing premature interruptions?

## Hypotheses

- **H1 — Detection:** Skill-enabled outputs more often identify true diminishing-return cases than baseline outputs.
- **H2 — Restraint:** Skill-enabled outputs do not increase false alarms in emotional support, deliberate practice, and creative exploration.
- **H3 — Actionability:** When a warning is justified, Skill-enabled outputs more often propose a concrete next step.
- **H4 — Calibration:** When evidence is insufficient or mixed, Skill-enabled outputs preserve uncertainty rather than overstate confidence.

These are hypotheses, not established findings.

## Design

### Conditions

- **Baseline:** the model receives the case context and is asked to assess the conversation without the Skill.
- **Skill:** the same model receives the same context and the Skill instructions.

Keep model version, sampling settings, prompt wording, context, and output format identical wherever possible. Randomize case order. If comparing multiple models, analyze each model separately before aggregating.

### Starter dataset

Use `evals/cases.json` as a pilot set. It contains 12 hand-authored scenario summaries. This is too small and synthetic to support broad claims. Before drawing conclusions, expand it with realistic, privacy-scrubbed transcripts and have at least two independent reviewers label them.

For stronger evaluation:
1. Aim for at least 50–100 cases across the five states and multiple conversation modes.
2. Include ambiguous examples and hard negatives where repetition is valuable.
3. Write expected labels and rationales before viewing model outputs.
4. Keep a held-out set that is not used to revise the Skill.
5. Remove names, identifying details, and sensitive content from contributed transcripts.

### Required output schema

Ask both conditions to return:
- `state`: one of the five documented states;
- `evidence`: a short explanation grounded in the provided turns;
- `warning`: yes/no;
- `next_step`: one concrete suggestion or null;
- `uncertainty`: low/medium/high, with a short reason.

Do not require the model to invent a numerical probability.

## Human review

At least two reviewers should independently assess each output without seeing whether it came from baseline or Skill condition, where practical. Review these dimensions:

| Measure | What it captures |
|---|---|
| State accuracy | Agreement with the pre-registered expected state |
| False-positive warning rate | Warnings on cases where repetition is useful or evidence is insufficient |
| Miss rate | Failure to flag clear repeated loops |
| Evidence grounding | Whether the rationale cites actual changes or repetitions in the supplied context |
| Next-step usefulness | Whether the suggested move is concrete and relevant |
| User-agency violation | Nagging, shaming, or overriding an explicit user choice |

Report disagreements and the number of cases, not just a single overall score. Do not collapse false positives and misses into one metric.

## Results template

For each condition, record:
- model name and exact version;
- date and run settings;
- number of cases;
- confusion matrix across the five states;
- false-positive warning rate on protected modes;
- clear-loop miss rate;
- reviewer agreement and adjudication method;
- representative successes and failures.

A blank CSV template is provided in `docs/results-template.csv`.

## Interpretation guardrails

- A better result on synthetic cases does not establish real-world effectiveness.
- Prompt changes made after seeing results should be evaluated on a fresh held-out set.
- Do not claim causal improvement from comparisons where the context or model settings differ.
- A high detection rate is not a win if false alarms interrupt valuable work.
- Publish negative and mixed results, including cases where the baseline performs better.

## Minimal pilot workflow

1. Freeze the Skill version and case labels.
2. Run both conditions on all pilot cases.
3. Save raw outputs with condition labels hidden from reviewers.
4. Have reviewers label outputs independently.
5. Resolve disagreements using written criteria.
6. Publish aggregate results, limitations, and anonymized examples.
