#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

typedef std::pair<long long, long long> P;

const int CORNERS = 3;

long long cross(P o, P a, P b) {
    return (a.first - o.first) * (b.second - o.second) -
           (a.second - o.second) * (b.first - o.first);
}
P vec(P a, P b) { return {b.first - a.first, b.second - a.second}; }
long long turn(P u, P w) { return u.first * w.second - u.second * w.first; }
long long dot(P u, P w) { return u.first * w.first + u.second * w.second; }

// whether the ray w lies in the closed sector turning left from u to v
bool within(P u, P v, P w) {
    long long c = turn(u, v);
    if (c > 0) return turn(u, w) >= 0 && turn(w, v) >= 0;
    if (c < 0) return !(turn(v, w) > 0 && turn(w, u) > 0);
    return turn(u, w) >= 0;
}

// rays from the bend b towards x and y stay on one side of the ravine
bool sameSideAtBend(P a, P b, P c, P x, P y) {
    P u = vec(b, a), v = vec(b, c), p = vec(b, x), q = vec(b, y);
    if (turn(u, v) == 0 && dot(u, v) > 0) return true;  // b is a free tip
    return (within(u, v, p) && within(u, v, q)) || (within(v, u, p) && within(v, u, q));
}

bool strictlyInside(P p, P a, P b) { return cross(a, b, p) == 0 && dot(vec(p, a), vec(p, b)) < 0; }

bool crosses(P p, P q, P a, P b) {
    return cross(p, q, a) * cross(p, q, b) < 0 && cross(a, b, p) * cross(a, b, q) < 0;
}

bool allowed(const std::vector<P> &path, P a, P b, P c) {
    for (size_t i = 0; i + 1 < path.size(); i++) {
        P p = path[i], q = path[i + 1];
        if (crosses(p, q, a, b) || crosses(p, q, b, c)) return false;
        // going straight through the bend must not change sides there
        if (strictlyInside(b, p, q) && !sameSideAtBend(a, b, c, p, q)) return false;
    }
    for (size_t i = 1; i + 1 < path.size(); i++) {
        P x = path[i - 1], v = path[i], y = path[i + 1];
        if (v == b && !sameSideAtBend(a, b, c, x, y)) return false;
        // an end of the ravine lying inside the other piece is no corner
        if (v == a && strictlyInside(a, b, c) && cross(b, c, x) * cross(b, c, y) < 0) return false;
        if (v == c && strictlyInside(c, a, b) && cross(a, b, x) * cross(a, b, y) < 0) return false;
    }
    return true;
}

int main() {
    int tests;
    if (scanf("%d", &tests) != 1) return 0;
    while (tests--) {
        P s, e, a, b, c;
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld", &s.first, &s.second, &e.first,
              &e.second, &a.first, &a.second, &b.first, &b.second, &c.first, &c.second);
        // a shortest way bends only at points of the ravine, at most once at
        // each of A, B and C; the shortest allowed candidate is the answer
        std::vector<std::pair<double, std::vector<P>>> candidates;
        P corner[] = {a, b, c};
        for (int mask = 0; mask < (1 << CORNERS); mask++) {
            std::vector<int> chosen;
            for (int k = 0; k < CORNERS; k++) {
                if (mask >> k & 1) chosen.push_back(k);
            }
            do {
                std::vector<P> path = {s};
                for (int k : chosen) path.push_back(corner[k]);
                path.push_back(e);
                double size = 0;
                for (size_t i = 0; i + 1 < path.size(); i++) {
                    size += std::hypot(path[i + 1].first - path[i].first,
                                       path[i + 1].second - path[i].second);
                }
                candidates.push_back({size, path});
            } while (std::next_permutation(chosen.begin(), chosen.end()));
        }
        std::sort(candidates.begin(), candidates.end());
        for (const auto &cand : candidates) {
            if (allowed(cand.second, a, b, c)) {
                printf("%.6f\n", cand.first);
                break;
            }
        }
    }
}
