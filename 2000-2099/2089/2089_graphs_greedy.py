import sys

UNSET = 0


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    teams = list(map(int, data[2:2 + 2 * n]))
    ends = list(zip(teams[0::2], teams[1::2]))
    incident = [[] for _ in range(k + 1)]
    for i, (x, y) in enumerate(ends):
        incident[x].append(i)
        incident[y].append(i)
    # every team may win at most one pair: a team with a single open pair takes
    # it, which never hurts, and the pair is closed for the other team
    winner = [UNSET] * n
    degree = [len(e) for e in incident]
    leaves = [v for v in range(1, k + 1) if degree[v] == 1]
    while leaves:
        v = leaves.pop()
        if degree[v] != 1:
            continue
        i = next(i for i in incident[v] if winner[i] == UNSET)
        winner[i] = v
        degree[v] = 0
        u = ends[i][0] + ends[i][1] - v
        degree[u] -= 1
        if degree[u] == 1:
            leaves.append(u)
    # what is left must be disjoint cycles (every degree 2); each cycle is walked
    # and every pair is won by the team it leads to
    for v in range(1, k + 1):
        if degree[v] > 2:
            print("No")
            return
    for start in range(1, k + 1):
        if degree[start] != 2:
            continue
        v = start
        while True:
            i = next(i for i in incident[v] if winner[i] == UNSET)
            u = ends[i][0] + ends[i][1] - v
            winner[i] = u
            degree[v] -= 1
            degree[u] -= 1
            v = u
            if v == start:
                break
    print("Yes")
    print("\n".join(map(str, winner)))


main()
