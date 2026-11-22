import sys


def main():
    values = map(int, sys.stdin.buffer.read().split())
    count, current = next(values), next(values)
    answer = current - 2
    for _ in range(count):
        answer += next(values) - next(values) - 2
    print(answer if answer >= 0 else "Big Bang!")


main()
