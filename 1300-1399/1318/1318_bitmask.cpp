#include <cstdio>
#include <vector>

typedef unsigned __int128 u128;
typedef unsigned long long u64;

const int BITS = 128;
const int HALF = 64;
const int WORD = 32;
const int PARTS = 4;
const u64 DECIMAL = 10;

int bitLength(u128 x) {
    u64 hi = (u64)(x >> HALF), lo = (u64)x;
    if (hi != 0)
        return BITS - __builtin_clzll(hi);
    return lo != 0 ? HALF - __builtin_clzll(lo) : 0;
}

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<u128> a(n);
    for (int i = 0; i < n; i++) {
        for (int p = 0; p < PARTS; p++) {
            unsigned w = 0;
            if (scanf("%u", &w) != 1)
                return 0;
            a[i] = a[i] << WORD | w;
        }
    }
    // a number of bit length L is at least every power of ten that is
    // shorter, and at least the one power of length L only if it reaches it
    int base[BITS + 1] = {0};
    bool has[BITS + 1] = {false};
    u128 limit[BITS + 1] = {0};
    u128 most = ~(u128)0;
    for (u128 p = DECIMAL;; p *= DECIMAL) {
        int len = bitLength(p);
        has[len] = true;
        limit[len] = p;
        for (int l = len + 1; l <= BITS; l++)
            base[l]++;
        if (p > most / DECIMAL)
            break;
    }
    long long total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            u128 x = a[i] ^ a[j];
            int len = bitLength(x);
            total += base[len] + (has[len] && x >= limit[len]);
        }
    }
    printf("%lld\n", 2 * total); // every pair counts in both orders
    return 0;
}
