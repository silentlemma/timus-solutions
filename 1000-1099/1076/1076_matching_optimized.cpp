#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <limits>

constexpr int MAX_SIZE = 150;
constexpr int INF = std::numeric_limits<int>::max() / 2;
using Matrix = std::array<std::array<uint8_t, MAX_SIZE + 1>, MAX_SIZE + 1>;
using Indices = std::array<int, MAX_SIZE + 1>;

int maximumSaved(const Matrix &amounts, int n) {
    Indices rowPrice{}, colPrice{}, owner{}, previous{}, unmatched{};
    int unmatchedCount = 0;
    // Match free row maxima first, where the reduced cost is already zero.
    for (int row = 1; row <= n; ++row) {
        int largest = *std::max_element(amounts[row].begin() + 1, amounts[row].begin() + n + 1);
        rowPrice[row] = -largest;
        int col = 1;
        while (col <= n && (amounts[row][col] != largest || owner[col] != 0))
            ++col;
        if (col <= n)
            owner[col] = row;
        else
            unmatched[unmatchedCount++] = row;
    }

    for (int i = 0; i < unmatchedCount; ++i) {
        Indices slack{}, remaining{}, visited{};
        slack.fill(INF);
        for (int j = 0; j < n; ++j)
            remaining[j] = j + 1;
        int left = n, visitedCount = 0, col = 0;
        owner[0] = unmatched[i];
        while (true) {
            visited[visitedCount++] = col;
            int row = owner[col], delta = INF, best = 0;
            for (int pos = 0; pos < left; ++pos) {
                int j = remaining[pos];
                int reduced = -amounts[row][j] - rowPrice[row] - colPrice[j];
                if (reduced < slack[j]) {
                    slack[j] = reduced;
                    previous[j] = col;
                }
                if (slack[j] < delta ||
                    (slack[j] == delta && owner[j] == 0 && owner[remaining[best]] != 0)) {
                    delta = slack[j];
                    best = pos;
                }
            }
            if (delta != 0) {
                for (int pos = 0; pos < visitedCount; ++pos) {
                    int j = visited[pos];
                    rowPrice[owner[j]] += delta;
                    colPrice[j] -= delta;
                }
                for (int pos = 0; pos < left; ++pos)
                    slack[remaining[pos]] -= delta;
            }
            col = remaining[best];
            if (owner[col] == 0)
                break;
            remaining[best] = remaining[--left];
        }
        while (col != 0) {
            owner[col] = owner[previous[col]];
            col = previous[col];
        }
    }
    int saved = 0;
    for (int col = 1; col <= n; ++col)
        saved += amounts[owner[col]][col];
    return saved;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    Matrix amounts{};
    int total = 0;
    for (int row = 1; row <= n; ++row)
        for (int col = 1; col <= n; ++col) {
            int amount;
            scanf("%d", &amount);
            amounts[row][col] = static_cast<uint8_t>(amount);
            total += amount;
        }
    printf("%d\n", total - maximumSaved(amounts, n));
}
