import sys
from itertools import groupby


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    numbers = list(map(int, words[1 : 1 + n]))
    # each run of equal numbers is said as its length and then the number
    out = []
    for value, run in groupby(numbers):
        out += [str(len(list(run))), str(value)]
    print(" ".join(out))


main()
