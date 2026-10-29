import sys


def main():
    # the prices are read line by line, one per line, and the running sums are
    # compared directly instead of calling max()
    readline = sys.stdin.buffer.readline
    n = int(readline())
    # best is the largest segment sum so far (the empty segment gives 0), and
    # ending is the largest sum of a segment that ends at the current number
    best = ending = 0
    for _ in range(n):
        p = int(readline())
        ending += p
        if ending < 0:
            ending = 0
        if ending > best:
            best = ending
    print(best)


main()
