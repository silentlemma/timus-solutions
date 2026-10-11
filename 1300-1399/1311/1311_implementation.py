import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 1
    # the layer above: ends of each brick, the weight it carries (lengths)
    # and twice the moment of that weight about 0, R^2 - L^2 per brick
    up_left, up_right, up_weight, up_moment = [], [], [], []
    for _ in range(data[0]):
        k = data[pos]
        left = data[pos + 1 : pos + 1 + 2 * k : 2]
        right = data[pos + 2 : pos + 2 + 2 * k : 2]
        pos += 1 + 2 * k
        weight = [b - a for a, b in zip(left, right)]
        moment = [b * b - a * a for a, b in zip(left, right)]
        # each brick above rests on the one brick below that it overlaps, and
        # the centre of all it carries must lie strictly inside the overlap, a test
        # that the doubled moment keeps in whole numbers
        j = 0
        for a in range(len(up_left)):
            a_left, a_right = up_left[a], up_right[a]
            while j < k and right[j] <= a_left:
                j += 1
            if j == k or left[j] >= a_right:
                print("No")
                return
            lo, hi = max(a_left, left[j]), min(a_right, right[j])
            w, m = up_weight[a], up_moment[a]
            if not 2 * lo * w < m < 2 * hi * w:
                print("No")
                return
            weight[j] += w
            moment[j] += m
        up_left, up_right, up_weight, up_moment = left, right, weight, moment
    print("Yes")


main()
