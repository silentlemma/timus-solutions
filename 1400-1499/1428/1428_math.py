def main():
    a, b, c = map(int, input().split())
    # 2^(C-1) + 2^(C-1) = 2^C, and A and B both divide C - 1
    print(2 ** ((c - 1) // a))
    print(2 ** ((c - 1) // b))
    print(2)


main()
