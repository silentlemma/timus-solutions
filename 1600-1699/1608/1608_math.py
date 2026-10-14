DIGITS = 10
PAIR = DIGITS * (DIGITS - 1)  # two free mirrored digits that differ


def complete(prefix, length):
    """Lucky numbers of this length that start with these digits."""
    ways = 1
    for i in range((length + 1) // 2):
        j = length - 1 - i
        if i == j:
            ways *= 1 if i < len(prefix) else DIGITS
        elif j < len(prefix):
            if prefix[i] == prefix[j]:
                return 0
        elif i < len(prefix):
            ways *= DIGITS - 1  # the partner must differ from the fixed digit
        else:
            ways *= PAIR
    return ways


def lucky_up_to(n):
    """Lucky tickets numbered 1 .. n."""
    if n <= 0:
        return 0
    digits = [int(c) for c in str(n)]
    length = len(digits)
    # all shorter numbers, by their first digit
    total = sum(complete([d], k) for k in range(1, length) for d in range(1, DIGITS))
    # same length: the first position where the number drops below n
    for k in range(length):
        for d in range(1 if k == 0 else 0, digits[k]):
            total += complete(digits[:k] + [d], length)
    return total + complete(digits, length)


def main():
    a, b = (int(x) for x in input().split())
    print(lucky_up_to(b) - lucky_up_to(a - 1))


main()
