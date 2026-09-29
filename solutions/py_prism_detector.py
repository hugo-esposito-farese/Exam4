D = {(1, 0): "H", (-1, 0): "H-", (0, 1): "V", (0, -1): "V-",
     (1, 1): "D1", (-1, -1): "D1-", (-1, 1): "D2", (1, -1): "D2-"}


def prism_detector(grid: list[str], pattern: str):
    res = []
    if not grid or not pattern:
        return res
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for (dx, dy), code in D.items():
                if all(0 <= y + dy * i < len(grid) and 0 <= x + dx * i < len(grid[y + dy * i])
                       and grid[y + dy * i][x + dx * i] == c for i, c in enumerate(pattern)):
                    res.append((x, y, code))
    return res
