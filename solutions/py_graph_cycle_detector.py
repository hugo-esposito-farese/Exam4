def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    indeg = {n: 0 for n in graph}
    for vs in graph.values():
        for v in vs:
            indeg[v] = indeg.get(v, 0) + 1
    q = [n for n in indeg if not indeg[n]]
    seen = 0
    while q:
        n = q.pop()
        seen += 1
        for v in graph.get(n, ()):
            indeg[v] -= 1
            if not indeg[v]:
                q.append(v)
    return seen < len(indeg)
