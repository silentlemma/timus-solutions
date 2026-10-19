import sys


def rank(pages):
    # page i open is bit i - 1 of a Gray code word: F1 flips bit 0, the other
    # move flips the bit above the lowest set one; these are the reflected Gray
    # code steps, so the states form one path ordered by the decoded word
    gray = int(pages[::-1], 2)
    place = 0
    while gray:
        place ^= gray
        gray >>= 1
    return place


def main():
    _, start, goal = sys.stdin.read().split()
    print(abs(rank(start) - rank(goal)))


main()
