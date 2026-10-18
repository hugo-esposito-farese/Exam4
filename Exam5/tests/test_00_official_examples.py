"""Rejoue mot pour mot les exemples de https://rank06.42exam.net/"""
import ast, importlib, json, os, unittest
import common  # noqa: F401

with open(os.path.join(os.path.dirname(__file__), "rank06_examples.json")) as fd:
    DATA = json.load(fd)

# Erreur du site : put(1), put(2), put(3) en capacité 2 évince la clé 1 (la moins
# récemment utilisée), donc get(2) vaut 2 et non -1. Aucune LRU ne donne -1 ici ;
# il manque sans doute un c.get(1) (c'est alors l'exemple 3). On teste la vraie LRU.
SITE_ERRORS = {"c = CacheKeeper(2); c.put(1, 1); c.put(2, 2); c.put(3, 3); c.get(2)": 2}


def run(code, ns):
    tree = ast.parse(code)
    last = tree.body.pop()
    exec(compile(tree, "<ex>", "exec"), ns)
    return eval(compile(ast.Expression(last.value), "<ex>", "eval"), ns)


class Official(unittest.TestCase):
    def test_all(self):
        n = 0
        for s in DATA:
            mod = importlib.import_module(s["file"][:-3])
            for ex in s["examples"]:
                with self.subTest(s["name"], input=ex["input"]):
                    got = run(ex["input"], dict(vars(mod)))
                    self.assertEqual(got, SITE_ERRORS.get(ex["input"], ast.literal_eval(ex["output"])))
                    n += 1
        self.assertEqual(len(DATA), 8)
        print(f"\n{n} exemples officiels OK", end=" ")


if __name__ == "__main__":
    unittest.main()
