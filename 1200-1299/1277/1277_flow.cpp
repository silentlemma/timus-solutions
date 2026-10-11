#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>

std::vector<int> head, to, cap, nxt, level, current;
int sink;

void arc(int a, int b, int c) {
    to.push_back(b), cap.push_back(c), nxt.push_back(head[a]), head[a] = to.size() - 1;
    to.push_back(a), cap.push_back(0), nxt.push_back(head[b]), head[b] = to.size() - 1;
}

int push(int u, int limit) {
    if (u == sink)
        return limit;
    for (; current[u] >= 0; current[u] = nxt[current[u]]) {
        int e = current[u], v = to[e];
        if (cap[e] && level[v] == level[u] + 1) {
            int got = push(v, std::min(limit, cap[e]));
            if (got) {
                cap[e] -= got, cap[e ^ 1] += got;
                return got;
            }
        }
    }
    return 0;
}

int main() {
    int k, n, m, s, f;
    scanf("%d %d %d %d %d", &k, &n, &m, &s, &f);
    std::vector<int> cost(n);
    for (int &c : cost)
        scanf("%d", &c);
    if (s == f) {
        printf("NO\n");
        return 0;
    }
    // station v enters at 2v and leaves at 2v + 1; the arc between them
    // costs the police needed there. Museum and refuge cannot be taken,
    // and anything above K counts as too much
    int big = k + 1;
    head.assign(2 * n, -1);
    for (int v = 0; v < n; v++)
        arc(2 * v, 2 * v + 1, v + 1 == s || v + 1 == f ? big : std::min(cost[v], big));
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        a--, b--;
        arc(2 * a + 1, 2 * b, big);
        arc(2 * b + 1, 2 * a, big);
    }
    int source = 2 * (s - 1) + 1;
    sink = 2 * (f - 1);
    // Dinic's blocking flows until the flow exceeds K or nothing gets through
    int flow = 0;
    while (flow <= k) {
        level.assign(2 * n, -1);
        level[source] = 0;
        std::queue<int> queue;
        queue.push(source);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (int e = head[u]; e >= 0; e = nxt[e])
                if (cap[e] && level[to[e]] < 0)
                    level[to[e]] = level[u] + 1, queue.push(to[e]);
        }
        if (level[sink] < 0)
            break;
        current = head;
        while (flow <= k) {
            int got = push(source, big);
            if (!got)
                break;
            flow += got;
        }
    }
    printf(flow <= k ? "YES\n" : "NO\n");
}
