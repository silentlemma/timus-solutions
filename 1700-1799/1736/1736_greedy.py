import sys

WIN = 3
SIGNS = ("<", "<=", ">=", ">")


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    left = [int(w) for w in data[1:n + 1]]
    got = [[0] * n for _ in range(n)]
    active = list(range(n))
    # the weakest team plays all its games now: it keeps its own points
    # and hands the rest out, three a game, to the strongest teams first
    while len(active) > 1:
        active.sort(key=lambda t: (left[t], t))
        weak = active[0]
        give = WIN * (len(active) - 1) - left[weak]
        if give < 0:
            break
        for t in reversed(active[1:]):
            share = min(WIN, give)
            give -= share
            left[t] -= share
            got[t][weak], got[weak][t] = share, WIN - share
        left[weak] = 0
        if give or any(left[t] < 0 for t in active):
            break
        active.pop(0)
    if any(left):
        print("INCORRECT")
        return
    out = ["CORRECT"]
    for i in range(n):
        for j in range(i + 1, n):
            out.append("%d %s %d" % (i + 1, SIGNS[got[i][j]], j + 1))
    print("\n".join(out))


main()
