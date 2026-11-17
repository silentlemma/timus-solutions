import sys


def subset_sums(weights):
    sums = [0]
    for weight in weights:
        sums += [value + weight for value in sums]
    sums.sort()
    return sums


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    weights = values[1:]
    total = sum(weights)
    left = subset_sums(weights[: n // 2])
    right = subset_sums(weights[n // 2 :])
    best = total
    i, j = 0, len(right) - 1
    while i < len(left) and j >= 0:
        difference = total - 2 * (left[i] + right[j])
        best = min(best, abs(difference))
        if best == total % 2:
            break
        if difference > 0:
            i += 1
        else:
            j -= 1
    print(best)


main()
