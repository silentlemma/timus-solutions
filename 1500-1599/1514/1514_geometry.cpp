#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

const int SMALL = 8;     // pieces up to this size are checked triple by triple
const double HALF = 0.5; // a better triangle has every side shorter than half its perimeter

vector<long long> xs, ys;
vector<int> order;
double best = INFINITY;
vector<int> answer = {0, 1, 2};

double dist(int a, int b) { return hypot(double(xs[a] - xs[b]), double(ys[a] - ys[b])); }

// tries every triple of pts, sorted by y, that fits within reach vertically
void triples(const vector<int> &pts, double reach) {
    size_t size = pts.size();
    for (size_t i = 0; i < size; i++) {
        int a = pts[i];
        double top = ys[a] + reach;
        for (size_t j = i + 1; j < size && ys[pts[j]] < top; j++)
            for (size_t k = j + 1; k < size && ys[pts[k]] < top; k++) {
                int b = pts[j], c = pts[k];
                double p = dist(a, b) + dist(b, c) + dist(c, a);
                if (p < best) {
                    best = p;
                    answer = {a, b, c};
                    top = ys[a] + best * HALF;
                }
            }
    }
}

bool byY(int a, int b) { return ys[a] < ys[b]; }

// solves the points order[lo:hi]
void solve(int lo, int hi) {
    if (hi - lo <= SMALL) {
        vector<int> pts(order.begin() + lo, order.begin() + hi);
        sort(pts.begin(), pts.end(), byY);
        triples(pts, INFINITY);
        return;
    }
    int mid = (lo + hi) / 2;
    long long split = xs[order[mid]];
    solve(lo, mid);
    solve(mid, hi);
    // a better triangle across the split lies in a strip around it
    double reach = best * HALF;
    vector<int> strip;
    for (int i = lo; i < hi; i++)
        if (fabs(double(xs[order[i]] - split)) < reach)
            strip.push_back(order[i]);
    sort(strip.begin(), strip.end(), byY);
    triples(strip, reach);
}

int main() {
    int n;
    scanf("%d", &n);
    xs.resize(n);
    ys.resize(n);
    order.resize(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &xs[i], &ys[i]);
        order[i] = i;
    }
    sort(order.begin(), order.end(),
         [](int a, int b) { return xs[a] != xs[b] ? xs[a] < xs[b] : ys[a] < ys[b]; });
    solve(0, n);
    printf("%.6f\n%d %d %d\n", best, answer[0] + 1, answer[1] + 1, answer[2] + 1);
}
