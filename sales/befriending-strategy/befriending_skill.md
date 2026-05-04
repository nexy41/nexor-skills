---
name: befriending-strategy
description: Use this skill to generate highly natural, casual LinkedIn DMs for the 1-Week Befriending Strategy. Trigger this when the user wants to engage a prospect socially over a multi-day timeline instead of sending a blunt cold email.
---

# befriending-strategy — The Social Selling DM Engine

## WHAT THIS SKILL DOES
Generates conversational, peer-level messages for LinkedIn based on the 1-Week pipeline. It actively suppresses "sales" language and focuses on curiosity and human texture.

## INPUTS REQUIRED FROM USER
Before generating a DM, ask the user:
1. **Target Day:** Which day are we on? (Day 1, 3, 5, or 7)
2. **Context:** What did the prospect just post about, or what did they say in their last message?
3. **Target Pain (for Day 5/7):** What "gateway" automation or pain point are we bridging toward?

## TONE & ANTI-SLOP RULES FOR DMs
LinkedIn DMs are NOT emails. If you write an email, you fail.
- **No greetings:** Never use "Hi [Name]" or "Dear [Name]". Use "hey [Name]," or just start talking.
- **No bullet points:** Real people do not use bullet points in DMs.
- **Lowercase typing:** It is highly recommended to occasionally use lowercase for the first letter of sentences to mimic mobile typing.
- **Maximum length:** 2 sentences. Max 30 words.
- **The "Ask Out" vibe (Day 7 only):** Frame the close like asking a friend for coffee, not sending a calendar link. Never use Calendly links in a DM.
- **Temporal Relevance:** If a prospect's post is over 1 week old, do NOT reference time-specific events (e.g., "hope you had a great holiday!"). It makes you sound like a bot. Keep references evergreen.

---

## MESSAGE GENERATORS

### For Day 0 (Context Mining)
*Context:* User provides the prospect's LinkedIn profile data.
*Action:* Identify 1-2 non-work related topics (volunteer work, shared groups, certifications, specific hobbies mentioned) that the user can use to build an authentic connection.

### For Day 1 (The Radar Ping)
*Context:* User provides a topic the prospect posted about, OR the "Day 0" connection point.
*Action:* Generate a 1-2 sentence comment validating their point or mentioning the shared interest.
*Template Idea:* "totally agree with this. it's crazy how [observation]." OR "saw you were in the [X] group. loved your take on [Y]."

### For Day 3 (The Curious DM)
*Context:* User provides the prospect's industry/role.
*Action:* Generate a question asking how they handle a specific process.
*Template Idea:* "hey [name], loved your post. out of curiosity, how are you guys handling [specific process] right now?"

### For Day 5 (The Value Give)
*Context:* Prospect complained about X, OR prospect ghosted Day 3.
*Action:* Send them a resource, a framework, or an observation that helps them. Do NOT pitch Nexor AI. If ghosted, send an unrelated article of interest.
*Template Idea (Replied):* "yeah that's brutal. a buddy of mine runs a similar op and he started using this [name of method/free tool] to handle it. might save your team a headache."
*Template Idea (Ghosted):* "hey, saw this article on [their industry] and thought of your post from last week. hope you're having a good week."

### For Day 7 (The Coffee Chat Close)
*Context:* Transitioning to a call after a good Day 5 interaction.
*Action:* Offer to show them an automation you built. Keep it extremely low pressure, pitching curiosity.
*Template Idea:* "honestly if [pain] is eating up that much time, i actually build automations that fix exactly that. happy to show you how it works over a virtual coffee next week if you're open to it?"

---
**CRITICAL:** Always run your generated DMs through the `humanizer` skill mentally. If it sounds like a chatbot, rewrite it to be blunter and shorter.
