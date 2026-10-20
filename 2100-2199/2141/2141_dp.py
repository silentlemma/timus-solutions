import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    # plus and minus are the best sums of segments ending at the current dish
    # whose last dish counts with a plus or with a minus; before the second
    # dish no minus segment exists, and 0 there only means "start anew"
    plus, minus = values[0], 0
    best = max(0, plus)
    for a in values[1:]:
        plus, minus = a + max(0, minus), plus - a
        best = max(best, plus, minus)
    print(best)


main()
