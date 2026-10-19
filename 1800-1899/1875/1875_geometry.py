import sys

MONKEYS = 5


def main():
    v = list(map(int, sys.stdin.read().split()))
    xs, ys = v[0::2], v[1::2]
    full = (1 << MONKEYS) - 1

    def one_shot(i, j, k):
        # y / x = b - c x along a shot, so the slopes y / x of points on one
        # shot lie on a line in x; compared with all fractions cleared
        left = (ys[k] * xs[i] - ys[i] * xs[k]) * xs[j] * (xs[j] - xs[i])
        right = (ys[j] * xs[i] - ys[i] * xs[j]) * xs[k] * (xs[k] - xs[i])
        return left == right

    shots = [1 << i for i in range(MONKEYS)]
    for i in range(MONKEYS):
        for j in range(MONKEYS):
            # gravity bends the path down: the slope y / x must fall as x grows
            if xs[i] < xs[j] and ys[i] * xs[j] > ys[j] * xs[i]:
                shots.append(sum(1 << k for k in range(MONKEYS) if one_shot(i, j, k)))
    need = [0] + [MONKEYS] * full
    for mask in range(full + 1):
        for shot in shots:
            need[mask | shot] = min(need[mask | shot], need[mask] + 1)
    print(need[full])


main()
