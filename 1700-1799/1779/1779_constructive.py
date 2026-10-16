def main():
    n = int(input())
    # joining i and j whenever i + j > n gives student i a degree of i up to
    # the middle and i - 1 after it, so only one degree is shared, by two
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1) if i + j > n]
    lines = [str(len(pairs))] + ["%d %d" % p for p in pairs]
    print("\n".join(lines))


main()
