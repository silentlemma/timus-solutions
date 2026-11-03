#include <algorithm>
#include <cstdio>
#include <vector>

const int INPUT_FIELDS = 3;
std::vector<std::vector<int>> adjacent;
std::vector<int> match, seen;
int epoch;

bool augment(int v) {
    for (int u : adjacent[v]) {
        if (seen[u] == epoch)
            continue;
        seen[u] = epoch;
        // Reassign the old partner to make room, or take a free endpoint.
        if (match[u] < 0 || augment(match[u])) {
            match[u] = v;
            return true;
        }
    }
    return false;
}

int main() {
    int m, n, edges;
    if (scanf("%d%d%d", &m, &n, &edges) != INPUT_FIELDS)
        return 0;
    adjacent.resize(m);
    for (int i = 0; i < edges; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        adjacent[a - 1].push_back(b - 1);
    }
    match.assign(n, -1);
    seen.assign(n, 0);
    std::vector<bool> matched(m);
    int size = 0;
    // Any initial matching is safe and avoids unnecessary recursive searches.
    for (int v = 0; v < m; v++)
        for (int u : adjacent[v])
            if (match[u] < 0) {
                match[u] = v;
                matched[v] = true;
                size++;
                break;
            }
    for (int v = 0; v < m && size < std::min(m, n); v++)
        if (!matched[v]) {
            epoch++;
            if (augment(v))
                size++;
        }
    printf("%d\n", m + n - size);
}
