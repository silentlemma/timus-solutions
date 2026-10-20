import sys


def solve():
    source = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(source)
    days = next(source)
    length = next(source)
    moves = next(source)
    positions = n - length + 1
    dp = [[0] * positions]
    previous_low = 0
    queue = [0] * positions

    for day in range(1, days + 1):
        prefix = [0]
        for _ in range(n):
            prefix.append(prefix[-1] + next(source))
        starts = prefix[:positions]
        ends = prefix[length:]
        weight = [ends[x] - starts[x] for x in range(positions)]
        # A move to the same position can pad an unused part of the budget.
        low = max(0, moves - (days - day))
        high = min(day, moves)
        following = []
        for used in range(low, high + 1):
            if used < day:
                stay = dp[used - previous_low]
                current = [stay[x] + weight[x] for x in range(positions)]
            else:
                current = [0] * positions
            if used:
                previous = dp[used - 1 - previous_low]
                key = [previous[x] - starts[x] for x in range(positions)]
                head = tail = 0
                best = 0
                for y in range(positions):
                    if y >= length:
                        x = y - length
                        candidate = previous[x] + weight[x]
                        if candidate > best:
                            best = candidate
                    while head < tail and key[queue[tail - 1]] <= key[y]:
                        tail -= 1
                    queue[tail] = y
                    tail += 1
                    if queue[head] <= y - length:
                        head += 1
                    candidate = key[queue[head]] + ends[y]
                    disjoint = best + weight[y]
                    if disjoint > candidate:
                        candidate = disjoint
                    if candidate > current[y]:
                        current[y] = candidate
                key = [previous[x] + ends[x] for x in range(positions)]
                head = tail = 0
                best = 0
                for y in range(positions - 1, -1, -1):
                    if y + length < positions:
                        x = y + length
                        candidate = previous[x] + weight[x]
                        if candidate > best:
                            best = candidate
                    while head < tail and key[queue[tail - 1]] <= key[y]:
                        tail -= 1
                    queue[tail] = y
                    tail += 1
                    if queue[head] >= y + length:
                        head += 1
                    candidate = key[queue[head]] - starts[y]
                    disjoint = best + weight[y]
                    if disjoint > candidate:
                        candidate = disjoint
                    if candidate > current[y]:
                        current[y] = candidate
            following.append(current)
        dp = following
        previous_low = low
    print(max(dp[0]))


if __name__ == "__main__":
    solve()
