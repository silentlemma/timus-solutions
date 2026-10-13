import sys

EMPTY, WHITE, BLACK = 0, 1, 2


def main():
    n = int(sys.stdin.readline())
    hummocks = [WHITE] * n + [EMPTY] + [BLACK] * n
    hole = n
    moves = []
    # runs of 1, 2, ..., n, n, n, ..., 1 moves, the colours taking turns,
    # and in a run a frog jumps into the hole when it can and slides otherwise
    runs = list(range(1, n + 1)) + [n] + list(range(n, 0, -1))
    colour = BLACK
    for run in runs:
        step = 1 if colour == BLACK else -1  # where the frogs come from
        other = WHITE if colour == BLACK else BLACK
        for _ in range(run):
            far, near = hole + 2 * step, hole + step
            if 0 <= far <= 2 * n and hummocks[far] == colour and hummocks[near] == other:
                frog = far
            else:
                frog = near
            hummocks[hole], hummocks[frog] = colour, EMPTY
            hole = frog
            moves.append(frog)
        colour = other
    sys.stdout.write("%d\n%s\n" % (len(moves), " ".join(map(str, moves))))


main()
