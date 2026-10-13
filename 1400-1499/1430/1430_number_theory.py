def main():
    a, b, n = map(int, input().split())
    swapped = a < b
    if swapped:
        a, b = b, a
    # b items of price a can always become a items of price b, so x below b is enough,
    # with a >= b either b or n // a is at most sqrt(n)
    best = (-1, 0, 0)
    for x in range(min(n // a, b - 1) + 1):
        y = (n - x * a) // b
        if x * a + y * b > best[0]:
            best = (x * a + y * b, x, y)
            if best[0] == n:
                break
    _, x, y = best
    print(*((y, x) if swapped else (x, y)))


main()
