import sys


def main():
    values = map(int, sys.stdin.buffer.read().split())
    count, capacity = next(values), next(values)
    unused = survivors = 0
    for _ in range(count):
        amount = next(values)
        if amount > capacity:
            unused += amount - capacity
        else:
            survivors += capacity - amount
    print(unused, survivors)


main()
