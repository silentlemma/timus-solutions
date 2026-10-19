import sys
from fractions import Fraction


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, a = data[0], data[1:1 + data[0]]
    # least squares line through the points (i, a_i), i = 0 .. n - 1:
    # the normal equations give the step and then the first term
    sum_x = n * (n - 1) // 2
    sum_xx = sum(i * i for i in range(n))
    sum_a = sum(a)
    sum_xa = sum(i * v for i, v in enumerate(a))
    step = Fraction(n * sum_xa - sum_x * sum_a, n * sum_xx - sum_x * sum_x)
    first = (sum_a - step * sum_x) / n
    print(f"{float(first):.9f} {float(step):.9f}")


main()
