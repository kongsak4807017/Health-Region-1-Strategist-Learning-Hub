---
name: data-driven-problem-solving
description: "Data analytics and data-driven decision support. Use when asked to design or critique data analytics workflows, build or choose data science project templates, select GitHub repos for analytics/research, or translate business problems into measurable hypotheses. Triggers include: data analytic, data-driven, analytics project template, data science workflow, แก้ปัญหาด้วยข้อมูล, วางแผนวิเคราะห์ข้อมูล, หา repo data science."
---

# Data-Driven Problem Solving

## Overview
Provide a repeatable workflow for turning a problem into a data-driven decision, plus a curated repo catalog and reproducible research templates.

## Workflow
1. Frame the decision.
- Identify the decision owner, action options, and success metrics.
- Capture constraints (time, budget, compliance).

2. Translate to analytic questions.
- Define outcome/target variables.
- Draft hypotheses and assumptions.

3. Assess data readiness.
- Inventory sources, access, quality, and update cadence.
- Identify gaps and mitigation (collection, proxies, instrumentation).

4. Choose methods and evaluation.
- Select EDA, descriptive, causal, forecasting, ML, or experimentation.
- Define evaluation metrics, baselines, and robustness checks.

5. Plan project structure.
- Pick a template from `references/repo_catalog.md`.
- Map workstreams to folders and artifacts.

6. Validate and decide.
- Check bias, leakage, and sensitivity.
- Produce decision-ready summary and next steps.

## Repo Sourcing
- Use `references/repo_catalog.md` when the user asks for GitHub repos, templates, or tooling.
- Shortlist 2-3 repos with a one-line rationale and risks (archived, license, maintenance).
- If none fit, propose a minimal custom structure and note missing pieces.

## Research / New Knowledge
- Use `references/problem_solving_playbook.md` for research framing, experiment design, and reproducibility.
- Emphasize documentation, versioning, and citations.

## Output Template
Provide a structured deliverable with:
- Problem statement and decision
- Data inventory and gaps
- Analysis plan and methods
- Results and interpretation
- Recommendation and risks
- Next experiments or data needs

## Resources
- `references/repo_catalog.md`
- `references/problem_solving_playbook.md`
