import sys
from array import array
from bisect import bisect_left, bisect_right
from math import gcd


def minimum(start, moves, n, floor):
    size = len(moves)
    remaining = [0] * (size + 1)
    excess = [0] * (size + 1)
    largest = 0
    for i in range(size - 1, -1, -1):
        remaining[i] = remaining[i + 1] + moves[i]
        largest = max(largest, moves[i])
        excess[i] = 2 * largest - remaining[i]
    best = n + 1

    def walk(i, total, left, right):
        nonlocal best
        if best == floor or start[left] + total - remaining[i] >= best:
            return
        # If subtracting the largest remaining move must end below zero,
        # that move must be added, giving a stronger lower bound.
        if start[right] + total < excess[i] and start[left] + total + excess[i] >= best:
            return
        if i == size:
            best = start[left] + total
            return
        d = moves[i]
        down = total - d
        first = left
        if start[first] + down < 0:
            first = bisect_left(start, -down, left, right + 1)
        if first <= right:
            walk(i + 1, down, first, right)
        up = total + d
        last = right
        if start[last] + up > n:
            last = bisect_right(start, n - up, left, right + 1) - 1
        if left <= last:
            walk(i + 1, up, left, last)

    walk(0, 0, 0, len(start) - 1)
    return best


def main():
    n, s, k, *moves = map(int, sys.stdin.buffer.read().split())
    moves = moves[:k]
    total = sum(moves)
    if total <= min(s, n - s):
        print(s - total, s + total)
        return
    step = 0
    for d in moves:
        step = gcd(step, d)
    modulus = 2 * step
    half = k // 2
    start = array('i', [s])
    # Merge the two shifted sorted sequences, keeping each depth once.
    for d in moves[:half]:
        size = len(start)
        left = bisect_left(start, d)
        right = 0
        end = bisect_right(start, n - d)
        reach = array('i')
        while left < size and right < end:
            down = start[left] - d
            up = start[right] + d
            if down < up:
                reach.append(down)
                left += 1
            elif up < down:
                reach.append(up)
                right += 1
            else:
                reach.append(down)
                left += 1
                right += 1
        reach.extend(start[i] - d for i in range(left, size))
        reach.extend(start[i] + d for i in range(right, end))
        start = reach
    rest = moves[half:]
    low = minimum(start, rest, n, (s + total) % modulus)
    if 2 * s == n:
        print(low, n - low)
        return
    # Reflecting every depth exchanges the minimum and maximum answers.
    start = array('i', (n - x for x in reversed(start)))
    high = n - minimum(start, rest, n, (n - s + total) % modulus)
    print(low, high)


main()
