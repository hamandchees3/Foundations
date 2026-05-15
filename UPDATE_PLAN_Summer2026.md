# AI Foundations — Summer 2026 Update Plan

**Source:** `AI_Foundations_Revised.md` → **Working copy:** `AI_Foundations_Summer2026.md`
**Date drafted:** May 14, 2026
**Scope:** Chapter 6 onward. Adds four priority threads — Mythos & differential access for cyber, agent security, export controls (H200 licenses + Supermicro), and industry refresh — plus light touch-ups elsewhere.

---

## Priority threads (cross-cutting)

These are the four user-requested updates. Each gets a "primary home" chapter and lighter callouts where relevant.

### Thread 1 — Mythos and differential access for vulnerability discovery
- **Primary home:** New section in **Chapter 7 (Alignment)** *or* **Chapter 8 (Safety Beyond Misalignment)**. Recommend Ch. 8, because the policy question (who gets a dual-use tool first) is fundamentally a societal/governance issue rather than a values-alignment one. A short forward-reference from Ch. 7's "open vs. closed" section keeps the framing intact.
- **What to cover:**
  - Anthropic's April 2026 announcement of Claude Mythos Preview, with autonomously discovered zero-days across major OSes/browsers (e.g., the 27-year-old OpenBSD bug, 16-year-old FFmpeg bug).
  - **Project Glasswing** as the access-control mechanism: invite-only release to ~12 launch partners (AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks), restricted to cybersecurity use.
  - **The differential-access concept**: defenders get a capability window before the same capability becomes broadly available to attackers. Frame as an emerging governance pattern that may apply to other dual-use AI capabilities (bio, cyber-physical).
  - **The critique worth airing:** concentration risk — the best-defended orgs get the tool first; SMEs, regional infrastructure, and industrial systems remain exposed. Also: Microsoft's competing multi-agent system topped Mythos on a leading benchmark within weeks, suggesting the window of differential access is short.
- **Policy framing:** present differential access as one model on a spectrum — between "publish everything" (open release) and "never release" (capability withholding). Note the analogy to coordinated vulnerability disclosure norms in traditional security.

### Thread 2 — Agent security
- **Primary home:** New section in **Chapter 6** (which already introduces agents but stops at capability), with a policy-flavored callback in Ch. 7 or Ch. 10.
- **What to cover:**
  - **Prompt injection has graduated from theory to tier-one risk.** Indirect prompt injection (hidden instructions in web pages, documents, emails) is now being exploited in the wild against production agents.
  - **The "lethal trifecta"** framing: an agent with (a) access to untrusted content, (b) access to private data, and (c) ability to communicate externally is one prompt injection away from data exfiltration.
  - **RCE escalation:** Microsoft's May 2026 disclosure that prompt injection in agent frameworks (e.g., Semantic Kernel) can cross into host-level remote code execution once tools are wired up.
  - **The deployment gap:** 82% of executives confident their policies cover agents; only ~14% of orgs ship agents with full security/IT sign-off.
  - **Mitigations:** least-privilege tool access, human-in-the-loop for high-risk actions, runtime monitoring, content provenance.
- **Connection to Mythos:** the same capability that lets defenders find zero-days lets agents exploit them — agent security and Mythos-style discovery are two faces of the same offensive-capability frontier.

### Thread 3 — Export controls update (H200 licenses + Supermicro)
- **Primary home:** **Chapter 10 ("Export Controls: The Hardware Chokepoint")** and **Chapter 11 ("The Impact of Export Controls")** — these need parallel updates.
- **H200 license shift (Ch. 10 + Ch. 11):**
  - December 2025: Trump administration announces H200 exports to China will be allowed under a ~25% revenue-sharing arrangement (chips routed through US territory).
  - January 13, 2026: Commerce formalizes the rule. Buyers must demonstrate security procedures and non-military use; each customer capped at 75,000 chips.
  - May 14, 2026: ~10 Chinese firms cleared (Alibaba, Tencent, ByteDance, JD.com; distributors include Lenovo and Foxconn).
  - **The twist:** Beijing has reportedly told Chinese firms to hold off; **zero deliveries** had occurred as of mid-May 2026. So a "controlled re-opening" has run into a buyer-side blockade, complicating both sides' narratives.
  - **Policy framing:** this is a significant shift from the 2022–2025 posture of strict denial — the new model is "tax and trace" rather than "block." It also changes the analytic frame in Ch. 11: the compute-advantage estimate ("~30x") will need a footnote about the new regime, even if deliveries remain blocked.
- **Supermicro scandal (Ch. 10):**
  - March 19, 2026: Supermicro cofounder Yih-Shyan "Wally" Liaw arrested, charged with running a $2.5B scheme to divert Nvidia-equipped servers to China via a Thailand-based front entity (allegedly delivering to Alibaba and others).
  - Tradecraft details worth including: ~$500M shipped over a three-week window in mid-2025; thousands of staged dummy servers used to deceive compliance auditors.
  - Supermicro itself launched an independent probe in April 2026; the company is not named as a defendant but is "under the microscope."
  - **Why it matters policy-wise:** the case is the highest-profile real-world test of Entity List / export-control enforcement to date. It validates concerns about transshipment through Southeast Asia and raises the question of whether large OEMs need stricter end-use diligence requirements. Pair it with the existing "third-country transshipment" concern in Ch. 10 to show enforcement is happening but the underlying vulnerability is structural.

### Thread 4 — Industry refresh (Chapter 9)
- **Primary home:** Rewrite of **Chapter 9 ("Research Labs Leading the Charge")**, including its "Others" subsection.
- **Updates by company:**
  - **OpenAI:** Now valued around $852B; >$25B annualized revenue; targeting Q4 2026 IPO (caveats: not yet meeting public-reporting standards). Note the new non-exclusive Microsoft partnership structure. Add the "Deployment Company" investment vehicle (~$4B raised).
  - **Anthropic:** ~$19B annualized revenue; widely expected Q4 2026 IPO with rumored ~$60B raise. Has a parallel deployment-services vehicle (~$1.5B). Mythos/Glasswing positioning reinforces its safety-brand strategy.
  - **Google DeepMind:** Gemini 3.1 Pro and Flash-Lite (Feb/Mar 2026). Continued multi-product integration; touch up.
  - **Meta:** $115–135B 2026 AI capex. **Superintelligence Labs** under Alexandr Wang (post-Scale AI acquisition). Flagship model **Muse Spark** released; reframes Meta from "open-source advocate" to "open-source advocate with a closed flagship." This is a significant repositioning worth flagging.
  - **xAI:** Major change — **merged with SpaceX in February 2026**. New combined entity bundles launch capacity, frontier AI lab, and X social platform. Grok 4.20 Beta 2 (March 2026).
  - **Microsoft:** Restructured (non-exclusive) OpenAI partnership; own Muse-style internal frontier work; multi-agent cyber system (the one that beat Mythos on the benchmark) shows MSFT is building a competing frontier capability rather than just reselling.
  - **DeepSeek / Chinese labs:** Carry forward, but flag that the H200 re-opening (if/when deliveries resume) changes the hardware constraint story.
- **Add a new short subsection on IPO/financialization** — 2026 is shaping up as the AI IPO wave (OpenAI, Anthropic, possibly others). Policymakers should understand that public-market accountability is about to enter the frame, with implications for disclosure, governance, and the "voluntary commitments" model.

---

## Chapter-by-chapter changelog

| Ch. | Current title | Status | Key edits |
|---|---|---|---|
| 6 | Reasoning Models | **Update** | Add "Agent Security" section after "From Chatbot to Agent." Refresh task-horizon numbers if METR has published 2026 update. |
| 7 | The Alignment Problem | **Light update** | Tighten "deceptive alignment" section (point to 2025–26 alignment-faking research). Forward-reference Ch. 8 differential-access discussion in the "Open vs Closed" paragraph. |
| 8 | Safety Beyond Misalignment | **Add new section: "Dual-Use Capabilities and Differential Access"** | This is the natural home for Mythos/Glasswing. Frame as a new governance pattern alongside child-safety, mental-health, institutional-preparedness. Update Sewell Setzer aftermath if new rulings since early-2026 settlement. |
| 9 | AI Industry Landscape | **Major rewrite** | See Thread 4. Refresh every lab. Add IPO subsection. Reframe Meta. Rewrite xAI as SpaceX-merged. Refresh the Microsoft narrative. |
| 10 | US AI Policy | **Major update to Export Controls section** | H200 license regime (Dec 2025/Jan 2026/May 2026). Supermicro case. The "25% revenue share" model is itself novel and worth describing as a policy innovation. Verify state-law sections (CA SB 53, NY RAISE Act, IL HB 1806) haven't been amended. Check Genesis Mission for any new milestones since 270-day window. |
| 11 | China and AI Competition | **Update** | Add the H200 re-opening as a structural shift. Reframe stockpile/compute-gap discussion. Verify Huawei Ascend / SMIC numbers — likely 1–2 generations more recent now. Note Beijing's apparent counter-move (telling firms not to buy approved H200s) as a new dimension of the competition. |
| 12 | AI and the Labor Market | **Light refresh** | Update layoff totals through mid-2026 (the 55K figure was end-of-2025). Check whether the METR doubling cadence has been re-measured. The "regret factor" data may have grown with a year more evidence. |
| 13 | AI and Scientific Discovery | **Light refresh** | Check for new Erdos problems solved; new Arc Institute releases past Evo 2; new Kosmos updates. Amodei's 2026 timeline is now arriving — worth a short status-check paragraph: which of his predictions are tracking, which aren't. |

---

## Execution sequence (suggested)

1. **Chapter 9 first.** It's the most factually stale and the foundation for accurate framing in Ch. 10–11.
2. **Chapter 10 + 11 together.** The export-control story is one narrative split across two chapters; do them in one pass to keep the framing consistent.
3. **Chapter 6 (agent security insert).** Self-contained; can be done in isolation.
4. **Chapter 8 (Mythos/Glasswing insert).** Self-contained; can be done in isolation. Verify forward-references from Ch. 7.
5. **Chapters 7, 12, 13.** Light refresh pass.
6. **Final pass:** check all hyperlinks resolve; update the Table of Contents on lines 13–30; bump the "as of" date if there's one in the front matter.

---

## Open questions for you

1. **Tone on Mythos/Glasswing:** present as a model worth emulating, a model worth critiquing, or both-sides neutral? My draft assumes both-sides neutral with the concentration critique surfaced.
2. **Chapter 9 IPO subsection:** worth its own subsection, or fold into each lab's profile? I'd suggest a short standalone subsection since the IPO wave is a *systemic* development.
3. **Agent security depth:** policymaker-level (≈400 words, conceptual) or practitioner-level (≈800 words with the lethal-trifecta diagram and named CVEs)? Default is policymaker-level.
4. **Mythos in Ch. 7 vs. Ch. 8:** I recommend Ch. 8. Open to Ch. 7 instead if you'd rather frame it as an alignment governance question.
5. **Anything to *cut* from chapters 6+ to make room?** Some 2024-vintage examples (Sewell Setzer specifics, early SB 1047 detail) could be tightened.
