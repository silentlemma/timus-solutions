from math import gcd


def main():
    n, m = map(int, input().split())
    # an a by b grid: the diagonal crosses a + b - 2 inner lines, two at once
    # at each of the gcd(a, b) - 1 inner corners; it starts in one block and
    # every crossing enters a new one
    a, b = n - 1, m - 1
    print(a + b - gcd(a, b))


main()
