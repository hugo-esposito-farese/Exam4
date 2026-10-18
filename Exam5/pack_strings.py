def pack(strs: list[str]) -> str:
    return "".join(str(len(s)) + ":" + s for s in strs)


def unpack(s: str) -> list[str]:
    res, i = [], 0
    while i < len(s):
        j = s.index(":", i)
        n = int(s[i:j])
        res.append(s[j + 1:j + 1 + n])
        i = j + 1 + n
    return res
