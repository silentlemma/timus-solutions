import sys

NONE = float("-inf")  # an unreachable state


def main():
    data = list(map(int, sys.stdin.read().split()))
    x, n = data[0], data[1]
    a, b = data[2:2 + n], data[2 + n:2 + 2 * n]
    # utility above x is earned whatever the order; with b capped at x a task
    # done at repaired volume r (debt x - r) earns max(0, min(x, r) - (x - b))
    extra = sum(max(0, v - x) for v in b)
    need = [x - min(v, x) for v in b]
    order = sorted(range(n), key=lambda i: a[i])
    # some tasks are given up: they go first and only repair. The rest go by a
    # descending, so task i (ascending a) sees the given up ones before it and
    # every task from it on. best[s]: s = repair of given up tasks so far, capped
    suffix = [0] * (n + 1)
    for k in range(n - 1, -1, -1):
        suffix[k] = suffix[k + 1] + a[order[k]]
    best = [NONE] * (x + 1)
    best[0] = 0
    choice = []  # (previous s, given up) per step and state
    for k, i in enumerate(order):
        nxt = [NONE] * (x + 1)
        back = [None] * (x + 1)
        for s in range(x + 1):
            if best[s] == NONE:
                continue
            gain = best[s] + min(x, s + suffix[k]) - need[i]
            if gain > nxt[s]:
                nxt[s], back[s] = gain, (s, False)
            t = min(x, s + a[i])
            if best[s] > nxt[t]:
                nxt[t], back[t] = best[s], (s, True)
        best = nxt
        choice.append(back)
    s = max(range(x + 1), key=lambda v: best[v])
    total = best[s] + extra
    given_up, kept = [], []
    for k in range(n - 1, -1, -1):
        s, up = choice[k][s]
        (given_up if up else kept).append(order[k])
    # kept was collected by a descending already
    print(int(total))
    print(" ".join(str(i + 1) for i in given_up + kept))


main()
