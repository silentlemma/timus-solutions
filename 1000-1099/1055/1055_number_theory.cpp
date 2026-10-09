#include <cstdio>
#include <vector>

// the exponent of the prime p in x! (Legendre's formula)
long long exponent(long long x, long long p) {
    long long e = 0;
    for (; x > 0; x /= p)
        e += x / p;
    return e;
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<bool> composite(n + 1, false);
    int count = 0;
    for (int p = 2; p <= n; p++) {
        if (composite[p])
            continue;
        for (long long q = (long long)p * p; q <= n; q += p)
            composite[q] = true;
        if (exponent(n, p) - exponent(m, p) - exponent(n - m, p) > 0)
            count++;
    }
    printf("%d\n", count);
}
