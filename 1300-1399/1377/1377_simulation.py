import sys

# east, south, west, north: turning right moves one step along this list
STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def main():
    n, m, r1, c1, r2, c2 = map(int, sys.stdin.read().split())
    # dig the whole spiral, numbering the graves by the night they are dug,
    # with a frame of dug cells around the cemetery standing for the wall
    night = [[-1] * (m + 2) for _ in range(n + 2)]
    for r in range(n + 2):
        night[r][0] = night[r][m + 1] = 0
    night[0] = [0] * (m + 2)
    night[n + 1] = [0] * (m + 2)
    r, c, d = 1, 1, 0
    night[1][1] = 1
    for day in range(2, n * m + 1):
        while night[r + STEPS[d][0]][c + STEPS[d][1]] >= 0:
            d = (d + 1) % len(STEPS)
        r, c = r + STEPS[d][0], c + STEPS[d][1]
        night[r][c] = day
    print(abs(night[r1][c1] - night[r2][c2]))


main()
