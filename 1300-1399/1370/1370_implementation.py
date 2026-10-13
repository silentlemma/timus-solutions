import sys

WINDOW = 10  # digits seen in the window


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    digits = data[2 : 2 + n]
    # each click moves the window one digit on, around the wheel
    print("".join(digits[(m + i) % n] for i in range(WINDOW)))


main()
