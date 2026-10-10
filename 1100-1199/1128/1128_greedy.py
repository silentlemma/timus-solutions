import sys


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tok)
    enemies = [[next(tok) - 1 for _ in range(next(tok))] for _ in range(n)]
    side = [0] * n
    # a child with two or more enemies on its side has at most one on the
    # other, so moving it removes at least one pair of enemies sharing a
    # group; the moves stop after at most as many steps as there are pairs
    work = list(range(n))
    while work:
        v = work.pop()
        if sum(side[u] == side[v] for u in enemies[v]) >= 2:
            side[v] ^= 1
            work.extend(enemies[v])
            work.append(v)
    group = [v for v in range(n) if side[v] == side[0]]
    other = [v for v in range(n) if side[v] != side[0]]
    small = group if len(group) <= len(other) else other
    print(len(small))
    print(" ".join(str(v + 1) for v in small))


main()
