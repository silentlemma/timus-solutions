import sys

ROWS = 3
FRONTIER = 2 * ROWS
CELLS = FRONTIER + ROWS
MASKS = 1 << ROWS
GAIN = ROWS - 1
UNREACHABLE = -1
EMPTY = (0,) * FRONTIER
FINISHED = (-1,) * FRONTIER


def transition(state, mask):
    parent = list(range(CELLS))

    def root(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for i in range(FRONTIER):
        for j in range(i):
            if state[i] and state[i] == state[j]:
                parent[root(i)] = root(j)
    active = [bool(v) for v in state]
    active.extend(bool(mask >> r & 1) for r in range(ROWS))
    for r in range(ROWS):
        if not active[FRONTIER + r]:
            continue
        for c in range(2):
            for s in range(ROWS):
                if abs(r - s) != c + 1:
                    continue
                old = c * ROWS + s
                if active[old]:
                    a, b = root(old), root(FRONTIER + r)
                    if a == b:
                        return None
                    parent[a] = b
    old_roots = {root(i) for i in range(ROWS) if active[i]}
    new_roots = {root(i) for i in range(ROWS, CELLS) if active[i]}
    if old_roots - new_roots:
        if not new_roots and len(old_roots) == 1:
            return FINISHED
        return None
    labels = {}
    result = []
    for i in range(ROWS, CELLS):
        if active[i]:
            result.append(labels.setdefault(root(i), len(labels) + 1))
        else:
            result.append(0)
    return tuple(result)


def automaton():
    states = [EMPTY, FINISHED]
    indices = {state: i for i, state in enumerate(states)}
    edges = []
    for i, state in enumerate(states):
        outgoing = []
        if state == FINISHED:
            outgoing.append((i, 0, 0))
        else:
            for mask in range(MASKS):
                if state == EMPTY and mask == 0:
                    continue
                target = transition(state, mask)
                if target is None:
                    continue
                if target not in indices:
                    indices[target] = len(states)
                    states.append(target)
                outgoing.append((indices[target], mask, mask.bit_count()))
        edges.append(outgoing)
    return states, edges


def main():
    n = int(sys.stdin.buffer.read())
    states, edges = automaton()
    size = len(states)
    scores = [UNREACHABLE] * size
    scores[0] = 0
    history = []
    stable = False
    while len(history) < n and not stable:
        following = [UNREACHABLE] * size
        previous = [UNREACHABLE] * size
        masks = [0] * size
        for source, outgoing in enumerate(edges):
            if scores[source] == UNREACHABLE:
                continue
            for target, mask, weight in outgoing:
                candidate = scores[source] + weight
                if candidate > following[target]:
                    following[target] = candidate
                    previous[target] = source
                    masks[target] = mask
        # An equal score shift is preserved by every subsequent DP step.
        stable = all(
            a == b == UNREACHABLE or a != UNREACHABLE and b == a + GAIN
            for a, b in zip(scores, following)
        )
        scores = following
        history.append((previous, masks))
    best = UNREACHABLE
    vertex = 0
    for i, state in enumerate(states):
        if (state == FINISHED or max(state) == 1) and scores[i] > best:
            best = scores[i]
            vertex = i
    board = [0] * n
    for column in range(n - 1, -1, -1):
        layer = min(column, len(history) - 1)
        previous, masks = history[layer]
        board[column] = masks[vertex]
        vertex = previous[vertex]
    output = [" ".join(str(mask >> row & 1) for mask in board) for row in range(ROWS)]
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
