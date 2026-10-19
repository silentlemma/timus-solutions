import sys

GOALS = 3
MODULUS = 1000000007


def count_forecasts(size):
    total = GOALS * size * (size - 1) // 2
    maximum = GOALS * (size - 1)
    current = [[0] * (maximum + 1)]
    current[0][0] = 1
    lower = 0
    for used in range(size):
        next_used = used + 1
        next_lower = GOALS * next_used * used // 2
        next_upper = total * next_used // size
        following = [[0] * (maximum + 1) for _ in range(next_upper - next_lower + 1)]
        for offset, row in enumerate(current):
            partial = lower + offset
            minimum_last = (partial + used - 1) // used if used else 0
            first = max(0, next_lower - partial, minimum_last)
            last = min(
                maximum, next_upper - partial, (total - partial) // (size - used)
            )
            if first > last:
                continue
            prefix = sum(row[:first])
            for value in range(first, last + 1):
                prefix += row[value]
                if prefix:
                    following[partial + value - next_lower][value] = prefix % MODULUS
        current = following
        lower = next_lower
    return sum(current[0]) % MODULUS


if __name__ == "__main__":
    print(count_forecasts(int(sys.stdin.buffer.read())))
