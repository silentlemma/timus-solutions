import sys

RECORDS = 6


def solve(records):
    groups = {}
    for _, model, price in records:
        count, cheapest = groups.get(model, (0, price))
        groups[model] = count + 1, min(cheapest, price)
    return min(groups, key=lambda model: (-groups[model][0], groups[model][1], model))


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    records = []
    for _ in range(RECORDS):
        friend = next(tokens)
        model = next(tokens).decode()
        price = int(next(tokens))
        records.append((friend, model, price))
    print(solve(records))


if __name__ == "__main__":
    main()
