from typing import Any


def py_room_scheduler_site_format(meetings: list[list[int]]) -> dict[str, Any]:
    rooms = []
    for m in sorted(meetings, key=lambda m: m[0]):
        for r in rooms:
            if r[-1][1] <= m[0]:
                r.append(m)
                break
        else:
            rooms.append([m])
    return {"total_rooms": len(rooms), "schedule": rooms}
