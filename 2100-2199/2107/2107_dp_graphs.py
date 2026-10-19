import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[:2]
    following = [value - 1 for value in data[2:]]
    indegree = [0] * n
    for target in following:
        if target >= 0:
            indegree[target] += 1
            if indegree[target] > 1:
                return "No\n"

    seen = [False] * n
    paths = [[] for _ in range(n + 1)]
    for start in range(n):
        if indegree[start] != 0:
            continue
        path = []
        vertex = start
        while vertex >= 0:
            seen[vertex] = True
            path.append(vertex)
            vertex = following[vertex]
        paths[len(path)].append(path)
    for start in range(n):
        if seen[start]:
            continue
        length = 0
        vertex = start
        while not seen[vertex]:
            seen[vertex] = True
            length += 1
            vertex = following[vertex]
        if k % length != 0:
            return "No\n"

    lengths = [length for length in range(1, n + 1) if paths[length]]
    radix = [len(paths[length]) + 1 for length in lengths]
    multiplier = []
    states = 1
    for base in radix:
        multiplier.append(states)
        states *= base
    types = len(lengths)
    digits = [[0] * types for _ in range(states)]
    groups = []
    for state in range(1, states):
        row = digits[state]
        total = 0
        for kind in range(types):
            row[kind] = state // multiplier[kind] % radix[kind]
            total += row[kind] * lengths[kind]
        if k % total == 0:
            groups.append(state)

    # Each digit counts paths of one length, so equivalent paths share a state.
    choice = [-1] * states
    choice[0] = 0
    for state in range(1, states):
        row = digits[state]
        anchor = types - 1
        while row[anchor] == 0:
            anchor -= 1
        for group in groups:
            if group > state:
                break
            selected = digits[group]
            if selected[anchor] == 0 or choice[state - group] < 0:
                continue
            if all(selected[kind] <= row[kind] for kind in range(types)):
                choice[state] = group
                break
    if choice[-1] < 0:
        return "No\n"

    state = states - 1
    while state:
        group = choice[state]
        cycle = []
        for kind, length in enumerate(lengths):
            for _ in range(digits[group][kind]):
                cycle.append(paths[length].pop())
        for index, path in enumerate(cycle):
            following[path[-1]] = cycle[(index + 1) % len(cycle)][0]
        state -= group
    return "Yes\n" + " ".join(str(target + 1) for target in following) + "\n"


sys.stdout.write(solve())
