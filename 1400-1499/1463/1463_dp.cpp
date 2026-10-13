#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<long long> joy(n + 1, 0);
    for (int i = 1; i <= n; i++)
        scanf("%lld", &joy[i]);
    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < k; i++) {
        int a, b;
        long long c;
        scanf("%d %d %lld", &a, &b, &c);
        adj[a].push_back({b, c});
        adj[b].push_back({a, c});
    }
    // down[v]: the best route that starts at v and goes away from its parent,
    // nxt[v] the next city on it; the routes are in a forest, so each tree once
    vector<long long> down(joy);
    vector<int> nxt(n + 1, 0), parent(n + 1, -1);
    long long best = -1;
    int center = 0, endA = 0, endB = 0;
    for (int root = 1; root <= n; root++) {
        if (parent[root] != -1)
            continue;
        parent[root] = 0;
        vector<int> order, stack = {root};
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            order.push_back(v);
            for (auto [w, c] : adj[v])
                if (parent[w] == -1) {
                    parent[w] = v;
                    stack.push_back(w);
                }
        }
        for (int i = (int)order.size() - 1; i >= 0; i--) {
            int v = order[i];
            pair<long long, int> first = {0, 0}, second = {0, 0}; // through a child, the child
            for (auto [w, c] : adj[v])
                if (w != parent[v]) {
                    pair<long long, int> option = {c + down[w], w};
                    if (option > first) {
                        second = first;
                        first = option;
                    } else if (option > second) {
                        second = option;
                    }
                }
            down[v] = joy[v] + first.first;
            nxt[v] = first.second;
            if (joy[v] + first.first + second.first > best) {
                best = joy[v] + first.first + second.first;
                center = v;
                endA = first.second;
                endB = second.second;
            }
        }
    }
    vector<int> left, right;
    for (int a = endA; a; a = nxt[a])
        left.push_back(a);
    for (int b = endB; b; b = nxt[b])
        right.push_back(b);
    reverse(left.begin(), left.end());
    left.push_back(center);
    left.insert(left.end(), right.begin(), right.end());
    printf("%lld\n%d\n", best, (int)left.size());
    for (size_t i = 0; i < left.size(); i++)
        printf("%d%c", left[i], i + 1 == left.size() ? '\n' : ' ');
}
