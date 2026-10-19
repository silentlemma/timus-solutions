"""Count year types by one complete Gregorian calendar cycle."""

import sys

CYCLE = 400
CENTURY = 100
LEAP_STEP = 4
WEEK = 7
FRIDAY = 4
TARGET_DAY = 13
MONTHS = 12
BUCKETS = MONTHS + 1
MONTH_LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def calendar_types():
    weekday = 0
    types = []
    for year in range(1, CYCLE + 1):
        leap = year % CYCLE == 0 or (year % LEAP_STEP == 0 and year % CENTURY != 0)
        count = 0
        for month, days in enumerate(MONTH_LENGTHS):
            count += (weekday + TARGET_DAY - 1) % WEEK == FRIDAY
            weekday = (weekday + days + (month == 1 and leap)) % WEEK
        types.append(count)
    return types


def prefix(year, types, cycle_counts):
    cycles, remainder = divmod(year, CYCLE)
    answer = [cycles * value for value in cycle_counts]
    for count in types[:remainder]:
        answer[count] += 1
    return answer


def solve(first, last, types, cycle_counts):
    high = prefix(last, types, cycle_counts)
    low = prefix(first - 1, types, cycle_counts)
    return [a - b for a, b in zip(high, low)]


def main():
    first, last = map(int, sys.stdin.buffer.read().split())
    types = calendar_types()
    cycle_counts = [types.count(k) for k in range(BUCKETS)]
    for k, count in enumerate(solve(first, last, types, cycle_counts)):
        print(f"{k}: {count}")


if __name__ == "__main__":
    main()
