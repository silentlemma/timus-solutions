import sys
from itertools import islice


def main():
    stream = sys.stdin.buffer
    n = int(stream.readline())
    # the Boyer-Moore vote: a value met more often than all the others together
    # survives pairing every note with a different one
    leader = lead = 0
    # every line holds one value, so each of the n lines is converted as it is
    for value in map(int, islice(stream, n)):
        if lead == 0:
            leader, lead = value, 1
        elif value == leader:
            lead += 1
        else:
            lead -= 1
    print(leader)


main()
