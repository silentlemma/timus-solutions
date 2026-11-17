from sys import stdin


def main():
    exponent, modulus, remainder = map(int, stdin.buffer.read().split())
    found = False
    for value in range(modulus):
        if pow(value, exponent, modulus) == remainder:
            print(value, end=" ")
            found = True
    if not found:
        print(-1)


main()
