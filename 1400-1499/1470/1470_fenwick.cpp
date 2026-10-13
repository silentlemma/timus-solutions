#include <cstdio>
#include <vector>

using namespace std;

const int ADD = 1, ASK = 2; // record kinds; any other kind ends the input

int n, side;
vector<long long> tree; // a 3D Fenwick tree, indices from 1

void add(int x, int y, int z, long long k) {
    for (int i = x; i <= n; i += i & -i)
        for (int j = y; j <= n; j += j & -j) {
            long long *row = &tree[((long long)i * side + j) * side];
            for (int w = z; w <= n; w += w & -w)
                row[w] += k;
        }
}

long long prefix(int x, int y, int z) {
    long long total = 0;
    for (int i = x; i > 0; i -= i & -i)
        for (int j = y; j > 0; j -= j & -j) {
            const long long *row = &tree[((long long)i * side + j) * side];
            for (int w = z; w > 0; w -= w & -w)
                total += row[w];
        }
    return total;
}

int main() {
    scanf("%d", &n);
    side = n + 1;
    tree.assign((size_t)side * side * side, 0);
    int kind;
    while (scanf("%d", &kind) == 1 && (kind == ADD || kind == ASK)) {
        if (kind == ADD) {
            int x, y, z;
            long long k;
            scanf("%d %d %d %lld", &x, &y, &z, &k);
            add(x + 1, y + 1, z + 1, k);
        } else {
            int x1, y1, z1, x2, y2, z2;
            scanf("%d %d %d %d %d %d", &x1, &y1, &z1, &x2, &y2, &z2);
            x2++, y2++, z2++;
            // inclusion and exclusion over the eight corners of the box
            long long total = prefix(x2, y2, z2) - prefix(x1, y2, z2) - prefix(x2, y1, z2) -
                              prefix(x2, y2, z1) + prefix(x1, y1, z2) + prefix(x1, y2, z1) +
                              prefix(x2, y1, z1) - prefix(x1, y1, z1);
            printf("%lld\n", total);
        }
    }
}
