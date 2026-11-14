import sys


WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTH_START = {"September": 0, "October": 30, "November": 61, "December": 91}


def main():
    weekday, month, day, lower, upper = sys.stdin.read().split()
    minimum, maximum = int(lower), int(upper)
    week = len(WEEKDAYS)
    first = WEEKDAYS.index(weekday) + 1
    days = WEEKDAYS[first:] + WEEKDAYS[:first]
    full, extra = divmod(MONTH_START[month] + int(day) - 2, week)
    for count in range(1, week + 1):
        # A chosen weekday contributes one extra session if its index is below extra.
        fewest = max(0, count - (week - extra), minimum - count * full)
        if fewest <= min(count, extra, maximum - count * full):
            print(count, *days[:fewest], *days[extra : extra + count - fewest], sep="\n")
            return
    print("Impossible")


if __name__ == "__main__":
    main()
