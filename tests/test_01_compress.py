import random, unittest
from itertools import groupby
from common import *
from py_compress_decompress import compress, decompress


def ref_compress(s):
    out = ""
    for c, g in groupby(s):
        k = len(list(g))
        out += c + (str(k) if k > 1 else "")
    return out


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(compress("aabcccccaaa"), "a2bc5a3")
        self.assertEqual(decompress("a2bc5a3"), "aabcccccaaa")
        self.assertEqual(compress(""), "")
        self.assertEqual(decompress(""), "")

    def test_edges(self):
        self.assertEqual(compress("a"), "a")
        self.assertEqual(compress("ab"), "ab")
        self.assertEqual(compress("aa"), "a2")
        self.assertEqual(compress("a" * 12), "a12")
        self.assertEqual(compress("a" * 100 + "b" * 10), "a100b10")
        self.assertEqual(decompress("a12"), "a" * 12)
        self.assertEqual(decompress("a"), "a")
        self.assertEqual(decompress("abc"), "abc")
        self.assertEqual(decompress("a1b1"), "ab")
        self.assertEqual(decompress("a10b"), "a" * 10 + "b")
        self.assertEqual(decompress("x2y3z"), "xxyyyz")

    def test_special_chars(self):
        self.assertEqual(compress("\n\n\n  ..!!"), "\n3 2.2!2")
        self.assertEqual(decompress("\n3 2.2!2"), "\n\n\n  ..!!")
        self.assertEqual(compress("AAaa"), "A2a2")

    def test_random(self):
        rnd = random.Random(1)
        for _ in range(3000):
            s = "".join(rnd.choice("abcXY _\n.") * rnd.choice([1, 1, 2, 3, 9, 10, 11, 25])
                        for _ in range(rnd.randint(0, 12)))
            c = compress(s)
            self.assertEqual(c, ref_compress(s), s)
            self.assertEqual(decompress(c), s, s)


if __name__ == "__main__":
    unittest.main()
