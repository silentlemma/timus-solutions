#include <algorithm>
#include <cstdio>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long next = a % b;
        a = b;
        b = next;
    }
    return a;
}

constexpr int INPUT_FIELDS = 3;

int main() {
    long long a, b, n;
    if (std::scanf("%lld %lld %lld", &a, &b, &n) != INPUT_FIELDS)
        return 0;
    bool swapped = a < b;
    if (swapped)
        std::swap(a, b);
    long long divisor = gcd(a, b);
    long long limit = std::min(n / a, b / divisor - 1);
    long long step = a % b, remainder = n % b, best = remainder, bx = 0;
    long long lower_bound = n % divisor;
    for (long long x = 1; x <= limit && best > lower_bound; ++x) {
        remainder = remainder >= step ? remainder - step : remainder + b - step;
        if (remainder < best) {
            best = remainder;
            bx = x;
        }
    }
    long long by = (n - bx * a) / b;
    if (swapped)
        std::swap(bx, by);
    std::printf("%lld %lld\n", bx, by);
}
