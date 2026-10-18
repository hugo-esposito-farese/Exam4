import os, random, unittest
import common  # noqa: F401
from cache_keeper import CacheKeeper


class Ref:
    def __init__(self, cap): self.cap, self.l = cap, []  # [(k, v)] du moins au plus récent
    def get(self, k):
        for i, (a, v) in enumerate(self.l):
            if a == k:
                self.l.append(self.l.pop(i)); return v
        return -1
    def put(self, k, v):
        self.l = [x for x in self.l if x[0] != k] + [(k, v)]
        if len(self.l) > self.cap: self.l.pop(0)


class T(unittest.TestCase):
    def test_update_refreshes(self):
        c = CacheKeeper(2)
        c.put(1, 1); c.put(2, 2); c.put(1, 10); c.put(3, 3)
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(1), 10)
        self.assertEqual(c.get(3), 3)

    def test_cap1(self):
        c = CacheKeeper(1)
        self.assertIsNone(c.put(1, 1))
        c.put(2, 2)
        self.assertEqual(c.get(1), -1)
        self.assertEqual(c.get(2), 2)

    def test_miss_does_not_change_order(self):
        c = CacheKeeper(2)
        c.put(1, 1); c.put(2, 2); c.get(5); c.put(3, 3)
        self.assertEqual(c.get(1), -1)

    def test_random(self):
        for seed in range(1000):
            r = random.Random(seed)
            cap = r.randint(1, 5)
            c, ref = CacheKeeper(cap), Ref(cap)
            for _ in range(80):
                k = r.randrange(8)
                if r.random() < .5:
                    v = r.randrange(-5, 100); c.put(k, v); ref.put(k, v)
                else:
                    self.assertEqual(c.get(k), ref.get(k))

    def test_no_ordereddict(self):
        src = open(os.path.join(os.path.dirname(__file__), "..", "cache_keeper.py")).read()
        self.assertNotIn("OrderedDict", src)
        self.assertNotIn("import", src)


if __name__ == "__main__":
    unittest.main()
