import sys


def main():
    words = sys.stdin.buffer.read().split()
    n, m = int(words[0]), int(words[1])
    numbers = iter(words[2:])
    # sums of i and of i^2 for i up to x
    linear, square = [0] * (n + 2), [0] * (n + 2)
    for i in range(1, n + 2):
        linear[i] = linear[i - 1] + i
        square[i] = square[i - 1] + i * i
    # toll t_i on segment i (cities i and i + 1) is the prefix sum of the
    # differences dif_j; the sum of i^k t_i over i <= x is
    # S_k(x) * (sum of dif_j) - (sum of dif_j * S_k(j - 1)) over j <= x
    size = n + 1
    plain = [0] * (size + 1)
    zero, one, two = plain[:], plain[:], plain[:]

    def add(j, d):
        w0, w1, w2 = d * (j - 1), d * linear[j - 1], d * square[j - 1]
        while j <= size:
            plain[j] += d
            zero[j] += w0
            one[j] += w1
            two[j] += w2
            j += j & -j

    def prefix(x):
        # the sums of t_i, i t_i and i^2 t_i over i <= x
        s, s0, s1, s2 = 0, 0, 0, 0
        j = x
        while j:
            s += plain[j]
            s0 += zero[j]
            s1 += one[j]
            s2 += two[j]
            j -= j & -j
        return x * s - s0, linear[x] * s - s1, square[x] * s - s2

    out = []
    for _ in range(m):
        kind, a, b = next(numbers), int(next(numbers)), int(next(numbers))
        if kind == b"change":
            d = int(next(numbers))
            add(a, d)
            add(b, -d)
            continue
        (h0, h1, h2), (l0, l1, l2) = prefix(b - 1), prefix(a - 1)
        # segment i lies on (i - a + 1)(b - i) of the guild's routes
        total = -(h2 - l2) + (a + b - 1) * (h1 - l1) + b * (1 - a) * (h0 - l0)
        routes = (b - a + 1) * (b - a) // 2
        out.append("%.8f" % (total / routes))
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
