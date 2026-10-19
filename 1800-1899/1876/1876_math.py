LEGS = 40


def main():
    a, b = map(int, input().split())
    # either every right slipper turns up while the left legs are dressed,
    # or 39 rights do, and then every spare left slipper is thrown away
    # before the last right leg is dressed
    print(max(2 * b + LEGS, 2 * a + LEGS - 1))


main()
