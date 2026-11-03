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
    while (c <= ' ')
        c = readByte();
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return value;
}
int main() {
    int n = nextInt(), m = nextInt();
    vector<int> head(n, -1), to(2 * m), link(2 * m);
    for (int i = 0; i < m; i++) {
        int a = nextInt() - 1, b = nextInt() - 1, j = 2 * i;
        to[j] = b;
        link[j] = head[a];
        head[a] = j;
        to[j + 1] = a;
        link[j + 1] = head[b];
        head[b] = j + 1;
    }
    int start = nextInt() - 1, finish = nextInt() - 1, origin = nextInt() - 1;
    vector<int> queue(n), clearance(n, -1);
    queue[0] = origin;
    clearance[origin] = 0;
    int end = 1;
    for (int at = 0; at < end; at++) {
        int v = queue[at];
        for (int edge = head[v]; edge != -1; edge = link[edge]) {
            int u = to[edge];
            if (clearance[u] < 0) {
                clearance[u] = clearance[v] + 1;
                queue[end++] = u;
            }
        }
    }
    vector<int> depth(n, -1), best(n);
    queue[0] = start;
    depth[start] = 0;
    best[start] = clearance[start];
    end = 1;
    for (int at = 0; at < end; at++) {
        int v = queue[at];
        // Pop, rather than discovery: every predecessor layer has finished.
        if (v == finish) {
            printf("%d\n", best[v]);
            return 0;
        }
        for (int edge = head[v]; edge != -1; edge = link[edge]) {
            int u = to[edge];
            if (depth[u] < 0) {
                depth[u] = depth[v] + 1;
                queue[end++] = u;
            }
            if (depth[u] == depth[v] + 1)
                best[u] = max(best[u], min(best[v], clearance[u]));
        }
    }
}
