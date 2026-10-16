import sys

# counts are capped here: two ways already make the answer ambiguous
MANY = 2


def main():
    k, x = sys.stdin.read().split()
    n = len(k)
    # the Gray code of k has digit x(i) = k(i) xor k(i - 1), with a 0 before
    # the first digit; ways0[i] and ways1[i] count the readings of the first
    # i + 1 digits that end with k(i) = 0 or 1
    ways0 = [0] * n
    ways1 = [0] * n
    w0, w1 = 1, 0
    for i in range(n):
        x0, x1 = x[i] != "1", x[i] != "0"
        new0 = min(MANY, (w0 if x0 else 0) + (w1 if x1 else 0)) if k[i] != "1" else 0
        new1 = min(MANY, (w0 if x1 else 0) + (w1 if x0 else 0)) if k[i] != "0" else 0
        w0, w1 = new0, new1
        ways0[i], ways1[i] = w0, w1
    if w0 + w1 == 0:
        print("Impossible")
        return
    if w0 + w1 > 1:
        print("Ambiguity")
        return
    # walk back along the single reading: exactly one earlier digit of k
    # with a reading of its own leads on to the next one
    bits = [0] * n
    bits[-1] = 1 if w1 else 0
    for i in range(n - 1, 0, -1):
        cur = bits[i]
        for prev, ways in ((0, ways0[i - 1]), (1, ways1[i - 1])):
            if ways and x[i] != str(1 - (prev ^ cur)):
                bits[i - 1] = prev
    print("".join(map(str, bits)))
    print("".join(str(a ^ b) for a, b in zip([0] + bits, bits)))


main()
