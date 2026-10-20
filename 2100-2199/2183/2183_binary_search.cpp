#include <algorithm>
#include <cstdio>
#include <vector>

constexpr long long LIMIT = 1000000000;  // the largest absolute mood

int n;
std::vector<long long> a;
long long smallest;

bool possible(long long x) {
    // Every mood below x must be flipped, so the shortest segment covers them
    // all, and every mood inside must become at least x.
    int first = -1, last = -1;
    for (int i = 0; i < n; i++)
        if (a[i] < x) {
            if (first < 0) first = i;
            last = i;
        }
    if (first < 0) return smallest <= -x;  // some single mood can still be flipped
    long long largest = *std::max_element(a.begin() + first, a.begin() + last + 1);
    return largest <= -x;
}

int main() {
    scanf("%d", &n);
    a.resize(n);
    for (auto &x : a) scanf("%lld", &x);
    smallest = *std::min_element(a.begin(), a.end());
    long long lo = -LIMIT, hi = LIMIT;
    while (lo < hi) {
        long long middle = lo + (hi - lo + 1) / 2;
        if (possible(middle)) lo = middle;
        else hi = middle - 1;
    }
    printf("%lld\n", lo);
    return 0;
}
