---
name: humanizer
description: Detect and remove AI writing patterns from any Nexor AI output before it leaves the company. Always run as the final pass on cold emails and outreach messages. Trigger whenever the user asks to humanize, de-AI, make text sound natural, or check if something sounds robotic. Also trigger automatically after cold-outreach produces a draft. Based on brandonwise/humanizer and Nexor Brand Guidelines banned words list.
---

# humanizer — AI Writing Pattern Remover
## Final Pass Before Any Email Goes Out

---

## WHAT THIS SKILL DOES

Scans text for patterns that signal AI-generated writing and removes them.
Runs as the final step before delivery — after cold-outreach produces a draft.
Target score: 🟢 under 25 (mostly human-sounding).

Also cross-checks against the **Nexor Brand Guidelines banned words list** — any Nexor banned word is an automatic fail regardless of AI score.

---

## THE 4-PART CHECK

Run all 4 parts on every draft.

---

### PART 1 — BANNED WORDS

**Nexor Brand Banned Words (from Brand Guidelines — automatic fail):**
```
Synergy · Leverage (as a verb) · Disrupt · Revolutionary
Cutting-edge · Best-in-class · End-to-end solution · World-class
Unlock potential · Game-changing · Seamless · Transformative
Empower · Next-generation · Paradigm shift · Future-proof
Holistic · Robust (when we mean "works") · Ecosystem (when we mean "our tools")
Journey (when we mean "project")
```

**AI Writing Tier 1 — Dead Giveaways (always replace):**
```
delve · tapestry · vibrant · crucial · comprehensive
meticulous · embark · groundbreaking · robust · seamless
paradigm · multifaceted · myriad · cornerstone · reimagine
catalyst · bolster · spearhead · invaluable · bustling
nestled · realm · showcase · foster · garner
interplay · enduring · pivotal · intricate · harness
unleash · revolutionize · elucidate · encompass · holistic
utilize · facilitate · nuanced · transformative · paramount
poised · empower
```

**AI Writing Tier 2 — Suspicious (flag if used more than once):**
```
furthermore · additionally · notably · ultimately
significantly · innovative · cutting-edge · state-of-the-art
streamline · optimize · scalable · impactful · actionable
dynamic · proactive
```

---

### PART 2 — BANNED PHRASES

**AI fingerprint phrases — replace immediately:**

| Replace | With |
|---|---|
| "plays a crucial role" | "matters" or just say what it does |
| "serves as a testament" | "shows" or "proves" |
| "serves as" | "is" |
| "in the realm of" | "in" |
| "delve into" | "look at" |
| "harness the power of" | "use" |
| "embark on a journey" | "start" |
| "It is worth noting that" | just say it |
| "It is important to note that" | just say it |
| "At the end of the day" | cut it |
| "Moving forward" | cut it |
| "Going forward" | cut it |
| "Touch base" | "talk" |
| "Circle back" | "follow up" |
| "Game changer" | say what specifically changes |
| "In order to" | "to" |
| "Due to the fact that" | "because" |
| "In the event that" | "if" |
| "At this point in time" | "now" |
| "With regard to" | "about" |
| "Looking forward to hearing your thoughts" | replace with a clear next step |

**Also check for Nexor writing rule violations:**
- "very", "really", "actually", "basically", "literally" → remove
- Sentences over 25 words → split them
- Claims without evidence → add evidence or remove the claim

---

### PART 3 — BANNED PATTERNS

| # | Pattern | What It Looks Like | Fix |
|---|---|---|---|
| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..." | State the fact. Skip the drama. |
| 2 | **Vague attributions** | "Experts believe..." "Studies show..." | Name the source or drop the claim. |
| 3 | **Superficial -ing tails** | "...showcasing the importance of collaboration..." | Make it its own sentence. |
| 4 | **Copula avoidance** | "serves as" "functions as" "acts as" | Use "is" or "has". |
| 5 | **Negative parallelism** | "It's not just X, it's Y" | Just say Y. |
| 6 | **Rule of three lists** | "innovation, inspiration, and insights" | Use one strong word. |
| 7 | **Em-dash overuse** | too many — em dashes | Full stop or comma. |
| 8 | **Sycophantic opener** | "Great question!" "Absolutely!" | Delete. Just answer. |
| 9 | **Chatbot artifacts** | "I hope this helps!" "Let me know if..." | Delete entirely. |
| 10 | **Generic conclusion** | "The future looks bright." | End with a specific fact or action. |
| 11 | **Excessive hedging** | "could potentially possibly perhaps" | Pick one or drop them all. |
| 12 | **Formulaic challenge** | "Despite challenges, X continues to thrive." | Say what the actual challenge is. |

---

### PART 4 — HUMAN TEXTURE CHECK

| Quality | Check | Fix If Missing |
|---|---|---|
| **Burstiness** | Sentence lengths vary | Break up 3 sentences of similar length |
| **Vocabulary variety** | Same word not repeated within 3 sentences | Find a plain synonym |
| **Concrete specifics** | Numbers, names, places — not "many" or "some" | Replace vague quantifiers |
| **Natural speech** | Read aloud — if you would not say it, rewrite | Rewrite any stiff sentence |
| **Contractions** | Uses "you're", "it's", "we'll" naturally | Add where appropriate |
| **Nexor voice** | Clear, direct, warm, professional, no hype | Check against OS voice |

---

## SCORING

```
🟢 0–25   Mostly human — good to send (after Tier 2 human review)
🟡 26–50  Lightly AI — fix flagged words and patterns
🟠 51–75  Moderately AI — rewrite the worst sentences
🔴 76–100 Heavily AI — start over with cold-outreach framework
```

Target 🟢 for every cold email. Do not deliver above 🟡.

---

## QUICK SWAP REFERENCE

| AI Word | Human Replacement |
|---|---|
| "leverage" | "use" |
| "utilize" | "use" |
| "facilitate" | "help" |
| "robust" | "strong" or remove |
| "seamless" | remove or "easy" |
| "comprehensive" | "full" or "complete" |
| "streamline" | "cut the steps" |
| "innovative" | say what is actually new |
| "serves as" | "is" |
| "in order to" | "to" |
| "moving forward" | remove |
| "touch base" | "talk" |
| "game changer" | say what specifically changes |
| "transformative" | say what actually transforms |
| "empower" | say what they can now do |
| "holistic" | say what you actually mean |

---

## BEFORE AND AFTER

**Before (AI score: ~70, multiple Nexor banned words):**
```
Hi Aiman,

As an L&D Manager in the hospitality sector, you are undoubtedly
faced with the challenge of seamlessly facilitating comprehensive
training programmes. Our groundbreaking AI-powered solution 
leverages machine learning to streamline your workflows and 
empower your team to achieve transformative outcomes.

We would love to schedule a 30-minute discovery call.
```

**After (AI score: ~8, no Nexor banned words):**
```
Hi Aiman,

Most L&D Managers in hotels spend more time tracking who showed
up than actually running the training.

AI sends the briefing automatically when someone joins so you
stop running the same session five times a month.

We train your team to do this on-site and we're HRD Corp
certified, so your levy pays for it.

Reply "yes" if this sounds useful.
```

---

## WHERE THIS SKILL SITS

```
workflowskill   → research + angle
cold-outreach   → write the draft
humanizer       → final pass, remove all AI signals
                → deliver only when score is 🟢
                → flag Tier 2 for human review before sending
```

Never deliver an email that has not been through the humanizer pass.
Never deliver without the Tier 2 human review flag.
