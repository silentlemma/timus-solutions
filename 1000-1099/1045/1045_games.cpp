#include <cstdio>
#include <vector>

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2)
        return 0;
    std::vector<std::vector<int>> adj(n + 1);
    for (int i = 0; i + 1 < n; i++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // the destroyed airports are exactly the ones on the way back to k, so a
    // move always goes down the tree rooted at k; a breadth-first order lists
    // parents before children
    std::vector<int> parent(n + 1, 0), order = {k};
    parent[k] = -1;
    for (size_t i = 0; i < order.size(); i++)
        for (int w : adj[order[i]])
            if (w != parent[order[i]]) {
                parent[w] = order[i];
                order.push_back(w);
            }
    // win[v]: the player to move at v wins, that is, some child is a loss
    std::vector<bool> win(n + 1, false);
    for (size_t i = order.size(); i-- > 1;)
        if (!win[order[i]])
            win[parent[order[i]]] = true;
    int best = 0;
    for (int w : adj[k])
        if (!win[w] && (best == 0 || w < best))
            best = w;
    if (best == 0)
        printf("First player loses\n");
    else
        printf("First player wins flying to airport %d\n", best);
}
