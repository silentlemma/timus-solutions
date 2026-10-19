import sys

DIGIT_COUNT = 4
HEX_BASE = 16
DIGIT_BITS = 4
DIGIT_MASK = HEX_BASE - 1
PAIR_DOMAIN = HEX_BASE * HEX_BASE
TRIPLE_DOMAIN = PAIR_DOMAIN * HEX_BASE
PAIR_GROUPS = DIGIT_COUNT * (DIGIT_COUNT - 1) // 2


def distance_histogram(numbers):
    singles = tuple([0] * HEX_BASE for _ in range(DIGIT_COUNT))
    pairs = tuple([0] * PAIR_DOMAIN for _ in range(PAIR_GROUPS))
    triples = tuple([0] * TRIPLE_DOMAIN for _ in range(DIGIT_COUNT))
    single_pairs = double_pairs = triple_pairs = count = 0
    for number in numbers:
        first = number >> (DIGIT_BITS * (DIGIT_COUNT - 1))
        second = (number >> (2 * DIGIT_BITS)) & DIGIT_MASK
        third = (number >> DIGIT_BITS) & DIGIT_MASK
        fourth = number & DIGIT_MASK
        for bucket, key in zip(singles, (first, second, third, fourth)):
            single_pairs += bucket[key]
            bucket[key] += 1
        pair_keys = (
            number >> (2 * DIGIT_BITS),
            first * HEX_BASE + third,
            first * HEX_BASE + fourth,
            (number >> DIGIT_BITS) & (PAIR_DOMAIN - 1),
            second * HEX_BASE + fourth,
            number & (PAIR_DOMAIN - 1),
        )
        for bucket, key in zip(pairs, pair_keys):
            double_pairs += bucket[key]
            bucket[key] += 1
        triple_keys = (
            number >> DIGIT_BITS,
            (number >> (2 * DIGIT_BITS)) * HEX_BASE + fourth,
            first * PAIR_DOMAIN + (number & (PAIR_DOMAIN - 1)),
            number & (TRIPLE_DOMAIN - 1),
        )
        for bucket, key in zip(triples, triple_keys):
            triple_pairs += bucket[key]
            bucket[key] += 1
        count += 1
    distance_one = triple_pairs
    distance_two = double_pairs - (DIGIT_COUNT - 1) * distance_one
    distance_three = single_pairs - 2 * distance_two - (DIGIT_COUNT - 1) * distance_one
    distance_four = (
        count * (count - 1) // 2 - distance_one - distance_two - distance_three
    )
    return distance_one, distance_two, distance_three, distance_four


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    count = int(next(tokens))
    print(*distance_histogram(int(next(tokens), HEX_BASE) for _ in range(count)))


if __name__ == "__main__":
    main()
