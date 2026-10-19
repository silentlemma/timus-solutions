import sys


def optimal_totals(budget, gift, limit):
    current = [0] * (budget + 1)
    opponent = [0] * (budget + 1)
    for remaining in range(1, budget + 1):
        best, other = (gift, 0) if remaining < limit else (-1, 0)
        for request in range(1, min(remaining, limit) + 1):
            rest = remaining - request
            own_total = request + opponent[rest]
            other_total = current[rest]
            if own_total > best or (own_total == best and other_total < other):
                best, other = own_total, other_total
        current[remaining], opponent[remaining] = best, other
    return current[budget], opponent[budget]


def main():
    budget, gift, limit = map(int, sys.stdin.buffer.read().split())
    print(*optimal_totals(budget, gift, limit))


if __name__ == "__main__":
    main()
