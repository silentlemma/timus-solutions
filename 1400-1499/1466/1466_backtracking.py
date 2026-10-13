import itertools
import sys

FIELDS = 3  # a given cell: its column, its row and its number


def structures(n):
    # The square survives block swaps exactly when each number v sits in row pi_v(J) of
    # every block in column J and column sigma_v(I) of every block in row I, and each pair
    # (I, J) meets all positions (pi_v(J), sigma_v(I)) once; such sets are searched.
    perms = list(itertools.permutations(range(n)))
    slots = [(x, y) for x in perms for y in perms]
    used = [[set() for _ in range(n)] for _ in range(n)]
    chosen, found = [], []

    def grow(start):
        if len(chosen) == n * n:
            found.append(list(chosen))
            return
        for k in range(start, len(slots)):
            x, y = slots[k]
            keys = [(i, j, x[j], y[i]) for i in range(n) for j in range(n)]
            if any((r, c) in used[i][j] for i, j, r, c in keys):
                continue
            for i, j, r, c in keys:
                used[i][j].add((r, c))
            chosen.append(slots[k])
            grow(k + 1)
            chosen.pop()
            for i, j, r, c in keys:
                used[i][j].discard((r, c))

    grow(0)
    return found


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    n, k = data[0], data[1]
    given = [(0, 0, 0)]  # the corner holds 0
    cells = data[2:]
    for i in range(k):
        given.append(tuple(cells[FIELDS * i : FIELDS * (i + 1)]))
    for structure in structures(n):
        # each given cell pins its number to the one slot that lands there
        slot_of, number_of, fine = {}, {}, True
        for a, b, v in given:
            j, c, i, r = divmod(a, n) + divmod(b, n)
            s = next(t for t, (x, y) in enumerate(structure) if x[j] == r and y[i] == c)
            if slot_of.setdefault(v, s) != s or number_of.setdefault(s, v) != v:
                fine = False
                break
        if fine:
            print("YES")
            return
    print("NO")


main()
