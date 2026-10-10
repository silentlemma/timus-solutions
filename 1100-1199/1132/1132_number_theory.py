import sys


def sqrt_mod(a, p, z):
    # Tonelli-Shanks for an odd prime p = q * 2^s + 1, a quadratic residue a
    # and a non-residue z
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    c, t, r = pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        # the order of t is 2^i with i < s; b fixes the top bits
        i, tt = 0, t
        while tt != 1:
            tt = tt * tt % p
            i += 1
        b = pow(c, 1 << (s - i - 1), p)
        s, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    non_residue = {}
    out = []
    for j in range(k):
        a, p = int(data[2 * j + 1]), int(data[2 * j + 2])
        a %= p
        if p == 2:
            out.append("1")
            continue
        half = (p - 1) // 2
        if pow(a, half, p) != 1:
            out.append("No root")
            continue
        if p not in non_residue:
            z = 2
            while pow(z, half, p) != p - 1:
                z += 1
            non_residue[p] = z
        r = sqrt_mod(a, p, non_residue[p])
        out.append("%d %d" % (min(r, p - r), max(r, p - r)))
    sys.stdout.write("\n".join(out) + "\n")


main()
