def main():
    n, k = map(int, input().split())
    # n - k + 1 zeros, then 1, -1, 2, -2, ...: k distinct values and only k
    # distinct segment sums, the least possible
    values = [0] * (n - k + 1)
    values += [(i + 1) // 2 if i % 2 else -(i // 2) for i in range(1, k)]
    print(" ".join(map(str, values)))


main()
