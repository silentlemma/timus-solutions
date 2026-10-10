import sys
from collections import deque
from itertools import repeat

BYTE = 8


def search(root, adj, seen):
    """Marks everything reachable from root that seen does not hold yet.
    A set of senators is a big integer with one byte per senator, so each
    senator in the search costs a few whole-set operations."""
    frontier = 1 << BYTE * root
    seen |= frontier
    while frontier:
        nxt = 0
        while frontier:
            low = frontier & -frontier
            nxt |= adj[(low.bit_length() - 1) // BYTE]
            frontier ^= low
        frontier = nxt & ~seen
        seen |= frontier
    return seen


def main():
    # the whole input is read at once, since reading such long lines one
    # at a time through a buffered reader is slow
    lines = sys.stdin.buffer.read().split(b"\n")
    n = int(lines[0])
    # rows[u][v] is 1 when senator u holds a file on senator v; each list
    # ends with a 0 and usually fills one line, but may span several
    rows, pending = [bytearray(n + 1)], []
    for line in lines[1:]:
        pending += line.split()
        while b"0" in pending and len(rows) <= n:
            end = pending.index(b"0")
            row = bytearray(n + 1)
            deque(map(row.__setitem__, map(int, pending[:end]), repeat(1)), 0)
            rows.append(row)
            del pending[: end + 1]
    adj = [int.from_bytes(row, "little") for row in rows]

    # nobody outside the marked set can reach the root of the last search,
    # so that root lies in a strongly connected component with no way in
    seen, root = 0, 1
    for u in range(1, n + 1):
        if not seen >> BYTE * u & 1:
            root = u
            seen = search(u, adj, seen)
    answer = []
    if search(root, adj, 0) == int.from_bytes(bytes(1) + bytes([1]) * n, "little"):
        # the columns of the matrix are the files held on each senator
        radj = [int.from_bytes(bytes(1) + bytes(col), "little") for col in zip(*rows[1:])]
        back = search(root, radj, 0)
        answer = [u for u in range(1, n + 1) if back >> BYTE * u & 1]
    print(" ".join(map(str, answer + [0])))


main()
