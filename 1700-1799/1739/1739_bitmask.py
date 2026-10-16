import sys

SCALE = 1000
SAFE = 256 * SCALE
DEODORANT, PERFUME = 1, 2
BOTH = DEODORANT | PERFUME
DOWN_NUM = 3
DOWN_DEN = 4
UP_NUM = 11
UP_DEN = 10
INF = float("inf")


def maximal(sets):
    # keep the sets not inside another one: carrying more costs nothing,
    # since fruit already outside can be brought back and carried again
    kept = []
    for a in sorted(sets, key=lambda m: -bin(m).count("1")):
        if not any(a & b == a for b in kept):
            kept.append(a)
    return kept


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # aromas times 1000 keep 3/4, 11/10 and both together whole
    w = [int(x) * SCALE for x in data[1:n + 1]]
    full = (1 << n) - 1
    total = [0] * (full + 1)
    for m in range(1, full + 1):
        low = (m & -m).bit_length() - 1
        total[m] = total[m & (m - 1)] + w[low]
    # moves: (treatments used, deodorized fruit, perfumed fruit, set carried)
    moves = []
    for m in maximal([m for m in range(1, full + 1) if total[m] % SAFE == 0]):
        moves.append((0, -1, -1, m))
    # what each spray adds to the total of a set holding the fruit
    weaker = [x * DOWN_NUM // DOWN_DEN - x for x in w]
    stronger = [x * UP_NUM // UP_DEN - x for x in w]
    for i in range(n):
        bit = 1 << i
        for kind, change in ((DEODORANT, weaker[i]), (PERFUME, stronger[i])):
            sets = [m for m in range(1, full + 1) if m & bit and (total[m] + change) % SAFE == 0]
            for m in maximal(sets):
                moves.append((kind, i if kind == DEODORANT else -1,
                              i if kind == PERFUME else -1, m))
        for j in range(n):
            change = weaker[i] + stronger[j]
            if i == j:
                change = w[i] * DOWN_NUM * UP_NUM // (DOWN_DEN * UP_DEN) - w[i]
            pair = bit | 1 << j
            sets = [m for m in range(1, full + 1)
                    if m & pair == pair and (total[m] + change) % SAFE == 0]
            for m in maximal(sets):
                moves.append((BOTH, i, j, m))
    # carrying more is never worse, so of the moves with the same sprays only
    # the largest sets are kept, and none inside a set needing fewer sprays
    kinds = (0, DEODORANT, PERFUME, BOTH)
    group = {kind: {} for kind in kinds}
    for move in moves:
        kind, _, _, m = move
        group[kind].setdefault(m, move)
    kept = {}
    for kind in kinds:
        cover = [m for k in kinds if k != kind and k & kind == k for m in kept[k]]
        kept[kind] = [m for m in maximal(group[kind])
                      if not any(m & c == m for c in cover)]
    # best[used][mask]: fewest exits that get the fruit of mask out
    best = [[INF] * (full + 1) for _ in range(BOTH + 1)]
    choice = [[None] * (full + 1) for _ in range(BOTH + 1)]
    for used in range(BOTH + 1):
        best[used][0] = 0
    for mask in range(1, full + 1):
        for used in range(BOTH + 1):
            value, pick = INF, None
            for kind in kinds:
                if kind & used:
                    continue
                after = best[used | kind]
                for m in kept[kind]:
                    if m & mask and after[mask & ~m] < value:
                        value, pick = after[mask & ~m], group[kind][m]
            best[used][mask] = value + 1
            choice[used][mask] = pick
    if best[0][full] == INF:
        print("IMPOSSIBLE")
        return
    out = []
    mask, used = full, 0
    while mask:
        kind, i, j, m = choice[used][mask]
        back = m & ~mask
        if back:
            names = [str(k + 1) for k in range(n) if back >> k & 1]
            out.append("return %d %s" % (len(names), " ".join(names)))
        if i >= 0:
            out.append("dearomatize %d" % (i + 1))
        if j >= 0:
            out.append("aromatize %d" % (j + 1))
        names = [str(k + 1) for k in range(n) if m >> k & 1]
        out.append("take %d %s" % (len(names), " ".join(names)))
        used |= kind
        mask &= ~m
    print(len(out))
    print("\n".join(out))


main()
