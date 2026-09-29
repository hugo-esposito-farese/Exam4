import unittest
from common import *
from py_spiral_matrix import generate_spiral


def ref(n):  # layer by layer, independent of the solution's walking technique
    m = [[0] * n for _ in range(n)]
    k = 1
    for L in range((n + 1) // 2):
        lo, hi = L, n - 1 - L
        for c in range(lo, hi + 1): m[lo][c] = k; k += 1
        for r in range(lo + 1, hi + 1): m[r][hi] = k; k += 1
        if hi > lo:
            for c in range(hi - 1, lo - 1, -1): m[hi][c] = k; k += 1
            for r in range(hi - 1, lo, -1): m[r][lo] = k; k += 1
    return m


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(generate_spiral(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        self.assertEqual(generate_spiral(1), [[1]])

    def test_known(self):
        self.assertEqual(generate_spiral(2), [[1, 2], [4, 3]])
        self.assertEqual(generate_spiral(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
        self.assertEqual(generate_spiral(5), [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7],
                                              [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])

    def test_zero(self):
        self.assertEqual(generate_spiral(0), [])

    def test_vs_ref_and_props(self):
        for n in range(0, 40):
            m = generate_spiral(n)
            self.assertEqual(m, ref(n), n)
            self.assertEqual(len(m), n)
            self.assertTrue(all(len(r) == n for r in m))
            self.assertEqual(sorted(v for r in m for v in r), list(range(1, n * n + 1)))
            self.assertTrue(all(type(v) is int for r in m for v in r))

    def test_rows_independent(self):
        m = generate_spiral(3)
        m[0][0] = 99
        self.assertEqual(generate_spiral(3)[0][0], 1)
        self.assertEqual(len({id(r) for r in generate_spiral(4)}), 4)


if __name__ == "__main__":
    unittest.main()
