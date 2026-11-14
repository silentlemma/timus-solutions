BASE = 10
ODD_FACTOR = 5
ONE_DIGIT_SOLUTIONS = 3


def count_solutions(digits):
    # Find x = 0 mod 5**digits and x = 1 mod 2**digits.
    odd_power = ODD_FACTOR**digits
    ending = odd_power * pow(odd_power, -1, 1 << digits)
    suffix = str(ending).zfill(digits)[:-1]
    # The other branch has each higher digit complemented to 9.
    excluded = suffix.count("0") + suffix.count(str(BASE - 1))
    return ONE_DIGIT_SOLUTIONS + 2 * len(suffix) - excluded


if __name__ == "__main__":
    print(count_solutions(int(input())))
