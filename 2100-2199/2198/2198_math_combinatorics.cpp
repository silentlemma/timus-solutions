#include <cstdint>
#include <iostream>
#include <vector>

constexpr int PADDING = 3;
constexpr std::int64_t MOD = 1000000007;

int main() {
    int n;
    std::cin >> n;
    const int edges = n - 1;
    const int length = 2 * edges;
    std::vector<std::int64_t> inverse(length + 2), choose(length + PADDING);
    inverse[1] = 1;
    choose[0] = 1;
    for (int i = 1; i <= length; ++i) {
        if (i > 1) {
            inverse[i] = MOD - (MOD / i) * inverse[MOD % i] % MOD;
        }
        choose[i] = choose[i - 1] * (length - i + 1) % MOD * inverse[i] % MOD;
    }

    // Contour walks are Dyck paths. Sum the counts whose maximum is at least h.
    // Reflection at levels -1 and h gives this second difference, with width h + 1.
    std::int64_t answer = 0;
    for (int width = 2; width <= edges + 1; ++width) {
        for (int offset = width; offset <= edges + 1; offset += width) {
            const int index = edges + offset;
            answer += choose[index - 1] - 2 * choose[index] + choose[index + 1];
        }
    }
    std::cout << (answer % MOD + MOD) % MOD << '\n';
}
