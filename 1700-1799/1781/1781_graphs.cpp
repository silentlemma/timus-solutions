#include <cstdio>
#include <queue>
#include <utility>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<std::vector<int>> grid(n, std::vector<int>(n));
    for (auto &row : grid)
        for (int &v : row) scanf("%d", &v);
    // renumbering contests and rooms together, room j must be free of every
    // later contest, so a contest that uses room b must come no later than
    // contest b: an order of the graph with an edge a -> b for each such use
    std::vector<int> waiting(n, 0), order;
    for (int a = 0; a < n; a++)
        for (int b = 0; b < n; b++)
            if (a != b && grid[a][b]) waiting[b]++;
    std::queue<int> ready;
    for (int v = 0; v < n; v++)
        if (!waiting[v]) ready.push(v);
    while (!ready.empty()) {
        int a = ready.front();
        ready.pop();
        order.push_back(a);
        for (int b = 0; b < n; b++)
            if (a != b && grid[a][b] && --waiting[b] == 0) ready.push(b);
    }
    if ((int)order.size() < n) {
        puts("-1");
        return 0;
    }
    // each swap puts the next contest of the order in its place, so at most
    // n - 1 swaps are needed
    std::vector<int> where(n), here(n);
    for (int v = 0; v < n; v++) where[v] = here[v] = v;
    std::vector<std::pair<int, int>> swaps;
    for (int i = 0; i < n; i++) {
        int j = where[order[i]];
        if (j == i) continue;
        swaps.push_back({i + 1, j + 1});
        std::swap(here[i], here[j]);
        where[here[i]] = i;
        where[here[j]] = j;
    }
    printf("%d\n", (int)swaps.size());
    for (auto [i, j] : swaps) printf("%d %d\n", i, j);
    return 0;
}
