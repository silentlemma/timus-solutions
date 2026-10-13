import sys

LIMIT = 200  # the values repeat with PERIOD from 52 on, well below this
PERIOD = 34
TAKE = 3  # a move takes up to three files out of play


def main():
    n = int(sys.stdin.read())
    # Dawson's chess: a row of n files plays like the octal game 0.137, where
    # a move takes one file (only if it is all), two (leaving one row) or three
    # (leaving up to two rows); White, moving first, wins when the value is not 0
    g = [0] * (LIMIT + 1)
    for size in range(1, LIMIT + 1):
        seen = set()
        if size == 1:
            seen.add(0)
        if size >= 2:
            seen.add(g[size - 2])
        for left in range(size - TAKE + 1):
            seen.add(g[left] ^ g[size - TAKE - left])
        value = 0
        while value in seen:
            value += 1
        g[size] = value
    if n > LIMIT:
        n = LIMIT - PERIOD + (n - LIMIT) % PERIOD
    print("White" if g[n] else "Black")


main()
