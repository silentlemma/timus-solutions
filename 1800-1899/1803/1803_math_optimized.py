import sys


FIELD_BITS = 4
FIELD_BASE = 1 << FIELD_BITS
FIELD_MASK = FIELD_BASE - 1


def binary_costs(radix, count):
    bits = radix.bit_length() - 1
    a = b = 1
    if bits == 1:
        for _ in range(count):
            yield a.bit_count()
            a, b = b, a + b
        return
    mask = ((1 << (bits * count)) - 1) // (radix - 1)
    planes = [(mask << bit, 1 << bit) for bit in range(bits)]
    for _ in range(count):
        yield sum((a & plane).bit_count() * weight for plane, weight in planes)
        a, b = b, a + b


def packed_costs(radix, count):
    bias = FIELD_BASE - radix
    low_bits = ((1 << (FIELD_BITS * count)) - 1) // FIELD_MASK
    highest_shift = FIELD_BITS
    biases = bias | (bias << highest_shift)
    previous, current = 1, 1 + biases
    old_sum = current_sum = 1
    yield old_sum
    yield current_sum
    for _ in range(count - 2):
        if current >> highest_shift != bias:
            highest_shift += FIELD_BITS
            extension = bias << highest_shift
            biases |= extension
            current |= extension
        result = current + previous
        carries = ((current ^ previous ^ result) >> FIELD_BITS) & low_bits
        # Each carry replaces radix units in one place with one in the next.
        old_sum, current_sum = (
            current_sum,
            old_sum + current_sum - (radix - 1) * carries.bit_count(),
        )
        previous = current - biases
        current = result + carries * bias
        yield current_sum


def main():
    radix, count = map(int, sys.stdin.buffer.read().split())
    if radix & (radix - 1):
        costs = packed_costs(radix, count)
    else:
        costs = binary_costs(radix, count)
    order = sorted(cost * count + i for i, cost in enumerate(costs))
    print(" ".join(str(key % count + 1) for key in order))


if __name__ == "__main__":
    main()
