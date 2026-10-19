import sys


def main():
    data = sys.stdin.buffer.read().split()
    total = sum(map(int, data[1:]))
    # a trip to a city with load L costs L d there and (L - d) d back; summed over
    # any order this is (sum of d)^2, so the order does not matter
    print(total * total)


main()
