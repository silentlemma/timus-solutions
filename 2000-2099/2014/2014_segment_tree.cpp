#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

constexpr int DAY_SLOTS = 32;
constexpr int HOURS_PER_DAY = 24;
constexpr int MINUTES_PER_HOUR = 60;

std::vector<long long> solve(const std::vector<int> &keys, const std::vector<long long> &amounts) {
    int n = static_cast<int>(keys.size());
    std::vector<int> order(n), ranks(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) { return keys[a] < keys[b]; });
    for (int i = 0; i < n; ++i)
        ranks[order[i]] = i;
    int size = 1;
    while (size < n)
        size <<= 1;
    std::vector<long long> sums(2 * size), prefixes(2 * size), result;
    result.reserve(n);
    for (int i = 0; i < n; ++i) {
        int index = size + ranks[i];
        sums[index] = amounts[i];
        prefixes[index] = std::min(0LL, amounts[i]);
        for (index >>= 1; index; index >>= 1) {
            int left = index << 1, right = left + 1;
            sums[index] = sums[left] + sums[right];
            prefixes[index] = std::min(prefixes[left], sums[left] + prefixes[right]);
        }
        result.push_back(prefixes[1]);
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<int> keys(n);
    std::vector<long long> amounts(n);
    for (int i = 0; i < n; ++i) {
        int day, month, hour, minute;
        char separator;
        std::cin >> amounts[i] >> day >> separator >> month >> hour >> separator >> minute;
        keys[i] = ((month * DAY_SLOTS + day) * HOURS_PER_DAY + hour) * MINUTES_PER_HOUR + minute;
    }
    for (long long value : solve(keys, amounts))
        std::cout << value << '\n';
}
