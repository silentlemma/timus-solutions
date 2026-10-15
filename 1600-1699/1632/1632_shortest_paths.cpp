#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const double LIMIT = 1e6;
const double TIGHT = 1e-7;  // a smaller slack counts as an equality

struct Edge {
    int lo, hi;
    double lift;
};

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<long long> x(n), y(n), u(n), v(n), w(n);
    for (int i = 0; i < n; i++)
        for (long long *field : {&x[i], &y[i], &u[i], &v[i], &w[i]})
            if (scanf("%lld", field) != 1)
                return 0;
    int m;
    if (scanf("%d", &m) != 1)
        return 0;
    // z[hi] - z[lo] must exceed lift: the gap of the beams where they cross
    vector<Edge> edges(m);
    vector<vector<int>> out(n);
    for (int k = 0; k < m; k++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        a--, b--;
        long long det = u[a] * v[b] - v[a] * u[b];
        long long dx = x[b] - x[a], dy = y[b] - y[a];
        long long top = w[b] * (v[a] * dx - u[a] * dy) - w[a] * (dx * v[b] - dy * u[b]);
        edges[k] = {b, a, (double)top / det};
        out[b].push_back(k);
    }
    // longest paths from an imaginary source tied to every laser by 0.
    // Only lasers raised in the last round can raise others.
    vector<double> z(n, 0);
    vector<int> active(n);
    for (int i = 0; i < n; i++)
        active[i] = i;
    vector<char> mark(n);
    for (int round = 0; round < n && !active.empty(); round++) {
        vector<int> raised;
        for (int lo : active)
            for (int k : out[lo]) {
                const Edge &e = edges[k];
                if (z[lo] + e.lift > z[e.hi]) {
                    z[e.hi] = z[lo] + e.lift;
                    if (!mark[e.hi]) {
                        mark[e.hi] = 1;
                        raised.push_back(e.hi);
                    }
                }
            }
        for (int h : raised)
            mark[h] = 0;
        active.swap(raised);
    }
    // equalities form an acyclic graph; a step per level of it makes them
    // strict, small enough to keep the other constraints and the bounds
    vector<vector<int>> tight(n);
    vector<int> indegree(n), level(n);
    double slackMin = -1;
    for (const Edge &e : edges) {
        double slack = z[e.hi] - z[e.lo] - e.lift;
        if (slack < TIGHT) {
            tight[e.lo].push_back(e.hi);
            indegree[e.hi]++;
        } else if (slackMin < 0 || slack < slackMin) {
            slackMin = slack;
        }
    }
    vector<int> queue;
    for (int i = 0; i < n; i++)
        if (!indegree[i])
            queue.push_back(i);
    for (size_t head = 0; head < queue.size(); head++) {
        int at = queue[head];
        for (int to : tight[at]) {
            level[to] = max(level[to], level[at] + 1);
            if (--indegree[to] == 0)
                queue.push_back(to);
        }
    }
    int levels = *max_element(level.begin(), level.end());
    double step = 0;
    if (levels) {
        double spread = *max_element(z.begin(), z.end()) - *min_element(z.begin(), z.end());
        double room = 2 * LIMIT - spread;
        if (slackMin >= 0)
            room = min(room, slackMin);
        step = room / (2 * levels + 2);
    }
    for (int i = 0; i < n; i++)
        z[i] += step * level[i];
    double middle = (*max_element(z.begin(), z.end()) + *min_element(z.begin(), z.end())) / 2;
    for (int i = 0; i < n; i++)
        printf("%.10f\n", z[i] - middle);
}
