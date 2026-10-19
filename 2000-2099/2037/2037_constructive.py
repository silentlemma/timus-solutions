import sys

SMALL_LIMIT = 7
STABLE_MIN = 8
EXTRA_COUNT = 6
PERIOD = "babbaa"


def construct(n, count):
    minimum = n if n <= SMALL_LIMIT else SMALL_LIMIT if n == STABLE_MIN else STABLE_MIN
    if count < minimum:
        return "NO"
    if count == n:
        return "a" * n
    if n == STABLE_MIN:
        return "aababbaa"
    run = count - EXTRA_COUNT
    tail = n - run
    return "a" * run + (PERIOD * ((tail + len(PERIOD) - 1) // len(PERIOD)))[:tail]


def main():
    n = int(sys.stdin.buffer.read())
    for count in range(1, n + 1):
        print(f"{count} : {construct(n, count)}")


if __name__ == "__main__":
    main()
