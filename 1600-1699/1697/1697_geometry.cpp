#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long ll;

const int DIM = 3;  // coordinates of the sniper
const size_t AREA = 3;  // corners of a polygon with an inside

const size_t SIDES = 4;  // the wall constraints come first
enum { LX, LY, RX, RY, HEIGHT, FIELDS };  // a building

struct Line {
    ll p, q, c;  // the closed half-plane p u + q v >= c
};

struct Corner {
    ll u, v, den;  // the point (u / den, v / den), den > 0
};

struct Gap {
    ll loN, loD, hiN, hiD;  // the open interval (loN / loD, hiN / hiD) of t
};

// the open interval of t for which the shot from S to A + t (B - A) passes
// through the inside of the box; a point of the shot is S + u (A - S) +
// v (B - A) with v = u t, so the box pulls back to a convex polygon in (u, v)
bool blockedInterval(const ll s[], const ll a[], const ll b[], const ll box[], Gap& gap) {
    ll ax = a[0] - s[0], ay = a[1] - s[1], dx = b[0] - a[0], dy = b[1] - a[1];
    std::vector<Line> cons = {{ax, dx, box[LX] - s[0]}, {-ax, -dx, s[0] - box[RX]},
                              {ay, dy, box[LY] - s[1]}, {-ay, -dy, s[1] - box[RY]},
                              {1, 0, 0},  {-1, 0, -1},  // 0 <= u <= 1
                              {1, 1, 0},  {2, -1, 0}};  // -1 <= t <= 2 keeps it bounded
    for (size_t i = 0; i < SIDES; i++) {
        if (cons[i].p == 0 && cons[i].q == 0 && cons[i].c >= 0) {
            return false;  // the plane of the shots holds a wall or misses the box
        }
    }
    if (s[2] > 0) {
        cons.push_back({s[2], 0, s[2] - box[HEIGHT]});  // below the roof: sz (1 - u) <= h
    }
    std::vector<Corner> corners;
    for (size_t i = 0; i < cons.size(); i++) {
        for (size_t j = i + 1; j < cons.size(); j++) {
            const Line &f = cons[i], &g = cons[j];
            ll den = f.p * g.q - g.p * f.q;
            if (den == 0) {
                continue;
            }
            ll u = f.c * g.q - g.c * f.q, v = f.p * g.c - g.p * f.c;
            if (den < 0) {
                den = -den;
                u = -u;
                v = -v;
            }
            bool inside = true;
            for (const Line& h : cons) {
                inside = inside && h.p * u + h.q * v >= h.c * den;
            }
            bool fresh = true;
            for (const Corner& k : corners) {
                fresh = fresh && !(u * k.den == k.u * den && v * k.den == k.v * den);
            }
            if (inside && fresh) {
                corners.push_back({u, v, den});
            }
        }
    }
    // the polygon has an inside exactly when it has three different corners
    if (corners.size() < AREA) {
        return false;
    }
    // t = v / u, and u > 0 at every corner, as S is outside the box
    gap = {corners[0].v, corners[0].u, corners[0].v, corners[0].u};
    for (const Corner& k : corners) {
        if (k.v * gap.loD < gap.loN * k.u) {
            gap.loN = k.v;
            gap.loD = k.u;
        }
        if (k.v * gap.hiD > gap.hiN * k.u) {
            gap.hiN = k.v;
            gap.hiD = k.u;
        }
    }
    return true;
}

int main() {
    ll s[DIM], a[2], b[2];
    int n;
    scanf("%lld %lld %lld %lld %lld %lld %lld %d", &s[0], &s[1], &s[2], &a[0], &a[1], &b[0], &b[1],
          &n);
    std::vector<Gap> gaps;
    for (int i = 0; i < n; i++) {
        ll box[FIELDS];
        for (ll& value : box) {
            scanf("%lld", &value);
        }
        Gap gap;
        if (blockedInterval(s, a, b, box, gap)) {
            gaps.push_back(gap);
        }
    }
    // the free times form a closed set whose first point is 0 or the right
    // end of some blocked interval
    std::vector<std::pair<ll, ll>> candidates = {{0, 1}};
    for (const Gap& g : gaps) {
        if (0 <= g.hiN && g.hiN <= g.hiD) {
            candidates.push_back({g.hiN, g.hiD});
        }
    }
    std::sort(candidates.begin(), candidates.end(), [](const auto& f, const auto& g) {
        return f.first * g.second < g.first * f.second;
    });
    for (auto [tn, td] : candidates) {
        bool free = true;
        for (const Gap& g : gaps) {
            free = free && !(g.loN * td < tn * g.loD && tn * g.hiD < g.hiN * td);
        }
        if (free) {
            double t = (double)tn / td;
            printf("%.10f %.10f\n", a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t);
            return 0;
        }
    }
    printf("Impossible\n");
}
