from math import comb


def count_upto(n, k, b):
    """How many numbers in [0, n] are sums of exactly k different powers of b,
    that is, have only digits 0 and 1 in base b with k ones."""
    digits = []
    while n > 0:
        digits.append(n % b)
        n //= b
    digits.reverse()
    # a digit above 1 lets every smaller number with 0/1 digits through: it and
    # all digits after it may as well be 1
    for i, d in enumerate(digits):
        if d > 1:
            digits[i:] = [1] * (len(digits) - i)
            break
    # count 0/1 strings with k ones not above the digits, from the top
    total = ones = 0
    for i, d in enumerate(digits):
        if d == 1 and ones <= k:
            total += comb(len(digits) - 1 - i, k - ones)
            ones += 1
    return total + (ones == k)


def main():
    x, y, k, b = map(int, open(0).read().split())
    print(count_upto(y, k, b) - count_upto(x - 1, k, b))


main()
