class PrefixDictionary:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            n = n.setdefault(c, {})
        n["$"] = {}  # fin de mot

    def _node(self, s):
        n = self.root
        for c in s:
            if c not in n:
                return None
            n = n[c]
        return n

    def search(self, word: str) -> bool:
        n = self._node(word)
        return n is not None and "$" in n

    def starts_with(self, prefix: str) -> bool:
        return bool(self._node(prefix))  # noeud existant et non vide
