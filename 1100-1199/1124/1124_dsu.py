import sys


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    m, n = next(tok), next(tok)
    parent = list(range(m))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # a piece of colour c in box b is an edge b -> c; every box has n pieces
    # and should get n back, so each connected group of boxes is an Euler
    # circuit, walked one carried piece per move
    moves = 0
    touched = set()
    for box in range(m):
        for _ in range(n):
            colour = next(tok) - 1
            if colour != box:
                moves += 1
                touched.update((box, colour))
                parent[find(box)] = find(colour)
    groups = len({find(x) for x in touched})
    # one empty move of the hand between groups
    print(moves + groups - 1 if moves else 0)


main()
