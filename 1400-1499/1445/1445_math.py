import sys


def main():
    data = sys.stdin.read().split()
    sizes = [int(x) for x in data[1:]]
    biggest, total = max(sizes), sum(sizes)
    # the biggest company needs gifts from outside it: prepared or from the others
    best = max(1, 2 * biggest - total)
    # in the worst order the biggest company comes first, and that many always suffice
    print(best, biggest)


main()
