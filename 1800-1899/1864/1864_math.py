import sys

MONEY = 100


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, bought = data[0], data[1:]
    # everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
    # litre, friend i paid for bought[i] (n + 1) - total litres of others
    total = sum(bought)
    over = [max(0, b * (n + 1) - total) for b in bought]
    print(*(MONEY * x // sum(over) for x in over))


main()
