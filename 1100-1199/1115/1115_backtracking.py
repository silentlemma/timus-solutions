import sys


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n, m = next(tok), next(tok)
    ships = sorted((next(tok) for _ in range(n)), reverse=True)
    rows = [next(tok) for _ in range(m)]
    # the shortest rows first: they have the fewest ways to be filled
    order = sorted(range(m), key=lambda r: rows[r])
    owner = [-1] * n

    def fill(pos):
        if pos == m - 1:
            # the last row takes every ship that is left
            rest = [i for i in range(n) if owner[i] < 0]
            if sum(ships[i] for i in rest) != rows[order[pos]]:
                return False
            for i in rest:
                owner[i] = order[pos]
            return True
        free = [i for i in range(n) if owner[i] < 0]
        # reach[k]: the sums that the free ships from k on can make, as bits
        reach = [1] * (len(free) + 1)
        for k in range(len(free) - 1, -1, -1):
            reach[k] = reach[k + 1] | reach[k + 1] << ships[free[k]]
        return pick(pos, free, reach, 0, rows[order[pos]])

    def pick(pos, free, reach, k, need):
        if need == 0:
            return fill(pos + 1)
        if not reach[k] >> need & 1:
            return False
        last = None
        for j in range(k, len(free)):
            length = ships[free[j]]
            # equal ships are interchangeable: try each length once per place
            if length == last or length > need:
                continue
            if not reach[j + 1] >> (need - length) & 1:
                continue
            last = length
            owner[free[j]] = order[pos]
            if pick(pos, free, reach, j + 1, need - length):
                return True
            owner[free[j]] = -1
        return False

    fill(0)
    out = []
    for r in range(m):
        row = [ships[i] for i in range(n) if owner[i] == r]
        out.append(str(len(row)))
        out.append(" ".join(map(str, row)))
    print("\n".join(out))


main()
