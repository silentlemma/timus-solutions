import sys
from collections import deque


def calls(adj, informed, fresh):
    """Who calls whom so that every person in fresh is called by a
    different informed neighbour, or None if that cannot be done."""
    caller_of = {}  # callee for each caller already busy

    def place(person, seen):
        for caller in range(len(adj)):
            if adj[person] >> caller & 1 and informed >> caller & 1 and caller not in seen:
                seen.add(caller)
                if caller not in caller_of or place(caller_of[caller], seen):
                    caller_of[caller] = person
                    return True
        return False

    for person in range(len(adj)):
        if fresh >> person & 1 and not place(person, set()):
            return None
    return sorted(caller_of.items(), key=lambda call: call[1])


def main():
    words = sys.stdin.read().split()
    m = int(words[1])
    ends, leader = words[2 : 2 + 2 * m], words[2 + 2 * m]
    index, names = {}, []
    for name in ends + [leader]:
        if name not in index:
            index[name] = len(names)
            names.append(name)
    adj = [0] * len(names)
    for first, second in zip(ends[::2], ends[1::2]):
        a, b = index[first], index[second]
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    full = (1 << len(names)) - 1
    start = 1 << index[leader]
    # breadth-first search over the sets of people who know the news
    came = {start: None}
    queue = deque([start])
    while queue and full not in came:
        informed = queue.popleft()
        reach = 0
        for person in range(len(names)):
            if informed >> person & 1:
                reach |= adj[person]
        reach &= ~informed
        fresh = reach
        while fresh:
            if informed | fresh not in came:
                plan = calls(adj, informed, fresh)
                if plan is not None:
                    came[informed | fresh] = (informed, plan)
                    queue.append(informed | fresh)
            fresh = (fresh - 1) & reach
    steps = []
    state = full
    while came[state] is not None:
        state, plan = came[state]
        steps.append(plan)
    out = [str(len(steps))]
    for plan in reversed(steps):
        out.append(str(len(plan)))
        out.extend("%s %s" % (names[a], names[b]) for a, b in plan)
    print("\n".join(out))


main()
