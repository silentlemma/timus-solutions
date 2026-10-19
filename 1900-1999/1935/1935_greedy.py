import sys


def minimum_sheets(clearances):
    return sum(clearances) + max(clearances)


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    count = values[0]
    print(minimum_sheets(values[1 : count + 1]))


if __name__ == "__main__":
    main()
