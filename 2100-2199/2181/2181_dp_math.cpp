#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

constexpr long long MOD = 1000000007;

pair<long long, long long> count_paths(int n, int m, const vector<unsigned char> &down,
                                       const vector<unsigned char> &right, int source_row,
                                       int source_column) {
    vector<long long> dp(m, 0);
    long long upper = 0;
    long long lower = 0;
    for (int row = 0; row < n; ++row) {
        for (int column = 0; column < m; ++column) {
            int index = row * m + column;
            long long value = 0;
            if (row == source_row && column == source_column) {
                value = 1;
            } else {
                if (row > 0 && !down[index - m]) {
                    value = dp[column];
                }
                if (column > 0 && !right[index - 1]) {
                    value += dp[column - 1];
                }
                if (value >= MOD) {
                    value -= MOD;
                }
            }
            dp[column] = value;
            if (row == n - 2 && column == m - 1) {
                upper = value;
            }
            if (row == n - 1 && column == m - 2) {
                lower = value;
            }
        }
    }
    return {upper, lower};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, missing;
    if (!(cin >> n >> m >> missing)) {
        return 0;
    }
    vector<unsigned char> down(n * m, 0);
    vector<unsigned char> right(n * m, 0);
    for (int edge = 0; edge < missing; ++edge) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        if (a == c) {
            right[(a - 1) * m + min(b, d) - 1] = 1;
        } else {
            down[(min(a, c) - 1) * m + b - 1] = 1;
        }
    }
    if (right[0] || down[0] || down[(n - 2) * m + m - 1] || right[(n - 1) * m + m - 2]) {
        cout << 0 << '\n';
        return 0;
    }

    auto upper = count_paths(n, m, down, right, 0, 1);
    auto lower = count_paths(n, m, down, right, 1, 0);
    // Swapping tails cancels every pair that shares an internal vertex.
    long long answer = (upper.first * lower.second - upper.second * lower.first) % MOD;
    answer = (answer + MOD) % MOD;
    cout << answer * 2 % MOD << '\n';
    return 0;
}
