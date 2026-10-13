import sys

HALF = 3
TICKETS = 10**6


def lucky(number):
    digits = "%06d" % number
    return sum(map(int, digits[:HALF])) == sum(map(int, digits[HALF:]))


def main():
    number = int(sys.stdin.read())
    # the sums differ by one, so the ticket is neither 000000 nor 999999
    # and both neighbours are six-digit tickets
    neighbours = [n for n in (number - 1, number + 1) if 0 <= n < TICKETS]
    print("Yes" if any(lucky(n) for n in neighbours) else "No")


main()
