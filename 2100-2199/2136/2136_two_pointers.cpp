#include <algorithm>
#include <deque>
#include <iostream>
#include <utility>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int height, width, body_height, body_width;
    std::cin >> height >> width >> body_height >> body_width;

    std::deque<std::pair<int, int>> left_max, right_max;
    int best = 0;
    for (int row = 0; row < height; ++row) {
        int left, right;
        std::cin >> left >> right;
        while (!left_max.empty() && left_max.front().first < row - body_height) {
            left_max.pop_front();
        }
        while (!right_max.empty() && right_max.front().first < row - body_height) {
            right_max.pop_front();
        }
        while (!left_max.empty() && left_max.back().second <= left) {
            left_max.pop_back();
        }
        while (!right_max.empty() && right_max.back().second <= right) {
            right_max.pop_back();
        }
        left_max.emplace_back(row, left);
        right_max.emplace_back(row, right);
        // A downward move can touch body_height + 1 consecutive rows.
        best = std::max(best, left_max.front().second + right_max.front().second);
    }

    std::cout << std::max(0, width - body_width + 1 - best) << '\n';
}
