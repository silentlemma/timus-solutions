#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int n = 0, m = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> cost, caps; // caps as a mask over 1..n
    for (int i = 0; i < n; i++) {
        int price = 0;
        if (scanf("%d", &price) != 1)
            return 0;
        cost.push_back(price);
        caps.push_back(1 << i);
    }
    if (scanf("%d", &m) != 1)
        return 0;
    for (int j = 0; j < m; j++) {
        int price = 0, size = 0, mask = 0;
        if (scanf("%d %d", &price, &size) != 2)
            return 0;
        for (int k = 0; k < size; k++) {
            int cap = 0;
            if (scanf("%d", &cap) != 1)
                return 0;
            mask |= 1 << (cap - 1);
        }
        cost.push_back(price);
        caps.push_back(mask);
    }
    int count = 0;
    if (scanf("%d", &count) != 1)
        count = 0;
    // the wanted caps get the bits 0, 1, ... of a smaller mask
    std::vector<int> bit(n, 0);
    int wanted = 0;
    for (int k = 0; k < count; k++) {
        int cap = 0;
        if (scanf("%d", &cap) == 1 && bit[cap - 1] == 0)
            bit[cap - 1] = 1 << wanted++;
    }
    int full = (1 << wanted) - 1;
    // offers that hold each wanted cap, as a price and the bits they leave
    std::vector<std::vector<std::pair<int, int>>> byLow(wanted);
    for (size_t j = 0; j < cost.size(); j++) {
        int mask = 0;
        for (int i = 0; i < n; i++) {
            if (caps[j] >> i & 1)
                mask |= bit[i];
        }
        for (int i = 0; i < wanted; i++) {
            if (mask >> i & 1)
                byLow[i].push_back({cost[j], full & ~mask});
        }
    }
    // cheapest[s]: the least money that buys every cap of the set s; some
    // offer must hold its lowest cap
    std::vector<int> cheapest(full + 1, 0);
    for (int s = 1; s <= full; s++) {
        int low = __builtin_ctz(s), least = -1;
        for (auto &offer : byLow[low]) {
            int value = offer.first + cheapest[s & offer.second];
            if (least < 0 || value < least)
                least = value;
        }
        cheapest[s] = least;
    }
    printf("%d\n", cheapest[full]);
    return 0;
}
