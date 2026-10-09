#include <cstdio>
#include <numeric>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // cutting a shorter piece off a longer one keeps the gcd of all lengths,
    // so the last piece is always the gcd and the answer is never ambiguous
    long long g = 0;
    for (int i = 0; i < n; i++) {
        long long length;
        if (scanf("%lld", &length) != 1)
            return 0;
        g = std::gcd(g, length);
    }
    printf("%lld\n", g);
}
