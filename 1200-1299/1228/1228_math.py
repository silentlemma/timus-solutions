import sys


def main():
    n, s, *factors = map(int, sys.stdin.read().split())
    # each factor is the next one times the size of the next dimension, and
    # the first one times the size of the first dimension is the whole array
    sizes = [s] + factors[:n]
    print(" ".join(str(sizes[i] // sizes[i + 1] - 1) for i in range(n)))


main()
