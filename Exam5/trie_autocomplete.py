def trie_autocomplete(words: list[str], prefix: str) -> list[str]:
    return sorted({w for w in words if w.startswith(prefix)})
