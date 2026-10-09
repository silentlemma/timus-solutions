#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <vector>

std::vector<int> parent;

int find(int v) {
    while (parent[v] != v)
        v = parent[v] = parent[parent[v]];
    return v;
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    // the vertices of the grid are (i, j) -> i * (m + 1) + j; balance[v] is the number
    // of front stitches minus the number of back stitches that end at v
    int width = m + 1, vertices = (n + 1) * width;
    parent.resize(vertices);
    std::iota(parent.begin(), parent.end(), 0);
    std::vector<int> balance(vertices, 0);
    std::vector<bool> stitched(vertices, false);
    std::vector<char> row(m + 1);
    for (int side = 0; side < 2; side++) {
        int sign = side == 0 ? 1 : -1;
        for (int i = 0; i < n; i++) {
            if (scanf("%s", row.data()) != 1)
                return 0;
            for (int j = 0; j < m; j++) {
                char c = row[j];
                int ends[2][2] = {{i * width + j, (i + 1) * width + j + 1},
                                  {(i + 1) * width + j, i * width + j + 1}};
                for (int d = 0; d < 2; d++) {
                    bool present = d == 0 ? (c == '\\' || c == 'X') : (c == '/' || c == 'X');
                    if (!present)
                        continue;
                    int a = ends[d][0], b = ends[d][1];
                    balance[a] += sign;
                    balance[b] += sign;
                    stitched[a] = stitched[b] = true;
                    parent[find(a)] = find(b);
                }
            }
        }
    }
    // a group needs one thread per two unbalanced stitch ends, and at least one
    std::vector<long long> ends(vertices, 0);
    std::vector<bool> used(vertices, false);
    for (int v = 0; v < vertices; v++)
        if (stitched[v]) {
            int r = find(v);
            used[r] = true;
            ends[r] += std::abs(balance[v]);
        }
    long long threads = 0;
    for (int v = 0; v < vertices; v++)
        if (used[v])
            threads += ends[v] > 0 ? ends[v] / 2 : 1;
    printf("%lld\n", threads);
}
