#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>

const int SHAVES = 2;

struct Edge {
    int to, cap;
};

std::vector<Edge> edges;
std::vector<std::vector<int>> out;
std::vector<int> level, at;

int add(int a, int b, int cap) {
    out[a].push_back(edges.size());
    edges.push_back({b, cap});
    out[b].push_back(edges.size());
    edges.push_back({a, 0});
    return edges.size() - 2;
}

int push(int v, int sink, int limit) {
    if (v == sink) return limit;
    for (; at[v] < (int)out[v].size(); at[v]++) {
        int e = out[v][at[v]];
        if (edges[e].cap && level[edges[e].to] == level[v] + 1) {
            int got = push(edges[e].to, sink, std::min(limit, edges[e].cap));
            if (got) {
                edges[e].cap -= got;
                edges[e ^ 1].cap += got;
                return got;
            }
        }
    }
    return 0;
}

int maxFlow(int source, int sink) {
    int total = 0;
    while (true) {
        level.assign(out.size(), -1);
        level[source] = 0;
        std::queue<int> queue;
        queue.push(source);
        while (!queue.empty()) {
            int v = queue.front();
            queue.pop();
            for (int e : out[v]) {
                if (edges[e].cap && level[edges[e].to] < 0) {
                    level[edges[e].to] = level[v] + 1;
                    queue.push(edges[e].to);
                }
            }
        }
        if (level[sink] < 0) return total;
        at.assign(out.size(), 0);
        while (int got = push(source, sink, SHAVES)) total += got;
    }
}

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    std::vector<int> come(n), stay(n), cuts;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &come[i], &stay[i]);
        cuts.push_back(come[i]);
        cuts.push_back(come[i] + stay[i]);
    }
    // minutes between consecutive arrivals and departures see the same mages,
    // so they form blocks: a block of L minutes shaves k L times, at most
    // min(L, 2) of them on one mage
    std::sort(cuts.begin(), cuts.end());
    cuts.erase(std::unique(cuts.begin(), cuts.end()), cuts.end());
    int blocks = cuts.size() - 1, source = n + blocks, sink = source + 1;
    out.assign(sink + 1, {});
    std::vector<std::vector<std::pair<int, int>>> links(n);
    for (int i = 0; i < n; i++) {
        add(source, i, SHAVES);
        for (int j = 0; j < blocks; j++) {
            if (come[i] <= cuts[j] && cuts[j + 1] <= come[i] + stay[i]) {
                int cap = std::min(cuts[j + 1] - cuts[j], SHAVES);
                links[i].push_back({j, add(i, n + j, cap)});
            }
        }
    }
    for (int j = 0; j < blocks; j++) add(n + j, sink, k * (cuts[j + 1] - cuts[j]));
    if (maxFlow(source, sink) < SHAVES * n) {
        puts("No");
        return 0;
    }
    // inside a block the shaves are dealt out round the minutes, so the two
    // shaves of one mage fall on different minutes and no minute gets more
    // than k of them
    std::vector<int> dealt(blocks, 0);
    puts("Yes");
    for (int i = 0; i < n; i++) {
        std::vector<int> times;
        for (auto [j, e] : links[i]) {
            for (int u = 0; u < edges[e ^ 1].cap; u++) {
                times.push_back(cuts[j] + dealt[j]++ % (cuts[j + 1] - cuts[j]));
            }
        }
        std::sort(times.begin(), times.end());
        printf("%d %d\n", times[0], times[1]);
    }
    return 0;
}
