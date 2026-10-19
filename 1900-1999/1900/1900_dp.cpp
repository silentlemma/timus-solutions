#include <algorithm>
#include <iostream>
#include <vector>

constexpr int INF = 1000000000;

class Partition {
    const std::vector<std::vector<int>> &cost;
    const std::vector<int> &previous;
    std::vector<int> &current;
    std::vector<int> &parent;

  public:
    Partition(const std::vector<std::vector<int>> &values, const std::vector<int> &before,
              std::vector<int> &after, std::vector<int> &choices)
        : cost(values), previous(before), current(after), parent(choices) {}

    void fill(int left, int right, int first, int last) {
        if (left > right) {
            return;
        }
        const int middle = (left + right) / 2;
        int best = INF;
        int split = first;
        for (int cut = first; cut <= std::min(last, middle - 1); ++cut) {
            const int value = previous[cut] + cost[cut + 1][middle];
            if (value < best) {
                best = value;
                split = cut;
            }
        }
        current[middle] = best;
        parent[middle] = split;
        fill(left, middle - 1, first, split);
        fill(middle + 1, right, split, last);
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    std::cin >> n >> k;
    const int width = n + 1;
    std::vector<std::vector<int>> weights(width, std::vector<int>(width));
    std::vector<std::vector<int>> cost(width, std::vector<int>(width));
    for (int left = 1; left < n; ++left) {
        for (int right = left + 1; right <= n; ++right) {
            std::cin >> weights[left][right];
        }
    }
    for (int left = n - 1; left >= 1; --left) {
        int prefix = 0;
        for (int right = left + 1; right <= n; ++right) {
            prefix += weights[left][right];
            cost[left][right] = cost[left + 1][right] + prefix;
        }
    }
    const int groups = k + 1;
    std::vector<int> previous(width, INF);
    std::vector<std::vector<int>> parent(groups + 1, std::vector<int>(width));
    for (int end = 1; end <= n - groups + 1; ++end) {
        previous[end] = cost[1][end];
    }
    for (int group = 2; group <= groups; ++group) {
        std::vector<int> current(width, INF);
        const int end = n - groups + group;
        Partition layer(cost, previous, current, parent[group]);
        layer.fill(group, end, group - 1, end - 1);
        previous.swap(current);
    }
    std::vector<int> cuts;
    int end = n;
    for (int group = groups; group > 1; --group) {
        end = parent[group][end];
        cuts.push_back(end);
    }
    std::reverse(cuts.begin(), cuts.end());
    std::cout << cost[1][n] - previous[n] << '\n';
    for (int i = 0; i < k; ++i) {
        std::cout << (i == 0 ? "" : " ") << cuts[i];
    }
    std::cout << '\n';
}
