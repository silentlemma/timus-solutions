def main():
    n = int(input())
    # The Catalan numbers: every leading square of their Hankel matrix has
    # determinant 1. C(k + 1) = C(k) * 2 (2k + 1) / (k + 2), always exact.
    out, c = [], 1
    for k in range(2 * n - 1):
        out.append(c)
        c = c * 2 * (2 * k + 1) // (k + 2)
    print("\n".join(map(str, out)))


main()
