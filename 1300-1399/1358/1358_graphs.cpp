#include <cstdio>
#include <vector>

const int STEP = 2;    // columns two apart keep every pair of points farther than 1
const int LIMIT = 999; // the leftmost column, so that 1000 columns fit in [-999, 999]

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a = 0, b = 0;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // column = preorder index, row = depth: the subtrees of the vertices on
    // one row take disjoint ranges of columns, so no two wires cross
    std::vector<int> x(n + 1, 0), y(n + 1, 0);
    std::vector<bool> seen(n + 1, false);
    std::vector<int> stack(1, 1);
    seen[1] = true;
    int order = 0;
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        x[v] = order++ * STEP - LIMIT;
        for (auto it = adj[v].rbegin(); it != adj[v].rend(); ++it)
            if (!seen[*it]) {
                seen[*it] = true;
                y[*it] = y[v] + 1;
                stack.push_back(*it);
            }
    }
    for (int v = 1; v <= n; v++)
        printf("%d %d\n", x[v], y[v]);
    return 0;
}
