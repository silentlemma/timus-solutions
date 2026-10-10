#include <algorithm>
#include <cstdio>

// sum over even e <= n of tz(e) - 1, that is sum over y <= n/2 of tz(y)
long long evens(long long n) {
    long long m = n / 2;
    return m - __builtin_popcountll(m);
}

// tz(x) - 1 for an even x, 0 for an odd one
long long extra(long long x) { return x % 2 == 0 ? __builtin_ctzll(x) - 1 : 0; }

int main() {
    long long i, j;
    if (scanf("%lld %lld", &i, &j) != 2)
        return 0;
    if (i > j)
        std::swap(i, j);
    // numbers run through the tree in order, so a node's height is the count of
    // trailing zeros; between k and k + 1 the even one is an ancestor of the
    // odd leaf, and the message waits one day per node in between
    long long days = i == j ? 0 : 2 * (evens(j) - evens(i - 1)) - extra(i) - extra(j);
    printf("%lld\n", days);
}
