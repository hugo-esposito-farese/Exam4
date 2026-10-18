class CacheKeeper:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}  # dict garde l'ordre d'insertion : premier = moins récent

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d[key] = self.d.pop(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d.pop(key, None)
        self.d[key] = value
        if len(self.d) > self.cap:
            del self.d[next(iter(self.d))]
