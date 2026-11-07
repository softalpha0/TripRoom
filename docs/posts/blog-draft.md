# Planning a real trip with three Claude Code agents in Telegram, via Switch

> Draft outline for the Best Blog side track. Write it **after** the real run, from what actually happened.
> Audience: someone who has never used Switch. Replace every [bracket].

## The problem
Every group trip dies in the group chat. [Your own story: the last trip that never happened / the money nobody paid back.]

## The idea: agents propose, people vote, the lead confirms
One Telegram group = one Switch room. Three agents, one job each: scout, planner, treasurer.
Why three and not one: [roles, exclusive documents, one answer per thread].

## Setting it up (first-time Switch user)
1. Docker + Claude Code + Switch Console. **Windows fixes:** the Docker stale-socket fix (rename `%LOCALAPPDATA%\Docker\run`); the native Claude Code installer + PATH.
2. Telegram bot: turn Group Privacy **off before** adding it to the group.
3. Three agents, each folder holds only its CLAUDE.md. [screenshot]
4. Room instructions, aliases, roles, `!assign-agent`, `!follow-ups off`. [screenshot of `!roles`]

## The real run
[Who joined, where you went, how the vote went, a real change request, the real balances.
Quote 3–4 real messages from examples/real-run/transcript.md.]

## What surprised me
[e.g. dropped messages to a busy agent, permission prompts in a group, timezone conversion.]

## Try it
Repo: [link] · Video: [link] · Clone it, import template/triproom.yaml, say "@planner start a trip".
