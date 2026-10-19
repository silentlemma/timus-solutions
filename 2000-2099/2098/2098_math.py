PERCENT = 100


def main():
    b = int(input())
    c, d = map(int, input().split())
    k, p = map(int, input().split())
    # the usual insurance for the next k years; registering the accident costs
    # p percent of it on top, paying cash costs b on top
    usual = k * c + d * k * (k + 1) // 2
    # both sides times 100, so everything stays in integers
    gap = usual * p - b * PERCENT
    print("Cash" if gap > 0 else "Insurance")
    cents = abs(gap)
    print("%d.%02d" % (cents // PERCENT, cents % PERCENT))


main()
