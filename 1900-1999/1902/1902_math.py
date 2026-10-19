import sys


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    count, duration, start = next(values), next(values), next(values)
    for _ in range(count):
        doubled_time = start + duration + next(values)
        fraction = "000000" if doubled_time % 2 == 0 else "500000"
        print(f"{doubled_time // 2}.{fraction}")


if __name__ == "__main__":
    main()
