def combinations(places, ones):
    if not 0 <= ones <= places:
        return 0
    result = 1
    for chosen in range(1, min(ones, places - ones) + 1):
        result = result * (places + 1 - chosen) // chosen
    return result


def count(bound, ones, base):
    digits = []
    while bound:
        bound, digit = divmod(bound, base)
        digits.append(digit)

    total = 0
    for places in range(len(digits) - 1, -1, -1):
        digit = digits[places]
        if digit > 1:
            return total + combinations(places + 1, ones)
        if digit == 1:
            total += combinations(places, ones)
            if ones == 0:
                return total
            ones -= 1
    return total + (ones == 0)


def main():
    x, y, ones, base = map(int, open(0, "rb").read().split())
    print(count(y, ones, base) - count(x - 1, ones, base))


if __name__ == "__main__":
    main()
