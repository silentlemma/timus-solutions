import sys

LETTERS = 100000


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    s = data[1:n + 1]
    m = data[n + 1]
    t = data[n + 2:n + 2 + m]
    # every position of t meets every position of the cyclic s exactly once,
    # so the distance is n m minus the number of equal pairs
    a, b = [0] * (LETTERS + 1), [0] * (LETTERS + 1)
    for c in s:
        a[c] += 1
    for c in t:
        b[c] += 1
    p, q = a[0], b[0]
    a[0] = b[0] = 0
    equal = sum(x * y for x, y in zip(a, b))
    # the gain is linear in the letters chosen for the question marks of one
    # string, so all of them take one letter: the same letter for both
    # strings, or the best letter for each
    same = max(p * y + q * x for x, y in zip(a, b)) + p * q
    apart = p * max(b) + q * max(a)
    print(n * m - equal - max(same, apart))


main()
