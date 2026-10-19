import sys

GRAVITY_NUMERATOR = 49
GRAVITY_DENOMINATOR = 5
POINT_COUNT = 3


def can_reach(speed, dx, dy):
    threshold = GRAVITY_DENOMINATOR * speed * speed - GRAVITY_NUMERATOR * dy
    return threshold >= 0 and threshold * threshold >= GRAVITY_NUMERATOR**2 * (dx * dx + dy * dy)


def solve(speed, head, left, right):
    def jump(start, target):
        return can_reach(speed, target[0] - start[0], target[1] - start[1])

    return jump(left, right) and jump(right, left) and (jump(left, head) or jump(right, head))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    speed = next(tokens)
    points = [(next(tokens), next(tokens)) for _ in range(POINT_COUNT)]
    print("Yes" if solve(speed, *points) else "No")
