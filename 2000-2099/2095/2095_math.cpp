#include <cstdio>

constexpr long long FIRST = 2;  // the first step removes every second day

// among the first n days, step k removes every k-th of those still left,
// which is n / k of a prefix of length n; it stops mattering once n < k
long long quiet(long long n) {
    for (long long k = FIRST; n >= k; k++) n -= n / k;
    return n;
}

int main() {
    long long left, right;
    scanf("%lld %lld", &left, &right);
    printf("%lld\n", quiet(right) - quiet(left - 1));
}
