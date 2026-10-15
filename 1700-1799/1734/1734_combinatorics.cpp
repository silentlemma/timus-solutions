#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

const long long MOD = 1000000007;
const long long EDGE_KINDS = 3;
const long long MIDDLE_KINDS = 4;
const long long ONE_COLOUR_KINDS = 2;

std::vector<long long> fact, inv;

long long power(long long a, long long e) {
    long long r = 1;
    for (a %= MOD; e > 0; e >>= 1, a = a * a % MOD) {
        if (e & 1) r = r * a % MOD;
    }
    return r;
}

long long choose(int a, int b) {
    if (b < 0 || b > a) return 0;
    return fact[a] * inv[b] % MOD * inv[a - b] % MOD;
}

int main() {
    int n, k;
    std::cin >> n >> k;
    int squares = n * n / 2, row = n / 2, middle = squares - 2 * row;
    fact.assign(squares + 1, 1);
    inv.assign(squares + 1, 1);
    for (int i = 1; i <= squares; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[squares] = power(fact[squares], MOD - 2);
    for (int i = squares; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;
    // a dark square on the first or last row takes three kinds of piece
    // (the man that would be crowned there is out), any other square four
    long long total = 0;
    for (int a = 0; a <= std::min(2 * row, k); a++) {
        long long edge = choose(2 * row, a) * power(EDGE_KINDS, a) % MOD;
        long long rest = choose(middle, k - a) * power(MIDDLE_KINDS, k - a) % MOD;
        total = (total + edge * rest) % MOD;
    }
    // positions of one colour: on its last row only the king, elsewhere
    // the man or the king
    long long one = 0;
    for (int a = 0; a <= std::min(row, k); a++) {
        long long rest = choose(middle + row, k - a) * power(ONE_COLOUR_KINDS, k - a) % MOD;
        one = (one + choose(row, a) * rest) % MOD;
    }
    printf("%lld\n", ((total - 2 * one) % MOD + MOD) % MOD);
}
