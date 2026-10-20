"""Check the maximum knight count and every edge of the induced attack graph."""

import sys

ROWS = 3
FORWARD_MOVES = ((1, 2), (2, 1), (-1, 2), (-2, 1))


class Bad(Exception):
    pass


def check(source, expected, output):
    with open(source, encoding="utf-8") as stream:
        n = int(stream.read())
    with open(output, encoding="utf-8") as stream:
        lines = stream.read().splitlines()
    if len(lines) != ROWS:
        raise Bad("expected three rows")
    board = bytearray()
    for line in lines:
        words = line.split()
        if len(words) != n or any(word not in ("0", "1") for word in words):
            raise Bad("each row must contain n binary numbers")
        board.extend(int(word) for word in words)
    count = sum(board)
    # The trusted answer supplies the maximum count; its layout may differ.
    with open(expected, encoding="utf-8") as stream:
        optimum = sum(map(int, stream.read().split()))
    if count != optimum:
        raise Bad("expected %d knights, got %d" % (optimum, count))
    parent = list(range(ROWS * n))

    def root(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    components = count
    for row in range(ROWS):
        for column in range(n):
            vertex = row * n + column
            if not board[vertex]:
                continue
            for dr, dc in FORWARD_MOVES:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < ROWS and nc < n):
                    continue
                other = nr * n + nc
                if not board[other]:
                    continue
                a, b = root(vertex), root(other)
                if a == b:
                    raise Bad("the attack graph contains a cycle")
                parent[a] = b
                components -= 1
    if components != 1:
        raise Bad("the attack graph is disconnected")


def main():
    try:
        check(*sys.argv[1 : 1 + ROWS])
    except (Bad, OSError, UnicodeError, ValueError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
