#include <algorithm>
#include <cstdio>
#include <vector>

struct Edge {
    int to;
    long long s, w;
};

int main() {
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    std::vector<int> from(m), to(m);
    std::vector<long long> s(m), w(m);
    int size = n;
    for (int i = 0; i < m; i++) {
        scanf("%d %d %lld %lld", &from[i], &to[i], &s[i], &w[i]);
        size = std::max({size, from[i], to[i]});
    }
    std::vector<std::vector<Edge>> adj(size + 1);
    std::vector<int> indegree(size + 1, 0);
    for (int i = 0; i < m; i++) {
        adj[from[i]].push_back({to[i], s[i], w[i]});
        indegree[to[i]]++;
    }

    // The best route maximizes its smallest ratio s / w, stored as a
    // numerator and denominator; 1 / 0 stands for the empty route at 1.
    std::vector<long long> num(size + 1, 0), den(size + 1, 0);
    std::vector<char> reached(size + 1, 0);
    reached[1] = 1;
    num[1] = 1;
    std::vector<int> order;
    for (int v = 1; v <= size; v++)
        if (indegree[v] == 0) order.push_back(v);
    for (size_t head = 0; head < order.size(); head++) {
        int u = order[head];
        for (const Edge &e : adj[u]) {
            if (--indegree[e.to] == 0) order.push_back(e.to);
            if (!reached[u]) continue;
            long long a = num[u], b = den[u];
            if (e.s * b < a * e.w) a = e.s, b = e.w;
            if (!reached[e.to] || num[e.to] * b < a * den[e.to]) {
                reached[e.to] = 1;
                num[e.to] = a;
                den[e.to] = b;
            }
        }
    }

    for (int i = 0; i < q; i++) {
        long long price_s, price_w;
        scanf("%lld %lld", &price_s, &price_w);
        bool good = reached[n] && price_s * num[n] > price_w * den[n];
        puts(good ? "YES" : "NO");
    }
    return 0;
}
