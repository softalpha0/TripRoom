# Commands used, in order

Replace `<you>` with your Switch username. In Mattermost a `!` command must be the first thing in the
message. Telegram also accepts the slash form (`/invite_agent`, `/set_alias`, `/assign_agent`, …).

## Setup (once per room)

| # | Command | Why |
|---|---|---|
| 1 | `!invite-agent @scout.<you>` | Add the scout to the room |
| 2 | `!invite-agent @planner.<you>` | Add the planner |
| 3 | `!invite-agent @treasurer.<you>` | Add the treasurer |
| 4 | `!set-alias @scout.<you> @scout` | Short name for friends |
| 5 | `!set-alias @planner.<you> @planner` | 〃 |
| 6 | `!set-alias @treasurer.<you> @treasurer` | 〃 |
| 7 | role-definition message from [roles.md](roles.md) | Create scout / planner / treasurer roles |
| 8 | `@scout take the scout role` (and the other two) | Each agent takes its role |
| 9 | `!assign-agent @planner` | Un-tagged messages go to the planner (main agent) |
| 10 | `!follow-ups off` | Only one agent answers per thread |
| 11 | `!roles` | Check the roles |
| 12 | `!list-agents` | Check all three agents are in the room |
| 13 | `@planner what is this room for?` | Smoke test — a generic answer means the instructions didn't save |

> If `!assign-agent` or `!follow-ups` answers "Following the conversation isn't switched on for this
> Switch server", that feature is off on your server: un-tagged messages reach nobody. Then everyone
> starts every message with an agent's name, e.g. `@planner B`, `@planner confirm`.

## During the trip

| Command | Why |
|---|---|
| `!list-documents` | Show the four room documents |
| `!agents-status` | See which agent is working |
| `!interrupt @scout` | Stop a stuck agent |
| `!reset @planner` | Reset an agent (e.g. after changing its instructions) |
| `stop` (reply in a thread) | Agents stop work in that thread |

## Group phrases (not ! commands — plain chat)

| Type | What happens |
|---|---|
| `@planner start a trip` | Kickoff questions → Trip brief |
| `@scout find 3 destinations that fit the trip brief` | Options A/B/C with sources |
| `A` / `B` / `C` | Vote |
| `close the vote` (trip lead) | Planner tallies now |
| `confirm` (trip lead) | Decision is final → Decisions log |
| `change: …` | Revise the itinerary (version bump) |
| `@treasurer I paid 75 for the deposit` | Log an expense |
| `@treasurer balances` | Who owes whom |
| `@planner status` | Decisions, open votes, next step, who hasn't answered |
| `@planner checklist` | Per-person prep list |
