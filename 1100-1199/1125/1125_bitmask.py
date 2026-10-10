import math
import sys


def main():
    tok = sys.stdin.read().split()
    m, n = int(tok[0]), int(tok[1])
    if m == 0 or n == 0:
        sys.stdout.write("\n" * m)
        return
    final = tok[2 : 2 + m]
    visits = list(map(int, tok[2 + m :]))
    # row r as a bit mask of its cells visited an odd number of times
    odd = [sum((visits[r * n + c] & 1) << c for c in range(n)) for r in range(m)]
    # the offsets of integer length, the cell itself included
    offsets = [
        (dr, dc)
        for dr in range(1 - m, m)
        for dc in range(1 - n, n)
        if math.isqrt(dr * dr + dc * dc) ** 2 == dr * dr + dc * dc
    ]
    full = (1 << n) - 1
    out = []
    for r in range(m):
        # bit c is set when cell (r, c) was flipped an odd number of times
        flips = 0
        for dr, dc in offsets:
            if 0 <= r + dr < m:
                row = odd[r + dr]
                flips ^= (row >> dc if dc >= 0 else row << -dc) & full
        out.append("".join("WB"[(final[r][c] == "B") ^ (flips >> c & 1)] for c in range(n)))
    print("\n".join(out))


main()
