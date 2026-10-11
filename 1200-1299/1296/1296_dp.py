import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # best is the largest segment sum so far (the empty segment gives 0), and
    # ending is the largest sum of a segment that ends at the current number
    best = ending = 0
    for token in data[1 : n + 1]:
        ending = max(ending + int(token), 0)
        best = max(best, ending)
    print(best)


main()
