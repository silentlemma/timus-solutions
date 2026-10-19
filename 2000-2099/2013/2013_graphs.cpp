#include <iostream>
#include <string>
#include <vector>

constexpr int UNREACHED = -2;
constexpr int UNKNOWN = -1;
constexpr int MAX_EDGES = 100000;

std::vector<int> solve(const std::vector<int> &values, const std::vector<int> &offsets,
                       const std::vector<int> &edges) {
    int n = static_cast<int>(values.size());
    std::vector<int> entry(n, UNREACHED), pending;
    pending.reserve(2 * n);
    entry[0] = 0;
    pending.push_back(0);
    for (std::size_t head = 0; head < pending.size(); ++head) {
        int vertex = pending[head];
        int offered = values[vertex] ? values[vertex] : entry[vertex];
        for (int at = offsets[vertex]; at < offsets[vertex + 1]; ++at) {
            int target = edges[at], old = entry[target];
            int merged = old == UNREACHED ? offered : old == offered ? old : UNKNOWN;
            if (old != merged) {
                entry[target] = merged;
                pending.push_back(target);
            }
        }
    }
    return entry;
}

std::string word(int value) {
    if (value == UNKNOWN)
        return "unknown";
    return value ? std::to_string(value) : "sober";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<int> values(n), offsets(n + 1), edges;
    edges.reserve(MAX_EDGES);
    for (int i = 0; i < n; ++i) {
        int degree;
        std::cin >> values[i] >> degree;
        for (int j = 0; j < degree; ++j) {
            int target;
            std::cin >> target;
            edges.push_back(target - 1);
        }
        offsets[i + 1] = static_cast<int>(edges.size());
    }
    auto entry = solve(values, offsets, edges);
    for (int i = 0; i < n; ++i) {
        std::cout << word(entry[i]) << ' ' << word(values[i] ? values[i] : entry[i]) << '\n';
    }
}
