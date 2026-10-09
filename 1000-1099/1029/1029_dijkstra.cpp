#include <cstdio>
#include <functional>
#include <queue>
#include <vector>

const long long INF = 1LL << 62;
const int MOVES = 3;
// up a floor in the same room, or to a neighbouring room on the same floor
const int DI[MOVES] = {1, 0, 0}, DJ[MOVES] = {0, -1, 1};

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 1;
    std::vector<long long> fee(m * n);
    for (long long &f : fee)
        if (scanf("%lld", &f) != 1)
            return 1;
    // Dijkstra over the offices; every office of the first floor is a start
    std::vector<long long> dist(m * n, INF);
    std::vector<int> prev(m * n, -1);
    using Item = std::pair<long long, int>;
    std::priority_queue<Item, std::vector<Item>, std::greater<Item>> heap;
    for (int j = 0; j < n; j++) {
        dist[j] = fee[j];
        heap.push({dist[j], j});
    }
    while (!heap.empty()) {
        auto [d, s] = heap.top();
        heap.pop();
        if (d > dist[s])
            continue;
        int i = s / n, j = s % n;
        for (int k = 0; k < MOVES; k++) {
            int a = i + DI[k], b = j + DJ[k];
            if (a >= m || b < 0 || b >= n)
                continue;
            int t = a * n + b;
            if (d + fee[t] < dist[t]) {
                dist[t] = d + fee[t];
                prev[t] = s;
                heap.push({dist[t], t});
            }
        }
    }
    int best = (m - 1) * n;
    for (int s = best; s < m * n; s++)
        if (dist[s] < dist[best])
            best = s;
    std::vector<int> rooms;
    for (int s = best; s >= 0; s = prev[s])
        rooms.push_back(s % n + 1);
    for (size_t k = rooms.size(); k-- > 0;)
        printf("%d%c", rooms[k], k > 0 ? ' ' : '\n');
}
