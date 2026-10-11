def main():
    x, y = map(int, input().split())
    # each turn of the loop swaps x and y, and there are x + y turns; the
    # sum survives, so an odd sum of positive numbers means one swap
    if x > 0 and y > 0 and (x + y) % 2 == 1:
        x, y = y, x
    print(x, y)


main()
