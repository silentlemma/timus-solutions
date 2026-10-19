#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <vector>

constexpr int INDEX_BITS = 10;
constexpr int OUTPUT_DIGITS = 10;
constexpr int INDEX_MASK = (1 << INDEX_BITS) - 1;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i)
        std::cin >> x[i] >> y[i];
    std::vector<int> order(n), position(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) {
        if (y[a] != y[b])
            return y[a] > y[b];
        if (x[a] != x[b])
            return x[a] < x[b];
        return a < b;
    });
    std::vector<long long> px(n + 1), py(n + 1), best(n + 1);
    for (int i = 0; i < n; ++i) {
        position[order[i]] = i;
        px[i + 1] = px[i] + x[order[i]];
        py[i + 1] = py[i] + y[order[i]];
    }
    auto record = [&](int k, long long a, long long b) {
        best[k] = std::max(best[k], a * a + b * b);
        a = px[n] - a;
        b = py[n] - b;
        best[n - k] = std::max(best[n - k], a * a + b * b);
    };
    for (int k = 0; k <= n; ++k)
        record(k, px[k], py[k]);
    std::vector<int> events;
    events.reserve(n * (n - 1) / 2);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (y[i] == y[j])
                continue;
            int high = y[i] > y[j] ? i : j;
            int low = i + j - high;
            events.push_back((high << INDEX_BITS) | low);
        }
    }
    auto compare = [&](int a, int b) {
        int ah = a >> INDEX_BITS, al = a & INDEX_MASK;
        int bh = b >> INDEX_BITS, bl = b & INDEX_MASK;
        long long left = (x[al] - x[ah]) * (y[bh] - y[bl]);
        long long right = (x[bl] - x[bh]) * (y[ah] - y[al]);
        return left < right;
    };
    std::sort(events.begin(), events.end(), compare);
    std::vector<int> ends(n, -1), starts;
    std::vector<std::pair<int, int>> intervals;
    for (std::size_t at = 0; at < events.size();) {
        std::size_t after = at + 1;
        while (after < events.size() && !compare(events[at], events[after]))
            ++after;
        if (after == at + 1) {
            int a = position[events[at] >> INDEX_BITS];
            int b = position[events[at] & INDEX_MASK];
            int left = std::min(a, b);
            int first = order[left], second = order[left + 1];
            std::swap(order[left], order[left + 1]);
            position[first] = left + 1;
            position[second] = left;
            int k = left + 1;
            px[k] += x[second] - x[first];
            py[k] += y[second] - y[first];
            record(k, px[k], py[k]);
        } else {
            starts.clear();
            intervals.clear();
            for (std::size_t i = at; i < after; ++i) {
                int a = position[events[i] >> INDEX_BITS];
                int b = position[events[i] & INDEX_MASK];
                if (a > b)
                    std::swap(a, b);
                if (ends[a] < 0)
                    starts.push_back(a);
                ends[a] = std::max(ends[a], b);
            }
            std::sort(starts.begin(), starts.end());
            for (int left : starts) {
                int right = ends[left];
                ends[left] = -1;
                if (!intervals.empty() && left <= intervals.back().second) {
                    intervals.back().second = std::max(intervals.back().second, right);
                } else {
                    intervals.emplace_back(left, right);
                }
            }
            for (auto [left, right] : intervals) {
                std::reverse(order.begin() + left, order.begin() + right + 1);
                long long a = px[left], b = py[left];
                for (int i = left; i <= right; ++i) {
                    int id = order[i];
                    position[id] = i;
                    a += x[id];
                    b += y[id];
                    px[i + 1] = a;
                    py[i + 1] = b;
                    if (i < right)
                        record(i + 1, a, b);
                }
            }
        }
        at = after;
    }
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS);
    for (int k = 1; k <= n; ++k)
        std::cout << std::sqrt(static_cast<double>(best[k])) << '\n';
}
