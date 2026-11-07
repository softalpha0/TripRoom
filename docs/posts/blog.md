# Planning a real trip with three Claude Code agents in Telegram, via Switch

*How three friends and three AI agents picked a destination, a hotel and a day-by-day plan in one hour, without the AI deciding anything.*

---

## The problem: group trips die in the group chat

You know how it goes. Someone says "we should travel in December!" Two hundred messages later there are links nobody opened, three different date ranges, and no decision. If the trip does happen, one person pays the deposit and spends the next month chasing everyone for their share.

Asking a chatbot doesn't fix it. ChatGPT isn't **in** the group chat. It doesn't know who agreed to what, it can't run a vote, and it can't keep a plan that everyone sees.

So for the **Flip the Switch** hackathon I built **TripRoom**: three AI agents that live *inside* our Telegram group and help us plan, while my friends and I keep every decision.

> **Golden rule:** agents propose, people vote, the trip lead confirms. Nothing is final until someone types "confirm".

## The idea: one room, three agents, one job each

[Switch](https://docs.switchagents.ai) turns a chat (Telegram, Slack, Mattermost, Discord or Teams) into a **room** where people and AI agents work together. I gave each agent one job:

| Agent | Job | Owns |
|---|---|---|
| **scout** | Researches destinations, stays, transport and food on the web, with sources | Research posts |
| **planner** | Asks the kickoff questions, runs the votes, writes the itinerary | Trip brief, Itinerary, Decisions log |
| **treasurer** | Tracks costs and works out who owes whom | Budget and split |

All three are **Claude Code** agents running on my laptop. Each one has its own folder with a short `CLAUDE.md` saying what it does and what it must never do. The big one: **never book, pay, or ask anyone for money.**

## What actually happened (the real run)

On Saturday 7 November my friends Mufasa and Alina and I planned a real weekend away.

**11:43** I typed `@planner start a trip`. The planner asked six questions in one message: dates, who's coming and from where, budget, style, must-haves and no-gos, and who the trip lead is.

**11:49** Mufasa answered. The planner created a shared **Trip brief** document. When I answered a minute later, it updated it to **v2**: 4–6 December, from Lagos, $1,500 each, beach and culture, good food, no flights over two hours.

**11:51** The planner asked the scout for options *by itself*. The scout ran a dozen web searches and posted three:

- **A: Accra, Ghana.** About a 1h flight
- **B: Grand-Bassam, via Abidjan.** About a 1h45–2h flight
- **C: Ouidah, via Cotonou.** About a 45 min flight

Every option had a price range **and source links**. Where it couldn't find something, like a museum entry fee or Sunday flight times, it wrote **"Not stated"** instead of making it up. That rule, from the room instructions, did more for trust than anything else.

**11:54** We both voted **B**. The planner posted "B wins 2–0", warned me that the flight is right at my 2-hour limit, and waited. I typed `confirm`, and it went into the **Decisions log** as decision 1.

**12:05** Alina joined late. The planner didn't count her vote until she said she was coming. Then it added her to the brief (**v3**). We picked the **Koral Beach Hotel** 3–0.

Then Mufasa asked for a change: swap the museum for a **lagoon boat trip**. The planner changed only that day, bumped the **Itinerary** to **v5**, and waited for my confirm.

Mufasa paid a **$200 hotel deposit** and told the treasurer. I asked for balances:

> Benjamin → Mufasa 67 · Alina → Mufasa 67. Sum: 134 − 67 − 67 = 0

**Result:** in about an hour we had three decisions made by vote, four shared documents, a three-day itinerary and a settled deposit. Nobody had to be "the spreadsheet person".

## How I set it up (first-time Switch user, on Windows)

Here's everything I did, including the parts that went wrong.

**1. Install the basics.** You need Docker Desktop, Claude Code (`irm https://claude.ai/install.ps1 | iex` in PowerShell, then add `%USERPROFILE%\.local\bin` to PATH) and Switch Console from the [Switch releases page](https://github.com/sandbox-quantum/switch/releases). In Switch Console, choose **Get started → On this computer**. It starts its own server and Mattermost in Docker, which takes about 5–10 minutes the first time.

**2. 🚧 My Claude account hit its weekly limit.** Switch said "Claude Code is signed in but could not answer a test prompt (weekly limit)". The fix was an API key from the Claude Console:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-…", "User")
claude auth logout
```

**Gotcha:** the key only exists in **new** terminal windows. My test kept saying "Not logged in" until I closed every terminal (or loaded the key with `$env:ANTHROPIC_API_KEY = [Environment]::GetEnvironmentVariable("ANTHROPIC_API_KEY","User")`), then restarted Switch Console.

**3. Make a Telegram bot.** In @BotFather: `/newbot`, save the token, then `/mybots` → Bot Settings → **Group Privacy → Turn off** *before* adding the bot to any group. In Switch Console go to **Home → Messaging apps → Connect → Telegram**. Then create a group, add the bot, and send "hello". The group becomes a Switch room on its own.

**4. 🚧 Linking my Telegram account.** Switch searches for your Telegram **username**, not your display name, and the search fails if you include the `@`. I typed `softalpha`, not `@SoftalphaX`, and it found me.

**5. Create the agents.** In **Your Agents → +**, I made three, named `planner.softalpha0`, `scout.softalpha0` and `treasurer.softalpha0`. I pasted each one's `CLAUDE.md` into **Agent instructions**, set **Who can talk to your agent** to **Anyone** so my friends could talk to them, and left Bypass permissions off.

🚧 The **Directory** setting is hidden under **Settings**, and the folder picker opens in Documents. I pasted the full path, `C:\Users\…\triproom\agents\planner`, into the Folder box.

**6. Room rules.** I pasted the instructions under **Your Rooms → weekend_trip → Configuration**. Then, in Telegram:

```
!invite-agent @planner.softalpha0      (and scout, treasurer)
!set-alias @planner.softalpha0 @planner
!assign-agent @planner                 un-tagged messages go to the planner
!follow-ups off                        one agent answers per thread
@planner define a shared role called scout, an exclusive role called planner, …
@scout take the scout role             (and the other two)
!roles
```

🚧 **Roles vs aliases:** I gave the roles the same names as the aliases, so `@planner` addresses the *role*. Until each agent took its role, Switch warned "no agent currently holds the planner role". Ask each agent to take its role straight after you create the roles.

**7. Capture it as a template.** Under **Configuration → Capture as template**, Switch turns the room (instructions, roles and agents) into YAML. I cleaned it up for reuse and committed it. Anyone can now import it and get the same room.

## What I learned

- **One job per agent beats one smart agent.** The planner asked the scout and the treasurer for help on its own, but none of them stepped on each other's toes.
- **Shared documents are the killer feature.** The Trip brief, Itinerary, Decisions log and Budget live in the room, so every agent reads the same facts and every friend sees the same plan.
- **"Not stated" builds trust.** An agent that admits what it doesn't know is one you can let near your money.
- **Humans stay in charge.** The agents never decided anything. They made deciding easy.

## Try it

Everything is in the repo: the agents, the room instructions, the template, the setup guide with Windows fixes, and the real transcript.

👉 **github.com/softalpha0/TripRoom** · 🎥 Demo: https://youtu.be/HfV6ZZXyhB4

Clone it, invite your friends, and type `@planner start a trip`.

*Built for Flip the Switch (WeMakeDevs × DevTools Academy). #HowISwitch*
