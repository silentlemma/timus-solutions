#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int m;
std::vector<int> parent;
std::vector<std::vector<std::pair<int, long long>>> adj;

static int find(int v) {
    while (parent[v] != v) {
        v = parent[v] = parent[parent[v]];
    }
    return v;
}

// Distances from start within its tree, by an explicit stack.
static std::vector<long long> distances(int start) {
    std::vector<long long> dist(m + 1, -1);
    std::vector<int> stack = {start};
    dist[start] = 0;
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        for (auto [u, r] : adj[v]) {
            if (dist[u] < 0) {
                dist[u] = dist[v] + r;
                stack.push_back(u);
            }
        }
    }
    return dist;
}

int main() {
    int n;
    long long s;
    scanf("%d %d %lld", &m, &n, &s);
    parent.resize(m + 1);
    adj.assign(m + 1, {});
    for (int v = 0; v <= m; v++) {
        parent[v] = v;
    }
    for (int i = 0; i < n; i++) {
        int p, q;
        long long r;
        scanf("%d %d %lld", &p, &q, &r);
        int a = find(p), b = find(q);
        if (a == b) {
            // a cycle, a loop or a second road: drive round it as long as needed
            puts("YES");
            return 0;
        }
        parent[a] = b;
        adj[p].push_back({q, r});
        adj[q].push_back({p, r});
    }
    // a forest: the longest route is a diameter of one of its trees
    long long best = 0;
    std::vector<bool> seen(m + 1, false);
    for (int v = 1; v <= m; v++) {
        if (seen[v]) {
            continue;
        }
        std::vector<long long> d = distances(v);
        int end = v;
        for (int u = 1; u <= m; u++) {
            if (d[u] >= 0) {
                seen[u] = true;
                if (d[u] > d[end]) {
                    end = u;
                }
            }
        }
        std::vector<long long> e = distances(end);
        best = std::max(best, *std::max_element(e.begin(), e.end()));
    }
    puts(best >= s ? "YES" : "NO");
}
