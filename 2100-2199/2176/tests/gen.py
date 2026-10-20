import random
import sys


MAX_VALUE = 1_000_000_000
MAX_QUERIES = 1000
SMALL_MAX_VALUE = 50_000
SMALL_MAX_QUERIES = 50
TERNARY_BASE = 3
NEIGHBOR_RADIUS = 2
TOTAL_RADIUS = 1000


def beautiful_numbers():
    numbers = []
    pending = [(1, "1")]
    while pending:
        value, digits = pending.pop()
        if digits in format(value, "b"):
            numbers.append(value)
        for digit in (0, 1):
            following = value * TERNARY_BASE + digit
            if following <= MAX_VALUE:
                pending.append((following, digits + str(digit)))
    return sorted(numbers)


def repeat_shuffled(anchors, rng):
    values = [anchors[index % len(anchors)] for index in range(MAX_QUERIES)]
    rng.shuffle(values)
    return values


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))

    if mode == "small":
        count = rng.randint(1, SMALL_MAX_QUERIES)
        values = [rng.randint(1, SMALL_MAX_VALUE) for _ in range(count)]
    elif mode == "random":
        values = [rng.randint(1, MAX_VALUE) for _ in range(MAX_QUERIES)]
    elif mode == "maximum":
        values = [MAX_VALUE] * MAX_QUERIES
    else:
        numbers = beautiful_numbers()
        total = sum(numbers)
        if mode == "beautiful":
            anchors = [
                value + delta
                for value in numbers
                for delta in range(-NEIGHBOR_RADIUS, NEIGHBOR_RADIUS + 1)
                if 1 <= value + delta <= MAX_VALUE
            ]
            values = repeat_shuffled(anchors, rng)
        elif mode == "subset":
            values = []
            while len(values) < MAX_QUERIES:
                value = sum(number for number in numbers if rng.getrandbits(1))
                value += rng.randint(-NEIGHBOR_RADIUS, NEIGHBOR_RADIUS)
                if 1 <= value <= MAX_VALUE:
                    values.append(value)
        elif mode == "bounds":
            anchors = [1, 2, MAX_VALUE, MAX_VALUE - 1, total, total - 1, total + 1]
            for delta in range(1, TOTAL_RADIUS + 1):
                anchors.extend((delta, MAX_VALUE - delta))
            rng.shuffle(anchors)
            values = anchors[:MAX_QUERIES]
        elif mode == "total":
            anchors = [total, total - 1, total + 1]
            values = anchors + [
                total + rng.randint(-TOTAL_RADIUS, TOTAL_RADIUS)
                for _ in range(MAX_QUERIES - len(anchors))
            ]
            rng.shuffle(values)
        elif mode == "repeated":
            anchors = [1, 2, 10, total, MAX_VALUE]
            anchors.extend(numbers[-1] + delta for delta in (-1, 0, 1))
            values = repeat_shuffled(anchors, rng)
        elif mode == "prefix":
            anchors = []
            prefix = 0
            for number in numbers:
                prefix += number
                for delta in (-1, 0, 1):
                    if 1 <= prefix + delta <= MAX_VALUE:
                        anchors.append(prefix + delta)
                    if 1 <= total - prefix + delta <= MAX_VALUE:
                        anchors.append(total - prefix + delta)
            values = repeat_shuffled(anchors, rng)
        else:
            raise ValueError("unknown mode: " + mode)

    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
