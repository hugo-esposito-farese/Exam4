def trie_autocomplete(words: list[str], prefix: str) -> list[str]:
    root = {}
    for w in words:
        n = root
        for c in w:
            n = n.setdefault(c, {})
        n[""] = {}  # fin de mot

    n = root
    for c in prefix:
        if c not in n:
            return []
        n = n[c]

    def walk(n, s):
        res = [s] if "" in n else []
        for c in sorted(k for k in n if k):
            res += walk(n[c], s + c)
        return res

    return walk(n, prefix)
