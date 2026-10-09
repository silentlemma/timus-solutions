import re
import sys


def parse(tokens):
    """Builds a tree of ("or", a, b), ("and", a, b), ("not", a), ("const", v)
    and ("reg", name) by recursive descent; NOT binds tightest, OR loosest."""
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def take():
        nonlocal pos
        pos += 1
        return tokens[pos - 1]

    def disjunction():
        node = conjunction()
        while peek() == "OR":
            take()
            node = ("or", node, conjunction())
        return node

    def conjunction():
        node = negation()
        while peek() == "AND":
            take()
            node = ("and", node, negation())
        return node

    def negation():
        if peek() == "NOT":
            take()
            return ("not", negation())
        word = take()
        if word == "(":
            node = disjunction()
            take()
            return node
        if word in ("TRUE", "FALSE"):
            return ("const", word == "TRUE")
        return ("reg", word)

    return disjunction()


def value(node, reg):
    kind = node[0]
    if kind == "or":
        return value(node[1], reg) or value(node[2], reg)
    if kind == "and":
        return value(node[1], reg) and value(node[2], reg)
    if kind == "not":
        return not value(node[1], reg)
    if kind == "const":
        return node[1]
    return reg[node[1]]


def main():
    lines = sys.stdin.read().split("\n")
    tree = parse(re.findall(r"[A-Z]+|[()]", lines[0]))
    it = iter(" ".join(lines[1:]).split())
    n, m, k = int(next(it)), int(next(it)), int(next(it))
    forks = {(int(next(it)), int(next(it))) for _ in range(m)}
    switches = {}
    for _ in range(k):
        x, y = int(next(it)), int(next(it))
        switches[(x, y)] = next(it)
    reg = dict.fromkeys("ABCDEFGHIJKLMNOPQRSTUVWXYZ", False)
    x = y = 0
    dx, dy = 1, 0
    out = []
    while -n <= x <= n and -n <= y <= n:
        out.append("%d %d" % (x, y))
        if (x, y) in switches:
            name = switches[(x, y)]
            reg[name] = not reg[name]
        if (x, y) in forks:
            # TRUE turns right, FALSE turns left
            dx, dy = (dy, -dx) if value(tree, reg) else (-dy, dx)
        x, y = x + dx, y + dy
    sys.stdout.write("\n".join(out) + "\n")


main()
