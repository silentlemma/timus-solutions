import sys

LIMIT = 100000
SMALL = 9
REMAINDER = SMALL * (SMALL + 1) // 2


def main():
    remaining = int(sys.stdin.read())
    value = LIMIT - 1
    chosen = []
    # Large numbers contribute at most 45; stop before a small-digit finish.
    # The first ten thousand candidates already have total digit sum 270000.
    while remaining > REMAINDER:
        chosen.append(value)
        remaining -= sum(map(int, str(value)))
        value -= 1
    # Distinct digits 1..9 can make every sum from zero through 45.
    for digit in range(SMALL, 0, -1):
        if digit <= remaining:
            chosen.append(digit)
            remaining -= digit
    print(len(chosen))
    print(*chosen)


main()
