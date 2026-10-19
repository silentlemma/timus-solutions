#include <iostream>
#include <utility>
#include <vector>

constexpr int WINDOW_SIZE = 3;

std::pair<int, int> maximum_window(const std::vector<int> &values) {
    int current = 0;
    for (int index = 0; index < WINDOW_SIZE; ++index)
        current += values[index];
    int best = current, position = WINDOW_SIZE / 2 + 1;
    for (int start = 1; start + WINDOW_SIZE <= static_cast<int>(values.size()); ++start) {
        current += values[start + WINDOW_SIZE - 1] - values[start - 1];
        if (current > best) {
            best = current;
            position = start + WINDOW_SIZE / 2 + 1;
        }
    }
    return {best, position};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int> values(count);
    for (int &value : values)
        std::cin >> value;
    const auto answer = maximum_window(values);
    std::cout << answer.first << ' ' << answer.second << '\n';
}
