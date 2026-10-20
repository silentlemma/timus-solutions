import bisect
import sys

MAX_GEOMETRIC = 30
SEED_LIMIT = MAX_GEOMETRIC + 2
MAJORITY_SIZE = 2 * (2 * MAX_GEOMETRIC + 1)


def is_arithmetic(values):
    return len(values) <= 2 or all(
        values[i] - values[i - 1] == values[1] - values[0] for i in range(2, len(values))
    )


def is_geometric(values):
    if not values:
        return False
    if values[0] == 0:
        return values[-1] == 0
    return all(values[i] * values[0] == values[i - 1] * values[1] for i in range(2, len(values)))


def extract(values, start, step):
    arithmetic = []
    geometric = []
    expected = start
    for value in values:
        if value == expected:
            arithmetic.append(value)
            expected += step
        else:
            geometric.append(value)
            if len(geometric) > MAX_GEOMETRIC:
                return None
    # Three distinct geometric terms cannot form an arithmetic progression.
    for removed in range(2 + 1):
        if arithmetic and is_geometric(geometric):
            return arithmetic, geometric
        if removed == 2 or len(arithmetic) <= 1:
            break
        bisect.insort(geometric, arithmetic.pop())
    return None


def solve(values):
    values.sort()
    distinct = []
    repeated = []
    for i, value in enumerate(values):
        if i == 0 or value != values[i - 1]:
            distinct.append(value)
        elif i == 1 or value != values[i - 2]:
            repeated.append(value)
    if len(distinct) == 1:
        return values[:1], values[1:]
    if len(distinct) == 2:
        cut = bisect.bisect_right(values, values[0])
        return values[:cut], values[cut:]
    if len(repeated) == 1:
        constant = repeated[0]
        copies = values.count(constant)
        other = [value for value in values if value != constant]
        for moved in range(2):
            rest = other.copy()
            if moved:
                bisect.insort(rest, constant)
            equal = [constant] * (copies - moved)
            if is_geometric(rest):
                return equal, rest
            if is_arithmetic(rest):
                return rest, equal
    if len(values) <= MAX_GEOMETRIC + 1:
        for i, value in enumerate(values):
            rest = values[:i] + values[i + 1 :]
            if is_geometric(rest):
                return [value], rest
    if len(values) >= MAJORITY_SIZE:
        gaps = sorted(values[i] - values[i - 1] for i in range(1, len(values)))
        step = gaps[len(gaps) // 2]
        if step:
            for start in values[: MAX_GEOMETRIC + 1]:
                answer = extract(values, start, step)
                if answer is not None:
                    return answer
    else:
        limit = min(len(values), SEED_LIMIT)
        for i in range(limit):
            for j in range(i + 1, limit):
                step = values[j] - values[i]
                if step:
                    answer = extract(values, values[i], step)
                    if answer is not None:
                        return answer
    return None


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    answer = solve(data[1:])
    if answer is None:
        print(-1)
        return
    arithmetic, geometric = answer
    print(len(arithmetic))
    print(*arithmetic)
    print(*geometric)


if __name__ == "__main__":
    main()
