import sys
from array import array


def main():
    numbers = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(numbers)
    # the pocket is a stack: roll the balls in order, and whenever the top
    # one is the next ball the inspector took out, take it out
    # each ball is checked as it is read, so their order is never stored
    pocket = array("I", [0]) * n
    top, upcoming = 0, 1
    for ball in numbers:
        while upcoming <= ball:
            pocket[top] = upcoming
            top += 1
            upcoming += 1
        if top == 0 or pocket[top - 1] != ball:
            print("Cheater")
            return
        top -= 1
    print("Not a proof")


main()
