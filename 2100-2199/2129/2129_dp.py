import sys

MOD = 1_000_000_007


def count_sets(amount, base, length):
    if amount < length:
        return 0
    digits = []
    digit_sum = 0
    while amount:
        amount, digit = divmod(amount, base)
        digit_sum += digit
        if digit_sum > length:
            return 0
        digits.append(digit)
    difference = length - digit_sum
    if difference % (base - 1):
        return 0
    budget = difference // (base - 1)
    if budget == 0:
        return 1

    dp = [[0] * (used + 1) for used in range(budget + 1)]
    dp[0][0] = 1
    minimum = [0] + [budget + 1] * budget
    for digit in reversed(digits[1:]):
        # Minimum total splits needed to reach each current carry.
        minimum = [
            split + minimum[max(0, (split - digit + base - 1) // base)]
            for split in range(budget + 1)
        ]
        following = []
        width = 0
        for used in range(budget + 1):
            while width < budget and minimum[width + 1] <= used:
                width += 1
            following.append([0] * (width + 1))
        for used, row in enumerate(dp):
            total = sum(row)
            if total == 0:
                continue
            ways = total % MOD
            limit = budget - used + 1
            stop = min(limit, digit + 1)
            for split in range(stop):
                following[used + split][split] = ways
            # Each group of base split counts removes one possible parent carry.
            for previous in row:
                if stop == limit:
                    break
                ways = (ways - previous) % MOD
                end = min(limit, stop + base)
                if ways:
                    for split in range(stop, end):
                        following[used + split][split] = ways
                stop = end
        dp = following
    return sum(dp[budget]) % MOD


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    result = []
    for _ in range(next(data)):
        amount = next(data)
        base = next(data)
        length = next(data)
        result.append(str(count_sets(amount, base, length)))
    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()
