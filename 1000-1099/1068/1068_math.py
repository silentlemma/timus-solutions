def main():
    n = int(input())
    # the numbers between 1 and N form one interval whichever side N is on,
    # and its sum is the count times the average of the ends
    count = abs(n - 1) + 1
    print((1 + n) * count // 2)


main()
