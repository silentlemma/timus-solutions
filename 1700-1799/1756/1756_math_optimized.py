import sys


def main():
    m, first_days, days = map(int, sys.stdin.buffer.read().split())
    # the work is m * first_days digger-days; spreading it as evenly as possible
    # over the given days needs the fewest diggers, the rounded-up average
    low, extra = divmod(m * first_days, days)
    # each of the two constant runs is formatted once, without per-day integers or strings.
    text = (str(low) + " ") * (days - extra) + (str(low + 1) + " ") * extra
    sys.stdout.write(text[:-1] + "\n")


main()
