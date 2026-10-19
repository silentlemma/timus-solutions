import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def main():
    n = int(sys.stdin.read())
    # m, the least number not dividing n, divides no proper divisor either,
    # so colouring by x mod m separates every two artists d apart; m <= 13
    # since lcm(1, ..., 13) exceeds 300000
    m = 2
    while n % m == 0:
        m += 1
    p = 2
    while n % p:
        p += 1
    # the wrap-around neighbours are n - d apart, at least n - n/p; the
    # last n/p artists get a second palette, so no gap inside either part
    # is that long and the parts never share a colour
    front = n - n // p
    print("".join(ALPHABET[x % m + (m if x >= front else 0)] for x in range(n)))


main()
