import sys
from functools import cmp_to_key

# the recursion goes as deep as the number of hypotheses
DEPTH = 10000


def main():
    words = iter(sys.stdin.read().split())
    n = int(next(words))
    t, p, deps = [], [], []
    for _ in range(n):
        t.append(int(next(words)))
        p.append(float(next(words)))
        k = int(next(words))
        deps.append([int(next(words)) - 1 for _ in range(k)])
    # hypotheses on one cycle of dependencies are all true or all false,
    # and Tarjan's method finds those groups, dependencies first
    sys.setrecursionlimit(DEPTH)
    index, low, on_stack, stack, group = [-1] * n, [0] * n, [False] * n, [], [-1] * n
    groups = []
    counter = [0]

    def visit(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        for w in deps[v]:
            if index[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif on_stack[w]:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            members = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                group[w] = len(groups)
                members.append(w)
                if w == v:
                    break
            groups.append(members)

    for v in range(n):
        if index[v] < 0:
            visit(v)
    # a group is worth checking only when every group it rests on is fully
    # admissible; inside it, checks stop at the first failure, so the order
    # by t / (1 - p) is the cheapest
    order = cmp_to_key(lambda a, b: (t[a] * (1 - p[b]) > t[b] * (1 - p[a])) -
                       (t[a] * (1 - p[b]) < t[b] * (1 - p[a])))
    cost, sound, reach = [], [], []
    for g, members in enumerate(groups):
        still, expected = 1.0, 0.0
        for v in sorted(members, key=order):
            expected += still * t[v]
            still *= p[v]
        cost.append(expected)
        sound.append(still)
        below = 0
        for v in members:
            for w in deps[v]:
                if group[w] != g:
                    below |= reach[group[w]] | 1 << group[w]
        reach.append(below)
    answer = 0.0
    for g in range(len(groups)):
        chance = 1.0
        rest = reach[g]
        while rest:
            low_bit = rest & -rest
            chance *= sound[low_bit.bit_length() - 1]
            rest ^= low_bit
        answer += chance * cost[g]
    print("%.3f" % answer)


main()
