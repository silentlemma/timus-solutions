#include <algorithm>
#include <cstdio>

int main() {
    long long n, k;
    scanf("%lld %lld", &n, &k);
    // with r = N mod K, an s x s corner square is left over, s = min(r, K - r)
    long long r = n % k, s = std::min(r, k - r);
    printf("%lld\n", n < k ? 0 : (n * n - s * s) / k);
}
