#include <cstdio>
#include <string>
#include <vector>

// among three vectors no longer than L, some sum or difference of two of them
// is no longer than L, so they can be merged into one
const int KEEP = 3;

int main() {
    int n;
    long long len;
    if (scanf("%d %lld", &n, &len) != 2)
        return 0;
    // nodes 0..n-1 are the input vectors, later nodes are merged pairs
    std::vector<long long> x(2 * n), y(2 * n);
    std::vector<int> parent(2 * n, -1), rel(2 * n, 1);
    int nodes = n;
    auto join = [&](int a, int b, int s) {
        x[nodes] = x[a] + s * x[b];
        y[nodes] = y[a] + s * y[b];
        parent[a] = parent[b] = nodes;
        rel[b] = s;
        return nodes++;
    };
    std::vector<int> active;
    for (int i = 0; i < n; i++) {
        if (scanf("%lld %lld", &x[i], &y[i]) != 2)
            return 0;
        active.push_back(i);
        if ((int)active.size() < KEEP)
            continue;
        bool merged = false;
        for (int p = 0; p < KEEP && !merged; p++)
            for (int q = p + 1; q < KEEP && !merged; q++)
                for (int s = -1; s <= 1 && !merged; s += 2) {
                    int a = active[p], b = active[q];
                    long long dx = x[a] + s * x[b], dy = y[a] + s * y[b];
                    if (dx * dx + dy * dy > len * len)
                        continue;
                    std::vector<int> next;
                    for (int r = 0; r < KEEP; r++)
                        if (r != p && r != q)
                            next.push_back(active[r]);
                    next.push_back(join(a, b, s));
                    active = next;
                    merged = true;
                }
    }
    // two vectors no longer than L: a sign making their dot product
    // non-positive keeps the sum within sqrt(2) L
    if (active.size() == 2) {
        int a = active[0], b = active[1];
        join(a, b, x[a] * x[b] + y[a] * y[b] > 0 ? -1 : 1);
    }
    std::vector<int> sign(nodes, 1);
    for (int k = nodes - 1; k >= 0; k--)
        if (parent[k] >= 0)
            sign[k] = sign[parent[k]] * rel[k];
    std::string out(n, '+');
    for (int i = 0; i < n; i++)
        if (sign[i] < 0)
            out[i] = '-';
    printf("YES\n%s\n", out.c_str());
}
