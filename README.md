# TripRoom

**Plan a group trip with your friends and three AI agents, right in your group chat, through [Switch](https://docs.switchagents.ai).**

A **scout** researches places, stays and transport (with sources). A **planner** runs the plan, the votes and the itinerary. A **treasurer** keeps the budget and works out who owes whom. Your friends decide everything by voting in the chat, and the trip lead confirms. **Agents never book or pay for anything.**

Built for **Flip the Switch** (WeMakeDevs × DevTools Academy) · Track 02 — Best Personal or Creative Workflow

Full spec: [PRD.md](PRD.md)

## Demo

- **Demo video:** _add link_
- **Real run:** [`examples/real-run/`](examples/real-run/): three friends planned a real weekend in
  Grand-Bassam (Côte d'Ivoire) in one hour. 3 decisions by vote + confirm, 4 agent-written documents,
  one change request (Itinerary v4 → v5), and a $200 deposit settled as "Benjamin → Mufasa 67 · Alina → Mufasa 67".
  Includes the chat transcript and the final Trip brief, Itinerary, Decisions log and Budget and split.

## How it works

```
Lead:      @planner start a trip
planner:   5 quick questions: dates, departure cities, budget, style, must-haves
Friends:   (answer in the thread)                → planner saves the "Trip brief" document
Lead:      @scout find 3 destinations that fit the trip brief
scout:     A / B / C: why it fits, travel time, cost range, caution, sources
planner:   Vote: reply A, B or C by 18:00
Friends:   B · B · A
planner:   B wins 2–1. Trip lead, reply "confirm".
Lead:      confirm                                → logged in "Decisions log"
Lead:      @planner draft the itinerary           → "Itinerary" v1
Friend:    change: swap day 2 beach for the market   → v2
Friend:    @treasurer I paid 75 for the deposit
Lead:      @treasurer balances                    → "Ada → Tolu 25 · Sam → Tolu 25"
```

**Golden rule:** agents propose, people vote, the trip lead confirms.

## How Switch is used

| Switch feature | In TripRoom |
|---|---|
| Room | The friends' Telegram group (or a Mattermost channel). One room per trip |
| Room instructions | The workflow, the golden rule, timezone, Telegram-friendly formatting ([`room/instructions.md`](room/instructions.md)) |
| Agents | Three Claude Code agents (scout, planner, treasurer), each in its own folder with its own `CLAUDE.md` |
| Roles | scout (shared), planner (exclusive), treasurer (exclusive) ([`room/roles.md`](room/roles.md)) |
| Aliases | `@scout`, `@planner`, `@treasurer` in the live room (the template relies on the role names instead, since an alias can't share a role's name) |
| Main agent | `!assign-agent @planner`: un-tagged messages go to the planner |
| Follow-ups | `!follow-ups off`: one agent answers per thread |
| Room documents | Trip brief, Itinerary, Decisions log (planner) · Budget and split (treasurer) |
| Agent settings | Friends allowed via "Who can talk to your agent"; each agent sees only its own folder; auto mode on, bypass permissions off |
| Permission prompts | The owner approves tool use in chat (Allow once / session / Decline) |
| Commands | `!roles`, `!list-documents`, `!agents-status`, `!interrupt`, `!reset` ([`room/commands.md`](room/commands.md)) |
| Template | Captured from the real room in Switch Console, cleaned for reuse: [`template/triproom.yaml`](template/triproom.yaml) |

Without Switch there's no shared room, no roles, no shared documents and no way for several agents and several people to work in one chat.

## Agents connected

| Agent | Provider / model | Job | Tools |
|---|---|---|---|
| scout | Claude Code · sonnet | Research options with sources | WebSearch, WebFetch + Switch tools |
| planner | Claude Code · opus | Questions, votes, itinerary, status | WebSearch (travel times) + Switch tools |
| treasurer | Claude Code · sonnet | Budget, expenses, balances | Switch tools |

## Run it yourself

Full guide with screenshots and Windows fixes: [docs/setup.md](docs/setup.md)

1. Install **Docker Desktop**, **Claude Code** (`claude auth login`) and **Switch Console**, then choose **Get started → On this computer**.
2. **Telegram:** create a bot with @BotFather and turn **Group Privacy off**. Connect it in Switch Console → Home → Messaging apps → Telegram. Create a group with your friends and add the bot. (Or use the bundled Mattermost.)
3. **Agents:** in Switch Console → Your Agents, add `scout`, `planner` and `treasurer` (Claude Code, run on this computer, directory = `agents/<name>/`).
4. **Room:** paste [`room/instructions.md`](room/instructions.md) into the room's Instructions.
5. **In the chat:**
   ```
   !invite-agent @scout.<you>
   !invite-agent @planner.<you>
   !invite-agent @treasurer.<you>
   !set-alias @scout.<you> @scout
   !set-alias @planner.<you> @planner
   !set-alias @treasurer.<you> @treasurer
   !assign-agent @planner
   !follow-ups off
   ```
   Then create the roles with the messages in [`room/roles.md`](room/roles.md).
6. Or skip steps 4–5 on Mattermost: Switch Console → Templates → Import → [`template/triproom.yaml`](template/triproom.yaml). It creates the room with the instructions, the three roles and your three agents. (Telegram can't create chats, so on Telegram adopt your group and use steps 4–5.)
7. Say `@planner start a trip`.

## Commands for the group

| Type | What happens |
|---|---|
| `@planner start a trip` | Kickoff questions → Trip brief |
| `@scout find 3 destinations …` | Options with sources |
| `A` / `B` / `C` | Vote |
| `close the vote` (trip lead) | Planner tallies now |
| `confirm` (trip lead) | Makes a decision final |
| `change: …` | Revise the itinerary |
| `@treasurer I paid 75 for …` | Log an expense |
| `@treasurer balances` | Who owes whom |
| `@planner status` | Decisions, open votes, next step |
| `@planner checklist` | Per-person prep list |
| `stop` | Agents stop in this thread |

Want to double-check the treasurer? `python3 scripts/settle.py expenses.txt` prints balances and transfers and checks that they sum to zero. ([format](scripts/settle.py))

## Safety

- Agents never book, pay or ask for money. People do that themselves.
- Every price has a source; unknowns are marked "Not stated".
- Only first names and departure cities are collected. No passport, address or card details.
- Each agent folder holds only its `CLAUDE.md`; risky actions still ask the owner (auto mode on, bypass permissions off).

## Repo

```
agents/{scout,planner,treasurer}/CLAUDE.md   one job per agent
room/instructions.md · roles.md · commands.md
template/triproom.yaml                         captured from Switch Console
docs/setup.md · docs/screenshots/ · docs/posts/
examples/real-run/                             transcript + the four final documents
scripts/settle.py                              check the treasurer's maths
```

## Built with

Switch · Claude Code · Telegram · Mattermost

## License

[MIT](LICENSE)

## Author

Built by **softalpha0** for Flip the Switch. #HowISwitch
