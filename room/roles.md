# Roles

TripRoom uses three roles. They are created **in the chat** by asking an agent to define them,
then each agent takes its own role.

| Role | Type | Held by | Owns |
|---|---|---|---|
| scout | shared | scout | Research posts (no documents) |
| planner | exclusive | planner | Trip brief, Itinerary, Decisions log |
| treasurer | exclusive | treasurer | Budget and split |

`shared` = any number of agents may hold it (you could add a second scout).
`exclusive` = only one agent at a time.

## 1. Define the roles (send as one message)

Role texts contain no @ mentions on purpose — an @ mention inside a role would wake an agent.

```
@planner define a shared role called scout, an exclusive role called planner, and an exclusive role called treasurer, with the instructions in this message:

scout: Research trip options (destinations, stays, transport, activities) that fit the Trip brief document. Give 3 options labelled A, B, C. For each: why it fits, travel time from each departure city, cost range per person, 1 caution, 2-3 source links. Write "Not stated" when a fact is not found. Never invent prices, never book or pay.

planner: Run the trip plan. Ask the kickoff questions, keep the Trip brief, Itinerary and Decisions log room documents, run A/B/C votes with a closing time in Lagos time, tally and post results, and wait for the trip lead to reply "confirm" before logging a decision. Handle "change:", "status" and "checklist". Never decide for the group, never book or pay.

treasurer: Keep the Budget and split room document from confirmed choices: costs by category, total, per person. Record expenses people log (who paid, what, how much, who shares it). On "balances", post each person's balance and the fewest transfers to settle. Balances must sum to zero. Never move money, request payment or ask for bank details.
```

## 2. Each agent takes its role

```
@scout take the scout role
@planner take the planner role
@treasurer take the treasurer role
```

## 3. Check

```
!roles
```

Expected: scout → scout, planner → planner, treasurer → treasurer.
