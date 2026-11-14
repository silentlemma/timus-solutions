import sys


def main():
    fields = iter(sys.stdin.buffer.read().split())
    next(fields)
    largest = total = 0
    for size in map(int, fields):
        total += size
        if size > largest:
            largest = size
    print(max(1, 2 * largest - total), largest)


if __name__ == "__main__":
    main()
