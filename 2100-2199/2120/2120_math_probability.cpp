#include <cstdint>
#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::int64_t n;
    std::cin >> n;
    std::int64_t remaining = n - 2;
    std::int64_t fixed_weight = 0;
    std::int64_t unknown_count = 0;
    std::int64_t unknown_sum = 0;
    constexpr int UNKNOWN = -1;

    for (std::int64_t vertex = 1; vertex <= n; ++vertex) {
        int degree;
        std::cin >> degree;
        if (degree == UNKNOWN) {
            ++unknown_count;
            unknown_sum += vertex;
        } else {
            remaining -= degree - 1;
            fixed_weight += vertex * (degree - 1);
        }
    }

    std::int64_t answer = n * (n + 1) / 2 + n * fixed_weight;
    if (unknown_count != 0) {
        // Divide before multiplying by n to keep every product in 64 bits.
        const std::int64_t product = remaining * unknown_sum;
        answer += n * (product / unknown_count);
        answer += n * (product % unknown_count) / unknown_count;
    }
    std::cout << answer << '\n';
}
