"""A fillword that has a solution: a seed, the grid height and width, the
number of words, the longest word and the number of distinct letters.
Words are laid as random self-avoiding paths over free cells, the remaining
cells get random letters, and the words are listed in random order."""

import random
import sys

FIRST = ord("A")


def main():
    seed, n, m, p, longest, letters = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    abc = [chr(FIRST + k) for k in range(letters)]
    grid = [[None] * m for _ in range(n)]
    words = []
    free = [(r, c) for r in range(n) for c in range(m)]
    rng.shuffle(free)
    for r, c in free:
        if len(words) == p:
            break
        if grid[r][c] is not None:
            continue
        word = []
        size = rng.randint(1, longest)
        while True:
            grid[r][c] = rng.choice(abc)
            word.append(grid[r][c])
            steps = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            steps = [(a, b) for a, b in steps if 0 <= a < n and 0 <= b < m and grid[a][b] is None]
            if len(word) == size or not steps:
                break
            r, c = rng.choice(steps)
        words.append("".join(word))
    for row in grid:
        for c in range(m):
            if row[c] is None:
                row[c] = rng.choice(abc)
    rng.shuffle(words)
    lines = ["%d %d %d" % (n, m, len(words))] + ["".join(row) for row in grid] + words
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
