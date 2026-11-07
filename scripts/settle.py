#!/usr/bin/env python3
"""Check the treasurer's maths: balances and a short list of transfers.

The treasurer agent does this in chat; this script lets the trip lead double-check it.
It never touches money — it only does arithmetic.

Input file, one expense per line (blank lines and # comments ignored):

    people: Ada, Tolu, Sam
    Tolu paid 75 for deposit
    Ada paid 30 for fuel split Ada, Sam

"split A, B" limits who shares that expense; otherwise everyone shares it.

Usage:  python3 scripts/settle.py expenses.txt
"""
import re
import sys
from fractions import Fraction

LINE = re.compile(r"^(\w+) paid ([\d.]+) for (.+?)(?: split (.+))?$", re.I)


def parse(text):
    people, expenses = [], []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.lower().startswith("people:"):
            people = [p.strip() for p in line[7:].split(",") if p.strip()]
            continue
        m = LINE.match(line)
        if not m:
            raise ValueError(f"can't read line: {raw!r}")
        payer, amount, what, split = m.groups()
        sharers = [p.strip() for p in split.split(",")] if split else None
        expenses.append((payer, Fraction(amount), what, sharers))
    if not people:
        raise ValueError("missing 'people:' line")
    return people, expenses


def balances(people, expenses):
    bal = {p: Fraction(0) for p in people}
    for payer, amount, _what, sharers in expenses:
        sharers = sharers or people
        for name in [payer, *sharers]:
            if name not in bal:
                raise ValueError(f"{name} is not in the people list")
        bal[payer] += amount
        for p in sharers:
            bal[p] -= amount / len(sharers)
    assert sum(bal.values()) == 0, "balances do not sum to zero"
    return bal


def transfers(bal):
    """Greedy settle: largest debtor pays largest creditor. At most n-1 transfers."""
    debt = sorted(([-v, p] for p, v in bal.items() if v < 0), reverse=True)
    cred = sorted(([v, p] for p, v in bal.items() if v > 0), reverse=True)
    out = []
    while debt and cred:
        d, c = debt[0], cred[0]
        x = min(d[0], c[0])
        out.append((d[1], c[1], x))
        d[0] -= x
        c[0] -= x
        if d[0] == 0:
            debt.pop(0)
        if c[0] == 0:
            cred.pop(0)
        debt.sort(reverse=True)
        cred.sort(reverse=True)
    return out


def fmt(x):
    return f"{float(x):.2f}".rstrip("0").rstrip(".")


def main(path):
    with open(path, encoding="utf-8") as f:
        people, expenses = parse(f.read())
    bal = balances(people, expenses)
    print("Balances (+ is owed, - owes):")
    for p in people:
        print(f"  {p}: {fmt(bal[p])}")
    print("Transfers:")
    for a, b, x in transfers(bal) or []:
        print(f"  {a} -> {b} {fmt(x)}")
    print("Check: balances sum to 0 ✓")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
