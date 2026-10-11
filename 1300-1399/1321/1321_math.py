ONE_DIGIT = 4  # floors 1 to 5 show every indicator lit and unlit

SHORT = 5  # blocks of the second digit: 6 through 9, 0 to 2
LONG = 7  # blocks of the second digit: 2 to 9, 0

LOW_TOP = 3  # a leading digit up to this needs blank, 1, 2 on top
WIDE = 3  # blocks of the leading digit otherwise: blank through 4


def main():
    n = input().split()[0]
    digits = len(n)
    if digits == 1:
        print(ONE_DIGIT)
        return
    top, second = int(n[0]), int(n[1])
    if top == 1:
        lead, zeros = (SHORT if second >= 2 else LONG), digits - 2
    else:
        lead, zeros = (1 if top <= LOW_TOP else WIDE), digits - 1
    print(lead * 10**zeros + 1)


main()
