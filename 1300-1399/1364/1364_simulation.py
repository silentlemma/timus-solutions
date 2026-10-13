import sys

# east, south, west, north: turning right moves one step along this list
STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def main():
    n, m, rt, ct, rl, cl, t = map(int, sys.stdin.read().split())
    # dig the spiral up to the treasure, remembering the order of the graves
    seen = [[False] * (m + 2) for _ in range(n + 2)]
    for r in range(n + 2):
        seen[r][0] = seen[r][m + 1] = True
    seen[0] = [True] * (m + 2)
    seen[n + 1] = [True] * (m + 2)
    path = [(1, 1)]
    seen[1][1] = True
    r, c, d = 1, 1, 0
    while (r, c) != (rt, ct):
        dr, dc = STEPS[d]
        if seen[r + dr][c + dc]:
            d = (d + 1) % len(STEPS)
            continue
        r, c = r + dr, c + dc
        seen[r][c] = True
        path.append((r, c))
    # Lara runs along the tunnel, at most t graves either way
    here = path.index((rl, cl))
    lo, hi = max(0, here - t), min(len(path) - 1, here + t)
    print("\n".join("%d %d" % path[i] for i in range(lo, hi + 1)))


main()
