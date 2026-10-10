FIRST = 36
OTHER = 55


def main():
    k = int(input())
    # no position may carry: 36 pairs of leading digits with a sum of at
    # most 9, and 55 pairs of digits from 0 in every other position
    print(FIRST * OTHER ** (k - 1))


main()
