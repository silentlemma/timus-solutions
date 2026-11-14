HOUR = 60
HALF_DAY = 12 * HOUR
DAY = 2 * HALF_DAY
MINUTES_START = 3


def minutes(clock):
    return int(clock[:2]) * HOUR + int(clock[MINUTES_START:])


def main():
    out1, in1 = map(minutes, input().split())
    out2, in2 = map(minutes, input().split())
    # The difference is within ten minutes of twice the time-zone shift.
    difference = (in1 - out1 - in2 + out2 + HALF_DAY) % DAY - HALF_DAY
    print((abs(difference) + HOUR) // (2 * HOUR))


if __name__ == "__main__":
    main()
