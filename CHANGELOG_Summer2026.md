# Changelog — AI_Foundations_Summer2026.md

Tracks every substantive edit from the `AI_Foundations_Revised.md` baseline. Read this alongside a diff of the two files (`diff AI_Foundations_Revised.md AI_Foundations_Summer2026.md`) — this file is the narrative layer that explains *why* each change was made.

**Conventions:**
- **[Add]** new content not in the baseline
- **[Cut]** content removed from the baseline
- **[Rewrite]** material rewritten in place (substantively, not just wordsmithed)
- **[Refresh]** factual update to existing material (numbers, names, dates)
- **[Move]** content relocated to a different chapter or section

---

## Front matter / Table of Contents

*(pending — will be updated after all chapter edits)*

---

## Chapter 6 — Reasoning Models

### [Add] New subsection — "Agent Security"
- **Inserted:** after "From Chatbot to Agent," before Key Takeaways.
- **Length:** ~380 words (within the ≤400-word target).
- **Content:**
  - Prompt injection defined and framed as the defining agent vulnerability; the data-vs-instructions confusion that makes it possible.
  - The "lethal trifecta" framing (untrusted content + private data + external communication).
  - Microsoft's May 2026 disclosure that prompt injection in agent frameworks can escalate to host-level RCE.
  - The 82%-confidence-vs-14%-approved deployment gap from early-2026 industry surveys.
  - Three mitigations: least privilege, human-in-the-loop for high-risk actions, provenance and isolation.
  - Policy framing: agent deployment is increasingly a cybersecurity policy question; existing disclosure / liability / procurement frameworks will need to extend faster than current regulatory cycles allow.
- **Tone:** neutral/descriptive, no named vendors as villains.

### [Add] Key Takeaways — agent-security bullet
- Added a sixth bullet noting agent security as a first-order policy concern.

---

## Chapter 7 — The Alignment Problem

### [Refresh] "Mesa-optimizers / alignment-faking" paragraph
- Reworded to reflect that alignment-faking has moved from theoretical concern to documented empirical phenomenon in 2025–26 frontier-model research, while noting that prevalence and severity remain contested.

### [Add] Forward reference in "Open vs Closed" paragraph
- Added a new closing sentence noting that **differential or gated access** has emerged as a third release model, with a forward-reference to Chapter 8's Project Glasswing discussion.

---

## Chapter 8 — Safety Beyond Misalignment

### [Add] New paragraphs — "Differential access as a governance experiment" (under Institutional Preparedness)
- **Placement:** within the existing "Institutional Preparedness" subsection, after "Balancing innovation and precaution," before Key Takeaways. Per user instruction.
- **Length:** ~330 words across three paragraphs.
- **Content:**
  - **Paragraph 1:** Anthropic's April 2026 Claude Mythos Preview, its autonomous vulnerability-discovery capability (OpenBSD / FFmpeg examples), and Project Glasswing as an invite-only release framework with named launch partners (AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks).
  - **Paragraph 2:** the conceptual placement of Glasswing as a governance mechanism between "publish everything" and "never release," its kinship with traditional coordinated-disclosure norms, and the UK AISI's independent pre-release evaluation as illustration of evaluator-body function (cross-reference to Ch. 10).
  - **Paragraph 3:** observations worth carrying forward — concentration of defensive advantage among already-resourced organizations; the short access window demonstrated by Microsoft's multi-agent system surpassing Mythos on benchmark within weeks; the open question of whether the pattern generalizes to other dual-use capabilities.
- **Tone:** neutral/descriptive, framed as an illustration of defensive AI per user instruction. No editorial verdict.

### [Add] Key Takeaways — differential-access bullet
- Added a seventh bullet on differential access as an emerging release pattern.

---

## Chapter 9 — The AI Industry Landscape

### [Rewrite] OpenAI profile
- **Cut:** the "$10B+ Microsoft investment" framing, "Sam Altman calling for regulation" anecdote, "iterative deployment" line.
- **Added:** ~$25B annualized revenue (mid-2026); ~$852B valuation; Q4 2026 IPO trajectory; restructured (non-exclusive) Microsoft partnership; multi-billion-dollar "Deployment Company" acquisition vehicle.
- **Why:** OpenAI's commercial trajectory and the changed Microsoft relationship are the most consequential facts about the company that the baseline didn't capture.

### [Refresh] Google DeepMind profile
- **Refreshed:** Gemini 3.x is now the production line; AlphaFold's 2024 Nobel Prize moved into the lede; "Google Brain merger" kept as historical context.
- **Cut:** speculation about "tricky spot" with internal safety dissent; replaced with neutral framing about research-vs-product tension.
- **Why:** the Nobel + Gemini 3.x are more load-bearing than the older internal-politics framing.

### [Rewrite] Anthropic profile
- **Added:** ~$19B annualized revenue; reported Q4 2026 IPO with possible ~$60B raise; ~$1.5B deployment-services vehicle; forward-reference to the Mythos / Project Glasswing discussion in Chapter 8.
- **Cut:** "Anthropic has testified in U.S. Congress about bio-risk" (still true but vintage); "their motto is to scale AI cautiously" (replaced with the operationalized-safety framing via Mythos).
- **Why:** Anthropic's scale and the Mythos/Glasswing experiment are the two facts a 2026 policymaker most needs.

### [Rewrite] Microsoft (in "Others")
- **Cut:** "basically a commercialization arm for OpenAI's models"; Nadella "co-pilot for every user" quote.
- **Added:** Microsoft's pivot to independent frontier capability, evidenced by its multi-agent cybersecurity system surpassing Mythos on benchmark in May 2026; framing of the non-exclusive OpenAI partnership as formalizing the shift.
- **Why:** the most significant 2025–26 change in Microsoft's strategic posture is that it is no longer just a reseller.

### [Rewrite] Meta (in "Others")
- **Cut:** the "open-source advocate, Zuckerberg less concerned about existential risk" framing.
- **Added:** Superintelligence Labs under Alexandr Wang (post-Scale AI acquisition); $115–135B 2026 AI capex; Muse Spark as flagship; note that flagship is *not* fully open-weight even though Meta still releases smaller models openly.
- **Why:** Meta's position on open-source has shifted in a structurally meaningful way that the baseline misses.

### [Rewrite] xAI (in "Others")
- **Cut:** generic "rapidly scaled to become a frontier AI lab" line.
- **Added:** February 2026 merger with SpaceX; framing as a structurally novel arrangement (launch capacity + frontier lab + X distribution + unusual capital base).
- **Why:** the SpaceX merger is the single most important fact about xAI's 2026 posture.

### [Refresh] China's AI sector (in "Others")
- **Cut:** "Sputnik moment" framing of DeepSeek.
- **Added:** the H200 license clearances and Beijing's counter-instruction not to take delivery; forward-reference to Chapter 10 for detail; emphasis on continued Cyberspace Administration of China content registration.
- **Why:** the H200 license episode is the most live piece of the China story in mid-2026.

### [Light refresh] Hardware and Cloud bullets
- Mostly preserved; tightened language. ASML chokepoint and CUDA moat retained.

### [Rewrite] Closing paragraphs of "Research Labs Leading the Charge"
- **Cut:** the meandering "Policymakers might leverage this structure…" paragraph and the "We should mention regulatory bodies forming…" paragraph (the latter's content is now better covered in the Industry Orgs paragraph and Chapter 10).
- **Added:** a more focused two-paragraph synthesis of (a) concentration's safety-vs-market-power tradeoff and (b) the existence of joint cross-lab alignment evaluations as an informal but real governance mechanism.

### [Refresh] Industry orgs paragraph
- **Cut:** the "even competitors know cooperation is needed" stock line.
- **Added:** the UK AISI / U.S. CAISI / EU equivalents as a transnational evaluator network. (CAISI is also discussed in Ch. 10, intentionally cross-referenced.)

### [Add] New subsection — "The IPO Wave"
- **Why:** the user requested a short standalone coda contextualized by the secondary-market run-up and the exhaustion of private capital.
- **Content:** two paragraphs. First paragraph: facts about valuations (OpenAI ~$852B; Anthropic in IPO-prep), private-capital strain, the labs targeting late-2026 listings, xAI/SpaceX as an analogous-but-different move. Second paragraph: the policy implication—public-company disclosure, securities-fraud exposure, and the tension with the "voluntary commitments" governance model.

### [Cut] Concentration synthesis paragraph
- **Cut:** the "Only a few firms or alliances..." paragraph (the safety-vs-market-power synthesis after the "Others" bullets).
- **Why:** user feedback — paragraph was synthesis/commentary rather than load-bearing fact, and the Key Takeaways carry the same points in compressed form.

### [Cut] IPO Wave — second paragraph
- **Cut:** the "For policymakers, the IPO wave matters..." paragraph (securities disclosure / voluntary commitments tension).
- **Why:** user feedback — keeps the IPO Wave to a short factual coda. Kept the first paragraph (the run-up facts and IPO trajectory).

### [Cut] "Regulatory Efforts" subsection
- **Cut:** the entire "Regulatory Efforts" subsection from Chapter 9 (EU AI Act paragraph, U.S. voluntary commitments / NIST paragraph, CAISI / AI Action Plan paragraph).
- **Why:** user feedback — regulatory content is misplaced in an industry-landscape chapter. The U.S. material (CAISI, AI Action Plan) is already covered in Chapter 10. The EU AI Act paragraph has been removed pending a decision on whether to relocate it to Chapter 10 (as a brief international comparison) or cut entirely.

### [Rewrite] Key Takeaways
- All five bullets rewritten to reflect the updated lab profiles, the H200 license regime, the IPO wave, and the changed Microsoft / Meta posture. Old bullets that talked about "How to bring Chinese players into a global safety fold" replaced with sharper language about a contested international dynamic.

---

## Chapter 10 — US AI Policy

### [Refresh] "Effectiveness and challenges" paragraph (Export Controls)
- **Refreshed:** "30x compute advantage" reframed as a 2024–25 baseline; added Thailand as a transshipment node example (to set up the Supermicro case).

### [Add] New paragraph — "The 2025–26 license shift" (Export Controls)
- **Why:** the H200 license regime is the most consequential 2026 change to export-control policy.
- **Content:** December 2025 announcement of revenue-sharing approach; January 2026 BIS rule with the 25% revenue share, 75,000-chip cap, security-procedure / non-military-use conditions; May 2026 clearance of ~10 Chinese firms (Alibaba, Tencent, ByteDance, JD.com, Lenovo, Foxconn); Beijing's counter-instruction to delay purchases; framing as "tax and trace" rather than denial.

### [Add] New paragraph — "Enforcement: the Supermicro case" (Export Controls)
- **Why:** the most significant real-world test of Entity List enforcement to date.
- **Content:** March 2026 arrest of Supermicro co-founder Wally Liaw; $2.5B alleged scheme; Thailand-based front entity; $500M shipped in mid-2025; staged dummy servers; Alibaba as reported end-buyer; Supermicro's independent investigation. Closes with the structural-vulnerability framing (chip size + value + transshipment).

### [Add] New subsection — "International Comparisons" (before Key Takeaways)
- **Why:** the EU AI Act content was relocated here from the cut Chapter 9 "Regulatory Efforts" subsection (user-approved Option 2). UK AISI added to parallel CAISI and to set up the Mythos discussion in Chapter 8.
- **Content:** three subsections —
  - **The EU AI Act:** risk-based framework, full enforcement August 2026, extraterritorial reach. Reworded from the baseline Ch. 9 paragraph for tighter framing.
  - **The UK AI Safety Institute:** sector-led approach, pre-deployment evaluations, transnational network with CAISI, Mythos Preview evaluation as illustration.
  - **Implications for U.S. policy:** brief comparison of the three regimes (EU comprehensive-but-rigid, UK nimble-but-non-binding, U.S. CAISI in between with greater industry participation); note that frontier labs design compliance around the strictest applicable rule.

### [Rewrite] Key Takeaways
- **Refreshed:** the export-controls bullet now references the H200 license regime and Supermicro alongside the Entity List.
- **Added:** a sixth bullet on international comparisons (EU / UK / U.S. as three reference points).
- Other bullets (AI Action Plan, state laws, Genesis, copyright) preserved with minor wordsmithing.

---

## Chapter 11 — China and AI Competition

### [Refresh] Hardware constraints paragraph
- Tightened tense ("Through 2025...could not legally access...") to set up the 2026 re-opening that follows.

### [Add] New paragraph — "The 2026 re-opening — and its limits"
- **Content:** the H200 revenue-sharing license regime, the ~10 cleared Chinese firms (cross-referenced to Ch. 10 for detail), Beijing's counter-instruction, and the framing that both governments now have a veto.
- **Why:** parallel update to Ch. 10; gives the China-side context for the same event.

### [Refresh] Workarounds paragraph
- **Added:** explicit reference to the March 2026 Supermicro indictment as the most prominent enforcement action; cross-reference to Ch. 10.

### [Refresh] Ascend chips paragraph (Huawei)
- Folded the "2025 targets" framing forward to "2025–26 actuals/targets"; noted that the Ascend 910D's 5nm volume production has not been confirmed as of mid-2026.

### [Add] New paragraph — "A two-sided trade" (Strategic Implications)
- **Content:** the conceptual reframe — from unilateral denial vs. evasion to a two-sided regime in which both governments hold veto power; Beijing's apparent preference to keep concessions in reserve.

### [Refresh] "Technology denial has limits" paragraph
- Reworded to incorporate the new license channel; "selectively imported American hardware" added as a third path (alongside efficiency innovations and domestic alternatives).

### [Rewrite] Key Takeaways
- **Added:** new bullet on the 2025–26 H200 license regime and the two-sided veto dynamic.
- **Refreshed:** the Huawei bullet notes the CUDA-displacement challenge; other bullets lightly tightened.

---

## Chapter 12 — AI and the Labor Market

### [Refresh] Major examples paragraph (Companies and Layoffs)
- Added a closing clause to the 55,000-job-cut figure noting that the late-2025 baseline has continued to grow through H1 2026 as enterprises move from pilots to production agent deployments.
- Other content (Amazon/Microsoft/UPS/Salesforce/IBM specifics, Klarna regret case) preserved.

### [Rewrite] The Coding Disruption section
- **Cut:** the Cursor AI paragraph (vintage — the $29B valuation and "fastest-growing SaaS" framing is no longer the defining story).
- **Cut:** the Devin paragraph (vintage — 13.86% benchmark success and "handful of successes out of twenty tasks" reflects the 2024–25 generation of autonomous coding agents).
- **Rewrote GitHub Copilot** as the "first wave — IDE assistance" baseline rather than the leading example, preserving the install-base and productivity data but reframing it as the predecessor paradigm.
- **Added: "The second wave — headless coding agents"** paragraph introducing OpenAI's Codex and Anthropic's Claude Code as the dominant 2025–26 pattern. Notes that both ship as terminal tools, IDE integrations, and web environments, and that the agents run a full autonomous loop of exploration → plan → edit → test → self-review.
- **Added: "Parallel agents and near-100% generation"** paragraph on the workflow shift to dispatching many agents in parallel, with humans acting as reviewers/integrators/architects rather than authors. Frames the change as qualitative (unit of human work shifts from lines to agent outputs) and identifies specification quality, test infrastructure, and code review as the new bottlenecks.
- **Refreshed the METR task horizon paragraph** to connect the doubling cadence specifically to the headless-agent paradigm being itself transitional toward longer-horizon tasks.

### [Rewrite] Key Takeaways — "Coding is the leading indicator"
- Rewrote the bullet to reflect the two-year arc from Copilot → headless agents → parallel-agent / 100%-AI-generation workflows, and the shift in human work from author to reviewer/integrator.

---

## Chapter 13 — AI and Scientific Discovery

### [Add] New paragraph — "Status as of mid-2026" (under The "Compressed Century" Thesis)
- **Why:** Amodei's October 2024 essay predicted "powerful AI" could arrive "as early as 2026." We are now in that window, so the chapter benefits from a brief status check.
- **Content:** notes the arrival of autonomous research agents (Kosmos), Evo line, continued AlphaFold adoption, and the first AI-solved Erdos problems as evidence of meaningful narrow-domain acceleration; observes that the broad biomedical breakthroughs (cancer, infectious disease, Alzheimer's) Amodei described have not arrived; frames the 5–10-year window as still open but unresolved.

### Other Ch. 13 content (AlphaFold, Arc Institute, Erdos, Kosmos)
- Preserved as-is. The user requested chapter-length balance; Ch. 13 was already in good shape factually, so only the Compressed Century status check was added.
