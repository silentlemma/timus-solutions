import sys


def minimum_common(population, lower_bounds):
    answer = population
    for lower in lower_bounds:
        answer -= population - lower
    return max(0, answer)


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    population, count = next(data), next(data)
    lower_bounds = [next(data) for _ in range(count)]
    print(minimum_common(population, lower_bounds))


if __name__ == '__main__':
    main()
