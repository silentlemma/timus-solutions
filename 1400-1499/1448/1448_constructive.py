import sys

FULL = 100  # brightness is given in percent


def main():
    n, b = (int(x) for x in sys.stdin.read().split())
    # lamp i is on when floor((i + 1) b / 100) grows: every stretch then holds
    # less than one lamp more or less than L b / 100, and the pattern repeats
    period = "".join(str((i + 1) * b // FULL - i * b // FULL) for i in range(FULL))
    print((period * (n // FULL + 1))[:n])


main()
