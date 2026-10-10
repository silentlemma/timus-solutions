import sys


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n, m = next(tok), next(tok)
    total = 2 * n
    near = [[] for _ in range(total + 1)]
    for _ in range(m):
        a, b = next(tok), next(tok)
        near[a].append(b)
        near[b].append(a)
    # similar problems must go to different rounds: colour every component of
    # the conflict graph in two colours, or give up on an odd cycle
    colour = [-1] * (total + 1)
    comps = []
    for start in range(1, total + 1):
        if colour[start] >= 0:
            continue
        colour[start] = 0
        members, stack = [start], [start]
        while stack:
            v = stack.pop()
            for w in near[v]:
                if colour[w] < 0:
                    colour[w] = 1 - colour[v]
                    members.append(w)
                    stack.append(w)
                elif colour[w] == colour[v]:
                    print("IMPOSSIBLE")
                    return
        comps.append(members)
    # each component sends one of its colours to the first round; reach[k]
    # holds the sizes the first k components can give it
    sizes = [[sum(1 for v in c if colour[v] == side) for side in (0, 1)] for c in comps]
    reach = [{0}]
    for a, b in sizes:
        reach.append(
            {s + a for s in reach[-1] if s + a <= n} | {s + b for s in reach[-1] if s + b <= n}
        )
    if n not in reach[-1]:
        print("IMPOSSIBLE")
        return
    first = []
    s = n
    for k in range(len(comps) - 1, -1, -1):
        side = 0 if s - sizes[k][0] in reach[k] else 1
        first += [v for v in comps[k] if colour[v] == side]
        s -= sizes[k][side]
    chosen = set(first)
    print(" ".join(map(str, sorted(first))))
    print(" ".join(str(v) for v in range(1, total + 1) if v not in chosen))


main()
