def bridge_finder(graph: dict[int, list[int]]) -> list[tuple[int, int]]:
    disc, low, res = {}, {}, []
    for s in graph:
        if s in disc:
            continue
        disc[s] = low[s] = len(disc)
        stack = [[s, None, iter(graph.get(s, [])), False]]  # noeud, parent, voisins, arête parent vue
        while stack:
            top = stack[-1]
            u, p, it = top[0], top[1], top[2]
            for v in it:
                if v == p and not top[3]:
                    top[3] = True  # on ignore une seule fois l'arête vers le parent
                elif v in disc:
                    low[u] = min(low[u], disc[v])
                else:
                    disc[v] = low[v] = len(disc)
                    stack.append([v, u, iter(graph.get(v, [])), False])
                    break
            else:
                stack.pop()
                if p is not None:
                    low[p] = min(low[p], low[u])
                    if low[u] > disc[p]:
                        res.append((min(p, u), max(p, u)))
    return sorted(res)
