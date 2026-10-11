def main():
    n, a, b = map(int, input().split())
    # each panel has two sides of A * B square metres
    print(2 * n * a * b)


main()
