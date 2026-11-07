# Template

`triproom.yaml` must be **captured from a working room** in Switch Console — not hand-written.

1. Finish setup (docs/setup.md steps 1–8) so the room has its instructions, three agents, aliases,
   main agent and follow-ups setting.
2. Switch Console → **Templates → save this room as a template**.
3. Turn these into fields:
   - room name → field (e.g. `trip_name`)
   - scout, planner, treasurer → fields with type **agent**
4. Copy the YAML into `template/triproom.yaml` and commit it.

To use it: Switch Console → **Templates → Import template** → `triproom.yaml`, then pick your own
three agents for the agent fields.

> Status: **captured** from the real `weekend_trip` room on 7 Nov 2026. `triproom.yaml` is that capture
> with the trip's documents and members removed, the agent params typed `agent`, the messaging app made a
> param, and the aliases dropped (a room alias may not share a name with a role).
> The raw capture (`captured-room.yaml`) stays out of git because it lists friends' Telegram usernames.
