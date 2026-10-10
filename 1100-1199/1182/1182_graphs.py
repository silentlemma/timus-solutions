import sys


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data)
    knows = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in iter(lambda: next(data), 0):
            knows[i][j - 1] = True
    # two people who do not both know each other must be in different
    # teams, so these pairs must form a bipartite graph; each component
    # gives two sides, and one side of each goes to the first team
    side = [-1] * n
    parts = []
    for s in range(n):
        if side[s] >= 0:
            continue
        side[s] = 0
        groups, queue = ([], []), [s]
        for v in queue:
            groups[side[v]].append(v)
            for u in range(n):
                if u != v and not (knows[v][u] and knows[u][v]):
                    if side[u] < 0:
                        side[u] = 1 - side[v]
                        queue.append(u)
                    elif side[u] == side[v]:
                        print("No solution")
                        return
        parts.append(groups)
    # reach[k][size]: which side of part k-1 gives the first team that size
    reach = [{0: None}]
    for groups in parts:
        nxt = {}
        for size in reach[-1]:
            for pick in (0, 1):
                nxt.setdefault(size + len(groups[pick]), pick)
        reach.append(nxt)
    size = min(reach[-1], key=lambda s: abs(2 * s - n))
    first, second = [], []
    for k in range(len(parts) - 1, -1, -1):
        pick = reach[k + 1][size]
        first += parts[k][pick]
        second += parts[k][1 - pick]
        size -= len(parts[k][pick])
    for team in (first, second):
        print(len(team), " ".join(str(v + 1) for v in sorted(team)))


main()
