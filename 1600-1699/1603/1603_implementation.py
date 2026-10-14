import sys
from collections import Counter

SIDE = 4
CELLS = SIDE * SIDE


def main():
    data = sys.stdin.read().split()
    grid = "".join(data[:SIDE])
    n = int(data[SIDE])
    words = data[SIDE + 1 : SIDE + 1 + n]
    near = [[] for _ in range(CELLS)]
    for c in range(CELLS):
        r, col = divmod(c, SIDE)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= r + dr < SIDE and 0 <= col + dc < SIDE:
                near[c].append((r + dr) * SIDE + col + dc)
    have = Counter(grid)

    def found(word):
        if any(have[ch] < k for ch, k in Counter(word).items()):
            return False
        dead = set()  # (visited cells, last cell) that cannot finish the word

        def walk(cell, mask, i):
            # cell holds word[i - 1]; mask is every cell used so far
            if i == len(word):
                return True
            key = mask * CELLS + cell
            if key in dead:
                return False
            for nxt in near[cell]:
                if not mask >> nxt & 1 and grid[nxt] == word[i]:
                    if walk(nxt, mask | 1 << nxt, i + 1):
                        return True
            dead.add(key)
            return False

        return any(grid[c] == word[0] and walk(c, 1 << c, 1) for c in range(CELLS))

    out = []
    for w in words:
        out.append("%s: %s" % (w, "YES" if found(w) else "NO"))
    print("\n".join(out))


main()
