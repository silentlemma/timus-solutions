SIDE = 8
JUMPS = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))


for column in range(SIDE):
    counts = []
    for row in range(SIDE):
        attacked = sum(0 <= column + dc < SIDE and 0 <= row + dr < SIDE for dc, dr in JUMPS)
        counts.append(str(attacked))
    print(f'    b"{"".join(counts)}",')
