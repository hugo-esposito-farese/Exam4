def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    if end not in sentence:
        return 0
    words = set(sentence)
    q = {start}
    n = 1
    while q:
        if end in q:
            return n
        words -= q
        q = {w for w in words if any(len(u) == len(w) and sum(a != b for a, b in zip(u, w)) == 1 for u in q)}
        n += 1
    return 0
