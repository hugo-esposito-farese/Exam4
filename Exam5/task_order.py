import heapq


def task_order(n: int, prereqs: list[list[int]]) -> list[int]:
    nxt = [[] for _ in range(n)]
    deg = [0] * n
    for a, b in prereqs:
        nxt[b].append(a)
        deg[a] += 1
    q = [i for i in range(n) if deg[i] == 0]
    heapq.heapify(q)
    res = []
    while q:
        x = heapq.heappop(q)
        res.append(x)
        for y in nxt[x]:
            deg[y] -= 1
            if deg[y] == 0:
                heapq.heappush(q, y)
    return res if len(res) == n else []
