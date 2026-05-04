---
name: nexor-outreach-guide
description: Master operating guide for how an AI assistant uses workflowskill, cold-outreach, and humanizer together for Nexor AI sales outreach. Governs how all three skills interact. Load when the user asks about the end-to-end process, how the skills connect, or needs a combined workflow guide.
---

# Nexor AI — AI Assistant Outreach Operating Guide
## How to Use All 3 Skills Together

---

## GOVERNING DOCUMENTS

This guide derives from:
- **Nexor Operating System v1.1** — constitutional layer
- **Nexor AI Usage Policies v1.0** — AI governance
- **Nexor Brand & Communication Guidelines v1.0** — voice and tone

Where any content in the skills contradicts these documents, the OS wins.

---

## TIER 2 REMINDER

Cold outreach emails are **Tier 2** under the Nexor AI Usage Policy:
> *"Communications sent on behalf of Nexor to external parties — use AI, but a human Nexor reviews and approves before the output leaves Nexor."*

Every email produced by this workflow must be reviewed and approved by a human Nexor before sending. The reviewing human is accountable for the final output.

---

## SKILL LOAD ORDER

```
1. workflowskill       → product knowledge + cross-reference
2. cold-outreach       → writing framework + quality rules
3. humanizer           → AI-pattern removal pass
4. nexor-outreach-guide → governs how all 3 interact
```

---

## THE FULL PIPELINE

```
TRIGGER — user provides prospect name / title / company / URL
     │
     ▼
PHASE 1 — RESEARCH [workflowskill]
Fetch LinkedIn / company website if URL provided.
Collect: name, title, company, industry, context.
     │
     ▼
PHASE 2 — MATCH [workflowskill]
Cross-reference table → one department + one pain point.
     │
     ▼
PHASE 3 — BUILD [cold-outreach]
Select: greeting · hook formula · outcome formula
Select: delivery mode · HRDC line · soft CTA
     │
     ▼
PHASE 4 — WRITE [cold-outreach]
Write full email following all body rules and guardrails.
     │
     ▼
PHASE 5 — QUALITY CHECK [cold-outreach]
Run 15-point checklist. Fix every failure.
     │
     ▼
PHASE 6 — HUMANIZER PASS [humanizer]
Scan banned words, phrases, patterns.
Check human texture. Score must be 🟢.
     │
     ▼
PHASE 7 — DELIVER [cold-outreach]
Output in standard format.
Flag Tier 2 — human review required.
     │
     ▼
PHASE 8 — FOLLOW-UP & CRM [workflowskill / cold-outreach]
Log email sent in CRM.
If no reply after 4 days, generate follow-up adding new value.
```

---

## PHASE INSTRUCTIONS

### PHASE 1 — RESEARCH

1. Check what the user provided
2. LinkedIn URL provided → fetch profile immediately
3. Company website provided → fetch it immediately
4. Extract 4 data points: name + title · company + industry · context · value metric
5. If name and title missing → ask before proceeding
6. Never write without at minimum name, title, and company

### PHASE 2 — MATCH

1. Open workflowskill cross-reference table
2. Match industry + size + structure → department
3. Select one pain point from that department's current state
4. Confirm pain is: felt daily or weekly · relevant to their title · specific enough to name in one sentence

Decision rules:
- Title reveals a function → lead with that department
- Two equal pains → pick the one felt more frequently
- Company context reveals a trigger → tie pain to that event
- No clear match → default to HR (most universal opener)

### PHASE 3 — BUILD

Select in this order:
1. Greeting → match to seniority and LinkedIn tone
2. Hook formula → based on data available (see decision tree)
3. Outcome formula → match to pain angle
4. KPI example → from KPI bank, must be picturable
5. HRDC line → match delivery mode to company type (default to ultra-short)
6. CTA → default to "Let me know if it's useful."

### PHASE 4 — WRITE

**KILL THE 5-PART SKELETON.**
Use the new paradigm: Blunt + One Human Touch. Do not write a "pain bridge".

```
[Name],
[One line of real context OR human hedge] + [Direct Question or Blunt statement of what we do]
[Friction Remover — ultra short]
[Soft CTA]
— [Name], Nexor AI
```

Apply all 10 guardrails while writing:
No em-dashes · No bio quoting · 5th grade language · No assumptions as facts · Hook to outcome connected · AI named · No Nexor banned words · Spoken not written · No constructed benefit sentences · One human hedge

### PHASE 5 — QUALITY CHECK

Run all checklist items. Do not proceed until all pass.
Most common failures: padding to hit word count · constructed benefit sentences · passive voice in outcome · Nexor banned word in body · too confident (no hedge)

### PHASE 6 — HUMANIZER PASS

4 checks:
1. Banned words — no Tier 1 AI giveaways
2. Banned phrases — "serves as", "in order to", "moving forward", etc.
3. Banned patterns — no significance inflation, no sycophancy
4. Human texture — varied sentence lengths, contractions, read-aloud test

Score target: 🟢 under 25.

### PHASE 7 — DELIVER

Standard format with word count, humanizer score, and Tier 2 flag.

### PHASE 8 — FOLLOW-UP & CRM

Single emails rarely close deals. All activity must be logged in a CRM.

**1. The Follow-Up Cadence:**
- **Day 1:** Initial Outreach (Blunt + Human Touch)
- **Day 4:** The Value-Add Follow-Up
- **Day 9:** The Pain-Pivot Follow-Up
- **Day 14:** The Break-Up Follow-Up

**2. Follow-Up Rules:**
- Never send "just bubbling this up" or "touching base".
- Always use the specific formulas from `cold-outreach` STEP 8.

**3. CRM Logging:**
- After every email generation, run the `crm` skill to generate a structured block of data for the user to copy/paste directly into their CRM (Zoho/HubSpot).

---

## DECISION TREES

### Which Greeting?
```
C-suite or Director level?
├── YES → "Hello [Name],"
└── NO
    Short, direct email?
    ├── YES → "[Name]," (name only — feels like a real message)
    └── NO
        Casual informal LinkedIn posts?
        ├── YES → "Hey [Name]," (sparingly)
        └── NO → "Hi [Name]," (default)
```

### Which Hook Formula?
```
Can you ask one specific question about their daily workflow?
├── YES → Formula 6 (Direct Question) — PREFERRED
└── NO
    Know their title + can name their daily frustration?
    ├── YES → Formula 1 (Title + Daily Reality)
    └── NO
        Specific company event (expansion, new contract)?
        ├── YES → Formula 2 (Company Context + Consequence)
        └── NO
            Industry pain strong and universal?
            ├── YES → Formula 5 (Abrupt Observation)
            └── NO → Ask user for more context

⚠️ Avoid Formula 3 ("Most [titles] say the same thing") —
it is now a recognizable AI pattern. Use Direct Question instead.
```

### Which Outcome Formula?
```
Solution simple enough to state as fact?
├── YES → Formula F (Just Say What You Do) — PREFERRED
└── NO
    Solution is new — needs to be pictured first?
    ├── YES → Formula A (Imagine If)
    └── NO
        Prospect stuck in a manual loop?
        ├── YES → Formula B (What If) — use sparingly, becoming overused
        └── NO
        ├── YES → Formula E (Before and After)
        └── NO → Formula C (Direct Outcome)
```

### Which Delivery Mode?
```
Large enterprise (500+ staff)?
├── YES → In-house (Nexor AI Institute comes to you)
└── NO
    Outside Klang Valley?
    ├── YES → Online
    └── NO
        Cost-sensitive?
        ├── YES → Online
        └── NO → Generic HRD Corp line, no delivery mode specified
```

### Which Department?
```
Title reveals specific function?
├── YES → Lead with that department
└── NO
    Cross-reference table gives clear match?
    ├── YES → Lead with that department
    └── NO (two equal options)
        Which pain is felt more frequently?
        ├── One daily, one monthly → lead with daily
        └── Equal → default to HR
```

---

## GOOD EMAIL vs FAILING EMAIL

### Good ✅

```
Subject: Running HR and training at once at Berjaya Times Square

Hi Roslina,

Most people doing both HR and training in a hotel say the admin
side of training eats into time meant for actual training.

What if an AI chatbot answered new hire questions on leave,
claims, and hotel policy on its own so you spent more time on
the work that actually needs you in the room?

As an HRD Corp accredited trainer you already know your levy
covers this — we just help your team build it.

Reply "yes" if this sounds useful.

— [Name], Nexor AI
```

Why it works: Hook from title not bio · Pain is daily · AI named · Human keeps judgment ("actually needs you in the room") · HRDC line connects naturally · No em-dashes · No Nexor banned words · Plain language

---

### Failing ❌

```
Subject: Exciting AI Transformation Opportunity!

Hi Roslina, hope this email finds you well!

Your 'People-first leader' bio really resonated with me.

At Nexor AI, we leverage cutting-edge AI-powered solutions to 
seamlessly streamline your end-to-end HR workflows and empower 
your workforce to achieve transformative outcomes.

We'd love to schedule a 30-minute discovery call.
```

Why it fails:
- "Transformation", "leverage", "cutting-edge", "seamlessly", "empower", "transformative" — all Nexor banned words
- Bio quoted — invasive
- Generic opener — banned
- Hard CTA — 30 minutes from a cold contact
- No AI named specifically
- No HRDC line
- Passive framing throughout

---

## COMMON MISTAKES AND FIXES

| Mistake | Fix |
|---|---|
| Nexor banned words in body | Check full banned list before delivering |
| Bio quoted in hook | Anchor to title and industry role |
| Em-dash in body | Full stop or comma |
| Word count over 65 | Cut weakest sentence — usually pain bridge |
| AI not named | Add "AI chatbot" or "AI" to outcome sentence |
| HRDC line feels bolted on | Connect it to what was just said in the outcome |
| Two pain points | Pick the one felt most frequently, delete the other |
| Hard CTA | Replace with "Reply yes" or "Worth a quick look?" |
| Passive voice | Rewrite: "AI handles" not "is handled by AI" |
| Assumptions as facts | "Most [titles] I speak to..." not "Your company does X" |
| Forgot Tier 2 flag | Always include in output — human must review before sending |

---

## QUICK REFERENCE

| Task | Skill |
|---|---|
| Understand Nexor AI product | workflowskill |
| Match company to department | workflowskill |
| Select pain point | workflowskill |
| Check Malaysian market hooks | workflowskill |
| Select greeting | cold-outreach |
| Select hook formula | cold-outreach |
| Write email | cold-outreach |
| Select outcome formula and KPI | cold-outreach |
| Select HRDC + delivery line | cold-outreach |
| Select CTA | cold-outreach |
| Run 15-point checklist | cold-outreach |
| Remove AI writing patterns | humanizer |
| Score human-sounding quality | humanizer |
| Deliver with Tier 2 flag | cold-outreach |

---

*Nexor AI Sdn Bhd · ASEAN's AI Capability Stack Architect*
*We don't sell hype. We deliver capability.*
*Outreach Guide v1.2 — April 2026 — Derived from Nexor OS v1.1*
