import sys

PER_METRE = 9
LANE_TIME = 72
CAR_LENGTH = 5
UNITS_PER_SECOND = 50
INTERVAL_WIDTH = LANE_TIME + PER_METRE * CAR_LENGTH


def earliest_start(near, far):
    wait = i = j = 0
    while i < len(near) or j < len(far):
        if j == len(far) or i < len(near) and near[i] <= far[j]:
            start = near[i]
            i += 1
        else:
            start = far[j]
            j += 1
        if start >= wait:
            break
        wait = max(wait, start + INTERVAL_WIDTH)
    return wait


def main():
    words = iter(map(int, sys.stdin.buffer.read().split()))
    near = [PER_METRE * next(words) - LANE_TIME for _ in range(next(words))]
    far = [PER_METRE * next(words) - 2 * LANE_TIME for _ in range(next(words))]
    print(f"{earliest_start(near, far) / UNITS_PER_SECOND:.6f}")


if __name__ == "__main__":
    main()
