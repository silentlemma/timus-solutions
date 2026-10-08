import sys

END_OF_INPUT = -1
TOKENS_PER_QUESTION = 3


def find(parent, parity, x):
    """Root of x and the parity between x and the root, with path compression."""
    path = []
    while parent[x] != x:
        path.append(x)
        x = parent[x]
    root, acc = x, 0
    for node in reversed(path):
        acc ^= parity[node]
        parity[node] = acc
        parent[node] = root
    return root, (parity[path[0]] if path else 0)


def solve(questions):
    parent, parity, ids = [], [], {}

    def node(pos):
        if pos not in ids:
            ids[pos] = len(parent)
            parent.append(len(parent))
            parity.append(0)
        return ids[pos]

    for i, (left, right, w) in enumerate(questions):
        # ones in [left, right] = prefix(right) - prefix(left - 1)
        rx, px = find(parent, parity, node(left - 1))
        ry, py = find(parent, parity, node(right))
        if rx == ry:
            if px ^ py != w:
                return i
        else:
            parent[ry] = rx
            parity[ry] = px ^ py ^ w
    return len(questions)


def main():
    tokens = sys.stdin.read().split()
    pos, out = 0, []
    while int(tokens[pos]) != END_OF_INPUT:
        q = int(tokens[pos + 1])
        pos += 2
        questions = []
        for _ in range(q):
            left, right, word = int(tokens[pos]), int(tokens[pos + 1]), tokens[pos + 2]
            questions.append((left, right, 1 if word == "odd" else 0))
            pos += TOKENS_PER_QUESTION
        out.append(str(solve(questions)))
    sys.stdout.write("\n".join(out) + "\n")


main()
