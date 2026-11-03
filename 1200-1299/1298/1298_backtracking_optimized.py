import sys

MOVES = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))


def main():
    n = int(sys.stdin.read())
    adjacency = []
    for c in range(n):
        for r in range(n):
            mask = 0
            for dc, dr in MOVES:
                if 0 <= c + dc < n and 0 <= r + dr < n:
                    mask |= 1 << ((c + dc) * n + r + dr)
            adjacency.append(mask)
    path = []

    def tour(v, remaining):
        path.append(v)
        if remaining == 0:
            return True
        choices = adjacency[v] & remaining
        if choices and remaining & (remaining - 1):
            # An isolated unvisited square cannot belong to a remaining path
            # with more than one vertex, even if it touches the current vertex.
            scan = remaining
            while scan:
                bit = scan & -scan
                scan -= bit
                if not adjacency[bit.bit_length() - 1] & remaining:
                    choices = 0
                    break
        order = []
        while choices:
            bit = choices & -choices
            choices -= bit
            order.append(bit.bit_length() - 1)
        order.sort(key=lambda w: (adjacency[w] & remaining).bit_count())
        for w in order:
            if tour(w, remaining ^ (1 << w)):
                return True
        path.pop()
        return False

    whole = (1 << (n * n)) - 1
    # Reflection in either axis and transposition preserve all knight moves.
    # Each starting-square orbit has a representative in this triangle.
    for c in range((n + 1) // 2):
        for r in range(c, (n + 1) // 2):
            v = c * n + r
            if tour(v, whole ^ (1 << v)):
                print("\n".join(chr(ord("a") + v // n) + str(v % n + 1) for v in path))
                return
    print("IMPOSSIBLE")


main()
