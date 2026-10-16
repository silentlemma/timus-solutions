#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

const unsigned long long LIMIT = 1000000000000000000ULL;
const unsigned long long PRIMES[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
const int COUNT = sizeof(PRIMES) / sizeof(PRIMES[0]);
const int MOST = 64;

std::vector<std::pair<unsigned long long, long long>> found;

// the smallest number with a given set of exponents puts the largest
// exponents on the smallest primes, so only numbers 2^a 3^b 5^c ... with
// a >= b >= c >= ... can be answers
void grow(int index, int cap, unsigned long long value, long long divisors) {
    found.push_back({value, divisors});
    if (index == COUNT) return;
    for (int e = 1; e <= cap; e++) {
        if (value > LIMIT / PRIMES[index]) break;
        value *= PRIMES[index];
        grow(index + 1, e, value, divisors * (e + 1));
    }
}

int main() {
    grow(0, MOST, 1, 1);
    std::sort(found.begin(), found.end());
    std::vector<unsigned long long> values;
    std::vector<std::pair<unsigned long long, long long>> best;
    std::pair<unsigned long long, long long> top = {0, 0};
    for (const auto &f : found) {
        if (f.second > top.second) top = f;
        values.push_back(f.first);
        best.push_back(top);
    }
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        unsigned long long n;
        scanf("%llu", &n);
        size_t k = std::upper_bound(values.begin(), values.end(), n) - values.begin() - 1;
        printf("%llu %lld\n", best[k].first, best[k].second);
    }
}
