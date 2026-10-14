"""One test from a seed and a mode: a 4 x 4 grid and up to 100 words.
Mode 1 takes random letters from a small alphabet and words read off
random paths, some changed; mode 2 fills the grid with one letter but
one, and asks long words that end in the odd letter; mode 3 asks words
of every length along a snake; mode 4 is a random grid with random
words."""

import random
import sys

SIDE = 4
CELLS = SIDE * SIDE
WORDS = 100


def neighbours(c):
    r, col = divmod(c, SIDE)
    out = []
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= r + dr < SIDE and 0 <= col + dc < SIDE:
            out.append((r + dr) * SIDE + col + dc)
    return out


def path_word(rng, grid, length):
    """A word read along a random self-avoiding path, as long as it goes."""
    c = rng.randrange(CELLS)
    used, word = {c}, [grid[c]]
    while len(word) < length:
        options = [x for x in neighbours(c) if x not in used]
        if not options:
            break
        c = rng.choice(options)
        used.add(c)
        word.append(grid[c])
    return "".join(word)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        letters = "ab" if seed % 2 else "abc"
        grid = [rng.choice(letters) for _ in range(CELLS)]
        words = []
        for _ in range(WORDS):
            w = list(path_word(rng, grid, rng.randint(1, CELLS)))
            if rng.random() < 0.5:
                w[rng.randrange(len(w))] = rng.choice(letters)
            words.append("".join(w))
    elif mode == 2:
        grid = ["a"] * CELLS
        grid[rng.randrange(CELLS)] = "b"
        words = ["a" * rng.randint(CELLS - 4, CELLS - 1) + "b" for _ in range(WORDS)]
    elif mode == 3:
        grid = [rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(CELLS)]
        snake = [
            r * SIDE + (c if r % 2 == 0 else SIDE - 1 - c) for r in range(SIDE) for c in range(SIDE)
        ]
        line = "".join(grid[c] for c in snake)
        words = [line[i:j] for i in range(CELLS) for j in range(i + 1, CELLS + 1)]
        rng.shuffle(words)
        words = words[:WORDS]
    else:
        grid = [rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(CELLS)]
        words = [
            "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 4)))
            for _ in range(WORDS)
        ]
    for r in range(SIDE):
        print("".join(grid[r * SIDE : (r + 1) * SIDE]))
    print(len(words))
    for w in words:
        print(w)


main()
