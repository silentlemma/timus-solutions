import sys

SHIFTS = 3
EPS = 1e-9


def main():
    tok = iter(sys.stdin.buffer.read().split())
    t0, t1 = float(next(tok)), float(next(tok))
    n = int(next(tok))
    lo, hi = [0.0] * n, [0.0] * n
    for i in range(n):
        lo[i], hi[i] = float(next(tok)), float(next(tok))
    # greedy cover: each step takes the observer reaching furthest among those
    # already present, so only neighbouring observers of the chain overlap
    order = sorted(range(n), key=lambda i: lo[i])
    chain = []
    cur, i = t0, 0
    while cur < t1 and i < n:
        best = -1
        while i < n and lo[order[i]] <= cur:
            if best < 0 or hi[order[i]] > hi[best]:
                best = order[i]
            i += 1
        if best < 0 or hi[best] <= cur:
            cur = lo[order[i]] if i < n else t1
            continue
        chain.append(best)
        cur = hi[best]
    # dropping every third observer of the chain leaves each piece of time
    # alone in two of the three shifts, so the best shift keeps 2/3 of it
    best_shift, best_alone = 0, -1.0
    for shift in range(SHIFTS):
        alone = 0.0
        kept = [k % SHIFTS != shift for k in range(len(chain))]
        for k, obs in enumerate(chain):
            if kept[k]:
                alone += hi[obs] - lo[obs]
                if k + 1 < len(chain) and kept[k + 1]:
                    alone -= 2 * max(0.0, hi[obs] - lo[chain[k + 1]])
        if alone > best_alone:
            best_shift, best_alone = shift, alone
    if best_alone < (t1 - t0) * 2 / SHIFTS - EPS:
        print(0)
        return
    painted = [obs + 1 for k, obs in enumerate(chain) if k % SHIFTS != best_shift]
    print("\n".join(map(str, [len(painted)] + painted)))


main()
