import sys
from array import array


def first_bad(a, direction):
    i = 0
    while i + 1 < len(a) and a[i] * direction <= a[i + 1] * direction:
        i += 1
    return i


def main():
    # Heights fit signed 32-bit cells. Consume line tokens directly rather
    # than retaining 100000 Python integers plus their byte-string tokens.
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(tokens)
    a = array("i", tokens)
    del tokens
    up, down = first_bad(a, 1), first_bad(a, -1)
    if up == n - 1 or down == n - 1:
        print("Nothing to do here")
        return
    for direction, left in ((1, up), (-1, down)):
        # Equal runs can hide the actual swapped endpoint behind a violation.
        while left > 0 and a[left - 1] == a[left]:
            left -= 1
        right = n - 1
        while a[right - 1] * direction <= a[right] * direction:
            right -= 1
        while right + 1 < n and a[right + 1] == a[right]:
            right += 1
        a[left], a[right] = a[right], a[left]
        if first_bad(a, direction) == n - 1:
            print("Yes")
            print(left + 1, right + 1)
            return
        a[left], a[right] = a[right], a[left]
    print("No hope")


main()
