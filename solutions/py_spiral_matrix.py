def generate_spiral(n: int) -> list[list[int]]:
    m = [[0] * n for _ in range(n)]
    x = y = 0
    dx, dy = 1, 0
    for i in range(1, n * n + 1):
        m[y][x] = i
        if not (0 <= x + dx < n and 0 <= y + dy < n and m[y + dy][x + dx] == 0):
            dx, dy = -dy, dx
        x += dx
        y += dy
    return m
