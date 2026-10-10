# a prime above the 4e9 + 1 possible answers; no Fibonacci number with index
# up to 2000 is divisible by it
P = 4294967291


def main():
    i, fi, j, fj, n = map(int, input().split())
    if i > j:
        i, fi, j, fj = j, fj, i, fi
    # F(j) = A F(i) + B F(i + 1), with A and B found by stepping coefficients
    a, b, na, nb = 1, 0, 0, 1
    for _ in range(j - i):
        a, b, na, nb = na, nb, (a + na) % P, (b + nb) % P
    cur = fi % P
    nxt = (fj - a * cur) * pow(b, P - 2, P) % P
    for _ in range(n - i):
        cur, nxt = nxt, (cur + nxt) % P
    for _ in range(i - n):
        cur, nxt = (nxt - cur) % P, cur
    print(cur - P if cur > P // 2 else cur)


main()
