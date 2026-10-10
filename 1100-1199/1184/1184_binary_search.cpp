#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    const long long CENTS = 100;
    int n;
    long long k;
    scanf("%d %lld", &n, &k);
    // lengths have exactly two decimals, so in centimetres they are exact
    std::vector<long long> cables(n);
    for (auto &c : cables) {
        long long whole, part;
        scanf("%lld.%lld", &whole, &part);
        c = whole * CENTS + part;
    }
    // more pieces come out of shorter ones, so the longest length that still
    // gives k pieces is found by binary search; 0 means even 1 cm is too long
    long long low = 0, high = *std::max_element(cables.begin(), cables.end());
    while (low < high) {
        long long mid = (low + high + 1) / 2, pieces = 0;
        for (long long c : cables) {
            pieces += c / mid;
        }
        if (pieces >= k) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    printf("%lld.%02lld\n", low / CENTS, low % CENTS);
}
