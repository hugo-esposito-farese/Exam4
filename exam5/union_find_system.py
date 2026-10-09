class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.r[x] < self.r[y]:
            x, y = y, x
        self.p[y] = x
        self.r[x] += self.r[x] == self.r[y]
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
