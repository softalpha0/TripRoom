import unittest
from fractions import Fraction
from settle import parse, balances, transfers


class SettleTest(unittest.TestCase):
    def test_readme_example(self):
        people, ex = parse("people: Ada, Tolu, Sam\nTolu paid 75 for deposit")
        self.assertEqual(sorted(transfers(balances(people, ex))),
                         [("Ada", "Tolu", 25), ("Sam", "Tolu", 25)])

    def test_partial_split_and_zero_sum(self):
        people, ex = parse(
            "people: Ada, Tolu, Sam\n"
            "Tolu paid 120 for boat tour\n"
            "Ada paid 30 for fuel split Ada, Sam\n"
        )
        bal = balances(people, ex)
        self.assertEqual(sum(bal.values()), 0)
        self.assertEqual(bal["Tolu"], 80)
        moved = {}
        for a, b, x in transfers(bal):
            moved[a] = moved.get(a, 0) - x
            moved[b] = moved.get(b, 0) + x
        self.assertEqual({k: v for k, v in moved.items()}, {k: v for k, v in bal.items() if v})

    def test_unknown_person(self):
        people, ex = parse("people: Ada\nBob paid 10 for snacks")
        with self.assertRaises(ValueError):
            balances(people, ex)

    def test_thirds(self):
        people, ex = parse("people: A, B, C\nA paid 100 for stay")
        bal = balances(people, ex)
        self.assertEqual(bal["B"], Fraction(-100, 3))
        self.assertEqual(sum(bal.values()), 0)


if __name__ == "__main__":
    unittest.main()
