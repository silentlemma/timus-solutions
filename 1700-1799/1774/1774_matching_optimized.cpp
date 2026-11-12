#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

const int SHAVES = 2;
const int MAX_TIME = 2000;

struct Edge {
    uint16_t to, next, cap;
};

struct Flow {
    std::vector<Edge> edges;
    std::vector<uint16_t> head, at, level, queue;

    Flow(int nodes, int edgeCount) : head(nodes), at(nodes), level(nodes), queue(nodes) {
        edges.reserve(edgeCount);
        edges.resize(SHAVES);
    }

    void add(int a, int b, int cap) {
        edges.push_back({uint16_t(b), head[a], uint16_t(cap)});
        head[a] = uint16_t(edges.size() - 1);
        edges.push_back({uint16_t(a), head[b], 0});
        head[b] = uint16_t(edges.size() - 1);
    }

    int push(int v, int sink, int limit) {
        if (v == sink)
            return limit;
        while (at[v]) {
            int e = at[v], w = edges[e].to;
            if (edges[e].cap && level[w] == level[v] + 1) {
                int got = push(w, sink, std::min(limit, int(edges[e].cap)));
                if (got) {
                    edges[e].cap -= got;
                    edges[e ^ 1].cap += got;
                    return got;
                }
            }
            at[v] = edges[e].next;
        }
        return 0;
    }

    int solve(int sink, int need) {
        int total = 0;
        while (total < need) {
            std::fill(level.begin(), level.end(), 0);
            at = head;
            int length = 1;
            queue[0] = 0;
            level[0] = 1;
            for (int i = 0; i < length; ++i) {
                int v = queue[i];
                for (int e = head[v]; e; e = edges[e].next) {
                    int w = edges[e].to;
                    if (edges[e].cap && !level[w]) {
                        level[w] = level[v] + 1;
                        queue[length++] = w;
                    }
                }
            }
            if (!level[sink])
                break;
            while (total < need) {
                int got = push(0, sink, need - total);
                if (!got)
                    break;
                total += got;
            }
        }
        return total;
    }
};

int main() {
    int n = 0, k = 0;
    if (scanf("%d %d", &n, &k) != SHAVES)
        return 0;
    std::vector<int> start(n), end(n), cuts;
    uint16_t index[MAX_TIME + 1] = {};
    for (int i = 0; i < n; ++i) {
        int stay = 0;
        if (scanf("%d %d", &start[i], &stay) != SHAVES)
            return 0;
        end[i] = start[i] + stay;
        index[start[i]] = index[end[i]] = 1;
    }
    for (int t = 0; t <= MAX_TIME; ++t)
        if (index[t]) {
            index[t] = uint16_t(cuts.size());
            cuts.push_back(t);
        }
    int blocks = int(cuts.size()) - 1, sink = n + blocks + 1, edgeCount = n + blocks;
    for (int i = 0; i < n; ++i) {
        start[i] = index[start[i]];
        end[i] = index[end[i]];
        edgeCount += end[i] - start[i];
    }
    Flow flow(sink + 1, SHAVES * (edgeCount + 1));
    for (int i = 0; i < n; ++i) {
        flow.add(0, i + 1, SHAVES);
        for (int j = start[i]; j < end[i]; ++j)
            flow.add(i + 1, n + j + 1, std::min(SHAVES, cuts[j + 1] - cuts[j]));
    }
    for (int j = 0; j < blocks; ++j)
        flow.add(n + j + 1, sink, std::min(SHAVES * n, k * (cuts[j + 1] - cuts[j])));
    if (flow.solve(sink, SHAVES * n) < SHAVES * n) {
        puts("No");
        return 0;
    }
    puts("Yes");
    std::vector<int> dealt(blocks);
    for (int i = 1; i <= n; ++i) {
        int times[SHAVES], used = 0;
        for (int e = flow.head[i]; e; e = flow.edges[e].next) {
            int w = flow.edges[e].to;
            if (w <= n || w >= sink)
                continue;
            int block = w - n - 1;
            for (int count = flow.edges[e ^ 1].cap; count; --count)
                times[used++] = cuts[block] + dealt[block]++ % (cuts[block + 1] - cuts[block]);
        }
        if (times[0] > times[1])
            std::swap(times[0], times[1]);
        printf("%d %d\n", times[0], times[1]);
    }
}
