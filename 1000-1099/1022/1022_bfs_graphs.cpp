#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    std::vector<std::vector<int>> children(n + 1);
    std::vector<int> parents(n + 1, 0);
    for (int v = 1; v <= n; v++)
        for (int c; scanf("%d", &c) == 1 && c != 0;) {
            children[v].push_back(c);
            parents[c]++;
        }
    // Kahn's algorithm: a member may speak once all its parents have spoken
    std::vector<int> order;
    for (int v = 1; v <= n; v++)
        if (parents[v] == 0)
            order.push_back(v);
    for (size_t i = 0; i < order.size(); i++)
        for (int c : children[order[i]])
            if (--parents[c] == 0)
                order.push_back(c);
    for (size_t i = 0; i < order.size(); i++)
        printf("%d%c", order[i], i + 1 < order.size() ? ' ' : '\n');
}
