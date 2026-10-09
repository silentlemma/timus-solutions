def main():
    tok = input().split()
    n, a = int(tok[0]), float(tok[1])
    # with the second height x, lamp i hangs at a + (i-1)(x - a) + (i-1)(i-2)
    # and the last height grows with x, so x is the smallest value keeping every
    # lamp at height 0 or above
    x = max(a - a / k - (k - 1) for k in range(1, n))
    print("%.2f" % (a + (n - 1) * (x - a) + (n - 1) * (n - 2)))


main()
