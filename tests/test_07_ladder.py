import random, unittest
from collections import deque, defaultdict
from common import *
from py_word_ladder import word_ladder as f


def ref(start, end, words):  # LeetCode-127 wildcard-bucket BFS
    ws = set(words)
    if end not in ws:
        return 0
    b = defaultdict(list)
    for w in ws | {start}:
        for i in range(len(w)):
            b[w[:i] + "*" + w[i + 1:]].append(w)
    q, seen = deque([(start, 1)]), {start}
    while q:
        w, d = q.popleft()
        if w == end:
            return d
        for i in range(len(w)):
            for n in b[w[:i] + "*" + w[i + 1:]]:
                if n not in seen:
                    seen.add(n); q.append((n, d + 1))
    return 0


class T(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(f("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEqual(f("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)

    def test_edges(self):
        self.assertEqual(f("a", "c", ["a", "b", "c"]), 2)
        self.assertEqual(f("hot", "dog", ["hot", "dog"]), 0)
        self.assertEqual(f("hot", "dot", ["dot"]), 2)
        self.assertEqual(f("hit", "cog", []), 0)
        self.assertEqual(f("hit", "hot", ["hot"]), 2)
        self.assertEqual(f("hot", "hot", ["hot"]), 1)
        self.assertEqual(f("aa", "bb", ["ab", "bb"]), 3)
        self.assertEqual(f("aa", "bb", ["bb"]), 0)                 # would need 2 changes
        self.assertEqual(f("abc", "abcd", ["abcd"]), 0)             # different lengths never adjacent
        self.assertEqual(f("hit", "cog", ["hot", "hot", "dot", "dog", "cog", "cog"]), 5)  # duplicates
        self.assertEqual(f("hit", "cog", ["hit", "hot", "dot", "dog", "cog"]), 5)  # start in list
        self.assertEqual(f("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]), 4)

    def test_random(self):
        rnd = random.Random(6)
        for _ in range(4000):
            L = rnd.randint(1, 4)
            gen = lambda: "".join(rnd.choice("abc") for _ in range(L))
            words = [gen() for _ in range(rnd.randint(0, 14))]
            s, e = gen(), gen()
            self.assertEqual(f(s, e, words), ref(s, e, words), (s, e, words))

    def test_input_untouched_and_speed(self):
        w = ["hot", "dot", "dog", "lot", "log", "cog"]
        f("hit", "cog", w)
        self.assertEqual(w, ["hot", "dot", "dog", "lot", "log", "cog"])
        import itertools, time
        words = ["".join(p) for p in itertools.product("abcd", repeat=5)]  # 1024 words
        t = time.time()
        self.assertEqual(f("aaaaa", "dddda", words), ref("aaaaa", "dddda", words))
        self.assertLess(time.time() - t, 5)


if __name__ == "__main__":
    unittest.main()
