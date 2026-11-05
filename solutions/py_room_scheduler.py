from typing import Any


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:
    rooms = {}
    compteur = 0

    for meeting in sorted(meetings):
        placed = False

        for room in rooms.values():
            if room[-1][1] <= meeting[0]:
                room.append(meeting)
                placed = True
                break

        if not placed:
            rooms[compteur] = [meeting]
            compteur += 1

    return {"total_rooms": compteur, "schedule": rooms}

def main():
    meetings = [
        [9, 10],
        [9, 12],
        [10, 11],
        [11, 12]
    ]

    result = py_room_scheduler(meetings)

    print(result)


if __name__ == "__main__":
    main()
    
