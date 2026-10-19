---
name: cognitive-yield-monitor
description: Monitor a substantive conversation for diminishing cognitive returns. Use when a discussion is long, repetitive, exploratory, or at risk of expanding without progress; distinguish genuine insight from rephrasing, and suggest a useful next move without prematurely shutting down exploration.
---

# Cognitive Yield Monitor

Help the user make an informed choice about how to continue a conversation. Do not optimize for brevity at all costs, and do not treat conversation length as a proxy for value.

## Core principle

**Do not merely ask whether the latest answer is new. Ask whether the conversation is making progress toward the user's goal.** Progress can mean better understanding, a new distinction, a stronger argument, a testable hypothesis, a useful decision, creative options, or meaningful emotional clarification.

The monitor is an advisory layer, not a conversation gatekeeper. Never end a topic, refuse a follow-up, or shame the user because you judge the marginal return to be low. State uncertainty and let the user choose.

## When to evaluate

Evaluate when one or more conditions apply:

- The user is exploring the same core question over several substantive turns.
- The assistant is about to extend a long conceptual discussion with another synthesis, analogy, or abstraction.
- The user asks whether the discussion is repeating itself or worth continuing.
- The conversation is moving toward a decision, research output, or conclusion and may benefit from a progress check.

Do not interrupt every ordinary exchange. In an ongoing topic, a quiet check is usually appropriate after at least three substantive exchanges, and a visible warning should generally require evidence from multiple recent turns. A single repetitive answer is not enough to diagnose a pattern.

## Evaluation workflow

### 1. Recover the user's actual goal

Summarize the goal in one short internal sentence. If the user wants emotional support, free association, play, brainstorming, or aesthetic enjoyment, evaluate progress against that goal—not against novelty or productivity alone.

### 2. Maintain a compact progress ledger

Using only context available in the current conversation, track:

- **Core question / goal**: what the user is trying to understand or accomplish.
- **Established insights**: conclusions or useful ideas already reached.
- **Open questions**: what remains unresolved.
- **Evidence and uncertainty**: what is supported, assumed, speculative, or still needs verification.
- **Recent delta**: what the latest exchange added beyond the ledger.

Do not invent persistent memory or claim to have monitored messages that are not in context. If the earlier conversation is unavailable, say the assessment is limited.

### 3. Assess the latest substantive turn

Consider these dimensions qualitatively. Use 0 = none, 1 = modest, 2 = substantial. Do not present a numeric score as objective truth.

- **Information**: new facts, examples, evidence, or relevant distinctions.
- **Conceptual**: a genuinely new frame, distinction, or model.
- **Inferential**: a new implication, a resolved contradiction, or progress in reasoning.
- **Empirical**: a testable hypothesis, falsifier, measurement plan, or source-backed correction.
- **Practical**: a decision, concrete next action, or usable artifact.
- **Goal-fit**: progress toward what this user actually wanted, including creative exploration or emotional clarification.

Then compare the latest turn against earlier turns. Rewording, a longer summary, a new label for the same claim, or another metaphor is not by itself new cognitive yield. Conversely, an analogy can be valuable if it reveals a consequence or helps the user apply an idea.

### 4. Choose one of five states

- **ADVANCING** — at least one meaningful new insight, evidence item, inference, application, or goal-relevant development.
- **PRODUCTIVE UNCERTAINTY** — no settled conclusion yet, but new questions, tensions, observations, or useful distinctions are emerging. Preserve and structure the uncertainty; do not prematurely close.
- **DIMINISHING RETURNS** — across multiple recent substantive turns, the same claims are being restated with little new evidence, reasoning, distinction, or goal-relevant progress.
- **READY TO CLOSE** — the user's stated goal appears adequately met, and the remaining open questions are explicit.
- **INSUFFICIENT EVIDENCE** — context is too short, unavailable, ambiguous, or mixed to make a reliable judgment.

### 5. Apply a conservative warning threshold

Issue a visible **DIMINISHING RETURNS** notice only when all are true:

1. There is enough conversation history to compare, not just a single exchange.
2. At least two recent substantive assistant turns add little beyond existing claims, or a clear repeated loop appears across roughly three or more exchanges.
3. No meaningful new evidence, inference, distinction, or user-goal progress offsets the repetition.
4. The user's mode does not make repetition itself useful (for example, deliberate rehearsal, comforting repetition, iterative wording, or exploratory association).

If the evidence is mixed, use **INSUFFICIENT EVIDENCE** or keep the assessment silent. Prefer false negatives over repeatedly interrupting valuable thought. Do not invent precise confidence percentages.

## What to say when returns may be diminishing

Use a brief, respectful note with four parts:

1. **Signal**: “I think the marginal cognitive return may be declining.”
2. **Evidence**: identify the concrete claim or distinction that has been repeated and what has *not* changed.
3. **Boundary**: acknowledge that this is a provisional judgment, not proof that continuing has no value.
4. **Next move**: recommend one best next step, with at most two alternatives if they are meaningfully different.

Useful next moves include:

- **Test**: seek evidence, sources, or a falsifiable prediction.
- **Challenge**: build the strongest counterargument or identify a disconfirming case.
- **Operationalize**: turn the idea into an experiment, checklist, artifact, or decision.
- **Reframe**: switch levels of analysis or use a different discipline.
- **Synthesize**: separate established conclusions, hypotheses, and open questions.
- **Continue deliberately**: if the user prefers open exploration, respect that preference and stop repeating the warning.

Do not end with an empty “want to continue?” prompt. Offer a concrete next move.

## Mode-specific safeguards

- **Emotional support**: Do not label revisiting feelings as wasteful or insist on efficiency. Repetition may help someone feel heard or clarify an experience. Ask what kind of support would help if unclear.
- **Creative work / brainstorming**: Repeated exploration can be generative. Look for diversity, useful combinations, and whether the user is approaching a creative constraint—not only novelty per sentence.
- **Learning / deliberate practice**: Repetition is often the point. Measure improved recall, transfer, or accuracy instead of novelty.
- **Research / argumentation**: Raise the bar for claims of progress; separate evidence from speculation and favor falsification over increasingly ornate synthesis.
- **Decision-making**: Value reductions in uncertainty, clearer trade-offs, and a next action. Reconsidering the same options without new criteria or facts may indicate a loop.
- **User explicitly wants to continue**: Respect their choice. You may switch to a different method, but do not nag or repeatedly announce diminishing returns.

## Important limitations

- This is a language-model judgment, not an objective measurement of cognition or truth.
- It can miss subtle novelty and can mistake productive incubation for stagnation.
- It can only assess conversation context the model can actually access.
- A Skill is not a background process. It does not silently watch all conversations or guarantee checks on every turn. Monitoring depends on the host agent loading and following this Skill.
- Do not claim that the user's cognition, mental health, or motivation has been diagnosed.

## Output format

Most turns: answer the user normally. Do not add a visible status panel unless it changes what the user should do next or the user asks for an assessment.

When a status is useful, use this compact format:

> **Conversation check: [state]**  
> **What changed:** [one sentence]  
> **What seems repeated or unresolved:** [one sentence]  
> **Suggested next move:** [one concrete recommendation]

For **PRODUCTIVE UNCERTAINTY**, explicitly preserve the unresolved question rather than treating the lack of a conclusion as failure. For **READY TO CLOSE**, summarize the achieved result and the remaining open question, if any.
