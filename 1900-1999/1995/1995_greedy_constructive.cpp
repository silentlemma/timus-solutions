#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>

constexpr int PERCENT_SCALE = 100;

std::vector<int> construct(int size, int kept, int percentage) {
    std::vector<int> weights(size, 1);
    for (int i = size - kept; i < size; ++i)
        weights[i] = weights[(percentage * i - 1) / PERCENT_SCALE] + 1;
    return weights;
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size, kept, percentage;
    std::cin >> size >> kept >> percentage;
    const auto weights = construct(size, kept, percentage);
    const auto total = std::accumulate(weights.begin(), weights.end(), std::int64_t{0});
    std::cout << total << '\n';
    for (int i = 0; i < size; ++i)
        std::cout << weights[i] << (i + 1 == size ? '\n' : ' ');
    return 0;
}
