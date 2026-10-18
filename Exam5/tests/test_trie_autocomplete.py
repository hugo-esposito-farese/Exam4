import random, unittest
import common  # noqa: F401
from trie_autocomplete import trie_autocomplete as f


def trie_ref(words, prefix):
    root = {}
    for w in words:
        n = root
        for c in w:
            n = n.setdefault(c, {})
        n["$"] = 1
    n = root
    for c in prefix:
        if c not in n:
            return []
        n = n[c]
    out = []

    def dfs(n, s):
        if "$" in n:
            out.append(s)
        for c in sorted(k for k in n if k != "$"):
            dfs(n[c], s + c)
    dfs(n, prefix)
    return out


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(f(["apple", "app", "apricot", "banana"], "app"), ["app", "apple"])
        self.assertEqual(f(["apple", "app", "apricot", "banana"], "ban"), ["banana"])
        self.assertEqual(f(["hello", "world", "help", "heap"], "he"), ["heap", "hello", "help"])
        self.assertEqual(f(["test"], "xyz"), [])
        self.assertEqual(f(["cat", "car", "card", "care"], "car"), ["car", "card", "care"])
        self.assertEqual(f([], "test"), [])
        self.assertEqual(f(["a", "ab", "abc"], ""), ["a", "ab", "abc"])

    def test_duplicates(self):
        self.assertEqual(f(["a", "a", "ab", "ab", "a"], "a"), ["a", "ab"])

    def test_case_sensitive(self):
        self.assertEqual(f(["App", "app", "APP"], "app"), ["app"])
        self.assertEqual(f(["App", "app", "APP"], "A"), ["APP", "App"])

    def test_empty_prefix_unsorted_input(self):
        self.assertEqual(f(["b", "c", "a", "b"], ""), ["a", "b", "c"])
        self.assertEqual(f([], ""), [])

    def test_prefix_longer_than_word(self):
        self.assertEqual(f(["ab"], "abc"), [])

    def test_exact_word(self):
        self.assertEqual(f(["abc", "abcd"], "abc"), ["abc", "abcd"])

    def test_empty_word(self):
        self.assertEqual(f(["", "a"], ""), ["", "a"])

    def test_no_mutation_and_type(self):
        w = ["b", "a", "b"]
        r = f(w, "")
        self.assertEqual(w, ["b", "a", "b"])
        self.assertIs(type(r), list)

    def test_random_vs_oracle(self):
        for seed in range(500):
            rnd = random.Random(seed)
            ws = [chr(rnd.choice([65, 97, 98, 233, 0x4e2d])) * rnd.randint(0, 4) for _ in range(rnd.randint(0, 25))]
            p = rnd.choice(ws + [""]) [:rnd.randint(0, 2)] if ws else ""
            self.assertEqual(f(ws, p), sorted({w for w in ws if w.startswith(p)}), (ws, p))

    def test_long_words_and_many_words(self):
        w = "a" * 500
        self.assertEqual(f([w, w + "b"], "a" * 499), [w, w + "b"])
        ws = [str(i) for i in range(20000)]
        self.assertEqual(f(ws, "19"), sorted(x for x in ws if x.startswith("19")))

    def test_random_vs_trie(self):
        for seed in range(500):
            rnd = random.Random(seed)
            ws = ["".join(rnd.choice("abAB") for _ in range(rnd.randint(1, 5)))
                  for _ in range(rnd.randint(0, 25))]
            p = "".join(rnd.choice("abAB") for _ in range(rnd.randint(0, 3)))
            self.assertEqual(f(ws, p), trie_ref(ws, p), (ws, p))


if __name__ == "__main__":
    unittest.main()


class Extra(unittest.TestCase):
    def test_very_long_word(self):  # pas de RecursionError
        w = "a" * 5000
        self.assertEqual(f([w, w + "b", "b"], "a"), [w, w + "b"])
