from sys import stdin, stdout

LETTERS = 26
FIRST = ord("A")

rows, _, words = map(int, stdin.readline().split())
grid = "".join(stdin.readline().strip() for _ in range(rows))
used = "".join(stdin.readline().strip() for _ in range(words))
# The fixed 26-letter alphabet makes repeated native counts linear overall.
# Disjoint placements remove the same multiset regardless of their paths.
stdout.write(
    str(
        "".join(
            letter * (grid.count(letter) - used.count(letter))
            for letter in map(chr, range(FIRST, FIRST + LETTERS))
        )
    )
)
