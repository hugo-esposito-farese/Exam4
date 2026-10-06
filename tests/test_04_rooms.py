import copy, heapq, random, unittest
from common import *
from py_room_scheduler_site_format import py_room_scheduler_site_format as f


def min_rooms(ms):
    h = []
    for s, e in sorted(ms):
        if h and h[0] <= s:
            heapq.heapreplace(h, e)
        else:
            heapq.heappush(h, e)
    return len(h)


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(f([[0, 30], [5, 10], [15, 20]]),
                         {"total_rooms": 2, "schedule": [[[0, 30]], [[5, 10], [15, 20]]]})
        self.assertEqual(f([]), {"total_rooms": 0, "schedule": []})

    def test_known(self):
        self.assertEqual(f([[7, 10], [2, 4]]), {"total_rooms": 1, "schedule": [[[2, 4], [7, 10]]]})
        self.assertEqual(f([[1, 5], [5, 8]]), {"total_rooms": 1, "schedule": [[[1, 5], [5, 8]]]})  # touching ok
        self.assertEqual(f([[1, 5], [2, 6], [3, 7]])["total_rooms"], 3)
        self.assertEqual(f([[5, 10]]), {"total_rooms": 1, "schedule": [[[5, 10]]]})
        # unsorted input; first free room (lowest index) is used
        self.assertEqual(f([[15, 20], [0, 30], [5, 10]]),
                         {"total_rooms": 2, "schedule": [[[0, 30]], [[5, 10], [15, 20]]]})
        self.assertEqual(f([[0, 10], [1, 3], [4, 6], [11, 12]]),
                         {"total_rooms": 2, "schedule": [[[0, 10], [11, 12]], [[1, 3], [4, 6]]]})

    def test_no_mutation(self):
        ms = [[15, 20], [0, 30], [5, 10]]
        c = copy.deepcopy(ms)
        f(ms)
        self.assertEqual(ms, c)

    def test_random(self):
        rnd = random.Random(3)
        for _ in range(4000):
            ms = []
            for _ in range(rnd.randint(0, 12)):
                s = rnd.randint(0, 20)
                ms.append([s, s + rnd.randint(1, 8)])
            r = f(ms)
            rooms = r["schedule"]
            self.assertEqual(r["total_rooms"], len(rooms))
            self.assertEqual(len(rooms), min_rooms(ms), ms)          # minimal
            self.assertEqual(sorted(m for room in rooms for m in map(tuple, room)),
                             sorted(map(tuple, ms)))                    # every meeting once
            for room in rooms:
                self.assertTrue(room)
                for a, b in zip(room, room[1:]):
                    self.assertLessEqual(a[1], b[0], ms)                # no overlap, chronological
            # deterministic sequential assignment: each meeting is in the FIRST room that was free
            order = sorted(ms, key=lambda m: m[0])
            sim = []
            for m in order:
                for rr in sim:
                    if rr[-1][1] <= m[0]:
                        rr.append(m); break
                else:
                    sim.append([m])
            self.assertEqual(rooms, sim)


if __name__ == "__main__":
    unittest.main()
