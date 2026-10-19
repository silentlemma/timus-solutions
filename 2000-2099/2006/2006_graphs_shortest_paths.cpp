#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

constexpr int INFINITY_COST = 1000000000;
constexpr int PADDING = 2;
constexpr int DIRECTIONS = 4;
using Pair = std::pair<int, int>;

struct Search {
    std::vector<int> distance, parent, order;
};

Search bfs(const std::string &cells, const std::array<int, DIRECTIONS> &offsets, int start) {
    Search result{std::vector<int>(cells.size(), -1), std::vector<int>(cells.size(), -1), {}};
    result.distance[start] = 0;
    result.order.push_back(start);
    for (std::size_t head = 0; head < result.order.size(); ++head) {
        int vertex = result.order[head];
        for (int offset : offsets) {
            int other = vertex + offset;
            if (cells[other] == '.' && result.distance[other] < 0) {
                result.distance[other] = result.distance[vertex] + 1;
                result.parent[other] = vertex;
                result.order.push_back(other);
            }
        }
    }
    return result;
}

Pair solve(const std::vector<std::string> &grid, int sr, int sc, int tr, int tc) {
    int rows = static_cast<int>(grid.size()), cols = static_cast<int>(grid[0].size());
    int stride = cols + PADDING;
    std::string cells((rows + PADDING) * stride, '#');
    for (int row = 0; row < rows; ++row)
        cells.replace((row + 1) * stride + 1, cols, grid[row]);
    int start = (sr + 1) * stride + sc + 1, target = (tr + 1) * stride + tc + 1;
    auto coordinates = [stride](int vertex) {
        return Pair{vertex / stride - 1, vertex % stride - 1};
    };
    std::array<int, DIRECTIONS> offsets{-stride, 1, stride, -1};
    Search first = bfs(cells, offsets, start);
    const auto &ds = first.distance;
    if (ds[target] == 1) {
        for (int vertex = 0; vertex < static_cast<int>(cells.size()); ++vertex)
            if (cells[vertex] == '.' && vertex != start && vertex != target)
                return coordinates(vertex);
    }
    auto dt = bfs(cells, offsets, target).distance;
    std::vector<int> path;
    for (int vertex = target; vertex != -1; vertex = first.parent[vertex])
        path.push_back(vertex);
    std::reverse(path.begin(), path.end());
    int length = static_cast<int>(path.size()) - 1;
    std::vector<int> position(cells.size(), -1), level(cells.size(), -1);
    for (int at = 0; at <= length; ++at)
        position[path[at]] = at;
    for (int vertex : first.order)
        level[vertex] = position[vertex] >= 0 ? position[vertex] : level[first.parent[vertex]];
    std::vector<Pair> edges;
    std::vector<int> detour(cells.size(), INFINITY_COST);
    for (int vertex : first.order) {
        for (int offset : offsets) {
            int other = vertex + offset;
            if (level[vertex] >= level[other])
                continue;
            edges.emplace_back(vertex, other);
            if (position[other] < 0)
                detour[other] = std::min(detour[other], ds[vertex] + 1);
        }
    }
    std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> heap;
    for (int vertex : first.order)
        if (detour[vertex] < INFINITY_COST)
            heap.emplace(detour[vertex], vertex);
    while (!heap.empty()) {
        auto [distance, vertex] = heap.top();
        heap.pop();
        if (distance != detour[vertex])
            continue;
        for (int offset : offsets) {
            int other = vertex + offset;
            if (level[other] == level[vertex] && position[other] < 0 &&
                distance + 1 < detour[other]) {
                detour[other] = distance + 1;
                heap.emplace(distance + 1, other);
            }
        }
    }
    std::vector<int> answer(length + 1, INFINITY_COST);
    std::vector<std::tuple<int, int, int>> intervals;
    for (auto [x, y] : edges) {
        int left = level[x], right = level[y];
        if (left + 1 < right)
            intervals.emplace_back(left + 1, right - 1, ds[x] + 1 + dt[y]);
        if (position[x] < 0 && 1 <= left && left < length)
            answer[left] = std::min(answer[left], detour[x] + 1 + dt[y]);
    }
    std::sort(intervals.begin(), intervals.end());
    std::size_t at = 0;
    int best = 1;
    for (int failed = 1; failed < length; ++failed) {
        while (at < intervals.size() && std::get<0>(intervals[at]) <= failed) {
            auto [left, right, cost] = intervals[at++];
            (void)left;
            heap.emplace(cost, right);
        }
        while (!heap.empty() && heap.top().second < failed)
            heap.pop();
        if (!heap.empty())
            answer[failed] = std::min(answer[failed], heap.top().first);
        if (answer[failed] > answer[best])
            best = failed;
    }
    return coordinates(path[best]);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int rows, cols, sr, sc, tr, tc;
    std::cin >> rows >> cols >> sr >> sc >> tr >> tc;
    std::vector<std::string> grid(rows);
    for (auto &row : grid)
        std::cin >> row;
    auto answer = solve(grid, sr - 1, sc - 1, tr - 1, tc - 1);
    std::cout << answer.first + 1 << ' ' << answer.second + 1 << '\n';
}
