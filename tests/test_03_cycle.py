import random, unittest
from common import *
from py_graph_cycle_detector import py_graph_cycle_detector as f


def ref(g):  # recursive 3-colour DFS
    sys.setrecursionlimit(10000)
    col = {}
    def dfs(u):
        col[u] = 1
        for v in g.get(u, []):
            if col.get(v, 0) == 1 or (col.get(v, 0) == 0 and dfs(v)):
                return True
        col[u] = 2
        return False
    r = any(col.get(u, 0) == 0 and dfs(u) for u in list(g))
    sys.setrecursionlimit(200)
    return r


class T(unittest.TestCase):
    def test_examples(self):
        self.assertIs(f({0: [1], 1: [2], 2: [0]}), True)
        self.assertIs(f({0: [1], 1: [2], 2: []}), False)
        self.assertIs(f({}), False)

    def test_edges(self):
        self.assertIs(f({0: [0]}), True)                       # self loop
        self.assertIs(f({0: [1], 1: [0]}), True)
        self.assertIs(f({0: []}), False)
        self.assertIs(f({0: [1, 1], 1: []}), False)            # duplicate edges
        self.assertIs(f({0: [1, 2], 1: [3], 2: [3], 3: []}), False)  # diamond, not a cycle
        self.assertIs(f({0: [1], 1: []}), False)
        self.assertIs(f({0: [1]}), False)                      # neighbour missing from keys
        self.assertIs(f({0: [5], 5: [6], 6: [5]}), True)       # cycle on keyless-introduced node
        self.assertIs(f({0: [1], 1: [], 2: [3], 3: [4], 4: [2]}), True)   # disconnected, 2nd comp cyclic
        self.assertIs(f({0: [1], 1: [], 2: [3], 3: []}), False)
        self.assertIs(f({-1: [-2], -2: [-1]}), True)           # negative ids
        self.assertIs(f({1: [2], 2: [3], 3: [1, 4], 4: []}), True)
        self.assertIs(f({1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}), False)

    def test_input_untouched(self):
        g = {0: [1], 1: [2], 2: [0]}
        f(g)
        self.assertEqual(g, {0: [1], 1: [2], 2: [0]})

    def test_deep(self):
        n = 200000
        self.assertIs(f({i: [i + 1] for i in range(n)}), False)
        g = {i: [i + 1] for i in range(n)}; g[n] = [0]
        self.assertIs(f(g), True)

    def test_random(self):
        rnd = random.Random(2)
        for _ in range(5000):
            n = rnd.randint(0, 9)
            g = {i: [rnd.randrange(n + 2) for _ in range(rnd.randint(0, 3))] for i in range(n) if rnd.random() < .9}
            if rnd.random() < .5:  # sparse (acyclic-ish) variant
                g = {u: [v for v in vs if v > u] for u, vs in g.items()}
            self.assertEqual(f(g), ref(g), g)

    def test_forbidden(self):
        s = source("py_graph_cycle_detector")
        self.assertNotIn("graphlib", s)
        self.assertNotIn("TopologicalSorter", s)


if __name__ == "__main__":
    unittest.main()
