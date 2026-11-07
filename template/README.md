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

> Status: **not captured yet** — add `triproom.yaml` after the room is set up.
