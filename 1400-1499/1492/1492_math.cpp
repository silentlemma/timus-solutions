#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;

int n;
vector<ll> xs, ys;

// the segment of f that holds x, or the one to its right
int segment(ll x) {
    int j = int(upper_bound(xs.begin(), xs.end(), x) - xs.begin()) - 1;
    return min(j, n - 2);
}

double value(ll x) {
    int j = segment(x);
    return ys[j] + double(ys[j + 1] - ys[j]) * (x - xs[j]) / (xs[j + 1] - xs[j]);
}

int main() {
    scanf("%d", &n);
    xs.resize(n);
    ys.resize(n);
    for (int i = 0; i < n; i++)
        scanf("%lld %lld", &xs[i], &ys[i]);

    // f(x) = E(x) + O(x) with E(x) = (f(x) + f(-x)) / 2 and
    // O(x) = (f(x) - f(-x)) / 2; both are linear between the points of f
    // and their mirror images
    vector<ll> points(xs);
    for (ll x : xs)
        points.push_back(-x);
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());

    puts("Yes");
    for (int sign : {1, -1}) { // the even part, then the odd one
        // the slope of a part between neighbouring points: (a/b -+ c/d) / 2 with
        // the slopes a/b of f at x and c/d of f at -x, all below 2 * 10^9
        vector<pair<ll, ll>> slopes;
        for (size_t k = 0; k + 1 < points.size(); k++) {
            int j = segment(points[k]), i = segment(-points[k + 1]);
            ll a = ys[j + 1] - ys[j], b = xs[j + 1] - xs[j];
            ll c = ys[i + 1] - ys[i], d = xs[i + 1] - xs[i];
            slopes.push_back({a * d - sign * c * b, 2 * b * d});
        }
        for (size_t k = 0; k < points.size(); k++) {
            bool bend =
                k == 0 || k + 1 == points.size() ||
                slopes[k - 1].first * slopes[k].second != slopes[k].first * slopes[k - 1].second;
            if (bend) // only real bends stay
                printf("%.6f %.6f\n", (double)points[k],
                       (value(points[k]) + sign * value(-points[k])) / 2);
        }
    }
}
