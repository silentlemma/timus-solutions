MASKS = (0, 1, 2, 1 << 2, 1 | (1 << 2))
PEOPLE = (0, 1, 1, 1, 2)
SIDE = 3
RIGHT_START = 6
UNREACHABLE = -1000

COMPATIBLE = tuple(
    tuple(i for i, before in enumerate(MASKS) if not ((mask | mask << 1 | mask >> 1) & before))
    for mask in MASKS
)


def arrange(rows, offset):
    states = len(MASKS)
    scores = [0] + [UNREACHABLE] * (states - 1)
    previous = bytearray(len(rows) * states)
    for row, layout in enumerate(rows):
        free = 0
        for column in range(SIDE):
            if layout[offset + column] == ".":
                free |= 1 << column
        following = [UNREACHABLE] * states
        for state, mask in enumerate(MASKS):
            if mask & free != mask:
                continue
            best = max(COMPATIBLE[state], key=scores.__getitem__)
            following[state] = scores[best] + PEOPLE[state]
            previous[row * states + state] = best
        scores = following
    state = max(range(states), key=scores.__getitem__)
    count = scores[state]
    chosen = bytearray(len(rows))
    for row in range(len(rows) - 1, -1, -1):
        chosen[row] = MASKS[state]
        state = previous[row * states + state]
    return count, chosen


def main():
    _, group, *rows = open(0).read().split()
    needed = int(group)
    left_count, left = arrange(rows, 0)
    right_count, right = arrange(rows, RIGHT_START)
    if left_count + right_count < needed:
        print("PORAZHENIE")
        return
    answer = ["POBEDA"]
    for side, masks in enumerate((left, right)):
        for row, mask in enumerate(masks, 1):
            for column in range(SIDE):
                if mask & (1 << column):
                    answer.append(f"{row}{'ABCDEF'[side * SIDE + column]}")
                    if len(answer) > needed:
                        print("\n".join(answer))
                        return


if __name__ == "__main__":
    main()
