import sys


def best_count(sample, successes, population):
    return min(population, successes * (population + 1) // sample)


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    print(best_count(*values))


if __name__ == "__main__":
    main()
