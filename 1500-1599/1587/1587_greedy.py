import math
import sys

TWO = 2
THREE = 3


def main():
    sys.set_int_max_str_digits(0)  # the answer can have over 20000 digits
    words = sys.stdin.read().split()
    n = int(words[0])
    marks = [int(v) for v in words[1 : 1 + n]]
    # a nonzero product is +-2^a 3^b: prefix counts of twos, threes, negatives
    twos, threes = [0] * (n + 1), [0] * (n + 1)
    for i, x in enumerate(marks):
        twos[i + 1] = twos[i] + (abs(x) == TWO)
        threes[i + 1] = threes[i] + (abs(x) == THREE)

    def size(lo, hi):
        """The exponents (a, b) of the product of marks[lo:hi]."""
        return twos[hi] - twos[lo], threes[hi] - threes[lo]

    def key(ab):
        return ab[0] * math.log(TWO) + ab[1] * math.log(THREE)

    best = None  # the exponents of the best positive product
    i = 0
    while i < n:
        if marks[i] == 0:
            i += 1
            continue
        # a run without zeros: |x| >= 1, so longer runs never shrink the size
        j = i
        while j < n and marks[j] != 0:
            j += 1
        negatives = [k for k in range(i, j) if marks[k] < 0]
        if len(negatives) % 2 == 0:
            spans = [(i, j)]
        else:
            # drop the part up to the first negative or from the last one
            spans = [(negatives[0] + 1, j), (i, negatives[-1])]
        for lo, hi in spans:
            if lo < hi and (best is None or key(size(lo, hi)) > key(best)):
                best = size(lo, hi)
        i = j
    if best is not None:
        print(TWO ** best[0] * THREE ** best[1])
    elif 0 in marks:
        print(0)
    else:
        # one negative mark alone
        print(max(marks))


main()
