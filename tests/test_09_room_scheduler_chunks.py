import random, unittest
from common import *
from py_room_scheduler_chunks import py_room_scheduler as g
from py_room_scheduler import py_room_scheduler as main


class T(unittest.TestCase):
    def test_statement_examples(self):  # the 5 examples of the exam statement
        R = lambda n, a: {"rooms_needed": n, "room_assignments": a}
        self.assertEqual(g([[0, 30], [5, 10], [15, 20]]), R(2, {0: [[0, 30], [5, 10]], 1: [[15, 20]]}))
        self.assertEqual(g([[9, 10], [9, 12], [11, 13]]), R(2, {0: [[9, 10], [9, 12]], 1: [[11, 13]]}))
        self.assertEqual(g([[1, 5], [8, 9], [8, 9]]), R(2, {0: [[1, 5], [8, 9]], 1: [[8, 9]]}))
        self.assertEqual(g([]), R(0, {}))
        self.assertEqual(g([[1, 2], [3, 4], [5, 6]]), R(1, {0: [[1, 2], [3, 4], [5, 6]]}))

    def test_same_room_count_as_main(self):
        rnd = random.Random(9)
        for _ in range(2000):
            ms = [[s, s + rnd.randint(1, 8)] for s in (rnd.randint(0, 20) for _ in range(rnd.randint(0, 12)))]
            r = g(ms)
            self.assertEqual(r["rooms_needed"], main(ms)["rooms_needed"])
            self.assertEqual([m for v in r["room_assignments"].values() for m in v], sorted(ms, key=lambda m: m[0]))


if __name__ == "__main__":
    unittest.main()
