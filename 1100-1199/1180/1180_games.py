SPLIT = 3


def main():
    digits = input().strip()
    # no power of two is divisible by 3, so from a multiple of 3 every move
    # leaves a non-multiple, and from a non-multiple taking 1 or 2 stones
    # leaves a multiple; the remainder is also the smallest such move
    rest = sum(map(int, digits)) % SPLIT
    print("2" if rest == 0 else "1\n%d" % rest)


main()
