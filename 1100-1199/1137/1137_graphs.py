import sys


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n = next(tok)
    adj = {}
    edges = 0
    start = None
    for _ in range(n):
        m = next(tok)
        stops = [next(tok) for _ in range(m + 1)]
        start = stops[0] if start is None else start
        for a, b in zip(stops, stops[1:]):
            adj.setdefault(a, []).append(b)
            edges += 1
    # every old route is a cycle, so each stop is left as often as it is
    # entered; Hierholzer's walk then uses every segment once
    ptr = {v: 0 for v in adj}
    stack, circuit = [start], []
    while stack:
        v = stack[-1]
        out = adj.get(v, [])
        if ptr.get(v, 0) < len(out):
            ptr[v] += 1
            stack.append(out[ptr[v] - 1])
        else:
            circuit.append(stack.pop())
    if len(circuit) != edges + 1:
        print(0)
        return
    circuit.reverse()
    print(edges, " ".join(map(str, circuit)))


main()
