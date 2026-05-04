---
name: crm
description: Generate structured CRM data blocks after drafting outreach emails or follow-ups. Use this to format data specifically for copy-pasting into Zoho, HubSpot, or other CRMs. Trigger automatically after cold-outreach outputs a draft.
---

# crm — Data Logging & Tracking

## WHAT THIS SKILL DOES

Every cold email must be tracked. If you don't track the angle, you can't pivot in the follow-up. This skill generates a clean, copy-pasteable text block containing all the necessary metadata for the user's CRM.

## WHEN TO RUN

Always run this automatically at the end of Phase 7 (Delivery), immediately below the generated email draft.

## THE CRM OUTPUT FORMAT

Generate a markdown block with the following exact keys.

```text
--- CRM LOG ENTRY ---
[Prospect Name]: 
[Company]: 
[Title]: 
[Cadence Step]: Day 1 (Initial) / Day 4 (Value Add) / Day 9 (Pivot) / Day 14 (Break-Up)
[Primary Pain Angle Used]: (e.g., Onboarding bottlenecks, missing GRNs, WhatsApp approvals)
[Trigger Event]: (If any, e.g., "New C-level hire")
[Next Follow-Up Date]: (Calculate the exact date based on the cadence step)
---------------------
```

## RULES
1. **Never skip logging.** Even if it's just a test draft, output the log block so the user gets used to seeing it.
2. **Be precise with angles.** "HR Pain" is not an angle. "WhatsApp approvals missing audit trails" is an angle. This precision is required so the Day 9 Pivot follow-up actually pivots to something different.
3. **Calculate dates.** If today is Monday the 1st, and this is Day 1, the Next Follow-Up Date should literally say "Friday the 5th (Day 4 Value Add)".
