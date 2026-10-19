#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    long long total = 0;
    for (int i = 0; i < n; i++) {
        long long d;
        scanf("%lld", &d);
        total += d;
    }
    // a trip to a city with load L costs L d there and (L - d) d back; summed over
    // any order this is (sum of d)^2, so the order does not matter
    printf("%lld\n", total * total);
}
