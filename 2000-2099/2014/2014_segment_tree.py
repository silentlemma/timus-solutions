import sys

DAY_SLOTS = 32
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60


def solve(keys, amounts):
    ranks = [0] * len(keys)
    for position, event in enumerate(sorted(range(len(keys)), key=keys.__getitem__)):
        ranks[event] = position
    size = 1
    while size < len(keys):
        size <<= 1
    sums = [0] * (2 * size)
    prefixes = [0] * (2 * size)
    result = []
    for rank, amount in zip(ranks, amounts):
        index = size + rank
        sums[index] = amount
        prefixes[index] = amount if amount < 0 else 0
        index >>= 1
        while index:
            left = index << 1
            right = left + 1
            left_sum = sums[left]
            sums[index] = left_sum + sums[right]
            cross = left_sum + prefixes[right]
            first = prefixes[left]
            prefixes[index] = first if first < cross else cross
            index >>= 1
        result.append(prefixes[1])
    return result


def read_case(stream):
    n = int(stream.readline())
    keys, amounts = [], []
    for _ in range(n):
        amount, date, time = stream.readline().split()
        day, month = map(int, date.split(b"."))
        hour, minute = map(int, time.split(b":"))
        keys.append(((month * DAY_SLOTS + day) * HOURS_PER_DAY + hour) * MINUTES_PER_HOUR + minute)
        amounts.append(int(amount))
    return keys, amounts


if __name__ == "__main__":
    keys, amounts = read_case(sys.stdin.buffer)
    print("\n".join(map(str, solve(keys, amounts))))
