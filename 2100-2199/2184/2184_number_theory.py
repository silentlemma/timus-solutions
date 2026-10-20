import sys
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    coins = data[1:]
    total = sum(coins)

    # The first and last nonmultiples must change these GCDs.
    marked = bytearray(n)
    current = total
    for i, value in enumerate(coins):
        next_gcd = gcd(current, value)
        if next_gcd != current:
            marked[i] = 1
            current = next_gcd
    current = total
    for i in range(n - 1, -1, -1):
        next_gcd = gcd(current, coins[i])
        if next_gcd != current:
            marked[i] = 1
            current = next_gcd

    fixed = total
    critical = []
    for i, value in enumerate(coins):
        if marked[i]:
            critical.append(value)
        else:
            fixed = gcd(fixed, value)

    count = len(critical)
    suffix = [fixed] * (count + 1)
    for i in range(count - 1, -1, -1):
        suffix[i] = gcd(critical[i], suffix[i + 1])

    answer = suffix[0]
    before = fixed
    for first, value in enumerate(critical):
        current = before
        for second in range(first + 1, count):
            answer = max(answer, gcd(current, suffix[second + 1]))
            current = gcd(current, critical[second])
        before = gcd(before, value)
    print(answer)


if __name__ == "__main__":
    main()
