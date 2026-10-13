"""One test from a seed: a random ticket whose halves differ by one."""

import random
import sys

TICKETS = 10**6
HALF = 3


def main():
    rng = random.Random(int(sys.argv[1]))
    while True:
        ticket = "%06d" % rng.randrange(TICKETS)
        left, right = sum(map(int, ticket[:HALF])), sum(map(int, ticket[HALF:]))
        if abs(left - right) == 1:
            print(ticket)
            return


main()
