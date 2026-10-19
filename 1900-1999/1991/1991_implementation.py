import sys


def totals(capacity, amounts):
    unused = survivors = 0
    for amount in amounts:
        if amount > capacity:
            unused += amount - capacity
        else:
            survivors += capacity - amount
    return unused, survivors


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    count, capacity = values[:2]
    print(*totals(capacity, values[2 : count + 2]))


if __name__ == "__main__":
    main()
