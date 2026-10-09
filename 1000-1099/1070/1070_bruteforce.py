import sys

HOUR = 60
DAY = 24 * HOUR
LONGEST = 6 * HOUR
SPREAD = 10
MAX_SHIFT = 5


def minutes(s):
    h, m = s.split(".")
    return int(h) * HOUR + int(m)


def main():
    out1, in1, out2, in2 = map(minutes, sys.stdin.read().split())
    # when the second airport is k hours ahead, the real durations are the clock
    # differences minus and plus k hours, taken around the day
    for k in range(-MAX_SHIFT, MAX_SHIFT + 1):
        t1 = (in1 - out1 - k * HOUR) % DAY
        t2 = (in2 - out2 + k * HOUR) % DAY
        if t1 <= LONGEST and t2 <= LONGEST and abs(t1 - t2) <= SPREAD:
            print(abs(k))
            return


main()
