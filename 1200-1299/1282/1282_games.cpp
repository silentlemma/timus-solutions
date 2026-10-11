#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::vector<int>> children(n + 1);
    std::vector<int> value(n + 1), depth(n + 1);
    for (int v = 2; v <= n; v++) {
        char kind;
        int parent;
        scanf(" %c %d", &kind, &parent);
        children[parent].push_back(v);
        if (kind == 'L')
            scanf("%d", &value[v]);
    }
    // breadth-first order from the root, then values from the leaves up:
    // the first player moves at even depths and takes the largest result
    std::vector<int> order = {1};
    for (size_t i = 0; i < order.size(); i++)
        for (int c : children[order[i]]) {
            depth[c] = depth[order[i]] + 1;
            order.push_back(c);
        }
    for (int i = order.size() - 1; i >= 0; i--) {
        int v = order[i];
        if (children[v].empty())
            continue;
        int best = value[children[v][0]];
        for (int c : children[v])
            best = depth[v] % 2 == 0 ? std::max(best, value[c]) : std::min(best, value[c]);
        value[v] = best;
    }
    printf(value[1] > 0 ? "+1\n" : value[1] < 0 ? "-1\n" : "0\n");
}
