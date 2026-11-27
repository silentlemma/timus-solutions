# In 2D, neighbouring stones enable three-column/row reductions; isolated rows are separate.
GROUP = 3


def main():
    m, n = sorted(map(int, input().split()))
    if m == 1:
        print((n + 1) // 2)
    elif m % GROUP == 0 or n % GROUP == 0:
        print(2)
    else:
        print(1)


main()
