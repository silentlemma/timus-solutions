#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

const long long INF = 1LL << 62;
const int BUFFER = 1 << 16;

int n;
vector<int> cost, dist; // n by n, 0 marks a missing link, real values are positive

char buf[BUFFER];
int bufLen = 0, bufPos = 0;

int readInt() {
    int c, x = 0;
    do {
        if (bufPos == bufLen) {
            bufLen = fread(buf, 1, BUFFER, stdin);
            bufPos = 0;
        }
        c = buf[bufPos++];
    } while (c < '0');
    while (c >= '0') {
        x = x * 10 + c - '0';
        if (bufPos == bufLen) {
            bufLen = fread(buf, 1, BUFFER, stdin);
            bufPos = 0;
            if (bufLen == 0)
                break;
        }
        c = buf[bufPos++];
    }
    return x;
}

// Prim on the weights c q - d p, exact integers; returns the tree's
// total weight and sets its cost and length
long long tree(long long p, long long q, long long &tc, long long &td) {
    vector<long long> best(n, INF), bc(n, 0), bd(n, 0);
    vector<bool> used(n, false);
    best[0] = 0;
    long long total = 0;
    tc = td = 0;
    for (int step = 0; step < n; step++) {
        int u = -1;
        for (int v = 0; v < n; v++)
            if (!used[v] && (u < 0 || best[v] < best[u]))
                u = v;
        used[u] = true;
        total += best[u];
        tc += bc[u];
        td += bd[u];
        const int *cu = &cost[(size_t)u * n], *du = &dist[(size_t)u * n];
        for (int v = 0; v < n; v++)
            if (cu[v] && !used[v]) {
                long long w = cu[v] * q - du[v] * p;
                if (w < best[v]) {
                    best[v] = w;
                    bc[v] = cu[v];
                    bd[v] = du[v];
                }
            }
    }
    return total;
}

int main() {
    n = readInt();
    int m = readInt();
    cost.assign((size_t)n * n, 0);
    dist.assign((size_t)n * n, 0);
    for (int i = 0; i < m; i++) {
        int a = readInt() - 1, b = readInt() - 1, d = readInt(), c = readInt();
        cost[(size_t)a * n + b] = cost[(size_t)b * n + a] = c;
        dist[(size_t)a * n + b] = dist[(size_t)b * n + a] = d;
    }
    // Dinkelbach: the ratio p / q of the last tree drops until no tree beats it
    long long p, q, tc, td;
    tree(0, 1, p, q);
    while (tree(p, q, tc, td) < 0) {
        long long g = gcd(tc, td);
        p = tc / g;
        q = td / g;
    }
    printf("%.10f\n", (double)p / q);
}
