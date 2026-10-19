"""Generate seed/mode: 1 small; 2 chain; 3 backward self-chain; 4 random;
5 star; 6 missed departures; 7 duplicates; 8 high keys; 9 empty; 10 one-line chain."""

import random
import sys

MAX_PLANETS = 100_000
MAX_FLIGHTS = 100_000
MAX_TIME = 1_000_000


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        n, count = 4, 8
        flights = [
            (
                rng.randrange(1, n + 1),
                rng.randrange(1, n + 1),
                rng.randrange(11),
                rng.randrange(11),
            )
            for _ in range(count)
        ]
        query = (
            rng.randrange(1, n + 1),
            rng.randrange(1, n + 1),
            rng.randrange(11),
            rng.randrange(11),
        )
    elif mode in (2, 10):
        n, count = MAX_PLANETS, MAX_PLANETS - 1
        flights = [(i, i + 1, i - 1, i) for i in range(1, n)]
        query = (1, n, 0, n)
    elif mode == 3:
        n, count = 1, MAX_FLIGHTS
        flights = [(1, 1, count - i, count - i - 1) for i in range(count)]
        query = (1, 1, count, 0)
    elif mode == 4:
        n, count = MAX_PLANETS, MAX_FLIGHTS
        flights = [
            (
                rng.randrange(1, n + 1),
                rng.randrange(1, n + 1),
                rng.randrange(MAX_TIME + 1),
                rng.randrange(MAX_TIME + 1),
            )
            for _ in range(count)
        ]
        query = (1, n, 0, MAX_TIME)
    elif mode == 5:
        n, count = MAX_PLANETS, MAX_FLIGHTS
        flights = [(1, i % (n - 1) + 2, i, MAX_TIME - i) for i in range(count)]
        query = (1, n, 0, MAX_TIME)
    elif mode == 6:
        n, count = 2, MAX_FLIGHTS
        flights = [(1, 2, i, rng.randrange(MAX_TIME + 1)) for i in range(count)]
        query = (1, 2, MAX_TIME, MAX_TIME)
    elif mode == 7:
        n, count = MAX_PLANETS, MAX_FLIGHTS
        flights = [(1, 2, 0, 0)] * count
        query = (1, n, 0, 0)
    elif mode == 8:
        n, count = MAX_PLANETS, MAX_FLIGHTS
        flights = [(n, n - 1, MAX_TIME - i, i) for i in range(count)]
        query = (n, n - 1, MAX_TIME, MAX_TIME)
    elif mode == 9:
        n, count, flights = MAX_PLANETS, 0, []
        query = (1, n, 0, MAX_TIME)
    else:
        raise ValueError("Unknown mode")
    if mode == 10:
        print(n, count, end=" ")
        for flight in flights:
            print(*flight, end=" ")
        print(*query)
    else:
        print(n, count)
        for flight in flights:
            print(*flight)
        print(*query)


if __name__ == "__main__":
    main()
