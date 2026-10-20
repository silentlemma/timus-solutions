import sys
from collections import deque


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    height = next(data)
    width = next(data)
    body_height = next(data)
    body_width = next(data)

    left_max = deque()
    right_max = deque()
    best = 0
    for row in range(height):
        left = next(data)
        right = next(data)
        while left_max and left_max[0][0] < row - body_height:
            left_max.popleft()
        while right_max and right_max[0][0] < row - body_height:
            right_max.popleft()
        while left_max and left_max[-1][1] <= left:
            left_max.pop()
        while right_max and right_max[-1][1] <= right:
            right_max.pop()
        left_max.append((row, left))
        right_max.append((row, right))
        # A downward move can touch body_height + 1 consecutive rows.
        best = max(best, left_max[0][1] + right_max[0][1])

    print(max(0, width - body_width + 1 - best))


if __name__ == "__main__":
    main()
