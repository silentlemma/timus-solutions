import sys

# sums closer than this count as equal
EPS = 1e-9
# after the two currencies, a point gives a rate and a commission each way
TERMS = 4


def main():
    tok = iter(sys.stdin.read().split())
    n, m, s, v = int(next(tok)), int(next(tok)), int(next(tok)), float(next(tok))
    edges = []
    for _ in range(m):
        a, b = int(next(tok)), int(next(tok))
        rab, cab, rba, cba = (float(next(tok)) for _ in range(TERMS))
        edges += [(a, b, rab, cab), (b, a, rba, cba)]
    # best[c] is the most money of currency c that can be held; a pass that
    # still improves something after n passes has found a gaining cycle
    best = [-1.0] * (n + 1)
    best[s] = v
    for _ in range(n):
        changed = False
        for a, b, rate, fee in edges:
            if best[a] - fee >= 0:
                got = (best[a] - fee) * rate
                if got > best[b] + EPS:
                    best[b] = got
                    changed = True
        if best[s] > v + EPS or not changed:
            break
    print("YES" if best[s] > v + EPS or changed else "NO")


main()
