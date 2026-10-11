def main():
    n = int(input())
    # rows of the ages 1..k starting with 1: a(k) = a(k-1) + a(k-3) + 1,
    # with a(1) = 1 and the rule run back to a(0) = 0, a(-1) = -1
    older, old, cur = -1, 0, 1
    for _ in range(n - 1):
        older, old, cur = old, cur, cur + older + 1
    print(cur)


main()
