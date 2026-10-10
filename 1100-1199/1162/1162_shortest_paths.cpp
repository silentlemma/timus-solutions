#include <cstdio>
#include <vector>

// sums closer than this count as equal
const double EPS = 1e-9;
// the first line holds N, M, S and V; a point holds two currencies, then the
// rate and commission each way
const int HEADER = 4, FIELDS = 6;

struct Exchange {
    int from, to;
    double rate, fee;
};

int main() {
    int n, m, s;
    double v;
    if (scanf("%d %d %d %lf", &n, &m, &s, &v) != HEADER)
        return 0;
    std::vector<Exchange> edges;
    for (int k = 0; k < m; k++) {
        int a, b;
        double rab, cab, rba, cba;
        if (scanf("%d %d %lf %lf %lf %lf", &a, &b, &rab, &cab, &rba, &cba) != FIELDS)
            return 0;
        edges.push_back({a, b, rab, cab});
        edges.push_back({b, a, rba, cba});
    }
    // best[c] is the most money of currency c that can be held; a pass that
    // still improves something after n passes has found a gaining cycle
    std::vector<double> best(n + 1, -1);
    best[s] = v;
    bool changed = false;
    for (int pass = 0; pass < n; pass++) {
        changed = false;
        for (const Exchange &e : edges)
            if (best[e.from] - e.fee >= 0) {
                double got = (best[e.from] - e.fee) * e.rate;
                if (got > best[e.to] + EPS) {
                    best[e.to] = got;
                    changed = true;
                }
            }
        if (best[s] > v + EPS || !changed)
            break;
    }
    puts(best[s] > v + EPS || changed ? "YES" : "NO");
}
