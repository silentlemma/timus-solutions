#include <algorithm>
#include <cstdio>
#include <vector>

std::vector<std::vector<int>> children;
std::vector<bool> done;
std::vector<int> order;

// a member is appended after all its descendants: the reversed list puts
// everyone before their descendants
void visit(int v) {
    done[v] = true;
    for (int c : children[v])
        if (!done[c])
            visit(c);
    order.push_back(v);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    children.assign(n + 1, {});
    done.assign(n + 1, false);
    for (int v = 1; v <= n; v++)
        for (int c; scanf("%d", &c) == 1 && c != 0;)
            children[v].push_back(c);
    for (int v = 1; v <= n; v++)
        if (!done[v])
            visit(v);
    std::reverse(order.begin(), order.end());
    for (size_t i = 0; i < order.size(); i++)
        printf("%d%c", order[i], i + 1 < order.size() ? ' ' : '\n');
}
