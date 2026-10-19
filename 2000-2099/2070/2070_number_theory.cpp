#include <cstdio>
#include <vector>

using namespace std;

constexpr int LIMIT = 1000000;  // square root of the largest R

int main() {
    long long l, r;
    scanf("%lld %lld", &l, &r);
    vector<bool> composite(LIMIT + 1, false);
    composite[0] = composite[1] = true;
    for (long long i = 2; i * i <= LIMIT; i++)
        if (!composite[i])
            for (long long j = i * i; j <= LIMIT; j += i) composite[j] = true;
    // the only unsatisfying numbers are p^k, k >= 2, with k + 1 divisors and k + 1 prime
    long long bad = 0;
    for (long long p = 2; p * p <= r; p++) {
        if (composite[p]) continue;
        long long power = p * p;
        for (int k = 2;; k++) {
            if (power >= l && !composite[k + 1]) bad++;
            if (power > r / p) break;
            power *= p;
        }
    }
    printf("%lld\n", r - l + 1 - bad);
}
