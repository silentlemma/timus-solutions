def main():
    first, second = int(input()), int(input())
    # on night k the thief tries code k on lock 1 when k is even and on
    # lock 2 when k is odd
    print("yes" if first % 2 == 0 or second % 2 == 1 else "no")


main()
