#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

std::pair<std::int64_t, std::int64_t> solve(const std::vector<std::int64_t> &values, int first,
                                            int second) {
    std::int64_t total = 0, score = 0;
    for (auto value : values)
        total += value;
    if (first == second) {
        std::int64_t left = 0;
        for (int i = 0; i < first; ++i)
            left += values[i];
        std::int64_t right = total - left - values[first];
        score = values[first] + (left > right ? left : right);
    } else if (first < second) {
        int boundary = (first + second) / 2;
        for (int i = 0; i <= boundary; ++i)
            score += values[i];
    } else {
        int boundary = (first + second + 1) / 2;
        for (int i = boundary; i < static_cast<int>(values.size()); ++i)
            score += values[i];
    }
    return {score, total - score};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<std::int64_t> values(n);
    for (auto &value : values)
        std::cin >> value;
    int first, second;
    std::cin >> first >> second;
    auto result = solve(values, first - 1, second - 1);
    std::cout << result.first << ' ' << result.second << '\n';
}
