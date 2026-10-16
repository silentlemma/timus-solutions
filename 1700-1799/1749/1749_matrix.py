import sys

BASE = 10
SIZE = 4


def multiply(a, b, m):
    return [[sum(a[i][t] * b[t][j] for t in range(SIZE)) % m for j in range(SIZE)]
            for i in range(SIZE)]


def main():
    data = sys.stdin.read().split()
    digits = data[0]
    k, m = int(data[1]), int(data[2])
    # going left to right, E is the sum of the substrings ending at the
    # current digit: E' = 10 E + digit * (its position), and S adds up E,
    # so one copy of p acts linearly on (S, E, J, 1), J digits before it
    power, value, weighted = 1 % m, 0, 0
    sum_power = sum_value = sum_weighted = 0
    for i, ch in enumerate(digits, 1):
        d = ord(ch) - ord("0")
        power = power * BASE % m
        value = (value * BASE + d) % m
        weighted = (weighted * BASE + d * i) % m
        sum_power = (sum_power + power) % m
        sum_value = (sum_value + value) % m
        sum_weighted = (sum_weighted + weighted) % m
    block = [[1 % m, sum_power, sum_value, sum_weighted],
             [0, power, value, weighted],
             [0, 0, 1 % m, len(digits) % m],
             [0, 0, 0, 1 % m]]
    result = [[(1 if i == j else 0) % m for j in range(SIZE)] for i in range(SIZE)]
    while k:
        if k & 1:
            result = multiply(result, block, m)
        block = multiply(block, block, m)
        k >>= 1
    # starting from S = E = J = 0, the total is the constant column of S
    print(result[0][SIZE - 1])


main()
