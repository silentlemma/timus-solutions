"""Bus networks near the limits: a seed and a mode. Mode 1 has 1000
random routes of 199 stops among 100 000, mode 2 a chain of 1000 short
routes that needs a change at every link, mode 3 two halves that no
route joins, mode 4 one long route through every stop and short routes
around it. Mode 5 fills the 200000-number budget with heavily overlapping
routes followed by two necessary transfers. Mode 6 is a shuffled random
network of eight adjacent layers, with repeated stops and local routes."""

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
    elif mode == 5:
        # Counts plus stops total exactly 1000 * (1 + 199) numbers.
        routes = [list(range(1, 200)) for _ in range(N - 2)]
        routes += [[199, M - 1] + list(range(200, 397))]
        routes += [[M - 1, M] + list(range(397, 594))]
        for r in routes:
            rng.shuffle(r)
        rng.shuffle(routes)
        a, b = 1, M
    elif mode == 6:
        layers = 8
        width = 80
        labels = rng.sample(range(2, M), (layers + 1) * width - 2)
        labels = [1] + labels + [M]
        groups = [labels[i * width : (i + 1) * width] for i in range(layers + 1)]
        routes = [groups[i] + groups[i + 1] for i in range(layers)]
        for _ in range(N - layers):
            layer = rng.randrange(layers)
            pool = groups[layer] + groups[layer + 1]
            r = rng.sample(pool, rng.randint(2, 30))
            r += rng.choices(r, k=rng.randrange(4))
            rng.shuffle(r)
            routes.append(r)
        for r in routes:
            rng.shuffle(r)
        rng.shuffle(routes)
        a, b = 1, M
    else:
        line = list(range(1, M + 1))
        rng.shuffle(line)
        routes = [line] + [rng.sample(range(1, M + 1), 50) for _ in range(N - 1)]
        a, b = line[5], line[-5]
    print(N, M)
    print("\n".join(" ".join(map(str, [len(r)] + r)) for r in routes))
    print(a, b)


main()
