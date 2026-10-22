import os, random, unittest
import common  # noqa: F401
from bridge_finder import bridge_finder as f


def comps(nodes, edges):
    p = {x: x for x in nodes}
    def r(x):
        while p[x] != x: x = p[x]
        return x
    for u, v in edges: p[r(u)] = r(v)
    return len({r(x) for x in nodes})


def ref(g):  # brute force : on enlève chaque arête et on compte les composantes
    nodes = set(g) | {v for l in g.values() for v in l}
    edges = [(u, v) for u in g for v in g[u] if u < v]
    base = comps(nodes, edges)
    return sorted({e for i, e in enumerate(edges) if comps(nodes, edges[:i] + edges[i + 1:]) > base})


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(f({0: [1, 2], 1: [0, 2], 2: [0, 1]}), [])
        self.assertEqual(f({0: [1], 1: [0, 2], 2: [1]}), [(0, 1), (1, 2)])
        self.assertEqual(f({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}), [(1, 3)])
        self.assertEqual(f({}), [])
        self.assertEqual(f({0: [1], 1: [0]}), [(0, 1)])
        self.assertEqual(f({0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1], 3: [1, 4], 4: [1, 3]}), [])

    def test_edge_cases(self):
        self.assertEqual(f({0: []}), [])
        self.assertEqual(f({0: [], 1: []}), [])
        self.assertEqual(f({3: [1], 1: [3]}), [(1, 3)])               # u < v
        self.assertEqual(f({0: [1], 1: [0], 2: [3], 3: [2]}), [(0, 1), (2, 3)])  # plusieurs composantes
        self.assertEqual(f({0: [1, 1], 1: [0, 0]}), [])               # arête doublée : pas un pont
        self.assertEqual(f({0: [0, 1], 1: [0]}), [(0, 1)])            # boucle sur soi
        self.assertEqual(f({-2: [5], 5: [-2]}), [(-2, 5)])

    def test_types(self):
        r = f({0: [1], 1: [0]})
        self.assertIs(type(r), list); self.assertIs(type(r[0]), tuple)

    def test_random_vs_bruteforce(self):
        for seed in range(2000):
            rnd = random.Random(seed)
            n = rnd.randint(0, 10)
            g = {i: [] for i in range(n)}
            for _ in range(rnd.randint(0, 14)):
                if n < 2: break
                u, v = rnd.sample(range(n), 2)
                if v not in g[u]:
                    g[u].append(v); g[v].append(u)
            keys = list(g); rnd.shuffle(keys)
            g = {k: g[k] for k in keys}
            self.assertEqual(f(g), ref(g), g)

    def test_big_chain_no_recursion_error(self):
        n = 100000
        g = {i: [x for x in (i - 1, i + 1) if 0 <= x < n] for i in range(n)}
        self.assertEqual(f(g), [(i, i + 1) for i in range(n - 1)])
        g[0].append(n - 1); g[n - 1].append(0)  # on ferme le cycle
        self.assertEqual(f(g), [])

    def test_no_import(self):
        src = open(os.path.join(os.path.dirname(__file__), "..", "bridge_finder.py")).read()
        self.assertNotIn("import", src)


if __name__ == "__main__":
    unittest.main()
