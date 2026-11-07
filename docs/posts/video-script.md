# TripRoom — 3-minute demo video script

Target: 2:50. About 380 spoken words, roughly 130 words a minute.
Record your screen with **Xbox Game Bar** (Win+Alt+R) or OBS. Edit in **Clipchamp** (built into Windows).
Speed up every "Working…" wait to 4×. Blur phone numbers and any surnames.

---

## 0:00 – 0:15 · Hook
**Show:** the Telegram group `weekend_trip`, scrolling fast through the chat.

**Say:**
> "Every group trip dies in the group chat. Two hundred messages, no decision, and someone pays the deposit and never gets paid back. TripRoom puts three AI agents into the chat — but my friends still make every decision."

## 0:15 – 0:35 · The setup in Switch
**Show:** Switch Console → **Your Agents** (planner, scout, treasurer, green dots) → **Your Rooms → weekend_trip → Configuration** (the Instructions box) → Telegram `!roles` reply.

**Say:**
> "It runs on Switch. Three Claude Code agents, each with one job: a scout that researches, a planner that runs votes and the itinerary, and a treasurer for the money. The room has one rule: agents propose, people vote, the trip lead confirms. Each agent holds its own role in the room."

## 0:35 – 1:00 · Kickoff → Trip brief
**Show:** `@planner start a trip` → the six questions → Mufasa's and Benjamin's answers → "📄 created room document Trip brief" → the v2 summary.

**Say:**
> "I type 'start a trip'. The planner asks six questions in one message. My friends answer in the chat, and the planner saves everything as a shared Trip brief: Fourth to sixth of December, from Lagos, fifteen hundred dollars each, beach, culture, good food, no flights over two hours."

## 1:00 – 1:35 · Scout → vote → confirm
**Show:** scout's A/B/C posts (zoom on a "Sources:" line and a "Not stated") → "B" from Mufasa, "B" from you → "Vote result: B 2 to 0" → you: `confirm` → "📄 created room document Decisions log".

**Say:**
> "The scout searched the web and came back with three options: Accra, Grand-Bassam and Ouidah. Every price has a source, and where it couldn't find one, it says 'Not stated' instead of guessing. We vote in the chat. Grand-Bassam wins two–nil, I reply 'confirm', and it's logged as decision one."

## 1:35 – 2:05 · Stay, itinerary and a friend's change
**Show:** the stay vote (A, 3–0, Alina joining) → Itinerary summary → Mufasa's `change:` (museum → lagoon boat trip) → "Itinerary v5" → `confirm`.

**Say:**
> "Alina joins halfway through. The planner won't count her vote until she says she's coming, then adds her to the brief. We pick the Koral Beach Hotel three–nil. Then Mufasa asks for a change: swap the museum for a lagoon boat trip. The planner changes only that, bumps the itinerary to version five, and waits for my confirm."

## 2:05 – 2:30 · Money
**Show:** Mufasa's expense message → `@treasurer balances` → "Benjamin → Mufasa 67, Alina → Mufasa 67. Sum: 0".
Optional: PowerShell running `python scripts/settle.py examples/real-run/expenses-real-run.txt` with the same answer.

**Say:**
> "Mufasa paid a two-hundred-dollar hotel deposit. The treasurer splits it three ways and posts the fewest transfers: Benjamin pays Mufasa sixty-seven, Alina pays Mufasa sixty-seven. It all adds to zero. And no agent ever books or pays for anything — we do that ourselves."

## 2:30 – 2:50 · Proof and repo
**Show:** `!list-documents` (four documents) → Switch Console **Capture as template** → GitHub repo: `agents/`, `template/triproom.yaml`, `examples/real-run/`.

**Say:**
> "Four shared documents, three decisions, three real friends, one hour. The whole room is captured as a Switch template, and the repo has the agents, the setup guide and the real transcript. Clone it, and plan your own trip."

## End card (3 s)
`TripRoom · github.com/softalpha0/TripRoom · Built with Switch + Claude Code · #HowISwitch`

---

### Checklist before you record
- [ ] Telegram Desktop window large, font readable (Ctrl + mouse wheel to zoom)
- [ ] Switch Console open on **Your Agents**
- [ ] GitHub repo open in a browser tab
- [ ] Notifications off (Win+N → Do not disturb)
- [ ] Record the voice-over separately in Clipchamp if talking while scrolling is hard
