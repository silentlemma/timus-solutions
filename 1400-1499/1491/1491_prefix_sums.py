import sys

FIELDS = 3  # a, b and c


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # every gift adds c to the knights a..b: mark it at both ends of the
    # range, then a running sum gives each knight's total
    diff = [0] * (n + 2)
    words = data[1:]
    for k in range(n + 1):
        a, b, c = (int(w) for w in words[FIELDS * k : FIELDS * (k + 1)])
        diff[a] += c
        diff[b + 1] -= c
    out = []
    total = 0
    for i in range(1, n + 1):
        total += diff[i]
        out.append(total)
    print(" ".join(map(str, out)))


main()
