#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> rating(n + 1), parent(n + 1, 0);
    for (int v = 1; v <= n; v++)
        if (scanf("%d", &rating[v]) != 1)
            return 0;
    // children as linked lists: first[v], then next[c] for the next sibling
    std::vector<int> first(n + 1, 0), next(n + 1, 0);
    int child, boss;
    while (scanf("%d %d", &child, &boss) == 2 && child != 0) {
        parent[child] = boss;
        next[child] = first[boss];
        first[boss] = child;
    }
    // a breadth-first order from the roots puts every boss before the subordinates
    std::vector<int> order;
    for (int v = 1; v <= n; v++)
        if (parent[v] == 0)
            order.push_back(v);
    for (size_t i = 0; i < order.size(); i++)
        for (int c = first[order[i]]; c != 0; c = next[c])
            order.push_back(c);
    // take[v], skip[v]: the best sum in the subtree of v with v invited or not
    std::vector<int> take(n + 1, 0), skip(n + 1, 0);
    int total = 0;
    for (size_t i = order.size(); i-- > 0;) {
        int v = order[i];
        take[v] += rating[v];
        int best = std::max(take[v], skip[v]);
        if (parent[v] == 0) {
            total += best;
        } else {
            take[parent[v]] += skip[v];
            skip[parent[v]] += best;
        }
    }
    printf("%d\n", total);
}
