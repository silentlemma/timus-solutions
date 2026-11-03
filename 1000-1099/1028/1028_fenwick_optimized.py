import sys
from array import array

MAX_COORD = 32000


def main():
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(tokens)
    # Every counter is at most the15000 stars, so unsigned16-bit cells
    # suffice. Streaming tokens avoids retaining both coordinates of all stars.
    tree = array("H", [0]) * (MAX_COORD + 2)
    count = array("H", [0]) * n
    top = MAX_COORD + 1
    for _ in range(n):
        start = next(tokens) + 1
        next(tokens)
        j, level = start, 0
        while j:
            level += tree[j]
            j &= j - 1
        count[level] += 1
        j = start
        while j <= top:
            tree[j] += 1
            j += j & -j
    del tokens
    sys.stdout.write("\n".join(map(str, count)) + "\n")


main()
