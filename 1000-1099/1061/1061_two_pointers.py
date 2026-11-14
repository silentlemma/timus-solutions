import sys

ZERO = ord("0")
MAX_DIGIT = 9


def first_cheapest(states, width):
    best_position = 0
    best_sum = (ZERO + MAX_DIGIT) * width + 1
    offset = 1
    for run in states.split(b"*"):
        if len(run) >= width:
            window_sum = sum(run[:width])
            if window_sum < best_sum:
                best_position, best_sum = offset, window_sum
            for position, (old, new) in enumerate(zip(run, memoryview(run)[width:]), offset + 1):
                window_sum += new - old
                if window_sum < best_sum:
                    best_position, best_sum = position, window_sum
            if best_sum == ZERO * width:
                break
        offset += len(run) + 1
    return best_position


def main():
    stream = sys.stdin.buffer
    count, width = map(int, stream.readline().split())
    if width > count:
        print(0)
        return
    states = b"".join(stream.read().split())
    print(first_cheapest(states, width))


if __name__ == "__main__":
    main()
