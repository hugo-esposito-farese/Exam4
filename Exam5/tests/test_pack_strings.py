import random, unittest
import common  # noqa: F401
from pack_strings import pack, unpack

CASES = [[], [""], ["", ""], ["", "a", ""], ["hello", "world"], ["42", "exam#net", "level:6"],
         ["1:a", "0:", "::", "##", "3#x"], ["a\nb", "\n", " ", "\t", "é✓中😀"], ["12345678901"], ["x" * 100000]]


class T(unittest.TestCase):
    def test_cases(self):
        for c in CASES:
            p = pack(c)
            self.assertIs(type(p), str)
            self.assertEqual(unpack(p), c)

    def test_distinguish(self):
        self.assertNotEqual(pack([]), pack([""]))
        self.assertNotEqual(pack(["a", "b"]), pack(["ab"]))

    def test_random(self):
        alpha = "ab:#0123456789 \n\\\"'é😀"
        for seed in range(2000):
            r = random.Random(seed)
            c = ["".join(r.choice(alpha) for _ in range(r.randint(0, 12))) for _ in range(r.randint(0, 8))]
            self.assertEqual(unpack(pack(c)), c)

    def test_forbidden(self):
        import os
        src = open(os.path.join(os.path.dirname(__file__), "..", "pack_strings.py")).read()
        for w in ("json", "pickle", "eval"):
            self.assertNotIn(w, src)


if __name__ == "__main__":
    unittest.main()
