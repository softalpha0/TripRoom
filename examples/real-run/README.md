# Real run

> **Status: not recorded yet.** Everything in this folder must come from the real Telegram session
> with real friends. Nothing here is written by hand.

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

- [ ] ≥ 2 real people besides the lead
- [ ] ≥ 3 decisions by vote + confirm (destination, stay, itinerary)
- [ ] Every price/fact in scout posts has a source or "Not stated"
- [ ] 4 room documents created by agents
- [ ] Balances add to zero
- [ ] Someone else can rebuild TripRoom (setup.md + template YAML)
