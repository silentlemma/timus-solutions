#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

struct Road {
    int u, v, toll, time, height;
};

int n, m, s, f, budget, limit;
vector<Road> roads;
vector<vector<int>> out;

// a route from s to f within the limits using roads no higher than height,
// as road numbers; empty when there is none
vector<int> route(int height) {
    const int NONE = -1;
    // best[v][c]: the least time to v with c tolls paid
    vector<vector<int>> best(n + 1, vector<int>(budget + 1, NONE));
    vector<vector<int>> cameBy(n + 1, vector<int>(budget + 1, NONE));
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> heap;
    best[s][0] = 0;
    heap.push({0, 0, s});
    while (!heap.empty()) {
        auto [time, paid, v] = heap.top();
        heap.pop();
        if (best[v][paid] != time)
            continue;
        // a state is useless if fewer tolls already reach v as fast
        bool beaten = false;
        for (int c = 0; c < paid && !beaten; c++)
            beaten = best[v][c] != NONE && best[v][c] <= time;
        if (beaten)
            continue;
        if (v == f) {
            vector<int> path;
            while (cameBy[v][paid] != NONE) {
                const Road &r = roads[cameBy[v][paid]];
                path.push_back(cameBy[v][paid] + 1);
                paid -= r.toll;
                v = r.u;
            }
            reverse(path.begin(), path.end());
            return path;
        }
        for (int idx : out[v]) {
            const Road &r = roads[idx];
            int nt = time + r.time, np = paid + r.toll;
            if (r.height <= height && np <= budget && nt <= limit &&
                (best[r.v][np] == NONE || nt < best[r.v][np])) {
                best[r.v][np] = nt;
                cameBy[r.v][np] = idx;
                heap.push({nt, np, r.v});
            }
        }
    }
    return {};
}

int main() {
    scanf("%d %d %d %d %d %d", &n, &m, &s, &f, &budget, &limit);
    roads.resize(m);
    out.assign(n + 1, {});
    vector<int> heights;
    for (int i = 0; i < m; i++) {
        Road &r = roads[i];
        scanf("%d %d %d %d %d", &r.u, &r.v, &r.toll, &r.time, &r.height);
        out[r.u].push_back(i);
        heights.push_back(r.height);
    }
    if (s == f) {
        printf("0\n0\n\n");
        return 0;
    }
    // shorter parallel roads first, to avoid obsolete heap entries
    for (auto &edges : out)
        stable_sort(edges.begin(), edges.end(), [](int a, int b) {
            return roads[a].time < roads[b].time;
        });
    // a cheapest route repeats no city, so it pays at most n - 1 tolls
    budget = min(budget, n - 1);
    sort(heights.begin(), heights.end());
    heights.erase(unique(heights.begin(), heights.end()), heights.end());
    auto found = [&](int h) { return !route(h).empty(); };
    if (!found(heights.back())) {
        puts("-1");
        return 0;
    }
    int lo = 0, hi = heights.size() - 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (found(heights[mid]))
            hi = mid;
        else
            lo = mid + 1;
    }
    vector<int> path = route(heights[lo]);
    printf("%d\n%d\n", heights[lo], (int)path.size());
    for (size_t i = 0; i < path.size(); i++)
        printf("%d%c", path[i], i + 1 < path.size() ? ' ' : '\n');
    if (path.empty())
        printf("\n");
}
