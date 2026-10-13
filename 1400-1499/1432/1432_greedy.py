import sys

NINE = 9
NO = "No solution"
# positions fall into four classes by the signs of the two rules
CLASSES = 4
BOTH_UP = 0
X_UP = 1
Y_UP = 2
BOTH_DOWN = 3


def solve(s):
    size = len(s)
    half = size // 2
    rules = [
        [1 if k < half else -1 for k in range(size)],
        [1 if k % 2 == 0 else -1 for k in range(size)],
    ]
    # best: (first difference from s, digit there, combo, p, j, d)
    best = None
    for wx in rules:  # the rule that makes t lucky
        for wy in rules:  # the rule that makes t + 1 lucky
            cls = [(0 if wx[k] > 0 else 2) + (0 if wy[k] > 0 else 1) for k in range(size)]
            cnt = [[0] * (size + 1) for _ in range(CLASSES)]
            px = [0] * (size + 1)
            py = [0] * (size + 1)
            for k in range(size):
                for c in range(CLASSES):
                    cnt[c][k + 1] = cnt[c][k] + (cls[k] == c)
                px[k + 1] = px[k] + wx[k] * s[k]
                py[k + 1] = py[k] + wy[k] * s[k]
            tail = [0] * (size + 1)  # sum of wx over positions from k on
            for k in range(size - 1, -1, -1):
                tail[k] = tail[k + 1] + wx[k]

            def feasible(sx, sy, j, p, lo_j, hi_j, cls=cls, cnt=cnt, tail=tail, wy=wy):
                # digits before j give sums sx, sy; j in [lo_j, hi_j], free up to p,
                # p at most 8, nines after p; t must balance wx, t + 1 must balance wy
                a = -sx - NINE * tail[p + 1]
                b = -sy - wy[p]
                lo = [0] * CLASSES
                hi = [NINE * (cnt[c][p + 1] - cnt[c][j]) for c in range(CLASSES)]
                hi[cls[j]] += hi_j - NINE
                lo[cls[j]] += lo_j
                if p > j:
                    hi[cls[p]] -= 1
                if (a + b) % 2:
                    return False
                u, v = (a + b) // 2, (a - b) // 2
                return (
                    lo[BOTH_UP] - hi[BOTH_DOWN] <= u <= hi[BOTH_UP] - lo[BOTH_DOWN]
                    and lo[X_UP] - hi[Y_UP] <= v <= hi[X_UP] - lo[Y_UP]
                )

            for p in range(size):
                if s[p] < NINE and px[p + 1] + NINE * tail[p + 1] == 0 and py[p + 1] + wy[p] == 0:
                    # t keeps s up to p and has nines after it
                    dev = next((k for k in range(p + 1, size) if s[k] < NINE), size)
                    cand = (-dev, NINE, wx, wy, p, None, None, feasible)
                else:
                    cand = None
                    for j in range(p, -1, -1):
                        top = NINE - 1 if j == p else NINE
                        if s[j] + 1 <= top and feasible(px[j], py[j], j, p, s[j] + 1, top):
                            d = next(
                                d
                                for d in range(s[j] + 1, top + 1)
                                if feasible(px[j], py[j], j, p, d, d)
                            )
                            cand = (-j, d, wx, wy, p, j, d, feasible)
                            break
                if cand and (best is None or cand[:2] < best[0][:2]):
                    best = [cand]
                elif cand and cand[:2] == best[0][:2]:
                    best.append(cand)
    if not best:
        return None
    return min(build(s, c) for c in best)


def build(s, cand):
    _, _, wx, wy, p, j, d, feasible = cand
    size = len(s)
    if j is None:
        return s[: p + 1] + [NINE] * (size - p - 1)
    t = s[:j] + [d]
    sx = sum(w * x for w, x in zip(wx, t))
    sy = sum(w * x for w, x in zip(wy, t))
    for k in range(j + 1, p + 1):
        x = next(x for x in range(NINE + 1) if feasible(sx, sy, k, p, x, x))
        t.append(x)
        sx += wx[k] * x
        sy += wy[k] * x
    return t + [NINE] * (size - p - 1)


def main():
    s = [int(c) for c in sys.stdin.read().split()[0]]
    t = solve(s)
    if t is None:
        print(NO)
        return
    nxt = t[:]
    k = len(nxt) - 1
    while nxt[k] == NINE:
        nxt[k] = 0
        k -= 1
    nxt[k] += 1
    print("".join(map(str, t)), "".join(map(str, nxt)))


main()
