BASE = 10
ELEVEN = 11


def main():
    n = int(input())
    found = set()
    # strike digit d at place k from x = (a * 10 + d) * 10^k + b, b < 10^k:
    # then y = a * 10^k + b and x + y = (11a + d) * 10^k + 2b
    power = 1
    while power <= n:
        for carry in (0, 1):
            twice = n % power + carry * power
            if twice % 2 == 0 and twice // 2 < power:
                b = twice // 2
                a, d = divmod((n - twice) // power, ELEVEN)
                x = (a * BASE + d) * power + b
                # x has at least two digits and starts with a nonzero digit
                if d < BASE and x >= BASE and (a > 0 or d > 0):
                    found.add(x)
        power *= BASE
    print(len(found))
    for x in sorted(found):
        y = n - x
        print("%d + %0*d = %d" % (x, len(str(x)) - 1, y, n))


main()
