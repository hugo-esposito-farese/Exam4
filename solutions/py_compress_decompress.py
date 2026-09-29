import re


def compress(s: str) -> str:
    return re.sub(r'(.)\1+', lambda m: m[1] + str(len(m[0])), s, flags=re.S)


def decompress(s: str) -> str:
    return re.sub(r'(.)(\d+)', lambda m: m[1] * int(m[2]), s, flags=re.S)
