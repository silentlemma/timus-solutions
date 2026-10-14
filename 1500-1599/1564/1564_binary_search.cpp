#include <cstdio>

const long long BASE = 10;
const long long TOP = 1000000000000000000LL; // more than 10^18 ones are counted below this floor

// the number of digits 1 in the numbers from 1 to x: at each place p, every
// full block of 10 p numbers holds p ones there, and the last part adds p,
// the rest past the 1, or nothing, as its digit is above, at or below 1
long long ones(long long x) {
    long long total = 0;
    // x is at least 1; p stops before p * 10 could pass 10^19
    for (long long p = 1;; p *= BASE) {
        long long high = x / p / BASE, digit = x / p % BASE, low = x % p;
        total += high * p + (digit > 1 ? p : digit == 1 ? low + 1 : 0);
        if (p > x / BASE)
            break;
    }
    return total;
}

int main() {
    long long k;
    if (scanf("%lld", &k) != 1)
        return 0;
    // the floor where the k-th one was counted is the first x with ones(x) >= k
    long long lo = 1, hi = TOP;
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (ones(mid) >= k)
            hi = mid;
        else
            lo = mid + 1;
    }
    if (ones(lo) == k)
        printf("%lld\n", lo);
    else
        printf("Petr lies\n");
}
