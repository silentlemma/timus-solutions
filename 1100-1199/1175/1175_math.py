import sys


def main():
    a1, a2, a3, a4, b1, b2, c, x1, x2 = map(int, sys.stdin.read().split())

    def step(x, y):
        h = a1 * x * y + a2 * x + a3 * y + a4
        if h > b1 and h > b2 and c > 0:
            h -= (h - b2 + c - 1) // c * c
        return y, h

    # the next term depends only on the last two, so the pairs of
    # neighbouring terms run into a cycle; Brent's method finds it in O(1)
    # memory: the length first, then where it starts
    power = length = 1
    slow, fast = (x1, x2), step(x1, x2)
    while slow != fast:
        if power == length:
            slow, power, length = fast, power * 2, 0
        fast = step(*fast)
        length += 1
    slow = fast = (x1, x2)
    for _ in range(length):
        fast = step(*fast)
    start = 1
    while slow != fast:
        slow, fast = step(*slow), step(*fast)
        start += 1
    print(start, length)


main()
