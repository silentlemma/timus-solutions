import sys

BASE = 10
FIVE = 5  # the last digit of one of the two endless solutions of x^2 = x


def main():
    n = int(sys.stdin.readline())
    # x^2 ends with x exactly when x^2 = x mod 10^d for its d digits; besides
    # 0 and 1 the solutions are the endings of two 10-adic numbers, ...0625
    # and ...9376, whose digits other than the last add up to 9 place by place

    digits = [FIVE]  # the 5-adic one, lowest digit first
    carry = FIVE * FIVE // BASE  # carry into position d of the square so far
    for d in range(1, n):
        # digit d of x^2: the products x_i x_j with i + j = d, plus the carry, and
        # a new digit c adds 2 * 5 * c, a multiple of 10: c is forced
        total = carry + sum(digits[i] * digits[d - i] for i in range(1, d))
        c = total % BASE
        digits.append(c)
        carry = (total + 2 * FIVE * c) // BASE
    count = 1 + 2  # the numbers 1, 5 and 6
    for d in range(1, n):
        # a d + 1 digit number needs a nonzero leading digit
        count += (digits[d] != 0) + (digits[d] != BASE - 1)
    print(count)


main()
