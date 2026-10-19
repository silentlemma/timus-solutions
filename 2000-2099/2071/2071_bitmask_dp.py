import sys

KINDS = 8  # cocktails as masks of three juices; 0 is unused
JUICES = "ABP"
INF = float("inf")


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    glasses = [[] for _ in range(KINDS)]
    for i in range(1, n + 1):
        mask = 0
        for c in data[i]:
            mask |= 1 << JUICES.index(c)
        glasses[mask].append(i)
    # equal cocktails stand together; the cocktails present are ordered by a DP over
    # subsets, where best[used][last] counts the pourings, and a juice needs a new pouring
    # when a cocktail contains it and the previous one does not
    kinds = [k for k in range(1, KINDS) if glasses[k]]
    present = sum(1 << k for k in kinds)
    best = [[INF] * KINDS for _ in range(1 << KINDS)]
    came = [[0] * KINDS for _ in range(1 << KINDS)]
    for k in kinds:
        best[1 << k][k] = bin(k).count("1")
    for used in range(1 << KINDS):
        for last in kinds:
            if best[used][last] == INF:
                continue
            for k in kinds:
                if used >> k & 1:
                    continue
                cost = best[used][last] + bin(k & ~last).count("1")
                nxt = used | 1 << k
                if cost < best[nxt][k]:
                    best[nxt][k] = cost
                    came[nxt][k] = last
    last = min(kinds, key=lambda k: best[present][k])
    answer = best[present][last]
    order = []
    used = present
    while last:
        order.append(last)
        used, last = used ^ 1 << last, came[used][last]
    arrangement = [g for k in reversed(order) for g in glasses[k]]
    print(answer)
    print(" ".join(map(str, arrangement)))


main()
