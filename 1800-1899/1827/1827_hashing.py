import sys
from operator import add

SHIFT = 1 << 28  # above every star count
LONGEST = 50
TO_DIGITS = bytes.maketrans(b"\x00\x01", b"01")


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    stars = list(map(int, data[1:1 + n]))
    wanted = [set() for _ in range(LONGEST + 1)]
    wars = iter(data[2 + n:])
    for x, y, d in zip(wars, wars, wars):
        wanted[int(d)].add(int(x) * SHIFT + int(y))
    # a war of d days ending k days ago began k + d - 1 days ago, so for
    # each d the counts of all such first and last days are looked up at
    # once, and the hits become a bitmask smeared over the d days of war
    high = [v * SHIFT for v in stars]
    war = 0
    for d in range(2, min(LONGEST, n) + 1):
        if not wanted[d]:
            continue
        hits = bytes(map(wanted[d].__contains__, map(add, high[d - 1:], stars)))
        if not any(hits):
            continue
        mask = int(hits.translate(TO_DIGITS)[::-1], 2)
        span = 1
        while 2 * span <= d:
            mask |= mask << span
            span *= 2
        war |= mask | mask << (d - span)
    digits = bin(war)[2:][::-1][:n]
    print(digits + "0" * (n - len(digits)) if war else "0" * n)


main()
