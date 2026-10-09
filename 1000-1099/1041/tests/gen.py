"""Random vectors: a seed, M, N, the mode, the largest coordinate and the
largest price. Modes: random (independent coordinates), plane (every
vector has x_N = x_1 - x_2, so no N of them are independent), sparse
(mostly zero coordinates), multiples (few directions, many multiples),
late (rank N-1 until the last, most expensive vector completes the basis)."""

import random
import sys


def main():
    seed, m, n = (int(x) for x in sys.argv[1:4])
    mode = sys.argv[4]
    top, max_price = int(sys.argv[5]), int(sys.argv[6])
    rng = random.Random(seed)
    directions = [[rng.randint(-top, top) for _ in range(n)] for _ in range(n + 2)]
    lines = ["%d %d" % (m, n)]
    for i in range(m):
        if mode == "late":
            if i < n - 1:
                v = [top if j == i else 0 for j in range(n)]
            else:
                v = [rng.randint(-top, top) for _ in range(n)]
                v[n - 1] = top if i == m - 1 else 0
        elif mode == "plane":
            v = [rng.randint(-top // 2, top // 2) for _ in range(n)]
            v[n - 1] = v[0] - v[1]
        elif mode == "sparse":
            v = [rng.randint(-top, top) if rng.randrange(n) < 2 else 0 for _ in range(n)]
        elif mode == "multiples":
            d = rng.choice(directions)
            limit = max(abs(x) for x in d) or 1
            k = rng.choice([x for x in range(-top // limit, top // limit + 1) if x])
            v = [k * x for x in d]
        else:
            v = [rng.randint(-top, top) for _ in range(n)]
        lines.append(" ".join(map(str, v)))
    if mode == "late":
        lines += [str(rng.randint(1, max(1, max_price - 1))) for _ in range(m - 1)]
        lines.append(str(max_price))
    else:
        lines += [str(rng.randint(1, max_price)) for _ in range(m)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
