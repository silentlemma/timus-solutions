import sys

CAP = 100  # the largest single credit


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    rows = list(map(int, data[1 : 1 + n]))
    cols = list(map(int, data[1 + n : 1 + 2 * n]))
    matrix = []
    for need in rows:
        # take from the fullest columns first: lower them all towards a level
        def taken(level):
            return sum(min(CAP, max(0, c - level)) for c in cols)

        if taken(0) < need:
            print("NO")
            return
        lo, hi = 0, max(cols)
        while lo < hi:  # the lowest level that takes no more than needed
            mid = (lo + hi) // 2
            if taken(mid) <= need:
                hi = mid
            else:
                lo = mid + 1
        row = [min(CAP, max(0, c - lo)) for c in cols]
        extra = need - sum(row)
        for j, c in enumerate(cols):
            # one more unit from columns that stand exactly at the level
            if extra and row[j] < CAP and c - row[j] == lo and lo > 0:
                row[j] += 1
                extra -= 1
        cols = [c - x for c, x in zip(cols, row)]
        matrix.append(row)
    print("YES")
    print("\n".join(" ".join(map(str, row)) for row in matrix))


main()
