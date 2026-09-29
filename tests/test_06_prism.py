import random, unittest
from common import *
from py_prism_detector import prism_detector as f

# direction table exactly as written in the subject: (dx, dy) -> code, x = column, y = row (down)
DIRS = [((1, 0), "H"), ((-1, 0), "H-"), ((0, 1), "V"), ((0, -1), "V-"),
        ((1, 1), "D1"), ((-1, -1), "D1-"), ((-1, 1), "D2"), ((1, -1), "D2-")]


def ref(grid, pat):
    if not grid or not pat:
        return []
    out = []
    for y, row in enumerate(grid):
        for x in range(len(row)):
            for (dx, dy), code in DIRS:
                s = ""
                for i in range(len(pat)):
                    a, b = x + dx * i, y + dy * i
                    if 0 <= b < len(grid) and 0 <= a < len(grid[b]):
                        s += grid[b][a]
                if s == pat:
                    out.append((x, y, code))
    return out


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(f(["CAT", "A..", "T.."], "CAT"), [(0, 0, "H"), (0, 0, "V")])
        self.assertEqual(f([], "CAT"), [])

    def test_empty(self):
        self.assertEqual(f(["ABC"], ""), [])
        self.assertEqual(f([], ""), [])
        self.assertEqual(f([""], "A"), [])

    def test_each_direction(self):
        self.assertEqual(f(["CAT"], "TAC"), [(2, 0, "H-")])
        self.assertEqual(f(["T", "A", "C"], "TAC"), [(0, 0, "V")])
        self.assertEqual(f(["T", "A", "C"], "CAT"), [(0, 2, "V-")])
        self.assertEqual(f(["C..", ".A.", "..T"], "CAT"), [(0, 0, "D1")])
        self.assertEqual(f(["C..", ".A.", "..T"], "TAC"), [(2, 2, "D1-")])
        # (dx,dy) = (-1, 1) is the subject's "D2"; (1,-1) is "D2-" (vectors, not the prose, taken literally)
        self.assertEqual(f(["..C", ".A.", "T.."], "CAT"), [(2, 0, "D2")])
        self.assertEqual(f(["..C", ".A.", "T.."], "TAC"), [(0, 2, "D2-")])

    def test_multiple_and_bounds(self):
        self.assertEqual(f(["AA", "AA"], "AA"), ref(["AA", "AA"], "AA"))
        self.assertEqual(f(["CATCAT"], "CAT"), [(0, 0, "H"), (3, 0, "H")])
        self.assertEqual(f(["CAT"], "CATS"), [])
        self.assertEqual(f(["CA"], "CAT"), [])

    def test_random(self):
        rnd = random.Random(5)
        for _ in range(4000):
            R, C = rnd.randint(1, 6), rnd.randint(1, 6)
            g = ["".join(rnd.choice("AB") for _ in range(C)) for _ in range(R)]
            pat = "".join(rnd.choice("AB") for _ in range(rnd.randint(1, 4)))
            self.assertEqual(f(g, pat), ref(g, pat), (g, pat))
            self.assertTrue(all(type(t) is tuple for t in f(g, pat)))


if __name__ == "__main__":
    unittest.main()
