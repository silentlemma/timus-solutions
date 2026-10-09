import sys


def target(rows, cols, n):
    """A table with the given odd rows and odd columns and as few plus signs
    as possible: max(len(rows), len(cols)) of them."""
    t = [[False] * n for _ in range(n)]
    for r, c in zip(rows, cols):
        t[r][c] = True
    # the rest come in pairs, so a shared line keeps its parity
    for r in rows[len(cols) :]:
        t[r][0] = not t[r][0]
    for c in cols[len(rows) :]:
        t[0][c] = not t[0][c]
    return t


def main():
    tok = sys.stdin.read().split()
    n = 2 * int(tok[0]) + 1
    a = [[ch == "+" for ch in row] for row in tok[1 : 1 + n]]
    ops = []

    def flip(perm):
        ops.append(list(perm))
        for r, c in enumerate(perm):
            a[r][c] = not a[r][c]

    # two transversals that differ in two rows flip the corners of a
    # rectangle, which keeps every row and column parity; one transversal
    # flips all the parities at once
    odd_rows = [i for i in range(n) if sum(a[i]) % 2]
    odd_cols = [j for j in range(n) if sum(a[i][j] for i in range(n)) % 2]
    if max(len(odd_rows), len(odd_cols)) == n:
        flip(list(range(n)))
        odd_rows = [i for i in range(n) if sum(a[i]) % 2]
        odd_cols = [j for j in range(n) if sum(a[i][j] for i in range(n)) % 2]
    t = target(odd_rows, odd_cols, n)
    last = n - 1
    for i in range(last):
        for j in range(last):
            if a[i][j] != t[i][j]:
                # rows i and last take columns j and last, the others the rest
                rest = [c for c in range(n) if c != j and c != last]
                perm = []
                for r in range(n):
                    perm.append(j if r == i else last if r == last else rest.pop())
                flip(perm)
                perm[i], perm[last] = perm[last], perm[i]
                flip(perm)
    out = ["There is solution:"]
    out += [" ".join(str(c + 1) for c in perm) for perm in ops]
    sys.stdout.write("\n".join(out) + "\n")


main()
