#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long i64;

constexpr int BUF_SIZE = 1 << 16;
constexpr int LINE_BYTES = 20;  // enough for any answer and its newline

static char buf[BUF_SIZE];
int bufLen, bufPos;

int readChar() {
    if (bufPos == bufLen) {
        bufLen = (int)fread(buf, 1, sizeof(buf), stdin);
        bufPos = 0;
        if (bufLen <= 0) return -1;
    }
    return buf[bufPos++];
}

int readToken() {
    int c = readChar();
    while (c == ' ' || c == '\n' || c == '\r') c = readChar();
    return c;
}

long long readInt() {
    int c = readToken();
    long long x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + (c - '0');
        c = readChar();
    }
    return x;
}

int n, logN;
std::vector<int> tin, order, parentOf;
std::vector<i64> depth;
std::vector<std::vector<int>> table;
std::vector<int> fen, lg;

// The LCA of u != v is the parent with the smallest preorder number among the
// vertices in the preorder range (tin[u], tin[v]].
int lca(int u, int v) {
    if (u == v) return u;
    int l = tin[u], r = tin[v];
    if (l > r) std::swap(l, r);
    l++;
    int k = lg[r - l + 1];
    int best = std::min(table[k][l], table[k][r - (1 << k) + 1]);
    return order[best];
}

i64 dist(int u, int v) { return depth[u] + depth[v] - 2 * depth[lca(u, v)]; }

void fenAdd(int i, int d) {
    for (i++; i <= n; i += i & -i) fen[i] += d;
}

int fenPrefix(int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += fen[i];
    return s;
}

// the position of the k-th marked preorder position, k from 1
int fenKth(int k) {
    int pos = 0;
    for (int step = 1 << logN; step > 0; step >>= 1) {
        if (pos + step <= n && fen[pos + step] < k) {
            pos += step;
            k -= fen[pos];
        }
    }
    return pos;
}

int main() {
    n = (int)readInt();
    std::vector<int> head(n + 1, -1), nxt(2 * n), to(2 * n);
    std::vector<i64> wt(2 * n);
    int edges = 0;
    for (int i = 0; i + 1 < n; i++) {
        int u = (int)readInt(), v = (int)readInt();
        i64 w = readInt();
        to[edges] = v, wt[edges] = w, nxt[edges] = head[u], head[u] = edges++;
        to[edges] = u, wt[edges] = w, nxt[edges] = head[v], head[v] = edges++;
    }
    tin.assign(n + 1, 0);
    parentOf.assign(n + 1, 0);
    depth.assign(n + 1, 0);
    order.clear();
    std::vector<int> stack = {1};
    parentOf[1] = 1;
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        tin[v] = (int)order.size();
        order.push_back(v);
        for (int e = head[v]; e >= 0; e = nxt[e]) {
            int u = to[e];
            if (u == parentOf[v]) continue;
            parentOf[u] = v;
            depth[u] = depth[v] + wt[e];
            stack.push_back(u);
        }
    }
    lg.assign(n + 1, 0);
    for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
    logN = lg[n];
    table.assign(logN + 1, std::vector<int>(n));
    for (int i = 0; i < n; i++) table[0][i] = tin[parentOf[order[i]]];
    for (int k = 1; k <= logN; k++)
        for (int i = 0; i + (1 << k) <= n; i++)
            table[k][i] = std::min(table[k - 1][i], table[k - 1][i + (1 << (k - 1))]);
    fen.assign(n + 1, 0);

    int q = (int)readInt();
    int total = 0;
    i64 doubled = 0;  // the sum of distances around the marked vertices in preorder
    std::vector<char> out;
    out.reserve((size_t)q * LINE_BYTES);
    char tmp[LINE_BYTES];
    for (int i = 0; i < q; i++) {
        int sign = readToken();
        int v = (int)readInt();
        int p = tin[v];
        if (sign == '-') {
            fenAdd(p, -1);
            total--;
        }
        if (total > 0) {
            int before = fenPrefix(p);
            int a = order[fenKth(before > 0 ? before : total)];
            int b = order[fenKth(before < total ? before + 1 : 1)];
            i64 change = dist(a, v) + dist(v, b) - dist(a, b);
            doubled += sign == '+' ? change : -change;
        }
        if (sign == '+') {
            fenAdd(p, 1);
            total++;
        }
        i64 x = doubled / 2;
        int len = 0;
        do {
            tmp[len++] = (char)('0' + x % 10);
            x /= 10;
        } while (x > 0);
        while (len > 0) out.push_back(tmp[--len]);
        out.push_back('\n');
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
