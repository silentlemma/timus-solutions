"""Bus networks near the limits: a seed and a mode. Mode 1 has 1000
random routes of 199 stops among 100 000, mode 2 a chain of 1000 short
routes that needs a change at every link, mode 3 two halves that no
route joins, mode 4 one long route through every stop and short routes
around it."""

import random
import sys

N = 1000
M = 100000
TOTAL = 200000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        routes = [rng.sample(range(1, M + 1), TOTAL // N - 1) for _ in range(N)]
        a, b = routes[0][0], routes[-1][-1]
    elif mode == 2:
        # route i joins stops i and i + 1, each padded with a few private stops
        routes = [[i + 1, i + 2] + [N + 2 + 3 * i + k for k in range(3)] for i in range(N)]
        for r in routes:
            rng.shuffle(r)
        a, b = 1, N + 1
    elif mode == 3:
        half = M // 2
        routes = [
            rng.sample(range(1, half + 1) if r % 2 else range(half + 1, M + 1), 150)
            for r in range(N)
        ]
        a, b = routes[1][0], routes[0][0]
    else:
        line = list(range(1, M + 1))
        rng.shuffle(line)
        routes = [line] + [rng.sample(range(1, M + 1), 50) for _ in range(N - 1)]
        a, b = line[5], line[-5]
    print(N, M)
    print("\n".join(" ".join(map(str, [len(r)] + r)) for r in routes))
    print(a, b)


main()
