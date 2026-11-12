#include <iostream>
#include <utility>
#include <vector>

constexpr int COLUMN_STEP = 2;
constexpr int LEFTMOST_COLUMN = -999;

void place(int city, int parent, int depth, const std::vector<std::vector<int>> &graph,
           std::vector<std::pair<int, int>> &points, int &column) {
    points[city] = {column, depth};
    column += COLUMN_STEP;
    for (int child : graph[city]) {
        if (child != parent) {
            place(child, city, depth + 1, graph, points, column);
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n = 0;
    std::cin >> n;
    std::vector<std::vector<int>> graph(n + 1);
    for (int edge = 1; edge < n; ++edge) {
        int a = 0;
        int b = 0;
        std::cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    std::vector<std::pair<int, int>> points(n + 1);
    int column = LEFTMOST_COLUMN;
    place(1, 0, 0, graph, points, column);
    for (int city = 1; city <= n; ++city) {
        std::cout << points[city].first << ' ' << points[city].second << '\n';
    }
}
