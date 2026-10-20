#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    constexpr int HALF_DIGIT = 5;
    int n;
    std::cin >> n;
    std::vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> x[i] >> y[i];
    }

    std::vector<std::vector<long long>> cross(n, std::vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cross[i][j] = x[i] * y[j] - y[i] * x[j];
        }
    }
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += cross[i][(i + 1) % n];
    }

    // Scores are doubled areas; an edge places no restriction on the minimum.
    std::vector<std::vector<long long>> dp(n, std::vector<long long>(n));
    for (int i = 0; i + 1 < n; ++i) {
        dp[i][i + 1] = total;
    }
    for (int left = n - 2; left >= 0; --left) {
        for (int right = left + 2; right < n; ++right) {
            long long best = 0;
            for (int middle = left + 1; middle < right; ++middle) {
                long long candidate = dp[left][middle];
                if (candidate <= best) {
                    continue;
                }
                candidate = std::min(candidate, dp[middle][right]);
                if (candidate <= best) {
                    continue;
                }
                long long area = cross[left][middle] + cross[middle][right] - cross[left][right];
                best = std::max(best, std::min(candidate, area));
            }
            dp[left][right] = best;
        }
    }

    long long answer = dp[0][n - 1];
    std::cout << answer / 2 << '.' << answer % 2 * HALF_DIGIT << '\n';
}
