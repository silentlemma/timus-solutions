def main():
    n, m = map(int, input().split())
    # every full lap turns four times and peels two rows and two columns; the
    # spiral ends in the middle of the shorter side, so only that side counts
    print(2 * (n - 1) if n <= m else 2 * m - 1)


main()
