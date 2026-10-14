#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n, m, root;
    if (scanf("%d %d", &n, &m) != 2 || scanf("%d", &root) != 1)
        return 0;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int k, prev;
        if (scanf("%d %d", &k, &prev) != 2)
            return 0;
        for (int j = 1; j < k; j++) {
            int v;
            if (scanf("%d", &v) != 1)
                return 0;
            adj[prev].push_back(v);
            adj[v].push_back(prev);
            prev = v;
        }
    }
    // depth-first search without recursion, so every other edge joins a
    // vertex to one of its ancestors
    vector<int> parent(n + 1, 0), depth(n + 1, -1), next(n + 1, 0), order = {root};
    depth[root] = 0;
    vector<int> stack = {root};
    while (!stack.empty()) {
        int v = stack.back();
        if (next[v] == (int)adj[v].size()) {
            stack.pop_back();
            continue;
        }
        int u = adj[v][next[v]++];
        if (depth[u] < 0) {
            depth[u] = depth[v] + 1;
            parent[u] = v;
            order.push_back(u);
            stack.push_back(u);
        }
    }
    // every non-tree edge closes a cycle with the tree path between its ends
    vector<bool> onCycle(n + 1, false);        // the edge from v to its parent lies on a cycle
    vector<vector<vector<int>>> cycles(n + 1); // cycles listed at their top vertex
    for (int v = 1; v <= n; v++)
        for (int u : adj[v])
            if (depth[u] < depth[v] && u != parent[v]) {
                vector<int> members;
                for (int x = v; x != u; x = parent[x]) {
                    onCycle[x] = true;
                    members.push_back(x);
                }
                cycles[u].push_back(members);
            }
    // a tree edge to a child of value g is worth g + 1; a cycle fuses into
    // loops on its top vertex: one loop (worth 1) per edge, so its length
    // parity, together with everything hanging from its other vertices
    vector<int> value(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i], g = 0;
        for (int u : adj[v])
            if (parent[u] == v && !onCycle[u])
                g ^= value[u] + 1;
        for (const vector<int> &members : cycles[v]) {
            g ^= (members.size() + 1) % 2; // a cycle has as many edges as vertices
            for (int x : members)
                g ^= value[x];
        }
        value[v] = g;
    }
    printf("%s\n", value[root] ? "First" : "Second");
}
