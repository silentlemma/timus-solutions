from sys import stdin, stdout


def prefix(label):
    half = label // 2
    cost = 2 * (half - half.bit_count())
    if label % 2 == 0:
        # At the last even label, only one of its two adjacent gaps is included.
        cost -= (label & -label).bit_length() - 2
    return cost


a, b = map(int, stdin.readline().split())
stdout.write(str(abs(prefix(a) - prefix(b))))
