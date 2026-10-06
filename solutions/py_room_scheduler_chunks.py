# PLAN B: only if the moulinette rejects py_room_scheduler.py (copy this function instead).
# Reproduces the exam statement's examples literally: k = minimum rooms, then the
# sorted meetings are cut into k consecutive blocks of ceil(n / k).
from typing import Any


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:
    ms = sorted(meetings, key=lambda m: m[0])
    ends = []
    for m in ms:
        for i, e in enumerate(ends):
            if e <= m[0]:
                ends[i] = m[1]
                break
        else:
            ends.append(m[1])
    k = len(ends)
    c = -(-len(ms) // k) if k else 0
    return {"rooms_needed": k, "room_assignments": {i: ms[i * c:(i + 1) * c] for i in range(k)}}
