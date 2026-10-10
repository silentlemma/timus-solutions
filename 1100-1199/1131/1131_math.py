def main():
    n, k = map(int, input().split())
    # as long as fewer computers than cables have the program, each hour doubles
    # the count; after that k computers get it each hour
    have, hours = 1, 0
    while have < n and have < k:
        have *= 2
        hours += 1
    if have < n:
        hours += -(-(n - have) // k)
    print(hours)


main()
