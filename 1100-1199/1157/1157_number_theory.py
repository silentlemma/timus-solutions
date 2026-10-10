# answers above this are reported as 0
LIMIT = 10000


def main():
    m, n, k = map(int, input().split())
    # x tiles make one rectangle per divisor pair a * b = x with a <= b,
    # that is half the number of divisors, rounded up
    divisors = [0] * (LIMIT + 1)
    for d in range(1, LIMIT + 1):
        for x in range(d, LIMIT + 1, d):
            divisors[x] += 1
    shapes = [(c + 1) // 2 for c in divisors]
    print(next((t for t in range(k + 1, LIMIT + 1) if shapes[t] == n and shapes[t - k] == m), 0))


main()
