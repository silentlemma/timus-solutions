import sys


def main():
    data = sys.stdin.read()
    num, _, rest = data.strip().partition(" ")
    n, k = int(num), rest.count("!")
    # multiply n, n - k, ... while the factor stays positive
    product = 1
    for factor in range(n, 0, -k):
        product *= factor
    print(product)


main()
