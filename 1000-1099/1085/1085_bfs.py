import sys
from collections import deque

TICKET = 4
# money, stop and pass for each friend
FIELDS = 3


def rides_from(start, n, routes, routes_at):
    """Fewest rides from start to every stop; a ride covers a whole route."""
    rides = [-1] * (n + 1)
    rides[start] = 0
    used = [False] * len(routes)
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for r in routes_at[u]:
            if used[r]:
                continue
            used[r] = True
            for v in routes[r]:
                if rides[v] < 0:
                    rides[v] = rides[u] + 1
                    queue.append(v)
    return rides


def main():
    tok = list(map(int, sys.stdin.read().split()))
    n, m = tok[0], tok[1]
    pos = 2
    routes = []
    routes_at = [[] for _ in range(n + 1)]
    for r in range(m):
        size = tok[pos]
        routes.append(tok[pos + 1 : pos + 1 + size])
        for s in routes[-1]:
            routes_at[s].append(r)
        pos += 1 + size
    k = tok[pos]
    rest = tok[pos + 1 :]
    friends = [rest[i : i + FIELDS] for i in range(0, k * FIELDS, FIELDS)]
    total = [0] * (n + 1)
    ok = [True] * (n + 1)
    for money, start, card in friends:
        rides = rides_from(start, n, routes, routes_at)
        for t in range(1, n + 1):
            cost = 0 if card else TICKET * rides[t]
            if rides[t] < 0 or cost > money:
                ok[t] = False
            else:
                total[t] += cost
    best = [(total[t], t) for t in range(1, n + 1) if ok[t]]
    if best:
        cost, stop = min(best)
        print(stop, cost)
    else:
        print(0)


main()
