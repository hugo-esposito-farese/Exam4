import os, random, unittest
import common  # noqa: F401
from min_heap import MinHeap


class T(unittest.TestCase):
    def test_empty(self):
        h = MinHeap()
        self.assertIsNone(h.pop()); self.assertIsNone(h.peek()); self.assertEqual(h.size(), 0)

    def test_dups_negatives(self):
        h = MinHeap()
        for v in [3, -1, 3, 0, -1, 7]: h.push(v)
        self.assertEqual([h.pop() for _ in range(7)], [-1, -1, 0, 3, 3, 7, None])

    def test_heap_property_and_list(self):
        h = MinHeap()
        for v in random.Random(1).sample(range(1000), 300): h.push(v)
        lst = [v for v in vars(h).values() if isinstance(v, list)][0]
        self.assertTrue(all(lst[(i - 1) // 2] <= lst[i] for i in range(1, len(lst))))

    def test_random_vs_sorted(self):
        for seed in range(800):
            r = random.Random(seed)
            h, ref = MinHeap(), []
            for _ in range(60):
                if r.random() < .6:
                    v = r.randint(-20, 20); h.push(v); ref.append(v); ref.sort()
                else:
                    self.assertEqual(h.pop(), ref.pop(0) if ref else None)
                self.assertEqual(h.peek(), ref[0] if ref else None)
                self.assertEqual(h.size(), len(ref))

    def test_big(self):
        h = MinHeap()
        for v in range(100000, 0, -1): h.push(v)
        self.assertEqual([h.pop() for _ in range(5)], [1, 2, 3, 4, 5])

    def test_no_heapq(self):
        src = open(os.path.join(os.path.dirname(__file__), "..", "min_heap.py")).read()
        self.assertNotIn("heapq", src); self.assertNotIn("import", src)


if __name__ == "__main__":
    unittest.main()
