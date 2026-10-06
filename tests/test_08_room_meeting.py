import random, unittest
from common import *
from room_meeting import meeting as f
from py_room_scheduler import py_room_scheduler as old


class T(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(f([]), {"rooms_needed": 0, "room_assignments": {}})

    def test_example_3(self):  # input reconstructed from the output given by the exam notes
        self.assertEqual(f([[1, 5], [8, 9], [8, 9]]),
                         {"rooms_needed": 2, "room_assignments": {0: [[1, 5], [8, 9]], 1: [[8, 9]]}})

    def test_format_and_validity(self):
        rnd = random.Random(8)
        for _ in range(3000):
            ms = []
            for _ in range(rnd.randint(0, 12)):
                s = rnd.randint(0, 20); ms.append([s, s + rnd.randint(1, 8)])
            r = f(ms)
            self.assertEqual(set(r), {"rooms_needed", "room_assignments"})
            ra = r["room_assignments"]
            self.assertEqual(list(ra), list(range(r["rooms_needed"])))   # int keys 0..n-1
            self.assertTrue(all(type(k) is int for k in ra))
            o = old(ms)                                                   # same assignment as the validated old version
            self.assertEqual(r["rooms_needed"], o["total_rooms"])
            self.assertEqual(list(ra.values()), o["schedule"])
            for room in ra.values():
                for a, b in zip(room, room[1:]):
                    self.assertLessEqual(a[1], b[0])


if __name__ == "__main__":
    unittest.main()
