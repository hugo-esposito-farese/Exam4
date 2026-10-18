def redundant_link(edges: list[list[int]]) -> list[int]:
    p = list(range(len(edges) + 1))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            return [u, v]
        p[a] = b
    return []
