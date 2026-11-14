import sys
from array import array
from itertools import islice

HOURS = 12
MINUTE = 60
HOUR = MINUTE * MINUTE
DIAL = HOURS * HOUR


def choose(clocks, count):
    frequency = array("H", [0]) * DIAL
    for clock in clocks:
        hour, minute, second = map(int, clock.split(b":"))
        frequency[(hour % HOURS) * HOUR + minute * MINUTE + second] += 1

    later = count
    best_cost = count * DIAL
    best_time = 0
    for target, at_target in enumerate(frequency):
        if at_target:
            later -= at_target
            # The sum of the initial readings is independent of the target.
            cost = count * target + DIAL * later
            if cost < best_cost:
                best_cost, best_time = cost, target
    return best_time


def main():
    stream = sys.stdin.buffer
    count = int(stream.readline())
    hour, rest = divmod(choose(islice(stream, count), count), HOUR)
    minute, second = divmod(rest, MINUTE)
    print(f"{hour or HOURS}:{minute:02d}:{second:02d}")


if __name__ == "__main__":
    main()
