import sys
from collections import Counter

PAIRS_PER_CAR = 4


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sizes = Counter(map(int, data[1 : 1 + n]))
    # each diameter equips as many cars as it has full sets of four pairs
    print(sum(count // PAIRS_PER_CAR for count in sizes.values()))


main()
