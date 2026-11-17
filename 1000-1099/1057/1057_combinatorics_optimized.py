def choose(size, count):
    if count < 0 or count > size:
        return 0
    value = 1
    for i in range(1, min(count, size - count) + 1):
        value = value * (size + 1 - i) // i
    return value


def count(bound, ones, base):
    power, lower = 1, 0
    while power <= bound // base:
        power *= base
        lower += 1
    total = 0
    while power:
        digit, bound = divmod(bound, power)
        if digit > 1:
            return total + choose(lower + 1, ones)
        if digit:
            total += choose(lower, ones)
            if ones == 0:
                return total
            ones -= 1
        power //= base
        lower -= 1
    return total + (ones == 0)


x, y, k, b = map(int, open(0, "rb").read().split())
print(count(y, k, b) - count(x - 1, k, b))
