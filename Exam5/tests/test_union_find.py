import random, unittest
import common  # noqa: F401
from union_find_system import UnionFind


class T(unittest.TestCase):
    def test_example1(self):
        uf = UnionFind(5)
        self.assertIs(uf.connected(0, 1), False)
        self.assertIs(uf.union(0, 1), True)
        self.assertIs(uf.connected(0, 1), True)
        self.assertIs(uf.union(1, 2), True)
        self.assertIs(uf.connected(0, 2), True)
        self.assertIs(uf.union(0, 1), False)
        self.assertIn(uf.find(2), (0, 1, 2))
        self.assertEqual(uf.find(2), uf.find(0))

    def test_example2(self):
        uf = UnionFind(3)
        self.assertIs(uf.union(0, 1), True)
        self.assertIs(uf.union(1, 2), True)
        self.assertIs(uf.connected(0, 2), True)
        self.assertEqual(uf.find(0), uf.find(2))

    def test_initial(self):
        uf = UnionFind(4)
        for i in range(4):
            self.assertEqual(uf.find(i), i)
            for j in range(4):
                self.assertEqual(uf.connected(i, j), i == j)

    def test_self_union(self):
        uf = UnionFind(2)
        self.assertIs(uf.union(1, 1), False)
        self.assertIs(uf.connected(1, 1), True)

    def test_edge_sizes(self):
        UnionFind(0)
        uf = UnionFind(1)
        self.assertEqual(uf.find(0), 0)
        self.assertIs(uf.union(0, 0), False)

    def test_return_types(self):
        uf = UnionFind(3)
        self.assertIs(type(uf.union(0, 1)), bool)
        self.assertIs(type(uf.connected(0, 1)), bool)
        self.assertIs(type(uf.find(0)), int)

    def test_random_vs_naive(self):
        for seed in range(200):
            rnd = random.Random(seed)
            n = rnd.randint(1, 40)
            uf, lab = UnionFind(n), list(range(n))
            for _ in range(120):
                a, b = rnd.randrange(n), rnd.randrange(n)
                if rnd.random() < .5:
                    exp = lab[a] != lab[b]
                    self.assertEqual(uf.union(a, b), exp)
                    if exp:
                        o = lab[b]
                        lab = [lab[a] if l == o else l for l in lab]
                else:
                    self.assertEqual(uf.connected(a, b), lab[a] == lab[b])
                self.assertEqual(uf.find(a) == uf.find(b), lab[a] == lab[b])

    def test_path_compression(self):
        uf = UnionFind(10)
        uf.parent = [0] + list(range(9))  # chaîne 9->8->...->0
        uf.find(9)
        self.assertTrue(all(uf.parent[i] == 0 for i in range(1, 10)))

    def test_rank_balanced(self):
        n = 1 << 10
        uf = UnionFind(n)
        s = 1
        while s < n:  # fusions équilibrées
            for i in range(0, n, 2 * s):
                uf.union(i, i + s)
            s *= 2
        depth = lambda x: 0 if uf.parent[x] == x else 1 + depth(uf.parent[x])
        self.assertLessEqual(max(depth(i) for i in range(n)), 10)

    def test_large_chain_no_recursion_error(self):
        n = 200000
        uf = UnionFind(n)
        for i in range(n - 1):
            uf.union(i, i + 1)
        self.assertTrue(uf.connected(0, n - 1))


if __name__ == "__main__":
    unittest.main()
