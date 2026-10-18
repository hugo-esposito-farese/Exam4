import itertools, os, random, unittest
import common  # noqa: F401
from task_order import task_order


def ref(n, pre):  # naïf : à chaque étape, plus petit index dispo
    done, res = set(), []
    need = {i: {b for a, b in pre if a == i} for i in range(n)}
    while len(res) < n:
        ok = [i for i in range(n) if i not in done and need[i] <= done]
        if not ok:
            return []
        done.add(ok[0]); res.append(ok[0])
    return res


class T(unittest.TestCase):
    def test_edges(self):
        self.assertEqual(task_order(0, []), [])
        self.assertEqual(task_order(1, []), [0])
        self.assertEqual(task_order(1, [[0, 0]]), [])
        self.assertEqual(task_order(3, [[0, 2]]), [1, 2, 0])
        self.assertEqual(task_order(3, [[0, 1], [0, 1]]), [1, 0, 2])
        self.assertEqual(task_order(3, [[1, 0], [2, 1], [0, 2]]), [])
        self.assertEqual(task_order(4, [[1, 0], [0, 1]]), [])  # cycle partiel

    def test_random(self):
        for seed in range(1500):
            r = random.Random(seed)
            n = r.randint(0, 9)
            pre = [[r.randrange(n), r.randrange(n)] for _ in range(r.randint(0, 12))] if n else []
            pre = [p for p in pre if p[0] != p[1] or r.random() < .1]
            self.assertEqual(task_order(n, pre), ref(n, pre), (n, pre))

    def test_big(self):
        n = 100000
        self.assertEqual(task_order(n, [[i + 1, i] for i in range(n - 1)]), list(range(n)))

    def test_no_graphlib(self):
        src = open(os.path.join(os.path.dirname(__file__), "..", "task_order.py")).read()
        self.assertNotIn("graphlib", src)


if __name__ == "__main__":
    unittest.main()
