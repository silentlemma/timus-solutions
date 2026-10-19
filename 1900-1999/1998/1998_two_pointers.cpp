#include <cstdint>
#include <iostream>
#include <vector>

std::int64_t solve(const std::vector<std::int64_t> &weights,
                   const std::vector<std::int64_t> &events, std::int64_t limit) {
    int size = static_cast<int>(weights.size());
    std::vector<std::int64_t> prefix(size + 1);
    for (int i = 0; i < size; ++i)
        prefix[i + 1] = prefix[i] + weights[i];
    std::vector<int> retreat(size + 1);
    int left = 0;
    for (int height = 1; height <= size; ++height) {
        while (left + 1 < height && prefix[height] - prefix[left + 1] > limit)
            ++left;
        retreat[height] = left;
    }
    std::int64_t time = 0;
    int height = 0;
    for (std::int64_t event : events) {
        std::int64_t ordinary = event - time - 1;
        if (ordinary >= size - height)
            return time + size - height;
        height += static_cast<int>(ordinary);
        height = retreat[height];
        time = event;
    }
    return time + size - height;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m;
    std::int64_t limit;
    std::cin >> n >> m >> limit;
    std::vector<std::int64_t> weights(n), events(m);
    for (auto &value : weights)
        std::cin >> value;
    for (auto &value : events)
        std::cin >> value;
    std::cout << solve(weights, events, limit) << '\n';
}
