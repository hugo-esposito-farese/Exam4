import copy, random, unittest
from common import *
from py_island_matrix_counter import island_matrix_counter as f


def ref(m):  # union-find, independent of the traversal used by the solution
    R = len(m); C = len(m[0]) if R else 0
    p = {(i, j): (i, j) for i in range(R) for j in range(C) if m[i][j] == "1"}
    def find(a):
        while p[a] != a:
            p[a] = p[p[a]]; a = p[a]
        return a
    for (i, j) in p:
        for k in ((i + 1, j), (i, j + 1)):
            if k in p:
                p[find(k)] = find((i, j))
    return len({find(a) for a in p})


def M(*rows):
    return [list(r) for r in rows]


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(f(M("11110", "11100", "11110", "00000")), 1)
        self.assertEqual(f(M("11000", "11000", "00100", "00011")), 3)
        self.assertEqual(f([]), 0)

    def test_edges(self):
        self.assertEqual(f([[]]), 0)
        self.assertEqual(f(M("0")), 0)
        self.assertEqual(f(M("1")), 1)
        self.assertEqual(f(M("10", "01")), 2)          # diagonal not connected
        self.assertEqual(f(M("101")), 2)
        self.assertEqual(f(M("1", "0", "1")), 2)
        self.assertEqual(f(M("111", "101", "111")), 1)  # ring
        self.assertEqual(f(M("111", "010", "111")), 1)  # H shape
        self.assertEqual(f(M("101", "010", "101")), 5)
        self.assertEqual(f(M("1111", "0000", "1111")), 2)

    def test_no_recursion_limit_and_no_mutation(self):
        big = [["1"] * 300 for _ in range(300)]
        self.assertEqual(f(big), 1)
        snake = [["1" if (i % 2 == 0 or (i % 4 == 1 and j == 299) or (i % 4 == 3 and j == 0)) else "0"
                  for j in range(300)] for i in range(299)]
        self.assertEqual(f(snake), 1)
        m = M("11000", "11000", "00100", "00011")
        c = copy.deepcopy(m)
        f(m)
        self.assertEqual(m, c)

    def test_random(self):
        rnd = random.Random(4)
        for _ in range(4000):
            R, C = rnd.randint(1, 8), rnd.randint(1, 8)
            p = rnd.choice([.2, .4, .6])
            m = [["1" if rnd.random() < p else "0" for _ in range(C)] for _ in range(R)]
            self.assertEqual(f(m), ref(m), m)


if __name__ == "__main__":
    unittest.main()
