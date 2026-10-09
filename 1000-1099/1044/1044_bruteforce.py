from collections import Counter

DIGITS = 10


def main():
    half = int(input()) // 2
    # how many halves (numbers below 10^half) have each digit sum
    ways = Counter(sum(map(int, str(x))) for x in range(DIGITS**half))
    # the two halves are chosen independently with the same sum
    print(sum(w * w for w in ways.values()))


main()
