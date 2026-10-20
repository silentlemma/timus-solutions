#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>

using Int = std::int64_t;
constexpr Int MOD = 1000000007;
constexpr int SIEVE_LIMIT = 100000;

Int power(Int base, Int exponent) {
    Int result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent /= 2;
    }
    return result;
}

class Totients {
    int n, limit;
    std::vector<Int> small, large;

  public:
    explicit Totients(int size) : n(size), limit(std::min(n, SIEVE_LIMIT)), small(limit + 1) {
        std::iota(small.begin(), small.end(), Int{0});
        for (int prime = 2; prime <= limit; ++prime) {
            if (small[prime] == prime) {
                for (int multiple = prime; multiple <= limit; multiple += prime) {
                    small[multiple] -= small[multiple] / prime;
                }
            }
        }
        for (int i = 1; i <= limit; ++i) {
            small[i] += small[i - 1];
        }
        int count = n / (limit + 1);
        large.resize(count + 1);
        // Smaller quotient arguments have already been computed.
        for (int index = count; index >= 1; --index) {
            Int x = n / index;
            Int total = x * (x + 1) / 2;
            for (Int left = 2, right; left <= x; left = right + 1) {
                Int quotient = x / left;
                right = x / quotient;
                total -= (right - left + 1) * get(static_cast<int>(quotient));
            }
            large[index] = total;
        }
    }

    Int get(int x) const { return x <= limit ? small[x] : large[n / x]; }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    Totients totients(n);
    Int factorial = 1, weighted = 0, previous = 0, total = 0;
    for (int left = 1, right; left <= n; left = right + 1) {
        int quotient = n / left;
        right = n / quotient;
        // weighted is factorial times the current harmonic sum.
        for (Int i = left; i <= right; ++i) {
            weighted = (weighted * i + factorial) % MOD;
            factorial = factorial * i % MOD;
        }
        Int harmonic = weighted * power(factorial, MOD - 2) % MOD;
        Int difference = (harmonic - previous + MOD) % MOD;
        total = (total + difference * (totients.get(quotient) % MOD)) % MOD;
        previous = harmonic;
    }
    Int pairs = Int{n} * (n + 1) / 2 % MOD;
    std::cout << total * power(pairs, MOD - 2) % MOD << '\n';
}
