"""Checker: "Imaginary world" exactly when the reference prints it;
otherwise a map of 2H - 1 lines of 2W - 1 characters (trailing spaces
may be dropped) with an island at every even position, only fitting
bridge symbols between them, three bridges at every island, and a
bridge network that stays connected after removing any one bridge."""

import sys

NO_WORLD = "Imaginary world"
# the symbol allowed at each position parity and the step it joins
STEPS = {"-": (0, 1), "|": (1, 0), "\\": (1, 1), "/": (1, -1)}
ALLOWED = {(0, 1): " -", (1, 0): " |", (1, 1): " \\/"}
DEGREE = 3


def fail(reason):
    print(reason)
    sys.exit(1)


def bridgeless(n, adj):
    # iterative low-link search; a tree edge (p, v) is a bridge if low[v] > tin[p]
    tin = [-1] * n
    low = [0] * n
    timer = 0
    tin[0] = low[0] = timer
    stack = [(0, -1, iter(adj[0]))]
    while stack:
        v, edge, it = stack[-1]
        advanced = False
        for u, e in it:
            if e == edge:
                continue
            if tin[u] == -1:
                timer += 1
                tin[u] = low[u] = timer
                stack.append((u, e, iter(adj[u])))
                advanced = True
                break
            low[v] = min(low[v], tin[u])
        if advanced:
            continue
        stack.pop()
        if stack:
            p = stack[-1][0]
            low[p] = min(low[p], low[v])
            if low[v] > tin[p]:
                return False
    return all(t >= 0 for t in tin)


def main():
    inp, expected, output = sys.argv[1:4]
    w, h = map(int, open(inp).read().split()[:2])
    want = open(expected).read().strip()
    text = open(output).read().replace("\r", "")
    if want == NO_WORLD:
        if text.strip() != NO_WORLD:
            fail("expected " + NO_WORLD)
        return
    if text.strip() == NO_WORLD:
        fail("a world of this size exists")
    lines = text.rstrip("\n").split("\n")
    rows, cols = 2 * h - 1, 2 * w - 1
    if len(lines) != rows:
        fail("expected %d lines, got %d" % (rows, len(lines)))
    adj = [[] for _ in range(w * h)]
    edges = 0
    for r, line in enumerate(lines):
        line = line.rstrip(" ")
        if len(line) > cols:
            fail("line %d is too long" % (r + 1))
        line = line.ljust(cols)
        for c, ch in enumerate(line):
            if r % 2 == 0 and c % 2 == 0:
                if ch != "O":
                    fail("no island at line %d, column %d" % (r + 1, c + 1))
                continue
            if ch not in ALLOWED[r % 2, c % 2]:
                fail("unexpected %r at line %d, column %d" % (ch, r + 1, c + 1))
            if ch == " ":
                continue
            dr, dc = STEPS[ch]
            # the symbol at (r, c) joins island a to island a + (dr, dc)
            a = (r - dr) // 2 * w + (c - dc) // 2
            b = a + dr * w + dc
            adj[a].append((b, edges))
            adj[b].append((a, edges))
            edges += 1
    for v in range(w * h):
        if len(adj[v]) != DEGREE:
            fail("island %d, %d has %d bridges" % (v % w + 1, v // w + 1, len(adj[v])))
    if not bridgeless(w * h, adj):
        fail("the network is disconnected or has a bridge whose loss splits it")


main()
