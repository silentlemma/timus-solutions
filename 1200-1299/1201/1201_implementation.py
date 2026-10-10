NAMES = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK = 7
YEAR = 365
LEAP = 4
CENTURY = 100
ERA = 400
CELL = 5


def leap(y):
    return y % LEAP == 0 and (y % CENTURY != 0 or y % ERA == 0)


def main():
    d, m, y = map(int, input().split())
    lengths = MONTH[:]
    lengths[1] += leap(y)
    # days from 1 January of year 1, a Monday, to the first of the month
    past = y - 1
    before = YEAR * past + past // LEAP - past // CENTURY + past // ERA
    first = (before + sum(lengths[: m - 1])) % WEEK
    days = lengths[m - 1]
    cols = (first + days + WEEK - 1) // WEEK
    for row, name in enumerate(NAMES):
        line = name
        for col in range(cols):
            day = col * WEEK + row - first + 1
            last = col == cols - 1
            # every column is five characters wide, the last one four,
            # unless the bracketed date sits in it
            if day == d:
                line += " [%2d]" % day
            elif 1 <= day <= days:
                line += "  %2d" % day + ("" if last else " ")
            else:
                line += " " * (CELL - last)
        print(line)


main()
