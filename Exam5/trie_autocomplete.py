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

    res, stack = [], [(n, prefix)]
    while stack:
        n, s = stack.pop()
        if "" in n:
            res.append(s)
        for c in sorted((k for k in n if k), reverse=True):
            stack.append((n[c], s + c))
    return res
