#include <iostream>
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
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long n;
    if (!(std::cin >> n))
        return 0;
    auto [parallel, perpendicular] = count(n);
    std::cout << parallel << ' ' << perpendicular << '\n';
}
