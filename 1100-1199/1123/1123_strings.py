import sys


def mirror(digits):
    n = len(digits)
    return digits[: (n + 1) // 2] + digits[: n // 2][::-1]


def main():
    s = sys.stdin.read().split()[0]
    n = len(s)
    best = mirror(s)
    # same length strings of digits compare like the numbers they spell
    if best < s:
        # add one to the left half with its middle digit; it is not all nines,
        # since all nines mirror to the largest number of this length
        half = list(s[: (n + 1) // 2])
        k = len(half) - 1
        while half[k] == "9":
            half[k] = "0"
            k -= 1
        half[k] = chr(ord(half[k]) + 1)
        best = mirror("".join(half) + s[(n + 1) // 2 :])
    print(best)


main()
