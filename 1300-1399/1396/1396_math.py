import sys

BITS = 61  # every n is below 2^60, and a lowered bit leaves at most 60 free ones


def step(x, y, bit):
    """(a_m, a_m+1) -> (a_2m+bit, a_2m+bit+1)."""
    return (x, x + y) if bit == 0 else (x + y, y)


def endings(r):
    """Suffixes of r free bits among which the largest value always lies:
    alternating bits, with the last one or two bits changed."""
    out = set()
    for first in (0, 1):
        alt = [(first + k) % 2 for k in range(r)]
        out.add(tuple(alt))
        if r >= 1:
            out.add(tuple(alt[:-1] + [1]))
        if r >= 2:
            out.add(tuple(alt[:-2] + [1, 1]))
            out.add(tuple(alt[:-2] + [0, 1]))
    return out


def main():
    # maps[r]: (p, q) with a = p a_m + q a_m+1 after each candidate suffix of r bits
    maps = []
    for r in range(BITS):
        pairs = []
        for bits in endings(r):
            p, q = (1, 0), (0, 1)
            for b in bits:
                p, q = step(*p, b), step(*q, b)
            pairs.append((p[0], q[0]))
        maps.append(pairs)
    out = []
    for token in sys.stdin.read().split():
        n = int(token)
        if n == 0:
            break
        length = n.bit_length()
        best, x, y = 0, 0, 1  # (a_0, a_1) for the empty prefix
        for k in range(length - 1, -1, -1):
            bit = n >> k & 1
            if bit:
                # lower this bit to 0: the k bits below are free
                lx, ly = step(x, y, 0)
                best = max(best, max(p * lx + q * ly for p, q in maps[k]))
            x, y = step(x, y, bit)
        out.append(str(max(best, x)))
    print("\n".join(out))


main()
