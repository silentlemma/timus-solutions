import sys


def solve(capacity, values):
    values = sorted(values)
    left, right = 0, len(values) - 1
    trips = 0
    order = []
    while left < right:
        if values[left] + values[right] > capacity:
            order.extend((values[left], values[right]))
            left += 1
            right -= 1
            trips += 2
        else:
            order.extend((values[left], values[left + 1]))
            left += 2
            trips += 1
    if left == right:
        order.append(values[left])
        trips += 1
    return trips, order


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count, capacity = next(tokens), next(tokens)
    trips, order = solve(capacity, [next(tokens) for _ in range(count)])
    print(trips)
    print(*order)


if __name__ == "__main__":
    main()
