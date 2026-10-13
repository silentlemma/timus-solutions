import sys


def main():
    n = int(sys.stdin.read())
    # numbers of length k without two zeros in a row: Fibonacci F(k + 2), so
    # F(2N) bars go into F(N) safes, and F(2N) = F(N) L(N) with Lucas L(N)
    a, b = 2, 1  # L(0), L(1)
    for _ in range(n):
        a, b = b, a + b
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)  # the answer has thousands of digits
    print(a)


main()
