#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using Value = std::int64_t;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, days, length, moves;
    std::cin >> n >> days >> length >> moves;
    const int positions = n - length + 1;
    std::vector<std::vector<Value>> dp(1, std::vector<Value>(positions));
    std::vector<Value> prefix(n + 1), weight(positions), key(positions);
    std::vector<int> queue(positions);
    int previous_low = 0;

    for (int day = 1; day <= days; ++day) {
        for (int j = 0; j < n; ++j) {
            Value gain;
            std::cin >> gain;
            prefix[j + 1] = prefix[j] + gain;
        }
        for (int x = 0; x < positions; ++x) {
            weight[x] = prefix[x + length] - prefix[x];
        }
        // Keep only move counts that can still finish with exactly the budget.
        const int low = std::max(0, moves - (days - day));
        const int high = std::min(day, moves);
        std::vector<std::vector<Value>> next(high - low + 1, std::vector<Value>(positions));
        for (int used = low; used <= high; ++used) {
            auto &current = next[used - low];
            if (used < day) {
                const auto &stay = dp[used - previous_low];
                for (int x = 0; x < positions; ++x) {
                    current[x] = stay[x] + weight[x];
                }
            }
            if (used == 0) {
                continue;
            }
            const auto &previous = dp[used - 1 - previous_low];
            for (int x = 0; x < positions; ++x) {
                key[x] = previous[x] - prefix[x];
            }
            int head = 0, tail = 0;
            Value best = 0;
            for (int y = 0; y < positions; ++y) {
                if (y >= length) {
                    const int x = y - length;
                    best = std::max(best, previous[x] + weight[x]);
                }
                while (head < tail && key[queue[tail - 1]] <= key[y]) {
                    --tail;
                }
                queue[tail++] = y;
                if (queue[head] <= y - length) {
                    ++head;
                }
                // An overlap contributes one contiguous union, never two copies.
                const Value overlap = key[queue[head]] + prefix[y + length];
                current[y] = std::max(current[y], std::max(overlap, best + weight[y]));
            }
            for (int x = 0; x < positions; ++x) {
                key[x] = previous[x] + prefix[x + length];
            }
            head = tail = 0;
            best = 0;
            for (int y = positions - 1; y >= 0; --y) {
                if (y + length < positions) {
                    const int x = y + length;
                    best = std::max(best, previous[x] + weight[x]);
                }
                while (head < tail && key[queue[tail - 1]] <= key[y]) {
                    --tail;
                }
                queue[tail++] = y;
                if (queue[head] >= y + length) {
                    ++head;
                }
                const Value overlap = key[queue[head]] - prefix[y];
                current[y] = std::max(current[y], std::max(overlap, best + weight[y]));
            }
        }
        dp.swap(next);
        previous_low = low;
    }
    std::cout << *std::max_element(dp[0].begin(), dp[0].end()) << '\n';
}
