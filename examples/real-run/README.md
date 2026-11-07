# Real run

> **Recorded Sat 7 Nov 2026, 11:32–12:30 Lagos time.** Three real people (Benjamin, Mufasa, Alina) in a
> Telegram group with the three agents. Everything in this folder comes from that session; nothing is
> written by hand.

## What happened

| | |
|---|---|
| Trip | Grand-Bassam via Abidjan, Côte d'Ivoire, Fri 4 – Sun 6 Dec 2026, 3 people from Lagos |
| Decision 1 | Destination: B (Grand-Bassam) won 2–0 over Accra and Ouidah → confirmed |
| Decision 2 | Stay: A (Koral Beach Hotel) won 3–0 → confirmed |
| Decision 3 | Mufasa's `change:` swapped the museum for a lagoon pirogue trip (Itinerary v4 → v5), voted 3–0 → confirmed |
| Documents | Trip brief v3, Itinerary v5, Decisions log (3 entries), Budget and split v6 |
| Money | Mufasa logged a $200 hotel deposit → Benjamin → Mufasa 67, Alina → Mufasa 67 (sum 0) |

Files: [transcript](transcript.md) · [Trip brief](trip-brief.md) · [Itinerary](itinerary.md) ·
[Decisions log](decisions-log.md) · [Budget and split](budget-and-split.md) ·
check the maths with `python3 scripts/settle.py examples/real-run/expenses-real-run.txt`.

Things we noticed:
- The planner opened a vote by itself when a friend answered "B" before any vote existed, and didn't count
  Alina's vote until she said she was travelling.
- The scout wrote "Not stated" for every price it couldn't source (entry fees, Sunday flight times).
- Room aliases and role names are the same (`planner`, …). `@planner` resolves to the *role*, so before
  the agents take their roles Switch warns "no agent currently holds the planner role". Have each agent
  take its role right after the roles are created.

## Run sheet (record your screen the whole time)

Before you start: tell friends the time, and that they only need to reply in the group.
Vote closing times give people who join late a chance.

| # | Who | Message | Done when |
|---|---|---|---|
| 1 | Lead | `@planner start a trip` | Planner asks 5 questions in one message |
| 2 | Friends | answer in the thread | Planner saves **Trip brief**, posts a 6-line summary |
| 3 | Lead | `@scout find 3 destinations that fit the trip brief` | A/B/C with sources |
| 4 | Lead | `@planner run a vote on the scout's destinations` | Vote with closing time |
| 5 | Friends | `A` / `B` / `C` | Planner tallies (or lead: `close the vote`) |
| 6 | Lead | `confirm` | Logged in **Decisions log** — decision 1 |
| 7 | Lead | `@scout 3 stays and transport options for <destination>` | Options with sources |
| 8 | Lead + friends | vote → `confirm` | Decision 2 |
| 9 | Lead | `@planner draft the itinerary` | **Itinerary** v1 + short daily summary |
| 10 | Friend | `change: swap day 2 beach for the market` (any real change) | Itinerary v2, what changed |
| 11 | Lead | `confirm` | Decision 3 |
| 12 | Lead | `@treasurer build the budget` | **Budget and split** + per-person cost |
| 13 | Friend | `@treasurer I paid 75 for the deposit` (real amount) | Expense recorded |
| 14 | Lead | `@treasurer balances` | Balances + transfers |
| 15 | Lead | `@planner status`, then `@planner checklist` | Status + per-person list |
| 16 | Lead | `!list-documents`, `!roles` | On camera |

If `!assign-agent` said "Following the conversation isn't switched on", tell friends to start every
reply with `@planner` (e.g. `@planner B`, `@planner change: …`), and send `@planner confirm` yourself.

Cuts if late (PRD §16): skip 7–8 and the checklist; keep destination vote, itinerary, budget.

## After the run — fill these files

| File | From |
|---|---|
| `transcript.md` | Telegram → export chat history (Desktop: ⋮ → Export chat history → JSON or HTML), then paste as text. Replace surnames/phone numbers with first names. |
| `trip-brief.md` | Room document **Trip brief** |
| `itinerary.md` | Room document **Itinerary** (final version) |
| `decisions-log.md` | Room document **Decisions log** |
| `budget-and-split.md` | Room document **Budget and split** |

Check the treasurer: write the expenses into a text file and run
`python3 scripts/settle.py expenses.txt` — balances must sum to zero.

## Success metrics (PRD §12)

- [x] ≥ 2 real people besides the lead (Mufasa, Alina)
- [x] ≥ 3 decisions by vote + confirm (destination, stay, itinerary change)
- [x] Every price/fact in scout posts has a source or "Not stated"
- [x] 4 room documents created by agents
- [x] Balances add to zero (134 − 67 − 67 = 0)
- [x] Someone else can rebuild TripRoom (docs/setup.md + template/triproom.yaml)
