#include <cstdint>
#include <cstdio>
#include <map>
#include <vector>

using namespace std;
typedef unsigned long long u64;

constexpr int SHORT = 32;  // cycles up to this length are summed directly
constexpr u64 MODS[] = {998244353, 167772161, 469762049};  // NTT primes, root 3
constexpr int PRIMES = 3;
constexpr u64 ROOT = 3;
constexpr size_t SPAN = 3;  // a product of L and 2L numbers has fewer than 3L

u64 power(u64 b, u64 e, u64 mod) {
    u64 r = 1;
    for (b %= mod; e; e >>= 1, b = b * b % mod)
        if (e & 1) r = r * b % mod;
    return r;
}

void ntt(vector<u64>& a, bool invert, u64 mod) {
    size_t n = a.size();
    for (size_t i = 1, j = 0; i < n; i++) {
        size_t bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (size_t len = 2; len <= n; len <<= 1) {
        u64 w = power(ROOT, (mod - 1) / len, mod);
        if (invert) w = power(w, mod - 2, mod);
        for (size_t i = 0; i < n; i += len) {
            u64 wn = 1;
            for (size_t k = 0; k < len / 2; k++, wn = wn * w % mod) {
                u64 u = a[i + k], v = a[i + k + len / 2] * wn % mod;
                a[i + k] = u + v < mod ? u + v : u + v - mod;
                a[i + k + len / 2] = u >= v ? u - v : u + mod - v;
            }
        }
    }
    if (invert) {
        u64 inv = power(n, mod - 2, mod);
        for (u64& x : a) x = x * inv % mod;
    }
}

// out[s] = sum over r of fold[r] * cycle[(s + r) mod L]; every sum is below 2^63
vector<u64> cyclic(const vector<u64>& fold, const vector<u64>& cycle) {
    size_t size = cycle.size();
    vector<u64> out(size, 0);
    if (size <= SHORT) {
        for (size_t s = 0; s < size; s++)
            for (size_t r = 0; r < size; r++) out[s] += fold[r] * cycle[(s + r) % size];
        return out;
    }
    // reversed fold times the cycle written twice, modulo three primes,
    // put together by Garner's method; wrapping 64-bit arithmetic is exact here
    size_t n = 1;
    while (n < SPAN * size) n <<= 1;
    vector<u64> residue[PRIMES];
    for (int k = 0; k < PRIMES; k++) {
        vector<u64> a(n, 0), b(n, 0);
        for (size_t r = 0; r < size; r++) a[size - 1 - r] = fold[r] % MODS[k];
        for (size_t i = 0; i < 2 * size; i++) b[i] = cycle[i % size] % MODS[k];
        ntt(a, false, MODS[k]);
        ntt(b, false, MODS[k]);
        for (size_t i = 0; i < n; i++) a[i] = a[i] * b[i] % MODS[k];
        ntt(a, true, MODS[k]);
        residue[k] = a;
    }
    u64 m0 = MODS[0], m1 = MODS[1], m2 = MODS[2];
    u64 inv01 = power(m0 % m1, m1 - 2, m1), inv012 = power(m0 * m1 % m2, m2 - 2, m2);
    for (size_t s = 0; s < size; s++) {
        size_t i = s + size - 1;
        u64 x0 = residue[0][i];
        u64 x1 = (residue[1][i] + m1 - x0 % m1) % m1 * inv01 % m1;
        u64 low = (x0 + x1 * m0) % m2;
        u64 x2 = (residue[2][i] + m2 - low) % m2 * inv012 % m2;
        out[s] = x0 + x1 * m0 + x2 * m0 * m1;
    }
    return out;
}

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    vector<int> p(n);
    for (int& x : p) scanf("%d", &x), x--;
    vector<u64> byYear(m + 1, 0);  // byYear[t] = q_t
    for (int t = 1; t <= m; t++) scanf("%llu", &byYear[t]);
    // the year t row is p applied t times, so the answer at j is the sum of
    // q_t p^t(j); along a cycle of p this is a cyclic correlation
    vector<u64> answer(n);
    vector<bool> seen(n, false);
    map<size_t, vector<u64>> folds;  // cycle length -> sums of q_t over t with equal remainders
    for (int start = 0; start < n; start++) {
        if (seen[start]) continue;
        vector<int> cycle;
        for (int j = start; !seen[j]; j = p[j]) seen[j] = true, cycle.push_back(j);
        size_t size = cycle.size();
        if (!folds.count(size)) {
            vector<u64> fold(size, 0);
            for (int t = 1; t <= m; t++) fold[t % size] += byYear[t];
            folds[size] = fold;
        }
        vector<u64> values(size);
        for (size_t s = 0; s < size; s++) values[s] = cycle[s] + 1;
        values = cyclic(folds[size], values);
        for (size_t s = 0; s < size; s++) answer[cycle[s]] = values[s];
    }
    for (int j = 0; j < n; j++) printf(j ? " %llu" : "%llu", answer[j]);
    printf("\n");
}
