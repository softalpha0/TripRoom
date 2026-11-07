# Setup — rebuild TripRoom from this repo

Time: about 1 hour the first time. Works on Windows, macOS and Linux; Windows fixes are called out.

You need: a computer that stays on during the trip planning, a Claude subscription (one is enough for
all three agents), and a Telegram account (or use the Mattermost bundled with Switch).

Screenshots go in [`screenshots/`](screenshots/) — file names are listed at each step.

---

## 1. Docker Desktop

Install Docker Desktop and start it. Switch runs its local server in Docker.

> **Windows fix — Docker crashes on startup with a stale-socket error.**
> Quit Docker completely (tray icon → Quit). Open `%LOCALAPPDATA%\Docker`, rename the `run` folder
> (e.g. to `run.old`), then start Docker again.

## 2. Claude Code

macOS / Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://claude.ai/install.ps1 | iex
```

> **Windows:** add `%USERPROFILE%\.local\bin` to your user PATH, open a new terminal.
> The Switch Console's own "Install Claude Code" button can fail on Windows — use the installer above.

Then sign in:

```bash
claude auth login
```

Optional, while building: give Claude Code the Switch docs.

```bash
claude mcp add switch-docs --transport http https://docs.switchagents.ai/mcp
```

## 3. Switch Console

1. Download Switch Console from the
   [v0.40.1 release](https://github.com/sandbox-quantum/switch/releases/tag/switch-console-v0.40.1)
   (Windows: `switch-console-x64.exe`). From PowerShell:
   ```powershell
   Invoke-WebRequest -Uri "https://github.com/sandbox-quantum/switch/releases/download/switch-console-v0.40.1/switch-console-x64.exe" -OutFile "$HOME\Downloads\switch-console-x64.exe"
   Start-Process "$HOME\Downloads\switch-console-x64.exe"
   ```
2. **Get started → On this computer.**
3. **Home** should show the server as running. 📸 `01-console-home.png`
4. Mattermost sign-in is under **Home → Mattermost**. Then **Home → Link your Mattermost account**.

## 4. Telegram (so friends can join from their phones)

1. In Telegram, open **@BotFather** → `/newbot` → choose a name and username → save the token.
2. `/mybots` → your bot → **Bot Settings → Group Privacy → Turn off.**
   Do this *before* adding the bot to any group, otherwise it can't see normal messages.
3. Switch Console → **Home → Messaging apps → Connect → Telegram** → bot name, token, username.
   📸 `02-telegram-connected.png`
4. Create a Telegram group with your friends (name it e.g. `trip-zanzibar`) and add the bot.
5. Post any message in the group, then **Link account** in the Console.

Skipping Telegram? Use **Your Rooms → Create room** in Mattermost instead. Everything else is the same.

## 5. Agents

Clone this repo first:

```bash
git clone https://github.com/softalpha0/triproom.git
```

Switch Console → **Your Agents → Add**, three times:

| Field | scout | planner | treasurer |
|---|---|---|---|
| Name | `scout` | `planner` | `treasurer` |
| Description | Researches trip options with sources | Runs the plan, votes, itinerary documents | Budget and fair cost split |
| Run location | This computer | This computer | This computer |
| Directory | `…/triproom/agents/scout` | `…/triproom/agents/planner` | `…/triproom/agents/treasurer` |
| Agent provider | Claude Code | Claude Code | Claude Code |
| Model | sonnet | opus (or sonnet) | sonnet |
| Advanced → Tools | WebSearch, WebFetch | WebSearch (travel times) | — |
| Bypass permissions | **off** | **off** | **off** |
| Who can talk to your agent | Custom rules: you + friends (or Anyone for a demo group) | same | same |

Switch's own tools are always kept. Each agent folder contains **only** its `CLAUDE.md` — don't put
anything else there; the agent can read its folder.

📸 `03-agents.png`

## 6. Room

- **Telegram:** the group becomes a room when the bot is added.
- **Mattermost:** Your Rooms → Create room.

Switch Console → the room → **General → Instructions** → paste the text from
[`room/instructions.md`](../room/instructions.md) (below the line). Restrict editing to yourself.
📸 `04-room-instructions.png`

## 7. In the chat

Replace `<you>` with your Switch username.

```
!invite-agent @scout.<you>
!invite-agent @planner.<you>
!invite-agent @treasurer.<you>
!set-alias @scout.<you> @scout
!set-alias @planner.<you> @planner
!set-alias @treasurer.<you> @treasurer
```

Send the role-definition message from [`room/roles.md`](../room/roles.md), then:

```
@scout take the scout role
@planner take the planner role
@treasurer take the treasurer role
!assign-agent @planner
!follow-ups off
!roles
```

Telegram also accepts `/invite_agent`, `/set_alias` etc. Mattermost accepts only the `!` form, and it
must be the first thing in the message. 📸 `05-roles.png`

The full ordered list is in [`room/commands.md`](../room/commands.md).

## 8. Smoke test

```
@planner what is this room for?
```

It should mention the golden rule (agents propose, people vote, the trip lead confirms).
A generic answer means the instructions didn't save — paste them again, then restart the agent
(or `!reset @planner`).

Permission prompts: when an agent wants to use a tool, you'll be asked to **Allow once / Allow for
session / Decline**. If the buttons don't show in the Telegram group, answer with `yes` / `no`.

## 9. Capture the template

Switch Console → **Templates → save this room as a template**. Make the room name a field, and make
the three agents fields with type **agent**. Copy the YAML into
[`template/triproom.yaml`](../template/). See [`template/README.md`](../template/README.md).

## 10. Plan the trip

```
@planner start a trip
```

The run sheet is in [`examples/real-run/README.md`](../examples/real-run/README.md).

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `!assign-agent` or `!follow-ups` replies "Following the conversation isn't switched on for this Switch server" | Your server has that feature off, so un-tagged messages reach nobody. Skip both commands and **tag an agent in every message**, votes included: `@planner B`, `@planner confirm`, `@planner change: …`. |
| Agent doesn't answer, no "Working…" status | Messages to a busy agent can be dropped. Wait for it to finish, then repost. One request per agent at a time. |
| Several agents answer one message | `!follow-ups off`, `!assign-agent @planner`, and tag agents explicitly. |
| Agent uses old instructions | Restart it in the Console, or `!reset @agent`. |
| Agent stuck | `!interrupt @agent` |
| Tables look broken in Telegram | The room instructions forbid tables; remind the agent or re-save instructions. |
| Bot can't see group messages | Group Privacy was on when it joined. Turn it off, remove and re-add the bot. |
| Times are an hour off | Switch timestamps are UTC; rule 5 of the instructions says to convert to Lagos time. Change the timezone line if your group is elsewhere. |
| Want to check the treasurer's maths | `python3 scripts/settle.py your-expenses.txt` |
