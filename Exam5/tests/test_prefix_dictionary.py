import random, unittest
import common  # noqa: F401
from prefix_dictionary import PrefixDictionary


class T(unittest.TestCase):
    def test_empty(self):
        d = PrefixDictionary()
        self.assertIs(d.search("a"), False)
        self.assertIs(d.starts_with("a"), False)
        self.assertIs(d.starts_with(""), False)  # aucun mot inséré
        self.assertIs(d.search(""), False)

    def test_basic(self):
        d = PrefixDictionary()
        d.insert("apple")
        self.assertIs(d.search("apple"), True)
        self.assertIs(d.search("app"), False)
        self.assertIs(d.search("apples"), False)
        self.assertIs(d.starts_with("app"), True)
        self.assertIs(d.starts_with("apple"), True)
        self.assertIs(d.starts_with("apples"), False)
        self.assertIs(d.starts_with("b"), False)
        self.assertIs(d.starts_with(""), True)
        d.insert("app")
        self.assertIs(d.search("app"), True)
        d.insert("apple")
        self.assertIs(d.search("apple"), True)

    def test_return_types(self):
        d = PrefixDictionary()
        self.assertIsNone(d.insert("a"))

    def test_random(self):
        for seed in range(300):
            r = random.Random(seed)
            d, ws = PrefixDictionary(), set()
            for _ in range(60):
                w = "".join(r.choice("abc") for _ in range(r.randint(0, 5)))
                op = r.randrange(3)
                if op == 0:
                    d.insert(w); ws.add(w)
                elif op == 1:
                    self.assertIs(d.search(w), w in ws)
                else:
                    self.assertIs(d.starts_with(w), any(x.startswith(w) for x in ws))

    def test_long(self):
        d = PrefixDictionary()
        d.insert("a" * 5000)
        self.assertTrue(d.search("a" * 5000))
        self.assertTrue(d.starts_with("a" * 4999))


if __name__ == "__main__":
    unittest.main()
