"""Print seed mode: max_inc, max_dec, max_two_inc, max_two_dec, max_mixed,
max_mixed_reversed, max_late_fail, max_early_fail, random_two_inc,
random_two_dec, random_mixed. All modes use n=100000; only random_* use seed.
"""
import random
import sys


MAX_SIZE = 100000
OBSTRUCTION = (3, 5, 2, 1, 6, 4)


def build(seed, mode):
    size = MAX_SIZE
    half = size // 2
    increasing = list(range(1, size + 1))
    if mode == 'max_inc':
        return increasing, [increasing[:-1], increasing[-1:]], None
    if mode == 'max_dec':
        return increasing[::-1], [increasing[:0:-1], increasing[:1]], None
    if mode in ('max_two_inc', 'max_two_dec'):
        first = list(range(half + 1, size + 1))
        second = list(range(1, half + 1))
        values = [value for pair in zip(first, second) for value in pair]
        if mode == 'max_two_dec':
            values, first, second = values[::-1], first[::-1], second[::-1]
        return values, [first, second], None
    if mode in ('max_mixed', 'max_mixed_reversed'):
        first = list(range(1, size + 1, 2))
        second = list(range(size, 0, -2))
        values = [value for pair in zip(first, second) for value in pair]
        if mode == 'max_mixed_reversed':
            values, first, second = values[::-1], first[::-1], second[::-1]
        return values, [first, second], None
    if mode == 'max_late_fail':
        values = list(range(1, size - len(OBSTRUCTION) + 1))
        values.extend(size - len(OBSTRUCTION) + v for v in OBSTRUCTION)
        return values, None, list(range(size - len(OBSTRUCTION), size))
    if mode == 'max_early_fail':
        values = list(OBSTRUCTION) + list(range(len(OBSTRUCTION) + 1, size + 1))
        return values, None, list(range(len(OBSTRUCTION)))
    if mode not in ('random_two_inc', 'random_two_dec', 'random_mixed'):
        raise ValueError('Unknown generator mode')
    rng = random.Random(seed)
    rng.shuffle(increasing)
    first, second = sorted(increasing[:half]), sorted(increasing[half:])
    if mode == 'random_two_dec':
        first.reverse()
    if mode in ('random_two_dec', 'random_mixed'):
        second.reverse()
    values = []
    at_first = at_second = 0
    while at_first < half or at_second < half:
        choose_first = at_second == half or (at_first < half and rng.randrange(2) == 0)
        if choose_first:
            values.append(first[at_first])
            at_first += 1
        else:
            values.append(second[at_second])
            at_second += 1
    return values, [first, second], None


def main():
    values, _, _ = build(int(sys.argv[1]), sys.argv[2])
    print(len(values))
    print(*values)


if __name__ == '__main__':
    main()
