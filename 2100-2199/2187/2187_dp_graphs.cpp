#include <algorithm>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

using namespace std;

using Profit = long long;
constexpr Profit NEGATIVE_INFINITY = numeric_limits<Profit>::lowest() / 2;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<Profit> treasure(n), cost(n);
    for (Profit &value : treasure) {
        cin >> value;
    }
    for (int length = 1; length < n; ++length) {
        cin >> cost[length];
    }

    vector<int> first(m), second(m), degree(n);
    for (int edge = 0; edge < m; ++edge) {
        cin >> first[edge] >> second[edge];
        --first[edge];
        --second[edge];
        ++degree[first[edge]];
        ++degree[second[edge]];
    }

    vector<int> offset(n + 1);
    for (int edge = 0; edge < m; ++edge) {
        int u = first[edge], v = second[edge];
        if (degree[u] < degree[v]) {
            ++offset[u + 1];
        } else if (degree[v] < degree[u]) {
            ++offset[v + 1];
        }
    }
    for (int vertex = 0; vertex < n; ++vertex) {
        offset[vertex + 1] += offset[vertex];
    }
    vector<int> next = offset;
    vector<int> adjacent(offset[n]);
    for (int edge = 0; edge < m; ++edge) {
        int u = first[edge], v = second[edge];
        if (degree[u] < degree[v]) {
            adjacent[next[u]++] = v;
        } else if (degree[v] < degree[u]) {
            adjacent[next[v]++] = u;
        }
    }

    vector<int> count(n + 1);
    for (int value : degree) {
        ++count[value + 1];
    }
    for (int value = 0; value < n; ++value) {
        count[value + 1] += count[value];
    }
    vector<int> order(n);
    for (int vertex = 0; vertex < n; ++vertex) {
        order[count[degree[vertex]]++] = vertex;
    }

    // A state stores the profit before paying for the unfinished journey.
    vector<vector<Profit>> states(n);
    states[0].push_back(treasure[0]);
    Profit answer = treasure[0];
    for (int u : order) {
        vector<Profit> current = move(states[u]);
        if (current.empty()) {
            continue;
        }
        Profit best = current[0];
        for (size_t length = 1; length < current.size(); ++length) {
            if (current[length] != NEGATIVE_INFINITY) {
                best = max(best, current[length] - cost[length] + treasure[u]);
            }
        }
        current[0] = best;
        answer = max(answer, best);
        for (int edge = offset[u]; edge < offset[u + 1]; ++edge) {
            vector<Profit> &target = states[adjacent[edge]];
            if (target.size() <= current.size()) {
                target.resize(current.size() + 1, NEGATIVE_INFINITY);
            }
            for (size_t length = 0; length < current.size(); ++length) {
                target[length + 1] = max(target[length + 1], current[length]);
            }
        }
    }
    cout << answer << '\n';
}
