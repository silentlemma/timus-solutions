#include <cstdint>
#include <iostream>

constexpr std::int64_t SQUARE_FACTOR = 3;
constexpr std::int64_t CONSTANT_FACTOR = 12;
constexpr std::int64_t SEARCH_LIMIT = 2000000000;

std::int64_t solve(std::int64_t a, std::int64_t b, std::int64_t c) {
    const std::int64_t scaled = SQUARE_FACTOR * b * b / a - CONSTANT_FACTOR * c;
    if (scaled < 0)
        return 1;
    const std::int64_t threshold = scaled / a + 1;
    std::int64_t low = 1, high = SEARCH_LIMIT;
    while (low < high) {
        const std::int64_t middle = low + (high - low) / 2;
        if (middle * middle > threshold)
            high = middle;
        else
            low = middle + 1;
    }
    return low;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int cases;
    std::cin >> cases;
    while (cases--) {
        std::int64_t a, b, c;
        std::cin >> a >> b >> c;
        std::cout << solve(a, b, c) << '\n';
    }
    return 0;
}
