import sys

# inputs are at most this
LARGEST = 10


def main():
    # a(n) counts weak orders of n objects: the k objects tied for the
    # smallest place are any k of them, followed by a weak order of the rest
    a = [1] + [0] * LARGEST
    binom = [[1] * (n + 1) for n in range(LARGEST + 1)]
    for n in range(2, LARGEST + 1):
        for k in range(1, n):
            binom[n][k] = binom[n - 1][k - 1] + binom[n - 1][k]
    for n in range(1, LARGEST + 1):
        a[n] = sum(binom[n][k] * a[n - k] for k in range(1, n + 1))
    out = []
    for token in sys.stdin.read().split():
        n = int(token)
        if n < 0:
            break
        out.append(str(a[n]))
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
