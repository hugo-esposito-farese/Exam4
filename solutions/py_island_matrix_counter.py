def island_matrix_counter(matrix: list[list[str]]) -> int:
    seen = set()
    n = 0
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == "1" and (i, j) not in seen:
                n += 1
                seen.add((i, j))
                st = [(i, j)]
                while st:
                    y, x = st.pop()
                    for a, b in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if (0 <= a < len(matrix) and 0 <= b < len(matrix[a])
                                and matrix[a][b] == "1" and (a, b) not in seen):
                            seen.add((a, b))
                            st.append((a, b))
    return n
