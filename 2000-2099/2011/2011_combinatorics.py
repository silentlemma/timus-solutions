import sys

ALPHABET = 3
TARGET = 6


def solve(values):
    counts = [0] * ALPHABET
    ways = 1
    for length, value in enumerate(values, 1):
        counts[value - 1] += 1
        ways = ways * length // counts[value - 1]
        if ways >= TARGET:
            return True
    return False


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    print("Yes" if solve([next(tokens) for _ in range(n)]) else "No")
