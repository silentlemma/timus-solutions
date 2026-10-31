#include <cstdio>
#include <unordered_map>
#include <vector>

int n;
std::vector<int> monsters, volleys;
std::unordered_map<int, int> memo;

// cache damage plus the living sum; each successor then needs one lookup.
// store only reachable masks, rather than all 2^n subsets.
int damage(int mask) {
    if (mask == 0)
        return 0;
    auto found = memo.find(mask);
    if (found != memo.end())
        return found->second;
    int best = -1, sum = 0;
    for (int i = 0; i < n; ++i) {
        if (mask >> i & 1)
            sum += monsters[i];
        int rest = mask & ~volleys[i];
        if (rest != mask) {
            int cost = damage(rest);
            if (best < 0 || cost < best)
                best = cost;
        }
    }
    return memo[mask] = best + sum;
}

int main() {
    scanf("%d", &n);
    monsters.resize(n);
    int total = 0;
    for (int &value : monsters) {
        scanf("%d", &value);
        total += value;
    }
    for (int i = 0; i < n; ++i)
        volleys.push_back(1 << ((i + n - 1) % n) | 1 << i | 1 << ((i + 1) % n));
    printf("%d\n", damage((1 << n) - 1) - total);
}
