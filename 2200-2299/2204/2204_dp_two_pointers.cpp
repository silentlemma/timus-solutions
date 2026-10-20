#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

struct Interval {
    int left;
    int right;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    constexpr int OPTIONS = 2;
    int n, m;
    std::cin >> n >> m;
    std::vector<std::array<Interval, OPTIONS>> exams(n);
    for (auto &exam : exams) {
        for (auto &interval : exam) {
            std::cin >> interval.left >> interval.right;
        }
    }
    std::vector<Interval> trips(m);
    for (auto &trip : trips) {
        std::cin >> trip.left >> trip.right;
    }

    std::array<int, OPTIONS> cost{};
    std::array<int, OPTIONS> last{-1, -1};
    int first = 0;
    int end = 0;
    for (const auto &exam : exams) {
        std::array<int, OPTIONS> next_cost{};
        std::array<int, OPTIONS> next_last{};
        for (int option = 0; option < OPTIONS; ++option) {
            const auto &interval = exam[option];
            while (first < m && trips[first].right < interval.left) {
                ++first;
            }
            while (end < m && trips[end].left <= interval.right) {
                ++end;
            }
            const int count = end - first;
            // Only the boundary trip can have been canceled by an earlier exam.
            const int reuse_first = count > 0 && last[0] == first;
            const int reuse_second = count > 0 && last[1] == first;
            next_cost[option] = count + std::min(cost[0] - reuse_first, cost[1] - reuse_second);
            next_last[option] = count > 0 ? end - 1 : -1;
        }
        cost = next_cost;
        last = next_last;
    }
    std::cout << m - std::min(cost[0], cost[1]) << '\n';
}
