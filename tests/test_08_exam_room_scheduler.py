import random, unittest
from common import *
from py_room_scheduler import py_room_scheduler as f
from py_room_scheduler_site_format import py_room_scheduler_site_format as old


class T(unittest.TestCase):
    def test_exam_inputs(self):
        self.assertEqual(f([]), {"rooms_needed": 0, "room_assignments": {}})
        self.assertEqual(f([[1, 5], [8, 9], [8, 9]]),
                         {"rooms_needed": 2, "room_assignments": {0: [[1, 5], [8, 9]], 1: [[8, 9]]}})
        # one room -> {0: meetings}, not the bare list
        self.assertEqual(f([[1, 2], [3, 4], [5, 6]]),
                         {"rooms_needed": 1, "room_assignments": {0: [[1, 2], [3, 4], [5, 6]]}})
        self.assertEqual(f([[0, 30], [5, 10], [15, 20]]),
                         {"rooms_needed": 2, "room_assignments": {0: [[0, 30]], 1: [[5, 10], [15, 20]]}})
        self.assertEqual(f([[9, 10], [9, 12], [11, 13]]),
                         {"rooms_needed": 2, "room_assignments": {0: [[9, 10], [11, 13]], 1: [[9, 12]]}})

    def test_one_entry_per_room(self):
        r = f([[1, 5], [2, 6], [3, 7]])
        self.assertEqual(r["rooms_needed"], 3)
        self.assertEqual(r["room_assignments"], {0: [[1, 5]], 1: [[2, 6]], 2: [[3, 7]]})

    def test_same_as_validated_site_version(self):
        rnd = random.Random(8)
        for _ in range(3000):
            ms = []
            for _ in range(rnd.randint(0, 12)):
                s = rnd.randint(0, 20); ms.append([s, s + rnd.randint(1, 8)])
            r, o = f(ms), old(ms)
            self.assertEqual(set(r), {"rooms_needed", "room_assignments"})
            self.assertEqual(r["rooms_needed"], o["total_rooms"])
            self.assertEqual(r["room_assignments"], dict(enumerate(o["schedule"])))
            self.assertEqual(list(r["room_assignments"]), list(range(r["rooms_needed"])))


if __name__ == "__main__":
    unittest.main()
