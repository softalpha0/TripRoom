# PRD — TripRoom

Plan a group trip with your friends and three AI agents, in your group chat, through Switch. TripRoom turns a Telegram group (or Mattermost channel) into a Switch room. In it, a scout researches options, a planner builds and revises the itinerary, and a treasurer keeps the budget and the cost split. The friends decide everything by voting in the chat, and the trip lead confirms. Agents never book or pay for anything.

| | |
|---|---|
| Hackathon | Flip the Switch (WeMakeDevs × DevTools Academy, powered by Switch) — tracker ID HK-013 |
| Track | Track 02 — Best Personal or Creative Workflow ($2,000) |
| Side tracks | Best Blog (AirPods) · #HowISwitch (keyboards) · Code with Wispr ($500, only if built by voice with Wispr Flow) |
| Deadline | Sat Nov 7, 2026, 11:59 PM IST = 7:29 PM Lagos. Submit by 6:30 PM Lagos. |
| Team | Solo builder (softalpha0) + 2–3 real friends as trip members in the demo |
| Status | Build spec v1.0 — 2026-11-07 |

> Instruction to the coding agent: build everything in this document in one pass, with no "later" phase. Most of TripRoom is Switch configuration (agents, room, instructions, roles, aliases, main agent, documents) plus a small repo that lets anyone reproduce it. Then run one real trip-planning task end to end with real people (§11) and record it. Use the Switch docs MCP while building: `claude mcp add switch-docs --transport http https://docs.switchagents.ai/mcp`.

## 1. What the judges want (and how TripRoom answers)

Challenge: "Build a workflow where an AI agent and the people in a team chat get a real task done together." At least one agent and one person must complete a real task through Switch. The Switch setup and workflow must be built during the hackathon.

| Criterion (weight per DevTools Academy) | TripRoom's answer |
|---|---|
| Use of Switch (30%): "would the project stop working without it?" | Everything happens in a Switch room. It uses three agents with roles, room instructions, aliases, a main agent, the follow-ups setting, agent-owned room documents, permission rules for friends and `!` commands. Without Switch there is no shared room, no roles and no documents. |
| Technical execution (25%): "could someone clone the repo and reproduce it?" | The repo ships agent folders (a `CLAUDE.md` in each), room instructions, role texts, a captured Switch template (YAML) and step-by-step setup (§10). |
| Creativity & impact (25%): "fresh idea, real problem" | Group trips die in chat: 200 messages, no decision, and someone pays and never gets paid back. No other Flip the Switch entry found plans trips. |
| Presentation (20%) | A 3-minute video of a real plan with real friends. The README shows exactly how Switch is used (agents, room setup, how to run). |

## 2. Problem

Planning a trip with friends happens in a group chat that quickly becomes chaos. Links get lost, nobody knows what was decided, dates and budgets never get pinned down, and after the trip one person is stuck chasing everyone for money. Asking a single AI chatbot doesn't help: it isn't in the group, doesn't know who agreed to what, and can't keep a shared plan.

## 3. Who it's for

| User | Need |
|---|---|
| Friend groups (2–8 people) | One chat where options, decisions, itinerary and money are all clear. |
| The trip lead | Stop doing all the research and spreadsheet work alone, and keep the final say. |
| Families and clubs | Reunions, weekend getaways, team retreats, school trips. |

## 4. Solution overview

One Switch room = one trip. The room is a Telegram group (friends join from their phones) or a Mattermost channel (bundled with local Switch, for solo testing).

Three agents (Claude Code), one job each:

| Agent (alias) | Role | Owns | Never does |
|---|---|---|---|
| scout (`@scout`) | scout (shared) | Research posts: destinations, stays, transport, activities, with sources and price ranges | Book, pay, or invent prices |
| planner (`@planner`) | planner (exclusive); also the room's main agent | Room documents Trip brief, Itinerary, Decisions log; runs votes | Decide for the group |
| treasurer (`@treasurer`) | treasurer (exclusive) | Room document Budget and split; who owes whom | Move or request real money |

People:

- **Trip lead** (the organiser, owner of the agents) confirms decisions with `confirm`.
- **Members** (friends) answer questions, vote and log expenses.

**Golden rule (room instructions):** Agents propose. People vote. The trip lead confirms. Nothing is final until "confirm".

## 5. Feature list (all in scope)

| # | Feature | How it works in Switch |
|---|---|---|
| F1 | Trip room | A Telegram group (or Mattermost channel) adopted as a Switch room named `trip-<destination-or-name>`; access restricted to the owner. |
| F2 | Room instructions | The briefing every agent reads on joining (§7). |
| F3 | Three agents | scout, planner, treasurer, each in its own working directory with its own `CLAUDE.md` (§8). |
| F4 | Roles | scout (shared), planner (exclusive), treasurer (exclusive). Each is defined by asking an agent, e.g. "@planner define an exclusive role called planner, with these instructions: …". Each agent takes its role. |
| F5 | Aliases | `!set-alias @scout.<owner> @scout` (etc.) so friends type short names. |
| F6 | Main agent + follow-ups | `!assign-agent @planner` so un-tagged messages go to the planner; `!follow-ups off` to stop several agents answering one thread. |
| F7 | Friends can talk to agents | Each agent's *Who can talk to your agent* is set to Custom rules naming the friends (or Anyone for the demo group). |
| F8 | Kickoff | The trip lead posts `@planner start a trip`. The planner asks 5 questions in one message (dates window, departure cities, budget per person, trip style, must-haves / no-gos), and members reply in the thread. |
| F9 | Trip brief document | The planner saves the answers as room document Trip brief ("create a room document called Trip brief with … use it before every plan") and posts a 6-line summary. |
| F10 | Destination research | `@scout find 3 destinations that fit the trip brief` gives 3 options. Each has: why it fits, travel time from each departure city, typical cost range per person, best area to stay, 1 caution, 2–3 source links. "Not stated" if a fact isn't found. |
| F11 | Votes | The planner posts a vote: *Reply A, B or C by 18:00 Lagos*. Members reply, the planner tallies and posts the result, and the trip lead replies `confirm`. The decision is logged in the Decisions log. |
| F12 | Stays & transport research | After a destination is confirmed, `@scout` posts 3 stay options and transport options with price ranges and links. Vote and confirm the same way. |
| F13 | Itinerary | The planner writes Itinerary (day by day: morning / afternoon / evening, travel times, rough cost per activity) as a room document. It posts a short daily summary in chat (Telegram has no tables, so short lines only). |
| F14 | Change requests | Any member: `change: swap day 2 beach for the market`. The planner revises, posts what changed and bumps the version (v1 → v2). The trip lead confirms. |
| F15 | Budget & split | `@treasurer` builds Budget and split from confirmed choices: total, per person, by category. Members log expenses: `@treasurer I paid 120 for the boat tour`. The treasurer keeps balances and posts the fewest transfers needed to settle ("Ada → Tolu 40"). |
| F16 | Status at a glance | `@planner status` shows confirmed decisions, open votes, the next step and who hasn't answered. |
| F17 | Pack & prep checklist | `@planner checklist` gives a per-person checklist (documents, bookings people need to make, what to pack) based on the itinerary. |
| F18 | Stop | `stop` in a thread makes agents stop work there. `!interrupt @agent` for a stuck agent. |
| F19 | Timezone awareness | The instructions tell agents the group's timezone (Switch timestamps are UTC). |
| F20 | Reproducible package | The repo contains everything needed to rebuild the room (§9, §10), including a captured Switch template YAML of the room. |
| F21 | Real-run evidence | The repo includes the real chat transcript, screenshots and the final room documents (§11). |

### Hard constraints

- **No booking, no payments, no money requests.** Agents only research, plan and calculate. People book and pay themselves.
- **Sources for every price or fact**: ranges, not fake exact prices; "Not stated" when unknown.
- **Minimal personal data**: first names and departure cities only; no passport numbers, addresses or card details in the room.
- **Least privilege**: agents get only the tools they need (§8); Bypass permissions stays off; each agent's working directory contains only its own `CLAUDE.md`.
- **Don't put @ mentions inside documents or instructions** (any @ mention wakes an agent).

## 6. Switch features used (README table)

| Switch feature | In TripRoom |
|---|---|
| Room (Telegram group / Mattermost channel) | One room per trip |
| Room instructions | Workflow, golden rule, timezone, formatting for Telegram |
| Multiple agents | scout, planner, treasurer (Claude Code), one job each |
| Roles (shared / exclusive) | scout shared; planner, treasurer exclusive |
| Aliases | `@scout`, `@planner`, `@treasurer` |
| Main agent (`!assign-agent`) | planner receives un-tagged messages |
| Follow-ups (`!follow-ups off`) | One agent answers per thread |
| Room documents (agent-owned) | Trip brief, Itinerary, Decisions log (planner); Budget and split (treasurer) |
| Agent settings | Custom "who can talk to your agent", limited tools, model per agent |
| Permission prompts | Owner approves tool use in chat (Allow once / session / Decline) |
| Commands | `!list-agents`, `!roles`, `!list-documents`, `!agents-status`, `!interrupt`, `!reset` |
| Templates | Room captured as YAML so others can recreate TripRoom |

## 7. Room instructions

Paste into Switch Console → room → General → Instructions. The text lives in [`room/instructions.md`](room/instructions.md).

## 8. Agents (Switch Console → Your Agents → Add)

Each agent: Run location = This computer; Directory = its own folder from the repo (`agents/<name>/`, contains only `CLAUDE.md`); Agent provider = Claude Code; Bypass permissions = off; Who can talk to your agent = Custom rules (trip lead + friends) or Anyone for the demo.

| Agent | Description | Model | Tools (Advanced → Tools) |
|---|---|---|---|
| scout | Researches trip options with sources | sonnet | WebSearch, WebFetch (+ Switch tools, always kept) |
| planner | Runs the plan, votes, itinerary documents | opus (or sonnet) | Switch tools only (+ WebSearch for travel times) |
| treasurer | Budget and fair cost split | sonnet | Switch tools only |

Agent instructions: [`agents/scout/CLAUDE.md`](agents/scout/CLAUDE.md), [`agents/planner/CLAUDE.md`](agents/planner/CLAUDE.md), [`agents/treasurer/CLAUDE.md`](agents/treasurer/CLAUDE.md).

## 9. Repo structure

```
triproom/
├─ agents/
│  ├─ scout/CLAUDE.md
│  ├─ planner/CLAUDE.md
│  └─ treasurer/CLAUDE.md
├─ room/
│  ├─ instructions.md          # §7
│  ├─ roles.md                 # role definitions + the exact chat messages used to create them
│  └─ commands.md              # every ! command used, in order
├─ template/
│  └─ triproom.yaml            # captured from Switch Console → Templates (room name + agents as fields)
├─ docs/
│  ├─ setup.md                 # §10, with screenshots
│  ├─ screenshots/
│  └─ posts/                   # blog + #HowISwitch drafts
├─ examples/real-run/
│  ├─ transcript.md            # exported chat of the real planning session
│  ├─ trip-brief.md            # copies of the final room documents
│  ├─ itinerary.md
│  ├─ decisions-log.md
│  └─ budget-and-split.md
├─ scripts/settle.py           # optional check of the treasurer's maths
├─ PRD.md · README.md · LICENSE (MIT)
```

The template YAML must be captured from a working room in Switch Console (Templates). Do not hand-write it. Make the room name and the three agents fields (set agent fields' type to `agent`).

## 10. Setup

See [`docs/setup.md`](docs/setup.md). It covers Docker Desktop (with the Windows stale-socket fix), Claude Code (native installer, PATH, `claude auth login`), Switch Console, the Telegram bot (Group Privacy off), the agents, the room, the chat commands, the smoke test and capturing the template.

## 11. The real run (must be real; this is the demo)

Plan a real trip with 2–3 real friends in the Telegram group (e.g. a weekend getaway next month). Run sheet: [`examples/real-run/README.md`](examples/real-run/README.md).

1. Lead: `@planner start a trip`. The planner asks 5 questions, friends answer, and the Trip brief is saved.
2. Lead: `@scout find 3 destinations that fit the trip brief`. The scout posts A/B/C with sources.
3. The planner posts the vote, friends reply, it tallies, the lead replies `confirm`, and the decision goes in the Decisions log.
4. `@scout 3 stays and transport options for <destination>`, then vote and confirm.
5. `@planner draft the itinerary` posts an Itinerary v1 summary in chat.
6. A friend sends `change: …`. The planner posts Itinerary v2 and the lead confirms.
7. `@treasurer build the budget` gives the per-person cost. A friend sends `@treasurer I paid 50 for the deposit`, then the lead asks `@treasurer balances`.
8. `@planner status` and `@planner checklist`.
9. Run `!list-documents` and `!roles` on camera to show Switch state.

Export the transcript and documents into `examples/real-run/`.

## 12. Success metrics

| Metric | Target |
|---|---|
| Real people in the run (besides you) | ≥ 2 |
| Decisions made by vote + confirm | ≥ 3 (destination, stay, itinerary) |
| Every price/fact in scout posts has a source or "Not stated" | 100% |
| Room documents created by agents | 4 |
| Balances add to zero after expenses | Yes |
| Someone else can rebuild TripRoom from the repo | Yes (setup.md + template YAML) |

## 13. Demo video (≤ 3 min)

- 0:00 Hook: "Every group trip dies in the group chat. TripRoom puts three AI agents in the chat, but the friends still decide."
- 0:15 Switch Console: three agents, the room's instructions, `!roles`.
- 0:35 Kickoff → friends answer → Trip brief.
- 1:00 Scout's 3 destinations → friends vote → lead confirm.
- 1:35 Itinerary summary → a friend's `change:` → v2.
- 2:05 Expense logged → balances → "Ada → Tolu 40".
- 2:30 `!list-documents`, repo tour (agents, template YAML), "clone it and plan your own trip".

## 14. Submission

- Track 02 — Best Personal or Creative Workflow.
- Public GitHub repo (MIT) with a README covering which agents are connected, how the room is set up and how to run it (the organiser's README requirements).
- Demo video link.
- Side tracks: a blog post, "Planning a real trip with three Claude Code agents in Telegram, via Switch" (Best Blog: write for a first-time Switch user and include the Windows fixes); a #HowISwitch post; the Wispr scorecard only if it was actually built by voice. Drafts: [`docs/posts/`](docs/posts/).

## 15. Build schedule (Lagos time, Sat Nov 7)

| Time | Task |
|---|---|
| 08:30–09:45 | Docker, Claude Code, Switch Console running; Mattermost reachable |
| 09:45–10:30 | Telegram bot + group with friends; connect in Console; link account |
| 10:30–11:30 | Three agents with CLAUDE.md, tools, permissions; room instructions; commands (§10.7) |
| 11:30–12:00 | Smoke test in the room; fix instructions |
| 12:00–14:30 | Real run with friends (§11). Record your screen as you go |
| 14:30–15:30 | Capture template YAML; export transcript + documents; screenshots |
| 15:30–16:30 | README + setup.md; push repo |
| 16:30–17:30 | Edit 3-minute video; upload |
| 17:30–18:15 | Blog post + #HowISwitch post |
| 18:15–18:30 | Submit (deadline 19:29) |

## 16. Risks & fallbacks

| Risk | Fallback |
|---|---|
| Switch Console on Windows (early access) fails | Apply the Docker and Claude Code fixes (§10); ask in the WeMakeDevs Discord immediately; use a Mac/Linux machine if available. |
| Friends not available at 12:00 | Ask them now; run asynchronously in Telegram (votes have closing times); minimum 1 friend + you. |
| Messages to a busy agent get dropped (known Switch issue) | One request per agent at a time; repost if no "Working…" status appears. |
| Several agents reply to one message | `!follow-ups off`, `!assign-agent @planner`, tag agents explicitly. |
| Agent uses old instructions | Restart the agent (or `!reset @agent`) after editing instructions. |
| Telegram formatting | Instructions forbid tables; short lines. |
| Only one Claude subscription | Fine. Three Claude Code agents can share it; use sonnet for scout and treasurer. |
| Running late | Cut the F17 checklist and the F12 stays vote; keep the destination vote, itinerary and budget. |

## 17. Open questions

- What fields does the submission form have? Sign in to the WeMakeDevs submit page now to see them.
- Can Switch's Telegram bot show approval buttons in groups? If not, the owner answers prompts with yes / no.
