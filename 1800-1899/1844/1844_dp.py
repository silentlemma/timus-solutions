import sys


def holding(ops, mage_count):
    # spans[a]: the (from, to) stretches of states, counted in done steps,
    # during which the plan keeps mage a in the office
    spans = [[] for _ in range(mage_count + 1)]
    since = [0] * (mage_count + 1)
    for step, (sign, a) in enumerate(ops):
        if sign == b"+":
            since[a] = step + 1
        else:
            spans[a].append((since[a], step + 1))
    return spans


def calm(n, m, k, sandro, zagamius):
    # cell (i, j): Sandro has done i steps and Zagamius j. A cell is taken
    # when both offices hold one mage, and a step is blocked exactly when it
    # leads into a taken cell. Row i is a bit mask over j.
    columns = [0] * (k + 1)
    for a, spans in enumerate(holding(zagamius, k)):
        for lo, hi in spans:
            columns[a] |= (1 << hi) - (1 << lo)
    # taken cells of row i: the columns of every mage Sandro holds in that
    # row, gathered with a segment tree over the rows
    size = 1
    while size < n + 1:
        size *= 2
    tag = [0] * (2 * size)
    for a, spans in enumerate(holding(sandro, k)):
        if not columns[a]:
            continue
        for lo, hi in spans:
            lo += size
            hi += size
            while lo < hi:
                if lo & 1:
                    tag[lo] |= columns[a]
                    lo += 1
                if hi & 1:
                    hi -= 1
                    tag[hi] |= columns[a]
                lo >>= 1
                hi >>= 1
    for v in range(1, size):
        tag[2 * v] |= tag[v]
        tag[2 * v + 1] |= tag[v]
    full = (1 << (m + 1)) - 1
    fence = (full << 1) | 1  # columns 0..m + 1
    free = [full & ~tag[size + i] for i in range(n + 1)] + [0]
    reach = 1
    for i in range(n + 1):
        row = free[i]
        seeds = reach & row if i else 1
        # from every seed Zagamius walks right until a taken cell: subtracting
        # the seeds from the blockers flips each free run from its first seed
        walls = fence ^ row
        reach = (((walls - seeds) ^ walls) & row) | seeds
        stuck = reach & ~free[i + 1] & ~(row >> 1)
        if i == n:
            stuck &= ~(1 << m)
        if stuck:
            return False
    return True


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m, k = (int(next(tokens)) for _ in "nmk")
        plans = [[(next(tokens), int(next(tokens))) for _ in range(count)] for count in (n, m)]
        out.append(":-)" if calm(n, m, k, *plans) else ":-(")
    print("\n".join(out))


main()
