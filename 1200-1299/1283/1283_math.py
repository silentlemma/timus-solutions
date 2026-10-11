PERCENT = 100


def main():
    gold, limit, fee = map(int, input().split())
    # after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
    # compare gold * (100 - fee)^k with limit * 100^k in whole numbers
    left, right, years = gold, limit, 0
    while left > right:
        left *= PERCENT - fee
        right *= PERCENT
        years += 1
    print(years)


main()
