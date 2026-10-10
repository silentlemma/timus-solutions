#include <cmath>
#include <cstdio>
#include <map>
#include <utility>
#include <vector>

typedef long long ll;
typedef std::pair<ll, ll> Dir; // a direction (y, x) through a corner

// directions compare by slope y/x, so equal slopes share one entry
struct BySlope {
    bool operator()(const Dir &a, const Dir &b) const {
        return a.first * b.second < b.first * a.second;
    }
};

std::map<Dir, std::pair<ll, ll>, BySlope> events;

void term(Dir start, Dir end, ll dp, ll dq) {
    events[start].first += dp;
    events[start].second += dq;
    events[end].first -= dp;
    events[end].second -= dq;
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<ll> x1(n), y1(n), x2(n), y2(n), c(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld %lld %lld", &x1[i], &y1[i], &x2[i], &y2[i], &c[i]);
    }
    ll c0, length;
    scanf("%lld %lld", &c0, &length);
    // walking at angle t, a vertical line x = a is crossed after a/cos t and a
    // horizontal one y = b after b/sin t; a rectangle adds (c - c0) times
    // (exit - entry), a sum of such terms, each valid between two corners
    for (int i = 0; i < n; i++) {
        ll w = c[i] - c0;
        // out through the right side or the top, in through the left or the bottom
        term({y1[i], x2[i]}, {y2[i], x2[i]}, w * x2[i], 0);
        term({y2[i], x2[i]}, {y2[i], x1[i]}, 0, w * y2[i]);
        term({y1[i], x1[i]}, {y2[i], x1[i]}, -w * x1[i], 0);
        term({y1[i], x2[i]}, {y1[i], x1[i]}, 0, -w * y1[i]);
    }
    // below the lowest corner no rectangle is met at all
    Dir lowest = events.begin()->first;
    double bestCost = c0 * length, bestT = std::atan2(lowest.first, lowest.second) / 2;
    // between corners the time is c0*L + p/cos t + q/sin t: with p, q > 0 it
    // is above c0*L, otherwise monotone or concave, so corners are enough
    ll p = 0, q = 0;
    for (auto &[dir, delta] : events) {
        double t = std::atan2(dir.first, dir.second);
        double cost = c0 * length + p / std::cos(t) + q / std::sin(t);
        if (cost < bestCost) {
            bestCost = cost;
            bestT = t;
        }
        p += delta.first;
        q += delta.second;
    }
    printf("%.6f\n%.6f %.6f\n", bestCost, length * std::cos(bestT), length * std::sin(bestT));
}
