import math
import sys


def visits(a, b, x, y, n):
    if x <= a or y <= b:
        return n

    divisor_a = math.gcd(a, x)
    divisor_b = math.gcd(b, y)
    period_a = x // divisor_a
    period_b = y // divisor_b
    events_a = a // divisor_a
    events_b = b // divisor_b
    common = math.gcd(period_a, period_b)
    modulus = period_b // common
    multiplier = pow(period_a // common, -1, modulus)
    period = period_a * modulus
    answer = (n * a + x - 1) // x + (n * b + y - 1) // y

    # Purchase indices are floor(j * period / events), starting with index zero.
    for i in range(events_a):
        first = i * period_a // events_a
        for j in range(events_b):
            second = j * period_b // events_b
            difference = second - first
            if difference % common:
                continue
            # CRT gives one shared purchase index per common period.
            shift = difference // common * multiplier % modulus
            start = first + period_a * shift
            if start < n:
                answer -= 1 + (n - 1 - start) // period
    return answer


def main():
    print(visits(*map(int, sys.stdin.buffer.read().split())))


if __name__ == "__main__":
    main()
