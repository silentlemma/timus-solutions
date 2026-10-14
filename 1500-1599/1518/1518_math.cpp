#include <cstdint>
#include <cstdio>
#include <vector>

using namespace std;

typedef uint64_t u64;

int n;
u64 y;
vector<int> steps; // the j with C[n + 1 - j] = 1

// p * q modulo the characteristic polynomial and y
vector<u64> times(const vector<u64> &p, const vector<u64> &q) {
    vector<u64> prod(2 * n - 1, 0);
    for (int i = 0; i < n; i++)
        if (p[i])
            for (int j = 0; j < n; j++)
                prod[i + j] = (prod[i + j] + p[i] * q[j]) % y;
    // x^n is the sum of x^(n - j) over the steps
    for (int d = 2 * n - 2; d >= n; d--)
        if (prod[d])
            for (int j : steps)
                prod[d - j] = (prod[d - j] + prod[d]) % y;
    prod.resize(n);
    return prod;
}

int main() {
    long long x;
    scanf("%d %lld %llu", &n, &x, (unsigned long long *)&y);
    vector<u64> keys(n);
    vector<int> shifts(n);
    for (u64 &k : keys)
        scanf("%llu", (unsigned long long *)&k);
    for (int &c : shifts)
        scanf("%d", &c);
    // K[i] = sum of K[i - j] * C[n + 1 - j] over j = 1 ... n
    for (int j = 1; j <= n; j++)
        if (shifts[n - j] == 1)
            steps.push_back(j);
    // K[x] is the x - 1 st term counting from K[1], and the coefficients of
    // x^(x - 1) reduced modulo the characteristic polynomial weigh K[1 ... n]
    vector<u64> result(n, 0), base(n, 0);
    result[0] = 1;
    if (n > 1)
        base[1] = 1;
    else
        base[0] = shifts[0] % y;
    for (long long e = x - 1; e > 0; e >>= 1) {
        if (e & 1)
            result = times(result, base);
        base = times(base, base);
    }
    u64 answer = 0;
    for (int i = 0; i < n; i++)
        answer = (answer + result[i] * (keys[i] % y)) % y;
    printf("%llu\n", (unsigned long long)answer);
}
