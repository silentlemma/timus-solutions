"""Generate readings and questions from a seed and a mode. Mode 1 gives
random readings, mode 2 every reading 10000 or every reading -10000,
mode 3 long questions only. Mode 4 gives random readings and ten shuffled
passes over all singleton questions. Mode 5 gives sparse nonzero readings
and random intervals, many with endpoints beside a nonzero reading.
Mode 6 gives all readings -10000 and seven questions including the full
interval for the exact minimum sum. All modes use 10000 readings;
modes 1-5 use 100000 questions."""

import random
import sys

N = 10000
Q = 100000
TOP = 10000


def extended(seed, mode):
    sys.stdout.reconfigure(newline="\n")
    rng = random.Random(seed)
    if mode == 6:
        readings = [-TOP] * N
        questions = [
            (1, N), (2, N), (1, N - 1), (N // 2, N // 2 + 1),
            (1, 1), (N, N), (2, N - 1),
        ]
    elif mode == 4:
        readings = [rng.randint(-TOP, TOP) for _ in range(N)]
        readings[0], readings[-1] = TOP, -TOP
        questions = []
        for _ in range(Q // N):
            order = list(range(1, N + 1))
            rng.shuffle(order)
            questions.extend((i, i) for i in order)
    else:
        readings = [0] * N
        positions = [1, N] + rng.sample(range(2, N), 30)
        for i in positions:
            readings[i - 1] = rng.choice([-1, 1]) * rng.randint(1, TOP)
        edges = sorted({i + d for i in positions for d in (-1, 0, 1) if 1 <= i + d <= N})
        questions = [(1, N), (1, 1), (N, N), (2, N - 1)]
        for i in positions:
            questions.extend(((i, i), (max(1, i - 1), min(N, i + 1))))
        while len(questions) < Q:
            if len(questions) % 2:
                i, j = rng.randint(1, N), rng.randint(1, N)
            else:
                i, j = rng.choice(edges), rng.choice(edges)
            questions.append((min(i, j), max(i, j)))
    print(N)
    print("\n".join(map(str, readings)))
    print(len(questions))
    for i, j in questions:
        print(i, j)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (4, 5, 6):
        extended(seed, mode)
        return
    rng = random.Random(seed)
    if mode == 2:
        readings = [rng.choice([TOP, -TOP])] * N
    else:
        readings = [rng.randint(-TOP, TOP) for _ in range(N)]
    print(N)
    print("\n".join(map(str, readings)))
    print(Q)
    for _ in range(Q):
        if mode == 3:
            i, j = rng.randint(1, N // 10), rng.randint(N - N // 10, N)
        else:
            i, j = sorted((rng.randint(1, N), rng.randint(1, N)))
        print(i, j)


main()
