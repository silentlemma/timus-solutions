import sys

LARGEST = 10000
BLOCK = 100  # exact factorials are kept at every BLOCK-th n


def main():
    # g(n) = n by induction, so f(n) = 1 + sum of i f(i) = n f(n - 1) = n!
    exact = [1]
    value = 1
    for i in range(1, LARGEST + 1):
        value *= i
        if i % BLOCK == 0:
            exact.append(value)
    data = sys.stdin.read().split()
    out = []
    for n, p in zip(map(int, data[0::2]), map(int, data[1::2])):
        if n == 0 and p == 0:
            break
        if n >= p:
            out.append(0)  # p itself is a factor of n!
            continue
        start = n // BLOCK * BLOCK
        r = exact[n // BLOCK] % p
        for i in range(start + 1, n + 1):
            r = r * i % p
        out.append(r)
    print("\n".join(map(str, out)))


main()
