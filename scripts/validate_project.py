#!/usr/bin/env python3
"""Validate the Cognitive Yield Monitor package structure and starter eval data.

Uses only Python's standard library. This is a packaging/data-schema check, not
an assessment of how well any language model detects diminishing returns.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FILES = [
    "SKILL.md", "README.md", "README.zh-CN.md", "LICENSE",
    "CONTRIBUTING.md", "CHANGELOG.md", "references/rubric.md",
    "references/examples.md", "prompts/optional-always-on.md",
    "evals/cases.json", "evals/README.md",
]
ALLOWED_STATES = {
    "ADVANCING", "PRODUCTIVE UNCERTAINTY", "DIMINISHING RETURNS",
    "READY TO CLOSE", "INSUFFICIENT EVIDENCE",
}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ValidationError(Exception):
    """Raised when a required project invariant is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read_text(relative_path: str) -> str:
    path = ROOT / relative_path
    require(path.is_file(), f"Missing required file: {relative_path}")
    return path.read_text(encoding="utf-8")


def parse_skill_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", content, re.DOTALL)
    require(match is not None, "SKILL.md must begin with YAML frontmatter delimited by ---")
    metadata: dict[str, str] = {}
    for line_number, line in enumerate(match.group(1).splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        require(":" in line, f"Invalid frontmatter line {line_number}: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        require(key not in metadata, f"Duplicate frontmatter key: {key}")
        metadata[key] = value
    return metadata


def validate() -> list[str]:
    notes: list[str] = []
    for relative_path in EXPECTED_FILES:
        read_text(relative_path)

    skill_text = read_text("SKILL.md")
    metadata = parse_skill_frontmatter(skill_text)
    require(metadata.get("name", "") == "cognitive-yield-monitor", "Unexpected Skill name")
    require(bool(SLUG_RE.fullmatch(metadata["name"])), "Skill name must be a lowercase hyphenated slug")
    description = metadata.get("description", "")
    require(bool(description), "SKILL.md description must not be empty")
    require(len(description) <= 1024, "SKILL.md description exceeds 1024 characters")
    require("When to evaluate" in skill_text, "SKILL.md is missing the evaluation workflow")
    require("Important limitations" in skill_text, "SKILL.md is missing a limitations section")
    require("PRODUCTIVE UNCERTAINTY" in skill_text, "Skill must guard against premature closure")

    cases_path = ROOT / "evals/cases.json"
    try:
        data: dict[str, Any] = json.loads(cases_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid evals/cases.json: {exc}") from exc
    cases = data.get("cases")
    require(isinstance(cases, list) and len(cases) >= 8, "Eval set must contain at least 8 cases")
    ids: set[str] = set()
    for index, case in enumerate(cases):
        prefix = f"eval case #{index + 1}"
        require(isinstance(case, dict), f"{prefix} must be an object")
        case_id = case.get("id")
        require(isinstance(case_id, str) and case_id.strip(), f"{prefix} needs a non-empty id")
        require(case_id not in ids, f"Duplicate eval case id: {case_id}")
        ids.add(case_id)
        for field in ("mode", "transcript_summary", "expected_state", "rationale"):
            require(isinstance(case.get(field), str) and case[field].strip(), f"{case_id} needs field {field!r}")
        require(case["expected_state"] in ALLOWED_STATES, f"{case_id} has unknown state {case['expected_state']!r}")

    readme = read_text("README.md")
    zh_readme = read_text("README.zh-CN.md")
    require("SKILL.md" in readme and "SKILL.md" in zh_readme, "Both READMEs must explain the Skill package")
    require("not" in readme.lower() and "background" in readme.lower(), "English README should explain the background-monitor limitation")
    notes.append(f"Checked {len(EXPECTED_FILES)} required project files")
    notes.append(f"Validated Skill metadata (name={metadata['name']!r}, description_length={len(description)})")
    notes.append(f"Validated {len(cases)} evaluation cases with unique IDs and known states")
    notes.append("Confirmed both READMEs and key safeguards are present")
    return notes


def main() -> int:
    try:
        notes = validate()
    except (ValidationError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for note in notes:
        print(f"PASS: {note}")
    print("\nProject validation passed. This does not evaluate model behavior or benchmark quality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
