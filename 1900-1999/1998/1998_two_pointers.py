import sys


def retreat_table(weights, limit):
    prefix = [0]
    for weight in weights:
        prefix.append(prefix[-1] + weight)
    left = 0
    retreat = [0] * len(prefix)
    for height in range(1, len(prefix)):
        while left + 1 < height and prefix[height] - prefix[left + 1] > limit:
            left += 1
        retreat[height] = left
    return retreat


def solve(weights, events, limit):
    retreat = retreat_table(weights, limit)
    size = len(weights)
    time, height = 0, 0
    for event in events:
        ordinary = event - time - 1
        if ordinary >= size - height:
            return time + size - height
        height += ordinary
        height = retreat[height]
        time = event
    return time + size - height


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, limit = next(values), next(values), next(values)
    weights = [next(values) for _ in range(n)]
    events = [next(values) for _ in range(m)]
    print(solve(weights, events, limit))


if __name__ == "__main__":
    main()
