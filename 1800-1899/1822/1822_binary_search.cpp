#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>

const double PERCENT = 100.0;

int n;
long long limit;
std::vector<int> own, order;
std::vector<std::vector<int>> children;

// x = 100 num/den: a noble with c vassals waits for ceil(num c/den) of
// them, so the wait is that order statistic of their ready days
bool readyBy(long long num, long long den) {
    std::vector<long long> ready(n + 1, 0), times;
    for (int v : order) {
        long long c = children[v].size();
        long long need = (num * c + den - 1) / den, wait = 0;
        if (need > 0) {
            times.clear();
            for (int w : children[v]) times.push_back(ready[w]);
            std::nth_element(times.begin(), times.begin() + need - 1, times.end());
            wait = times[need - 1];
        }
        ready[v] = wait + own[v];
    }
    return ready[1] <= limit;
}

int main() {
    if (scanf("%d %lld", &n, &limit) != 2) return 0;
    own.assign(n + 1, 0);
    children.assign(n + 1, {});
    for (int i = 2; i <= n; i++) {
        int parent;
        scanf("%d %d", &parent, &own[i]);
        children[parent].push_back(i);
    }
    order.push_back(1);
    for (size_t i = 0; i < order.size(); i++) {
        for (int w : children[order[i]]) order.push_back(w);
    }
    std::reverse(order.begin(), order.end());
    // the answer is a largest fraction m/c over the vassal counts c
    std::set<int> counts;
    for (int v = 1; v <= n; v++) {
        if (!children[v].empty()) counts.insert(children[v].size());
    }
    std::vector<std::pair<long long, long long>> fractions;
    for (int c : counts) {
        for (int m = 0; m <= c; m++) fractions.push_back({m, c});
    }
    if (fractions.empty()) fractions.push_back({1, 1});
    std::sort(fractions.begin(), fractions.end(), [](const auto &a, const auto &b) {
        return a.first * b.second < b.first * a.second;
    });
    int lo = 0, hi = fractions.size() - 1;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (readyBy(fractions[mid].first, fractions[mid].second)) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    printf("%.8f\n", PERCENT * fractions[lo].first / fractions[lo].second);
    return 0;
}
