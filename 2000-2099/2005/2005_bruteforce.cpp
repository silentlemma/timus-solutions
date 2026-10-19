#include <array>
#include <iostream>
#include <utility>

constexpr int POINTS = 5;
constexpr int END = POINTS - 1;
constexpr int FORBIDDEN_LAST = 2;
constexpr int MIDDLE_SUM = END * (END - 1) / 2;
using Matrix = std::array<std::array<int, POINTS>, POINTS>;
using Route = std::array<int, POINTS>;

std::pair<int, Route> solve(const Matrix &distance) {
    int best_cost = -1;
    Route best_route{};
    for (int first = 1; first < END; ++first) {
        for (int last = 1; last < END; ++last) {
            if (first == last || last == FORBIDDEN_LAST)
                continue;
            int middle = MIDDLE_SUM - first - last;
            Route route{0, first, middle, last, END};
            int cost = 0;
            for (int i = 0; i < END; ++i)
                cost += distance[route[i]][route[i + 1]];
            if (best_cost < 0 || cost < best_cost) {
                best_cost = cost;
                best_route = route;
            }
        }
    }
    return {best_cost, best_route};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    Matrix distance{};
    for (auto &row : distance)
        for (int &value : row)
            std::cin >> value;
    auto answer = solve(distance);
    std::cout << answer.first << '\n';
    for (int i = 0; i < POINTS; ++i)
        std::cout << answer.second[i] + 1 << (i == END ? '\n' : ' ');
}
