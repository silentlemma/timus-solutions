import sys

FIELD = 4  # bits per base-k digit, enough for k <= 10
FIELD_MASK = (1 << FIELD) - 1


def repeat(value, fields):
    """value in each of the lowest `fields` fields."""
    return value * (((1 << (FIELD * fields)) - 1) // FIELD_MASK)


def main():
    k, n = map(int, sys.stdin.read().split())
    if k == 2:
        # binary digits: the digit sum is the number of ones
        cost = [1, 1]
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
            cost.append(b.bit_count())
        order = sorted(range(n), key=cost.__getitem__)
        print(" ".join(str(i + 1) for i in order))
        return
    # each base-k digit sits in a 4-bit field. A biased field holds
    # digit + bias, so it overflows exactly when a base-k carry is due,
    # and plain binary addition carries from field to field
    bias = (1 << FIELD) - k
    limit = n  # F(n) has fewer than n digits in any base
    low = repeat(1, limit)
    weights = [repeat(1 << j, limit) for j in range(FIELD)]

    def digit_sum(value):
        return sum(((value & w).bit_count()) << j for j, w in enumerate(weights))

    fields = 2
    biases = repeat(bias, fields)
    previous = 1  # F(1), unbiased
    current = 1 + biases  # F(2), biased
    cost = [1, 1]
    for _ in range(n - 2):
        if (current >> (FIELD * (fields - 1))) != bias:
            # keep a biased zero on top for the next carry
            current |= bias << (FIELD * fields)
            biases |= bias << (FIELD * fields)
            fields += 1
        total = current + previous
        carries = ((current ^ previous ^ total) >> FIELD) & low
        # fields that carried out hold a bare digit: bias them again
        total += carries * bias
        previous = current - biases
        current = total
        cost.append(digit_sum(current - biases))
    order = sorted(range(n), key=cost.__getitem__)
    print(" ".join(str(i + 1) for i in order))


main()
