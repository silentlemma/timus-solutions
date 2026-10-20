#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    long long one_way, two_way;
    std::cin >> n >> m >> one_way >> two_way;
    std::vector<std::vector<int>> graph(n), reverse(n);
    for (int i = 0; i < m; ++i) {
        int from, to;
        std::cin >> from >> to;
        --from;
        --to;
        graph[from].push_back(to);
        reverse[to].push_back(from);
    }

    std::vector<char> seen(n, false);
    std::vector<int> order, stack;
    order.reserve(n);
    stack.reserve(n + m);
    for (int root = 0; root < n; ++root) {
        if (seen[root]) {
            continue;
        }
        stack.push_back(root);
        while (!stack.empty()) {
            int vertex = stack.back();
            stack.pop_back();
            // A complemented vertex marks the return from its DFS call.
            if (vertex < 0) {
                order.push_back(~vertex);
            } else if (!seen[vertex]) {
                seen[vertex] = true;
                stack.push_back(~vertex);
                for (int next : graph[vertex]) {
                    if (!seen[next]) {
                        stack.push_back(next);
                    }
                }
            }
        }
    }

    std::vector<int> component(n, -1);
    for (auto it = order.rbegin(); it != order.rend(); ++it) {
        int root = *it;
        if (component[root] != -1) {
            continue;
        }
        component[root] = root;
        stack.push_back(root);
        while (!stack.empty()) {
            int vertex = stack.back();
            stack.pop_back();
            for (int next : reverse[vertex]) {
                if (component[next] == -1) {
                    component[next] = root;
                    stack.push_back(next);
                }
            }
        }
    }

    std::fill(seen.begin(), seen.end(), false);
    long long answer = 0;
    for (int root = 0; root < n; ++root) {
        if (seen[root]) {
            continue;
        }
        long long vertices = 0, components = 0;
        seen[root] = true;
        stack.push_back(root);
        while (!stack.empty()) {
            int vertex = stack.back();
            stack.pop_back();
            ++vertices;
            components += component[vertex] == vertex;
            for (int next : graph[vertex]) {
                if (!seen[next]) {
                    seen[next] = true;
                    stack.push_back(next);
                }
            }
            for (int next : reverse[vertex]) {
                if (!seen[next]) {
                    seen[next] = true;
                    stack.push_back(next);
                }
            }
        }
        long long cost = (vertices - 1) * two_way;
        if (one_way < two_way) {
            long long tree = (vertices - components) * two_way + (components - 1) * one_way;
            cost = std::min(tree, vertices * one_way);
        }
        answer += cost;
    }
    std::cout << answer << '\n';
}
