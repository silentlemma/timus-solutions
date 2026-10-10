#include <algorithm>
#include <cstdio>
#include <vector>

int n;
std::vector<int> monsters, volleys, memo;

int alive(int mask) {
    int sum = 0;
    for (int i = 0; i < n; i++)
        if (mask >> i & 1)
            sum += monsters[i];
    return sum;
}

// the least damage still to come with these balconies occupied; the
// monsters left after each volley fire once
int damage(int mask) {
    if (!mask)
        return 0;
    if (memo[mask] >= 0)
        return memo[mask];
    int best = -1;
    for (int v : volleys)
        if (mask & v) {
            int rest = mask & ~v, cost = alive(rest) + damage(rest);
            if (best < 0 || cost < best)
                best = cost;
        }
    return memo[mask] = best;
}

int main() {
    if (scanf("%d", &n) != 1)
        return 0;
    monsters.resize(n);
    for (auto &m : monsters)
        if (scanf("%d", &m) != 1)
            return 0;
    // a volley at i clears balconies i - 1, i and i + 1 around the circle
    for (int i = 0; i < n; i++)
        volleys.push_back(1 << (i + n - 1) % n | 1 << i | 1 << (i + 1) % n);
    memo.assign(1 << n, -1);
    printf("%d\n", damage((1 << n) - 1));
}
