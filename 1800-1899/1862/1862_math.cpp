#include <cstdio>

const long long MOD = 1000000007;

int main() {
    long long level;
    if (scanf("%lld", &level) != 1) return 0;
    // the numbers form a perfect binary tree, and the mole walks the tree
    // distance; summing over every edge the nodes below it times the nodes
    // above it gives 2^l ((l - 1)(2^l + 1) - 2 (2^l - 2))
    long long power = 1, base = 2;
    for (long long e = level; e > 0; e >>= 1) {
        if (e & 1) power = power * base % MOD;
        base = base * base % MOD;
    }
    long long l = level % MOD;
    long long first = (l - 1 + MOD) % MOD * ((power + 1) % MOD) % MOD;
    long long second = 2 * ((power - 2 + MOD) % MOD) % MOD;
    long long inner = (first - second + MOD) % MOD;
    printf("%lld\n", power * inner % MOD);
    return 0;
}
