import sys
from bisect import bisect_left

# chunks bound token storage even when all input is on one line.
# every input integer has at most ten digits; only an unfinished token is kept.
INPUT_BUFFER = 8192


def numbers():
    tail = b""
    while chunk := sys.stdin.buffer.read(INPUT_BUFFER):
        parts = (tail + chunk).split()
        tail = parts.pop() if chunk[-1:] > b" " else b""
        yield from map(int, parts)
    if tail:
        yield int(tail)


CITY_BITS = 17


def main():
    nums = numbers()
    n = next(nums)
    # city <= 69999 needs 17 low bits; high bits hold the passenger count.
    pairs = sorted((next(nums) << CITY_BITS) | city for city in range(1, n + 1))
    q = next(nums)
    out = bytearray()
    for _ in range(q):
        lo, hi, x = next(nums), next(nums), next(nums)
        base = x << CITY_BITS
        k = bisect_left(pairs, base + lo)
        out += b"1" if k < n and pairs[k] <= base + hi else b"0"
    sys.stdout.buffer.write(out + b"\n")


main()
