import sys

SIZE = 8


def main():
    rows = sys.stdin.read().split()[:SIZE]
    # square (x, y), both from 0, is bit x * SIZE + y; the first input line is y = 7
    whites, blacks = 0, 0
    for r, line in enumerate(rows):
        for x, ch in enumerate(line):
            bit = 1 << (x * SIZE + SIZE - 1 - r)
            if ch == "W":
                whites |= bit
            elif ch == "B":
                blacks |= bit
    total = bin(blacks).count("1")
    # jumps[s]: the (jumped square, landing square) pairs from square s; only
    # squares off the edge can be jumped, so the landing stays on the board
    jumps = []
    for x in range(SIZE):
        for y in range(SIZE):
            here = []
            for dx in (-1, 1):
                for dy in (-1, 1):
                    tx, ty = x + 2 * dx, y + 2 * dy
                    if 0 <= tx < SIZE and 0 <= ty < SIZE:
                        here.append(((x + dx) * SIZE + y + dy, tx * SIZE + ty))
            jumps.append(here)
    best = total  # removing every black always wins

    def dfs(square, black, white, removed, taken):
        """black, white: the pieces still on the board, the mover excluded;
        removed: the white pieces taken away so far, taken: the blacks
        captured so far. Every black not captured has to be taken away."""
        nonlocal best
        best = min(best, removed + total - taken)
        for mid, to in jumps[square]:
            if not black >> mid & 1:
                continue
            nb, nw, cost = black & ~(1 << mid), white, removed
            if nb >> to & 1:
                nb &= ~(1 << to)  # a black in the way is taken away, uncaptured
            if nw >> to & 1:
                nw &= ~(1 << to)  # a white in the way costs one more
                cost += 1
            dfs(to, nb, nw, cost, taken + 1)

    start = whites
    while start:
        bit = start & -start
        start ^= bit
        dfs(bit.bit_length() - 1, blacks, whites & ~bit, 0, 0)
    print(best)


main()
