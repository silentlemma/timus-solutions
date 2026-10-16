#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <unordered_map>
#include <vector>

int n;
std::vector<uint32_t> cover;
std::unordered_map<uint32_t, int> failed;
std::vector<int> drops;

// pick at most budget cities covering the set left, appending to drops
bool search(uint32_t left, int budget) {
    if (!left) return true;
    auto it = failed.find(left);
    if (budget == 0 || (it != failed.end() && it->second >= budget)) return false;
    std::vector<int> gain(n);
    int best = 0;
    for (int v = 0; v < n; v++) {
        gain[v] = __builtin_popcount(cover[v] & left);
        best = std::max(best, gain[v]);
    }
    if (__builtin_popcount(left) > budget * best) {
        failed[left] = budget;
        return false;
    }
    // the uncovered city with the fewest cities able to hit it
    int u = -1;
    for (int v = 0; v < n; v++) {
        if ((left >> v & 1) &&
            (u < 0 || __builtin_popcount(cover[v]) < __builtin_popcount(cover[u]))) {
            u = v;
        }
    }
    std::vector<int> options;
    for (int v = 0; v < n; v++) {
        if (cover[u] >> v & 1) options.push_back(v);
    }
    std::stable_sort(options.begin(), options.end(),
                     [&](int a, int b) { return gain[a] > gain[b]; });
    std::vector<uint32_t> tried;
    for (int v : options) {
        uint32_t hit = cover[v] & left;
        // skip a drop that hits only part of what a tried one hits
        bool dominated = false;
        for (uint32_t t : tried) dominated |= (hit & ~t) == 0;
        if (dominated) continue;
        tried.push_back(hit);
        drops.push_back(v);
        if (search(left & ~hit, budget - 1)) return true;
        drops.pop_back();
    }
    failed[left] = budget;
    return false;
}

int main() {
    int r;
    if (scanf("%d %d", &n, &r) != 2) return 0;
    std::vector<int> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%d %d", &x[i], &y[i]);
    // cover[i]: the cities a bottle dropped on city i destroys
    cover.assign(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int dx = x[i] - x[j], dy = y[i] - y[j];
            if (dx * dx + dy * dy <= r * r) cover[i] |= 1u << j;
        }
    }
    uint32_t everything = (1u << n) - 1;
    int budget = 1;
    while (!search(everything, budget)) budget++;
    printf("%d\n", (int)drops.size());
    for (size_t i = 0; i < drops.size(); i++) printf(i ? " %d" : "%d", drops[i] + 1);
    puts("");
    return 0;
}
