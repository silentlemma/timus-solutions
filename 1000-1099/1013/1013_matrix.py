import sys


def multiply(x, y, m):
    return [[(x[i][0] * y[0][j] + x[i][1] * y[1][j]) % m for j in range(2)] for i in range(2)]


def main():
    n, k, m = map(int, sys.stdin.read().split())
    d = (k - 1) % m
    # (zero, other) -> (other, (zero + other)(K - 1)) is the matrix step,
    # after the first digit the pair is (0, K - 1)
    step, power, e = [[0, 1], [d, d]], [[1, 0], [0, 1]], n - 1
    while e:
        if e & 1:
            power = multiply(power, step, m)
        step = multiply(step, step, m)
        e >>= 1
    print((power[0][1] * d + power[1][1] * d) % m)


main()
