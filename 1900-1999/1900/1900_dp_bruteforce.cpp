#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    if (!(std::cin >> n >> k))
        return 0;

    std::vector<std::vector<int>> cost(n + 1, std::vector<int>(n + 1));
    for (int first = 1; first < n; ++first)
        for (int last = first + 1; last <= n; ++last)
            std::cin >> cost[first][last];

    // Replace the input weights with the sum of trips internal to [first, last].
    for (int first = n - 1; first >= 1; --first) {
        int rowSum = 0;
        for (int last = first + 1; last <= n; ++last) {
            rowSum += cost[first][last];
            cost[first][last] = rowSum + cost[first + 1][last];
        }
    }

    const int groups = k + 1;
    std::vector<std::vector<int>> missed(groups + 1, std::vector<int>(n + 1));
    std::vector<std::vector<int>> split(groups + 1, std::vector<int>(n + 1));
    missed[1] = cost[1];
    for (int group = 2; group <= groups; ++group) {
        for (int last = group; last <= n; ++last) {
            int best = std::numeric_limits<int>::max();
            for (int cut = group - 1; cut < last; ++cut) {
                const int candidate = missed[group - 1][cut] + cost[cut + 1][last];
                if (candidate < best) {
                    best = candidate;
                    split[group][last] = cut;
                }
            }
            missed[group][last] = best;
        }
    }

    std::vector<int> cuts;
    for (int group = groups, last = n; group > 1; --group) {
        last = split[group][last];
        cuts.push_back(last);
    }
    std::reverse(cuts.begin(), cuts.end());
    std::cout << cost[1][n] - missed[groups][n] << '\n';
    for (int i = 0; i < k; ++i)
        std::cout << (i == 0 ? "" : " ") << cuts[i];
    std::cout << '\n';
}
