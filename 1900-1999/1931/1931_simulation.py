import sys


def most_compared(values):
    values = iter(values)
    champion_value = next(values)
    champion = best = 0
    current_count = best_count = 0
    for index, value in enumerate(values, 1):
        current_count += 1
        if current_count > best_count:
            best_count, best = current_count, champion
        if value < champion_value:
            champion_value, champion = value, index
            current_count = 1
    return best + 1


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(values)
    print(most_compared(next(values) for _ in range(count)))


if __name__ == "__main__":
    main()
