import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    # variable i is true when friend i's first statement is the true one,
    # and literal 2 v means v while 2 v + 1 means not v
    groups = {}  # claims about one person or about one card: at most one holds
    nums = iter(data[1:])
    for i in range(n):
        a, b, c = next(nums), next(nums), next(nums)
        for key, literal in (
            ((0, i + 1), 2 * i),
            ((1, a), 2 * i),
            ((0, b), 2 * i + 1),
            ((1, c), 2 * i + 1),
        ):
            groups.setdefault(key, []).append(literal)
    count = n
    clauses = []  # each a pair of literals, one of which must hold
    for members in groups.values():
        # at most one: helper s_j means some of the first j members holds
        prev = None
        for lit in members:
            s = count
            count += 1
            clauses.append((lit ^ 1, 2 * s))  # lit -> s
            if prev is not None:
                clauses.append((2 * prev + 1, 2 * s))  # prev -> s
                clauses.append((2 * prev + 1, lit ^ 1))  # prev -> not lit
            prev = s
    graph = [[] for _ in range(2 * count)]
    for x, y in clauses:
        graph[x ^ 1].append(y)  # not x -> y
        graph[y ^ 1].append(x)  # not y -> x
    # Tarjan's components, numbered from the sinks up
    index, low, comp = [-1] * (2 * count), [0] * (2 * count), [-1] * (2 * count)
    stack, on_stack, counter, comps = [], [False] * (2 * count), 0, 0
    for root in range(2 * count):
        if index[root] >= 0:
            continue
        work = [(root, 0)]
        while work:
            v, k = work.pop()
            if k == 0:
                index[v] = low[v] = counter
                counter += 1
                stack.append(v)
                on_stack[v] = True
            elif k <= len(graph[v]):
                low[v] = min(low[v], low[graph[v][k - 1]])
            while k < len(graph[v]):
                u = graph[v][k]
                k += 1
                if index[u] < 0:
                    work.append((v, k))
                    work.append((u, 0))
                    break
                if on_stack[u]:
                    low[v] = min(low[v], index[u])
            else:
                if low[v] == index[v]:
                    while True:
                        u = stack.pop()
                        on_stack[u] = False
                        comp[u] = comps
                        if u == v:
                            break
                    comps += 1
    # a literal holds when its component comes before its negation's
    print(" ".join("1" if comp[2 * i] < comp[2 * i + 1] else "2" for i in range(n)))


main()
