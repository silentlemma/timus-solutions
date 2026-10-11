#include <cstdio>
#include <vector>

std::vector<int> parent;

int find(int x) {
    while (parent[x] != x)
        x = parent[x] = parent[parent[x]];
    return x;
}

int main() {
    int n, k, m;
    scanf("%d %d %d", &n, &k, &m); // the bridges themselves do not matter
    parent.resize(n + 1);
    for (int i = 0; i <= n; i++)
        parent[i] = i;
    // tunnels are free; every bridge joins two of the remaining groups
    int groups = n;
    for (int i = 0; i < k; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        a = find(a), b = find(b);
        if (a != b) {
            parent[a] = b;
            groups--;
        }
    }
    printf("%d\n", groups - 1);
}
