import sys

FRESH, WALKING, DONE = 0, 1, 2


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    to = [0] + [int(w) for w in data[1:n + 1]]
    incoming = [0] * (n + 1)
    for v in range(1, n + 1):
        incoming[to[v]] += 1
    # follow the arrows from every new programmer to find the cycles
    state = [FRESH] * (n + 1)
    cycles = on_cycles = bare = 0
    for start in range(1, n + 1):
        path = []
        v = start
        while state[v] == FRESH:
            state[v] = WALKING
            path.append(v)
            v = to[v]
        if state[v] == WALKING:
            cycle = path[path.index(v):]
            cycles += 1
            on_cycles += len(cycle)
            # a cycle nobody else points into needs a group of its own
            if all(incoming[u] == 1 for u in cycle):
                bare += 1
        for u in path:
            state[u] = DONE
    # fewest: every programmer nobody names starts a group, and so does
    # every bare cycle; most: a cycle goes into one group as soon as a
    # group enters it, and everyone else can stand alone
    starts = sum(1 for v in range(1, n + 1) if incoming[v] == 0)
    print(starts + bare, n - on_cycles + cycles)


main()
