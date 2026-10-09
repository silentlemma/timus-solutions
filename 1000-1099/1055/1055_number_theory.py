def exponent(x, p):
    """The exponent of the prime p in x! (Legendre's formula)."""
    e = 0
    while x:
        x //= p
        e += x
    return e


def main():
    n, m = map(int, input().split())
    composite = bytearray(n + 1)
    count = 0
    for p in range(2, n + 1):
        if composite[p]:
            continue
        composite[p * p :: p] = bytes([True]) * len(range(p * p, n + 1, p))
        if exponent(n, p) - exponent(m, p) - exponent(n - m, p) > 0:
            count += 1
    print(count)


main()
