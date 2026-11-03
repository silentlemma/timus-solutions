#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const int BUFFER = 1 << 14;
char buffer[BUFFER];
int position, available;
int readByte() {
    if (position == available) {
        available = (int)fread(buffer, 1, BUFFER, stdin);
        position = 0;
        if (!available)
            return EOF;
    }
    return buffer[position++];
}
int nextInt() {
    int c = readByte(), value = 0;
    while (c < '0' || c > '9')
        c = readByte();
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return value;
}
int width;
vector<int> tree;
int segmentMax(int left, int right) {
    int best = 0;
    for (left += width, right += width + 1; left < right; left >>= 1, right >>= 1) {
        if (left & 1)
            best = max(best, tree[left++]);
        if (right & 1)
            best = max(best, tree[--right]);
    }
    return best;
}
int main() {
    int n = nextInt();
    width = n;
    vector<int> first(n, -1), to(2 * n - 2), link(2 * n - 2);
    for (int i = 0; i < n - 1; i++) {
        int a = nextInt() - 1, b = nextInt() - 1, j = 2 * i;
        to[j] = b;
        link[j] = first[a];
        first[a] = j;
        to[j + 1] = a;
        link[j + 1] = first[b];
        first[b] = j + 1;
    }
    vector<int> parent(n, -1), depth(n), order(n), size(n, 1), heavy(n, -1), head(n), index(n);
    for (int i = 0, end = 1; i < n; i++) {
        int v = order[i];
        for (int e = first[v]; e != -1; e = link[e]) {
            int u = to[e];
            if (u != parent[v]) {
                parent[u] = v;
                depth[u] = depth[v] + 1;
                order[end++] = u;
            }
        }
    }
    for (int i = n - 1; i > 0; i--) {
        int v = order[i], p = parent[v];
        size[p] += size[v];
        if (heavy[p] == -1 || size[v] > size[heavy[p]])
            heavy[p] = v;
    }
    int next = 0;
    for (int v : order)
        if (v == 0 || heavy[parent[v]] != v) {
            for (int u = v; u != -1; u = heavy[u]) {
                head[u] = v;
                index[u] = next++;
            }
        }
    tree.assign(2 * n, 0);
    int q = nextInt();
    while (q--) {
        int kind = readByte();
        while (kind != 'I' && kind != 'G')
            kind = readByte();
        int u = nextInt() - 1, v = nextInt();
        if (kind == 'I') {
            int at = index[u] + n, value = tree[at] + v;
            tree[at] = value;
            // A point only increases; stop when this new value cannot change a maximum.
            for (at >>= 1; at && tree[at] < value; at >>= 1)
                tree[at] = value;
            continue;
        }
        --v;
        int best = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]])
                swap(u, v);
            best = max(best, segmentMax(index[head[u]], index[u]));
            u = parent[head[u]];
        }
        best = max(best, segmentMax(min(index[u], index[v]), max(index[u], index[v])));
        printf("%d\n", best);
    }
}
