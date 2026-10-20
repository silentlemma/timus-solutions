def main():
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())
    # the dual lands first cover what the red and blue lands miss, and every
    # land left over pays for the mana of any color
    missing = max(0, x - a) + max(0, y - b)
    if missing <= c and a + b + c >= x + y + z:
        print("It is a kind of magic")
    else:
        print("There are no miracles in life")


main()
