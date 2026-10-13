#include <algorithm>
#include <cmath>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

const int DIGITS = 4; // coordinates are given to four decimals
const double SCALE = 1e4;
const int TEXT = 64; // room for one number as text

// a coordinate times 10^4, read exactly
long long exact() {
    char text[TEXT];
    scanf("%63s", text);
    char *p = text;
    long long sign = 1, whole = 0, frac = 0;
    if (*p == '-' || *p == '+')
        sign = *p++ == '-' ? -1 : 1;
    for (; *p && *p != '.'; p++)
        whole = whole * 10 + (*p - '0');
    int digits = 0;
    if (*p == '.')
        for (p++; *p && digits < DIGITS; p++, digits++)
            frac = frac * 10 + (*p - '0');
    for (; digits < DIGITS; digits++)
        frac *= 10;
    return sign * (whole * (long long)SCALE + frac);
}

int n, m, size_;
vector<long long> xs, ys;
vector<double> num, ex, ey, midX, midY;
vector<int> best;

// how far along the middle ray of gap k the line of edge e lies
double distance(int e, int k) { return num[e] / (midX[k] * ey[e] - midY[k] * ex[e]); }

vector<int> first; // the leftmost gap under each tree node

// each node keeps the nearest edge among those covering all its gaps,
// and edges never cross, so one gap decides for the whole node
void offer(int x, int e) {
    if (best[x] < 0 || distance(e, first[x]) < distance(best[x], first[x]))
        best[x] = e;
}

void cover(int lo, int hi, int e) {
    for (lo += size_, hi += size_; lo < hi; lo >>= 1, hi >>= 1) {
        if (lo & 1)
            offer(lo++, e);
        if (hi & 1)
            offer(--hi, e);
    }
}

int main() {
    long long px = exact(), py = exact();
    scanf("%d", &n);
    xs.resize(n);
    ys.resize(n);
    for (int i = 0; i < n; i++) {
        xs[i] = exact() - px;
        ys[i] = exact() - py;
    }
    // the directions of the corners seen from the lamp, equal ones merged
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    vector<double> angle(n);
    for (int i = 0; i < n; i++)
        angle[i] = atan2((double)ys[i], (double)xs[i]);
    sort(order.begin(), order.end(), [&](int a, int b) { return angle[a] < angle[b]; });
    vector<int> group(n);
    vector<long long> dx, dy;
    for (int i : order) {
        bool same = !dx.empty() && xs[i] * dy.back() == ys[i] * dx.back() &&
                    xs[i] * dx.back() + ys[i] * dy.back() > 0;
        if (!same) {
            dx.push_back(xs[i]);
            dy.push_back(ys[i]);
        }
        group[i] = dx.size() - 1;
    }
    m = dx.size();
    // every gap between neighbouring directions is below half a turn; its middle
    midX.resize(m);
    midY.resize(m);
    for (int k = 0; k < m; k++) {
        int l = (k + 1) % m;
        double la = hypot((double)dx[k], (double)dy[k]), lb = hypot((double)dx[l], (double)dy[l]);
        midX[k] = dx[k] / la + dx[l] / lb;
        midY[k] = dy[k] / la + dy[l] / lb;
    }
    for (size_ = 1; size_ < m; size_ *= 2)
        ;
    first.assign(2 * size_, 0);
    for (int x = 2 * size_ - 1; x > 0; x--)
        first[x] = x >= size_ ? x - size_ : first[2 * x];
    best.assign(2 * size_, -1);
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        long long c = xs[i] * ys[j] - ys[i] * xs[j];
        if (c == 0)
            continue; // seen edge-on, it hides nothing
        int a = c > 0 ? i : j, b = c > 0 ? j : i, e = num.size();
        num.push_back((double)(xs[a] * (ys[b] - ys[a]) - ys[a] * (xs[b] - xs[a])));
        ex.push_back((double)(xs[b] - xs[a]));
        ey.push_back((double)(ys[b] - ys[a]));
        if (group[a] < group[b]) {
            cover(group[a], group[b], e);
        } else {
            cover(group[a], m, e);
            cover(0, group[b], e);
        }
    }
    double area = 0;
    for (int k = 0; k < m; k++) {
        int near = -1;
        for (int x = k + size_; x; x >>= 1)
            if (best[x] >= 0 && (near < 0 || distance(best[x], k) < distance(near, k)))
                near = best[x];
        int l = (k + 1) % m;
        double ta = num[near] / (dx[k] * ey[near] - dy[k] * ex[near]);
        double tb = num[near] / (dx[l] * ey[near] - dy[l] * ex[near]);
        area += ta * tb * ((double)dx[k] * dy[l] - (double)dy[k] * dx[l]) / 2;
    }
    printf("%.4f\n", area / SCALE / SCALE);
}
