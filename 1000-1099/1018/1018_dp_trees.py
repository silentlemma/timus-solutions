import sys

NONE = -1
TOKENS_PER_BRANCH = 3


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, q = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, apples = data[2 + TOKENS_PER_BRANCH * i : 2 + TOKENS_PER_BRANCH * (i + 1)]
        adj[a].append((b, apples))
        adj[b].append((a, apples))

    def solve(v, parent):
        # best[k]: the most apples on k branches kept in the subtree of v, all
        # of them connected to v
        best = [0]
        for child, apples in adj[v]:
            if child == parent:
                continue
            sub = solve(child, v)
            merged = [NONE] * min(q + 1, len(best) + len(sub))
            for i, a in enumerate(best):
                for j in range(min(len(sub), len(merged) - 1 - i) + 1):
                    gain = 0 if j == 0 else apples + sub[j - 1]
                    merged[i + j] = max(merged[i + j], a + gain)
            best = merged
        return best

    print(solve(1, 0)[q])


main()
