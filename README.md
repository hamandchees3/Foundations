# AI Foundations for Policymakers

A handbook introducing the fundamentals of AI for a policy audience — how modern systems work, what they can and can't do, who the major players are, and which policy questions are most active. Produced for the Conservative AI Policy Fellowship.

## Current edition

The **Summer 2026 edition** updates the handbook through mid-May 2026. Headline additions versus the prior revision:

- **Project Glasswing / Claude Mythos** — differential access as an emerging governance pattern for dual-use AI (Chapter 8).
- **Agent security** — prompt injection, the "lethal trifecta," and what it means for enterprise deployment (Chapter 6).
- **Export controls update** — the H200 license regime, the 25% revenue-share arrangement, and the Supermicro enforcement case (Chapters 10 and 11).
- **Industry refresh** — the OpenAI / Anthropic / xAI / Meta / Microsoft landscape and the unfolding AI IPO wave (Chapter 9).
- **Coding disruption rewrite** — the shift from IDE-assisted coding (Copilot) to headless coding agents (Codex, Claude Code) and parallel-agent workflows in which nearly 100% of new code is initially AI-generated (Chapter 12).
- **International comparisons** — EU AI Act and UK AISI as benchmarks for U.S. policy (Chapter 10).

## Files

| File | What it is |
|---|---|
| [`AI_Foundations_Summer2026.md`](AI_Foundations_Summer2026.md) | Current edition, Markdown source |
| [`AI_Foundations_Summer2026.html`](AI_Foundations_Summer2026.html) | Current edition, rendered HTML (with on-screen sidebar TOC; print-optimized) |
| [`CHANGELOG_Summer2026.md`](CHANGELOG_Summer2026.md) | Per-chapter narrative log of every change vs. the prior edition |
| [`UPDATE_PLAN_Summer2026.md`](UPDATE_PLAN_Summer2026.md) | Planning document used to scope the Summer 2026 update |
| [`AI_Foundations_Revised.md`](AI_Foundations_Revised.md) | Prior edition (baseline for the Summer 2026 diff) |
| [`AI_Foundations_Print.html`](AI_Foundations_Print.html) | Prior edition, rendered |
| [`AI_Foundations_for_Policymakers.pdf`](AI_Foundations_for_Policymakers.pdf) | Prior edition, PDF |
| [`_build_html.py`](_build_html.py) | Markdown → HTML converter used to produce the rendered handbook |

## Rebuilding the HTML

After editing the Markdown source:

```bash
python3 _build_html.py
```

The script reads `AI_Foundations_Summer2026.md` and writes `AI_Foundations_Summer2026.html` in place. No external dependencies — standard library only.

## Reading

Open `AI_Foundations_Summer2026.html` in any browser. A fixed sidebar table of contents tracks the current chapter as you scroll on viewports ≥ 1100px wide; on narrower screens, a floating "Contents" button opens the same TOC as a drawer. Both are hidden in the print view, so the document prints (or exports to PDF via the in-page button) as a clean letter-size handbook.
