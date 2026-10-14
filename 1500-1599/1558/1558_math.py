import sys


def main():
    lines = [line for line in sys.stdin.read().splitlines() if line.strip()]
    first, second = ("".join(c for c in line if c.isdigit()) for line in lines[:2])
    k = len(first)
    top = 10**k
    total = int(first) + int(second)
    # without a carry every block is the plain sum; with one, the lowest block
    # sends a carry on, and every block above it gets the carry and sends one
    if total < top:
        period, tail = total, None
    else:
        period, tail = total + 1 - top, total - top
    p = str(period).zfill(k)[::-1]  # digits from the least significant
    digits = p if tail is None else str(tail).zfill(k)[::-1] + p
    # the shortest period of the repeated block, then the shortest tail after
    # which every digit repeats the digit that period further up
    d = next(d for d in range(1, k + 1) if k % d == 0 and p == p[d:] + p[:d])
    digits += p * 2
    start = len(digits) - 2 * k
    while start > 0 and digits[start - 1] == digits[start - 1 + d]:
        start -= 1
    print("(" + digits[start : start + d][::-1] + ")" + digits[:start][::-1])


main()
