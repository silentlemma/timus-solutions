#include <iostream>
#include <limits>
#include <vector>

long long solve(const std::vector<std::vector<long long>> &cost, const std::vector<int> &plants) {
    int n = static_cast<int>(cost.size());
    std::vector<long long> best(n, std::numeric_limits<long long>::max());
    std::vector<bool> used(n);
    for (int v : plants)
        best[v] = 0;
    long long answer = 0;
    for (int step = 0; step < n; ++step) {
        int vertex = -1;
        for (int v = 0; v < n; ++v)
            if (!used[v] && (vertex < 0 || best[v] < best[vertex]))
                vertex = v;
        answer += best[vertex];
        used[vertex] = true;
        for (int v = 0; v < n; ++v)
            if (!used[v] && cost[vertex][v] < best[v])
                best[v] = cost[vertex][v];
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    if (!(std::cin >> n >> k))
        return 0;
    std::vector<int> plants(k);
    for (int &v : plants) {
        std::cin >> v;
        --v;
    }
    std::vector<std::vector<long long>> cost(n, std::vector<long long>(n));
    for (auto &row : cost)
        for (auto &value : row)
            std::cin >> value;
    std::cout << solve(cost, plants) << '\n';
}
