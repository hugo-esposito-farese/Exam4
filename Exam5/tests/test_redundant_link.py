import random, unittest
import common  # noqa: F401
from redundant_link import redundant_link


def is_tree(n, edges):
    p = list(range(n + 1))
    def f(x):
        while p[x] != x: x = p[x]
        return x
    for u, v in edges:
        a, b = f(u), f(v)
        if a == b: return False
        p[a] = b
    return len(edges) == n - 1


def ref(edges):  # dernier edge du tableau dont la suppression donne un arbre
    n = len(edges)
    for i in range(n - 1, -1, -1):
        if is_tree(n, edges[:i] + edges[i + 1:]):
            return edges[i]


class T(unittest.TestCase):
    def test_random(self):
        for seed in range(2000):
            r = random.Random(seed)
            n = r.randint(3, 12)
            nodes = list(range(1, n + 1)); r.shuffle(nodes)
            edges = [[nodes[i], nodes[r.randrange(i)]] for i in range(1, n)]
            edges = [e if r.random() < .5 else e[::-1] for e in edges]
            while True:
                u, v = r.sample(range(1, n + 1), 2)
                if [u, v] not in edges and [v, u] not in edges: break
            edges.insert(r.randint(0, len(edges)), [u, v])
            got = redundant_link([e[:] for e in edges])
            self.assertEqual(got, ref(edges), edges)

    def test_big(self):
        n = 100000
        edges = [[i, i + 1] for i in range(1, n)] + [[n, 1]]
        self.assertEqual(redundant_link(edges), [n, 1])


if __name__ == "__main__":
    unittest.main()
