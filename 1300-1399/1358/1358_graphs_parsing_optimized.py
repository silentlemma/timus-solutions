from array import array
from os import read as read_input
from os import _exit as _finish_process
import sys as _finish_sys
import sys

STEP = 2  # columns two apart keep every pair of points farther than 1
LIMIT = 999  # the leftmost column, so that 1000 columns fit in [-999, 999]


INPUT_BUFFER_BYTES = 4096


def words():
    """Yield tokens while retaining only one bounded input chunk and its unfinished token."""
    pending = b""
    while True:
        block = read_input(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > 32 else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = map(int, words())
    n = next(values)
    head = array("H", [0]) * (n + 1)
    target = array("H", [0]) * (2 * n - 1)
    link = array("H", [0]) * (2 * n - 1)
    edge = 0
    for _ in range(n - 1):
        a, b = next(values), next(values)
        edge += 1
        target[edge] = b
        link[edge] = head[a]
        head[a] = edge
        edge += 1
        target[edge] = a
        link[edge] = head[b]
        head[b] = edge
    # column = preorder index, row = depth: the subtrees of the vertices on
    # one row take disjoint ranges of columns, so no two wires cross
    column = array("H", [0]) * (n + 1)
    depth = array("H", [0]) * (n + 1)
    depth[1] = 1
    stack = [1]
    order = 0
    while stack:
        v = stack.pop()
        column[v] = order
        order += 1
        edge = head[v]
        while edge:
            u = target[edge]
            if not depth[u]:
                depth[u] = depth[v] + 1
                stack.append(u)
            edge = link[edge]
    sys.stdout.write(
        "\n".join(f"{column[v] * STEP - LIMIT} {depth[v] - 1}" for v in range(1, n + 1)) + "\n"
    )


main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
