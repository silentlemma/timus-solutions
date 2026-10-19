"""Generate n k inputs; --proof exhausts the finite operation-bound lemma."""

import sys

MAX_TUBES = 100000
SMALL_LIMIT = 256
PHASE_PARTS = 3


def verify():
    cases = 0
    for m in range(1, SMALL_LIMIT, 2):
        for a in range(1, SMALL_LIMIT, 2):
            if a == m:
                continue
            difference = a - m
            t = (abs(difference) & -abs(difference)).bit_length() - 1
            d = difference // (1 << t)
            sign = -1 if t % 2 else 1
            total = 2 * m + a
            assert (total - sign * d) % PHASE_PARTS == 0
            b = (total - sign * d) // PHASE_PARTS
            c = total - 2 * b
            assert b > 0 and b % 2 == 0 and c > 0 and c % 2 == 1
            before = (2 * m).bit_length() - 1 + a.bit_length() - 1
            after = 2 * (b.bit_length() - 1) + c.bit_length() - 1
            assert t + 1 <= 2 * (after - before) + PHASE_PARTS
            cases += 1
    return cases


def main():
    if sys.argv[1:] == ["--proof"]:
        print(verify())
        return
    n, k = map(int, sys.argv[1:])
    assert 1 <= k <= n <= MAX_TUBES
    print(n, k)


if __name__ == "__main__":
    main()
