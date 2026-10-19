#include <algorithm>
#include <array>
#include <cstdio>
#include <vector>

using namespace std;

constexpr int MAX_DISCOUNT = 100;
constexpr int MAX_PRICE = 50000;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    array<vector<int>, MAX_DISCOUNT + 1> prices;
    array<vector<long long>, MAX_DISCOUNT + 1> sums;
    array<int, MAX_DISCOUNT + 1> required;
    required.fill(n + 1);
    long long singles = 0;
    for (int i = 0; i < n; i++) {
        int price, discount;
        scanf("%d %d", &price, &discount);
        prices[discount].push_back(price);
        singles += 1LL * price * (MAX_DISCOUNT - discount);
    }
    for (int i = 0; i < m; i++) {
        int count, discount;
        scanf("%d %d", &count, &discount);
        required[discount] = min(required[discount], count);
    }

    array<int, MAX_DISCOUNT + 1> counts{};
    array<long long, MAX_DISCOUNT + 1> price_totals{}, weighted_totals{};
    for (int discount = 0; discount <= MAX_DISCOUNT; discount++) {
        auto &group = prices[discount];
        sort(group.begin(), group.end());
        sums[discount].push_back(0);
        for (int price : group)
            sums[discount].push_back(sums[discount].back() + price);
        counts[discount] = static_cast<int>(group.size());
        price_totals[discount] = sums[discount].back();
        weighted_totals[discount] = price_totals[discount] * discount;
        if (discount > 0) {
            counts[discount] += counts[discount - 1];
            price_totals[discount] += price_totals[discount - 1];
            weighted_totals[discount] += weighted_totals[discount - 1];
        }
    }

    long long best = singles;
    for (int discount = 1; discount <= MAX_DISCOUNT; discount++) {
        if (required[discount] > n)
            continue;
        long long candidate =
            singles + weighted_totals[discount] - discount * price_totals[discount];
        if (candidate >= best)
            continue;
        int need = required[discount] - counts[discount];
        if (need > 0) {
            // Find the least extra cost that supplies enough tickets.
            int low = 0, high = MAX_PRICE * (MAX_DISCOUNT - discount);
            while (low < high) {
                int middle = low + (high - low) / 2;
                int taken = 0;
                for (int other = discount + 1; other <= MAX_DISCOUNT; other++) {
                    const auto &group = prices[other];
                    int limit = middle / (other - discount);
                    taken += static_cast<int>(upper_bound(group.begin(), group.end(), limit) -
                                              group.begin());
                }
                if (taken >= need)
                    high = middle;
                else
                    low = middle + 1;
            }
            int taken = 0;
            for (int other = discount + 1; other <= MAX_DISCOUNT; other++) {
                const auto &group = prices[other];
                int limit = low / (other - discount);
                int count = static_cast<int>(upper_bound(group.begin(), group.end(), limit) -
                                             group.begin());
                taken += count;
                candidate += sums[other][count] * (other - discount);
            }
            // All surplus tickets have the threshold cost.
            candidate -= 1LL * (taken - need) * low;
        }
        best = min(best, candidate);
    }
    printf("%lld.%02lld\n", best / MAX_DISCOUNT, best % MAX_DISCOUNT);
}
