#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, q;
    std::cin >> n >> q;
    std::vector<long long> gain(n);
    for (auto &value : gain) {
        std::cin >> value;
    }
    long long total = 0;
    for (auto &value : gain) {
        long long speed;
        std::cin >> speed;
        total += value - speed;
        value = total;
    }

    std::vector<long long> suffix(n);
    long long minimum = gain.back();
    for (int i = n - 1; i >= 0; --i) {
        minimum = std::min(minimum, gain[i]);
        suffix[i] = minimum;
    }

    std::vector<long long> thresholds;
    std::vector<int> times;
    long long peak = 0;
    for (int i = 0; i < n; ++i) {
        // Avoiding an earlier overtake loses max(0, peak - distance) feet.
        if (suffix[i] > peak) {
            thresholds.push_back(suffix[i]);
            times.push_back(i + 1);
        }
        peak = std::max(peak, gain[i]);
    }

    while (q--) {
        long long distance;
        std::cin >> distance;
        auto position = std::upper_bound(thresholds.begin(), thresholds.end(), distance);
        if (position == thresholds.end()) {
            std::cout << -1 << '\n';
        } else {
            std::cout << times[position - thresholds.begin()] << '\n';
        }
    }
}
