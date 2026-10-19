"""Arguments: seed mode. Modes1..4 cover all legal divisors;5..10 stress queries."""

import random
import sys

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
MAX_DIGITS = 100000
MAX_QUERIES = 10000
MEDIUM_DIGITS = 20000
DIVISOR_NUMBER_DIGITS = 120
CHECKPOINT_INTERVAL = 100


def legal_divisors():
    values = [1]
    for prime in PRIMES:
        values += [value * prime for value in values]
    return sorted(values)


def generate(seed, mode):
    rng = random.Random(seed)
    divisors = legal_divisors()
    modulus = divisors[-1]
    if mode <= 4:
        number = str(rng.randint(1, 9)) + "".join(
            str(rng.randrange(10)) for _ in range(DIVISOR_NUMBER_DIGITS - 1)
        )
        first = (mode - 1) * MAX_QUERIES
        return number, [(0, value) for value in divisors[first : first + MAX_QUERIES]]
    if mode == 5:
        return "9" * MAX_DIGITS, [(0, rng.choice(divisors)) for _ in range(MAX_QUERIES)]
    if mode in (6, 7):
        number = "1" + "0" * (MAX_DIGITS - 1)
    elif mode == 10:
        number = "7"
    else:
        length = MEDIUM_DIGITS if mode == 9 else MAX_DIGITS
        number = str(rng.randint(1, 9)) + "".join(
            str(rng.randrange(10)) for _ in range(length - 1)
        )
    queries = []
    for index in range(MAX_QUERIES):
        if mode == 6 and index % CHECKPOINT_INTERVAL == CHECKPOINT_INTERVAL - 1:
            queries.append((0, modulus if index % 2 else rng.choice(divisors)))
        elif mode == 7:
            place = MAX_DIGITS if index % 2 else 1
            queries.append((1, place, index % 9 + 1))
        elif mode == 8:
            if index % 2:
                queries.append((0, rng.choice(divisors)))
            else:
                place = rng.choice((1, MAX_DIGITS, MAX_DIGITS // 2))
                queries.append(
                    (1, place, rng.randint(1 if place == MAX_DIGITS else 0, 9))
                )
        elif mode == 10:
            queries.append(
                (0, (1, 2, 5, modulus)[index % 4])
                if index % 2
                else (1, 1, rng.randint(1, 9))
            )
        elif mode == 9 and rng.randrange(2):
            queries.append((0, rng.choice(divisors)))
        else:
            place = rng.randint(1, len(number))
            queries.append((1, place, rng.randint(1 if place == len(number) else 0, 9)))
    return number, queries


def render(number, queries):
    return (
        number
        + f"\n{len(queries)}\n"
        + "".join(" ".join(map(str, query)) + "\n" for query in queries)
    )


if __name__ == "__main__":
    print(render(*generate(int(sys.argv[1]), int(sys.argv[2]))), end="")
