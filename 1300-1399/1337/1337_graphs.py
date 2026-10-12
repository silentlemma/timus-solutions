import sys

INF = float("inf")


def main():
    words = iter(int(x) for x in sys.stdin.read().split())
    n, week = next(words), next(words)
    day_of = [0] + [next(words) for _ in range(n)]

    def listed():
        items = []
        for value in words:
            if value == 0:
                return items
            items.append(value)
        return items

    needs = [[]] + [listed() for _ in range(n)]
    today = next(words)
    held = set(listed())
    wanted = listed()
    # every document still to get: the wanted ones and, behind them, the
    # papers they need, stopping at papers already held
    todo, stack = set(), [d for d in wanted if d not in held]
    while stack:
        doc = stack.pop()
        if doc not in todo:
            todo.add(doc)
            stack.extend(p for p in needs[doc] if p not in held)
    docs = sorted(todo)
    m = len(docs)
    index = {d: i for i, d in enumerate(docs)}
    pre = [[index[p] for p in needs[d] if p in todo] for d in docs]
    succ = [[] for _ in range(m)]
    for v in range(m):
        for p in pre[v]:
            succ[p].append(v)
    # day t (today is day 0) belongs to an official when t = off mod week
    off = [(day_of[d] - today) % week for d in docs]
    # a cycle among them makes the set impossible to get
    waiting = [len(pre[v]) for v in range(m)]
    topo = [v for v in range(m) if waiting[v] == 0]
    left = waiting[:]
    for v in topo:
        for u in succ[v]:
            left[u] -= 1
            if left[u] == 0:
                topo.append(u)
    if len(topo) < m:
        print("No Solution")
        return
    # tail[v]: days that must pass after v is fetched, along its longest chain
    tail = [0] * m
    for v in reversed(topo):
        for u in succ[v]:
            gap = (off[u] - off[v]) % week or week
            tail[v] = max(tail[v], gap + tail[u])
    done = [False] * m

    def first_day(t, v):
        """The first day from t on when the official of v receives."""
        return t + (off[v] - t) % week

    def lower_bound(t):
        """No plan from day t on can fetch the last document earlier."""
        earliest = [0] * m
        by_slot = [[] for _ in range(week)]
        for v in topo:
            if not done[v]:
                base = t
                for p in pre[v]:
                    if not done[p]:
                        base = max(base, earliest[p] + 1)
                earliest[v] = first_day(base, v)
                by_slot[off[v]].append((earliest[v], tail[v]))
        # k documents of one reception day that cannot come before day r
        # take k such days from r on, and the last still has a tail ahead
        bound = 0
        for docs_here in by_slot:
            docs_here.sort(reverse=True)
            count, shortest = 0, INF
            for first, after in docs_here:
                count += 1
                shortest = min(shortest, after)
                bound = max(bound, first + (count - 1) * week + shortest)
        return bound

    def choices(t, wait, taken):
        """The first day with a document to fetch, and those documents."""
        ready = [v for v in range(m) if not taken[v] and wait[v] == 0]
        day = min(first_day(t, v) for v in ready)
        return day, sorted(
            (v for v in ready if first_day(t, v) == day), key=lambda v: (-tail[v], v)
        )

    def greedy(t, count):
        """Fetch the document with the longest chain behind it each time."""
        wait, taken, plan, last = waiting[:], done[:], [], t - 1
        for _ in range(count):
            last, cands = choices(t, wait, taken)
            v = cands[0]
            taken[v] = True
            plan.append(v)
            for u in succ[v]:
                wait[u] -= 1
            t = last + 1
        return last, plan

    best_day, best_plan = greedy(0, m)
    best = [best_day, best_plan]
    seen = {}
    path = []

    def search(t, mask, count):
        if count == 0:
            if t - 1 < best[0]:
                best[0], best[1] = t - 1, path[:]
            return
        # the same documents in hand by an earlier day were already tried
        if seen.get(mask, INF) <= t:
            return
        seen[mask] = t
        if lower_bound(t) >= best[0]:
            return
        # fetching nothing on a day when something can be fetched never helps
        day, cands = choices(t, waiting, done)
        for v in cands:
            done[v] = True
            for u in succ[v]:
                waiting[u] -= 1
            path.append(v)
            last, rest = greedy(day + 1, count - 1)
            if last < best[0]:
                best[0], best[1] = last, path + rest
            if day < best[0]:
                search(day + 1, mask | 1 << v, count - 1)
            path.pop()
            for u in succ[v]:
                waiting[u] += 1
            done[v] = False

    if m:
        search(0, 0, m)
    else:
        best = [0, []]
    print(best[0])
    print(" ".join(str(docs[v]) for v in best[1]))


main()
