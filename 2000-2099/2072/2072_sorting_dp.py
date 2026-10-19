import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    dryness = list(map(int, data[1:n + 1]))
    order = sorted(range(n), key=lambda i: (dryness[i], i))
    # a group of equal dryness is a segment of positions, watered by walking it once.
    # The walk ends at its left or right end, and those two states carry over
    at_left = at_right = 0
    left = right = 0  # the previous group, starting from the leftmost flower
    i = 0
    while i < n:
        j = i
        while j < n and dryness[order[j]] == dryness[order[i]]:
            j += 1
        lo, hi = order[i], order[j - 1]
        width = hi - lo
        to_left = min(at_left + abs(left - hi), at_right + abs(right - hi)) + width
        to_right = min(at_left + abs(left - lo), at_right + abs(right - lo)) + width
        at_left, at_right, left, right = to_left, to_right, lo, hi
        i = j
    print(min(at_left, at_right) + n)


main()
