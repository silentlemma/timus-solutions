def main():
    m, d1, d2 = (int(v) for v in input().split())
    # the work is m * d1 digger-days; spreading it as evenly as possible
    # over d2 days needs the fewest diggers, the rounded-up average
    work = m * d1
    low, extra = divmod(work, d2)
    days = [low] * (d2 - extra) + [low + 1] * extra
    print(" ".join(map(str, days)))


main()
