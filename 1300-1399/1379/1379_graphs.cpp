#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <vector>

// weights in grams, times in minutes
const long long TRUCK = 3000000;
const long long CUP = 100;
const long long ORDER = 10000000;
const int DAY = 24 * 60;
const int ROAD = 4;

struct Road {
    int to, time;
    long long limit;
};

int n;
std::vector<std::vector<Road>> adj;

// can a truck of this weight reach n within a day
bool inTime(long long weight) {
    std::vector<int> dist(n + 1, DAY + 1);
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        std::greater<std::pair<int, int>>>
        heap;
    dist[1] = 0;
    heap.push({0, 1});
    while (!heap.empty()) {
        auto [d, v] = heap.top();
        heap.pop();
        if (v == n)
            return true;
        if (d > dist[v])
            continue;
        for (const Road &r : adj[v])
            if (r.limit >= weight && d + r.time < dist[r.to]) {
                dist[r.to] = d + r.time;
                heap.push({dist[r.to], r.to});
            }
    }
    return false;
}

int main() {
    int m = 0;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    if (n == 1) {
        printf("%lld\n", ORDER); // the cups are already there
        return 0;
    }
    adj.assign(n + 1, {});
    std::vector<long long> limits;
    for (int i = 0; i < m; i++) {
        int a = 0, b = 0, t = 0;
        long long limit = 0;
        if (scanf("%d %d %d %lld", &a, &b, &t, &limit) != ROAD)
            return 0;
        adj[a].push_back({b, t, limit});
        adj[b].push_back({a, t, limit});
        if (limit >= TRUCK)
            limits.push_back(limit);
    }
    // the heaviest possible truck weighs as much as some road allows, and
    // fewer roads are open to a heavier one, so search the road limits
    std::sort(limits.begin(), limits.end());
    limits.erase(std::unique(limits.begin(), limits.end()), limits.end());
    long long best = -1;
    int lo = 0, hi = (int)limits.size() - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (inTime(limits[mid])) {
            best = limits[mid];
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    printf("%lld\n", best < 0 ? 0 : std::min(ORDER, (best - TRUCK) / CUP));
    return 0;
}
