#include <iostream>
#include <utility>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<std::vector<bool>> graph(n, std::vector<bool>(n));
    for (int u = 0; u < n; ++u) {
        for (int v = 0; v < n; ++v) {
            char value;
            std::cin >> value;
            graph[u][v] = value == '1';
        }
    }

    std::vector<bool> used(n);
    std::vector<std::pair<int, int>> pairs;
    for (int u = 0; u < n; ++u) {
        if (used[u]) {
            continue;
        }
        for (int v = 0; v < n; ++v) {
            if (!used[v] && graph[u][v]) {
                used[u] = used[v] = true;
                pairs.emplace_back(u, v);
                break;
            }
        }
    }

    std::vector<int> unmatched;
    for (int u = 0; u < n; ++u) {
        if (!used[u]) {
            unmatched.push_back(u);
        }
    }

    // Unmatched vertices are independent; their degree sum forces a short augmentation.
    for (int pos = 0; pos + 1 < static_cast<int>(unmatched.size()); pos += 2) {
        int u = unmatched[pos];
        int v = unmatched[pos + 1];
        for (int i = 0; i < static_cast<int>(pairs.size()); ++i) {
            int a = pairs[i].first;
            int b = pairs[i].second;
            if (graph[u][a] && graph[v][b]) {
                pairs[i] = {u, a};
                pairs.emplace_back(v, b);
                break;
            }
            if (graph[u][b] && graph[v][a]) {
                pairs[i] = {u, b};
                pairs.emplace_back(v, a);
                break;
            }
        }
    }

    int triangle = -1;
    int extra = -1;
    if (unmatched.size() % 2 == 1) {
        extra = unmatched.back();
        // More than half the remaining vertices are friends of the extra vertex.
        for (int i = 0; i < static_cast<int>(pairs.size()); ++i) {
            if (graph[extra][pairs[i].first] && graph[extra][pairs[i].second]) {
                triangle = i;
                break;
            }
        }
    }

    std::cout << "YES\n" << pairs.size() << '\n';
    for (int i = 0; i < static_cast<int>(pairs.size()); ++i) {
        constexpr int triangle_size = 3;
        std::cout << (i == triangle ? triangle_size : 2) << ' ' << pairs[i].first + 1 << ' '
                  << pairs[i].second + 1;
        if (i == triangle) {
            std::cout << ' ' << extra + 1;
        }
        std::cout << '\n';
    }
}
