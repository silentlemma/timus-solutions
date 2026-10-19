from math import isqrt

SMALL = 50  # small primes: walk the whole sequence
FIVE = 5
QUAD = 4  # the discriminant of a y^2 + b y + c is b^2 - 4 a c


def sqrt_mod(a, p):
    # a square root of a modulo an odd prime p, or None (Tonelli-Shanks)
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r


def mul(u, v, p):
    # (a t + b)(c t + d) with t^2 = t + 1
    a, b = u
    c, d = v
    return ((a * c + a * d + b * c) % p, (a * c + b * d) % p)


def walk(p, x):
    # the pairs (F(k), F(k + 1)) repeat with a period of at most 4p + 4
    found, a, b = set(), 0, 1
    while True:
        if a == x:
            found.add(b)
        a, b = b, (a + b) % p
        if (a, b) == (0, 1):
            return found


def main():
    p, x = map(int, input().split())
    if p <= SMALL:
        found = walk(p, x)
    else:
        # t^k = F(k) t + F(k - 1) in F_p[t] / (t^2 - t - 1), and Cassini's
        # identity F(k + 1)^2 - F(k + 1) F(k) - F(k)^2 = (-1)^k limits y = F(k + 1)
        # to the roots of y^2 - x y - x^2 - s = 0, s = 1 or -1
        candidates = set()
        half = (p + 1) // 2
        for s in (1, -1):
            root = sqrt_mod(x * x + QUAD * (x * x + s), p)
            if root is not None:
                candidates.update({(x + root) * half % p, (x - root) * half % p})
        # a pair is a power of t when the discrete logarithm exists: baby steps
        # t^j, giant steps by t^-m; the period divides p - 1 or 2 (p + 1)
        bound = p - 1 if p % FIVE in (1, FIVE - 1) else 2 * (p + 1)
        m = isqrt(bound) + 1
        baby, e = {}, (0, 1)
        for j in range(m):
            baby.setdefault(e, j)
            e = mul(e, (1, 0), p)
        back, inverse, power = (0, 1), (1, p - 1), m  # t^-m = (t - 1)^m
        while power:
            if power & 1:
                back = mul(back, inverse, p)
            inverse = mul(inverse, inverse, p)
            power >>= 1
        found = set()
        for y in candidates:
            e = (x, (y - x) % p)
            for _ in range(m + 1):
                if e in baby:
                    found.add(y)
                    break
                e = mul(e, back, p)
    if not found:
        print(0)
    else:
        print(len(found))
        print(*sorted(found))


main()
