import sys

MOD = 1_000_000_007


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = []
    sizes = []
    factorial = 1
    denominator = 1

    for i in range(1, n + 1):
        value = data[i]
        factorial = factorial * i % MOD
        total = 0
        # Popped nodes have complete subtrees, including the accumulated right child.
        while values and values[-1] > value:
            values.pop()
            total += sizes.pop()
            denominator = denominator * total % MOD
        values.append(value)
        sizes.append(total + 1)

    total = 0
    while sizes:
        total += sizes.pop()
        denominator = denominator * total % MOD

    print(factorial * pow(denominator, MOD - 2, MOD) % MOD)


if __name__ == "__main__":
    main()
