#include <cstdio>
#include <utility>

constexpr long long FORBIDDEN_CHOICES = 3;

std::pair<long long, long long> count(long long n) {
    if (n % 2) {
        long long size = (n - FORBIDDEN_CHOICES) / 2;
        return {size >= 2 ? n * size : 0, 0};
    }
    long long half = n / 2, first = half - 1, second = half - 2;
    long long parallel = half * ((first >= 2 ? first : 0) + (second >= 2 ? second : 0));
    return {parallel, half * (n - FORBIDDEN_CHOICES)};
}

int main() {
    long long n;
    if (std::scanf("%lld", &n) != 1)
        return 0;
    auto [parallel, perpendicular] = count(n);
    std::printf("%lld %lld\n", parallel, perpendicular);
}
