#include <algorithm>
#include <iostream>

constexpr int MONTHS = 12;
constexpr int DAY_SLOTS = 32;
constexpr int HOURS = 24;
constexpr int MINUTES = 60;
constexpr int CALENDAR_SLOTS = MONTHS * DAY_SLOTS * HOURS * MINUTES;

constexpr int leaf_count() {
    int leaves = 1;
    while (leaves < CALENDAR_SLOTS) {
        leaves *= 2;
    }
    return leaves;
}

struct Summary {
    long long sum;
    long long minimum_prefix;
};

constexpr int LEAVES = leaf_count();
Summary tree[2 * LEAVES];

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int reports = 0;
    std::cin >> reports;
    for (int i = 0; i < reports; ++i) {
        long long amount = 0;
        int day = 0, month = 0, hour = 0, minute = 0;
        char separator = ' ';
        std::cin >> amount >> day >> separator >> month >> hour >> separator >> minute;
        int key = (((month - 1) * DAY_SLOTS + day - 1) * HOURS + hour) * MINUTES + minute;
        int node = LEAVES + key;
        tree[node] = {amount, std::min(0LL, amount)};
        for (node /= 2; node > 0; node /= 2) {
            const Summary left = tree[2 * node];
            const Summary right = tree[2 * node + 1];
            tree[node] = {left.sum + right.sum,
                          std::min(left.minimum_prefix, left.sum + right.minimum_prefix)};
        }
        std::cout << tree[1].minimum_prefix << '\n';
    }
}
