#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int> constants(count);
    for (int &value : constants)
        std::cin >> value;
    std::vector<std::pair<int, int>> intervals{{0, 1}};
    for (auto it = constants.rbegin(); it != constants.rend(); ++it) {
        std::vector<std::pair<int, int>> candidates;
        for (auto [left, right] : intervals) {
            if (right < 0)
                continue;
            left = std::max(left, 0);
            candidates.emplace_back(*it - right, *it - left);
            candidates.emplace_back(*it + left, *it + right);
        }
        std::sort(candidates.begin(), candidates.end());
        std::vector<std::pair<int, int>> merged;
        for (auto [left, right] : candidates) {
            if (!merged.empty() && left <= merged.back().second) {
                merged.back().second = std::max(merged.back().second, right);
            } else {
                merged.emplace_back(left, right);
            }
        }
        intervals.swap(merged);
    }
    std::cout << intervals.size() << '\n';
    for (auto [left, right] : intervals)
        std::cout << left << ' ' << right << '\n';
}
