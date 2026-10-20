import sys

CHOICES = 3


def main():
    n, modulus = map(int, sys.stdin.buffer.read().split())
    half = (modulus - 1) // 2
    exponent = 0
    digits = []
    remaining = n
    while remaining:
        remaining, digit = divmod(remaining, modulus)
        # Reflect central trinomial coefficients into the lower half.
        if digit > half:
            digit = modulus - 1 - digit
            exponent += half - digit
        digits.append(digit)
    digits.sort()

    index = 0
    previous = current = factorial = 1
    numerator = denominator = 1
    for digit in digits:
        while index < digit:
            index += 1
            before = index - 1
            # F_i = i! * T_i avoids division inside the recurrence.
            following = ((2 * index - 1) * current + CHOICES * before * before * previous) % modulus
            previous, current = current, following
            factorial = factorial * index % modulus
        numerator = numerator * current % modulus
        denominator = denominator * factorial % modulus

    draws = numerator * pow(denominator, modulus - 2, modulus) % modulus
    draws = draws * pow(modulus - CHOICES, exponent, modulus) % modulus
    answer = (pow(CHOICES, n, modulus) - draws) * ((modulus + 1) // 2) % modulus
    print(answer)


if __name__ == "__main__":
    main()
