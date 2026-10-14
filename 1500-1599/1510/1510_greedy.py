import sys


def main():
    stream = sys.stdin.buffer
    n = int(stream.readline())
    # Boyer-Moore vote: a value met more often than all the others together
    # survives pairing every note with a different one
    leader, lead = 0, 0
    seen = 0
    for line in stream:
        for token in line.split():
            value = int(token)
            if lead == 0:
                leader, lead = value, 1
            elif value == leader:
                lead += 1
            else:
                lead -= 1
            seen += 1
        if seen == n:
            break
    print(leader)


main()
