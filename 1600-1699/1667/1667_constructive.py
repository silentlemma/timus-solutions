import math
import sys

ROOT_LIMIT = 316227766  # the largest integer whose square is at most 10^17
LEGS = 40  # Pythagorean pairs from m^2 - n^2 and 2mn with n < m < LEGS

STARTS = 30  # first terms of the arithmetic sequences
STEPS = 6  # their differences
OFFSETS = 30  # where the runs of consecutive primes start
PRIMES = 80


def first_primes(count):
    found, n = [], 2
    while len(found) < count:
        if all(n % p for p in found if p * p <= n):
            found.append(n)
        n += 1
    return found


def from_us(us):
    """For u_1..u_k with S = sum of u^2, the numbers 2u_1, ..., 2u_k and
    S - 1 have squares adding up to (S + 1)^2; None if they repeat."""
    total = sum(u * u for u in us)
    nums = [2 * u for u in us] + [total - 1]
    return nums if len(set(nums)) == len(nums) else None


def ratios(nums):
    """The reduced fractions x / y < 1 between members of the list."""
    out = set()
    for x in nums:
        for y in nums:
            if x < y:
                g = math.gcd(x, y)
                out.add((x // g, y // g))
    return out


def lists(size, primes):
    """Lists of distinct positive integers whose squares add up to a
    square, smallest maximum first, with their ratio sets."""
    if size == 1:
        found = [[1]]
    elif size == 2:
        found = [[m * m - n * n, 2 * m * n] for m in range(2, LEGS) for n in range(1, m)
                 if math.gcd(m, n) == 1 and (m - n) % 2]
    else:
        k = size - 1
        found = [from_us([s + d * i for i in range(k)])
                 for s in range(1, STARTS) for d in range(1, STEPS + 1)]
        found += [from_us(primes[off:off + k]) for off in range(OFFSETS)]
        found = [f for f in found if f]
    found.sort(key=max)
    return [(f, ratios(f)) for f in found]


def table(rows, cols, pool):
    """Entry (i, j) is (a_i b_j)^2, so row i adds up to a_i^2 times a square
    and column j to b_j^2 times a square. Two products a_i b_j and a_k b_l
    are equal exactly when a_i / a_k = b_l / b_j, so the lists must share
    no ratio."""
    smallest = max(pool[cols][0][0])
    for a, ra in pool[rows]:
        if max(a) * smallest > ROOT_LIMIT:
            break
        for b, rb in pool[cols]:
            if max(a) * max(b) > ROOT_LIMIT:
                break
            if ra.isdisjoint(rb):
                return [[(x * y) ** 2 for y in b] for x in a]
    return None


def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    primes = first_primes(PRIMES)
    pool = {}
    blocks = []
    for k in range(t):
        rows, cols = int(data[1 + 2 * k]), int(data[2 + 2 * k])
        for size in (rows, cols):
            if size not in pool:
                pool[size] = lists(size, primes)
        grid = table(rows, cols, pool)
        if grid is None:
            blocks.append("-1")
        else:
            blocks.append("\n".join(" ".join(map(str, row)) for row in grid))
    print("\n\n".join(blocks))


main()
