#include <cstdio>
#include <vector>

const int VERTICES = 1000;

std::vector<int> parent(VERTICES + 1);

int find(int v) {
    while (parent[v] != v) {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    return v;
}

int main() {
    std::vector<int> edges(VERTICES + 1, 0); // edges of each component, kept at its root
    for (int v = 0; v <= VERTICES; v++)
        parent[v] = v;
    int a = 0, b = 0;
    while (scanf("%d %d", &a, &b) == 2) {
        int ra = find(a), rb = find(b);
        if (ra != rb) {
            parent[ra] = rb;
            edges[rb] += edges[ra];
        }
        edges[rb]++;
    }
    bool even = true;
    for (int v = 1; v <= VERTICES; v++) {
        if (parent[v] == v && edges[v] % 2 != 0)
            even = false;
    }
    printf("%d\n", even ? 1 : 0);
    return 0;
}
