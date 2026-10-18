class MinHeap:
    def __init__(self):
        self.h = []

    def push(self, val: int) -> None:
        h = self.h
        h.append(val)
        i = len(h) - 1
        while i > 0 and h[(i - 1) // 2] > h[i]:
            p = (i - 1) // 2
            h[i], h[p] = h[p], h[i]
            i = p

    def pop(self) -> int | None:
        h = self.h
        if not h:
            return None
        top = h[0]
        last = h.pop()
        if h:
            h[0] = last
            i = 0
            while True:
                m = i
                for c in (2 * i + 1, 2 * i + 2):
                    if c < len(h) and h[c] < h[m]:
                        m = c
                if m == i:
                    break
                h[i], h[m] = h[m], h[i]
                i = m
        return top

    def peek(self) -> int | None:
        return self.h[0] if self.h else None

    def size(self) -> int:
        return len(self.h)
