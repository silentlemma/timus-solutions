"""A random game: a seed, n, m and the largest move. The move 1 is always
there, so a move is possible from every pile."""

import random
import sys


def main():
    seed, n, m, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    moves = [1] + [rng.randint(1, min(top, n)) for _ in range(m - 1)]
    rng.shuffle(moves)
    sys.stdout.write("%d %d\n%s\n" % (n, m, " ".join(map(str, moves))))


if __name__ == "__main__":
    main()
