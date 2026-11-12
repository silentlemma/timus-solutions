#include <algorithm>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

int lowest_common_ancestor(int a, int b, const std::vector<int> &depth,
                           const std::vector<std::vector<int>> &ancestor) {
    if (depth[a] < depth[b]) {
        std::swap(a, b);
    }
    int difference = depth[a] - depth[b];
    for (int level = 0; difference > 0; ++level, difference /= 2) {
        if (difference % 2 != 0) {
            a = ancestor[level][a];
        }
    }
    if (a == b) {
        return a;
    }
    for (int level = static_cast<int>(ancestor.size()) - 1; level >= 0; --level) {
        if (ancestor[level][a] != ancestor[level][b]) {
            a = ancestor[level][a];
            b = ancestor[level][b];
        }
    }
    return ancestor[0][a];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    constexpr int ROOT = 1;
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
    int queries = 0;
    std::cin >> queries;
    if (queries == 0) {
        return 0;
    }

    int levels = 1;
    while ((1 << levels) <= n) {
        ++levels;
    }
    std::vector<std::vector<int>> ancestor(levels, std::vector<int>(n + 1, ROOT));
    std::vector<int> depth(n + 1);
    std::vector<int> order{ROOT};
    for (int index = 0; index < n; ++index) {
        const int city = order[index];
        for (int neighbor : graph[city]) {
            if (neighbor != ancestor[0][city]) {
                ancestor[0][neighbor] = city;
                depth[neighbor] = depth[city] + 1;
                order.push_back(neighbor);
            }
        }
    }
    for (int level = 1; level < levels; ++level) {
        for (int city = 1; city <= n; ++city) {
            const int halfway = ancestor[level - 1][city];
            ancestor[level][city] = ancestor[level - 1][halfway];
        }
    }

    int leaves = 1;
    while (leaves < n - 1) {
        leaves *= 2;
    }
    const std::pair<int, int> empty{std::numeric_limits<int>::max(), 0};
    std::vector<std::pair<int, int>> minimum(2 * leaves, empty);
    for (int city = 1; city < n; ++city) {
        const int common = lowest_common_ancestor(city, city + 1, depth, ancestor);
        minimum[leaves + city - 1] = {depth[common], common};
    }
    for (int node = leaves - 1; node > 0; --node) {
        minimum[node] = std::min(minimum[2 * node], minimum[2 * node + 1]);
    }

    while (queries-- > 0) {
        int left = 0;
        int right = 0;
        std::cin >> left >> right;
        if (left == right) {
            std::cout << left << '\n';
            continue;
        }
        // The route uses adjacent pairs starting at cities in [left, right).
        auto answer = empty;
        for (left += leaves - 1, right += leaves - 1; left < right; left /= 2, right /= 2) {
            if (left % 2 != 0) {
                answer = std::min(answer, minimum[left++]);
            }
            if (right % 2 != 0) {
                answer = std::min(answer, minimum[--right]);
            }
        }
        std::cout << answer.second << '\n';
    }
}
