def main():
    a, b = int(input()), int(input())
    # the fuses burn on the odd days; (x + 1) // 2 odd days are in 1..x
    print((b + 1) // 2 - a // 2)


main()
