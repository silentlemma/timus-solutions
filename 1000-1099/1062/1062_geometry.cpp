#include <cstdio>
#include <vector>

typedef __int128 Big;
const int STAGES = 3;

// a line a*x + b*y + c, shifted by a tiny eps: a*x + b*y + c + eps < 0 is
// the half-plane kept
struct Line {
    long long a, b, c;
};

// the corner of lines p and q, all shifted by eps: numerators of x and y as
// value plus eps coefficient, and the common denominator
struct Corner {
    Big x0, xe, y0, ye, det;
};

Corner corner(const Line &p, const Line &q) {
    return {-(Big)p.c * q.b + (Big)q.c * p.b, (Big)(p.b - q.b), (Big)p.c * q.a - (Big)q.c * p.a,
            (Big)(q.a - p.a), (Big)p.a * q.b - (Big)q.a * p.b};
}

// -1, 0 or 1: where the corner lies against the shifted line; the values
// stay below 3 * 10^37, inside 128 bits
int side(const Corner &v, const Line &l) {
    Big t0 = l.a * v.x0 + l.b * v.y0 + l.c * v.det;
    Big t1 = l.a * v.xe + l.b * v.ye + v.det;
    if (v.det < 0) {
        t0 = -t0;
        t1 = -t1;
    }
    if (t0 != 0)
        return t0 < 0 ? -1 : 1;
    return (t1 > 0) - (t1 < 0);
}

// cut the polygon, given by its lines in boundary order, by the line
std::vector<Line> clip(const std::vector<Line> &edges, const Line &l) {
    int m = edges.size();
    std::vector<int> sides(m);
    for (int k = 0; k < m; k++)
        sides[k] = side(corner(edges[(k + m - 1) % m], edges[k]), l);
    // edge k runs from corner k to corner k + 1; it stays if part of it is inside
    std::vector<bool> keep(m);
    int start = -1;
    for (int k = 0; k < m; k++) {
        keep[k] = sides[k] < 0 || sides[(k + 1) % m] < 0;
        if (keep[k] && start < 0)
            start = k;
    }
    std::vector<Line> out;
    if (start < 0)
        return out;
    for (int step = 0; step < m; step++) {
        int k = (start + step) % m, next = (k + 1) % m;
        if (!keep[k])
            continue;
        out.push_back(edges[k]);
        // the boundary leaves the half-plane before the next kept edge
        if (!keep[next] || sides[next] > 0)
            out.push_back(l);
    }
    if ((int)out.size() < STAGES)
        out.clear();
    return out;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<long long>> s(n, std::vector<long long>(STAGES));
    for (auto &row : s)
        for (auto &v : row)
            scanf("%lld", &v);
    // the sides of the triangle x > 0, y > 0, x + y < 1, in boundary order
    const std::vector<Line> triangle = {{0, -1, 0}, {1, 1, -1}, {-1, 0, 0}};
    for (int i = 0; i < n; i++) {
        std::vector<Line> edges = triangle;
        for (int j = 0; j < n && !edges.empty(); j++) {
            if (j == i)
                continue;
            // with u_k = length_k / s_ik > 0, i beats j when
            // sum (s_jk - s_ik) / s_jk * u_k < 0; times s_j1 s_j2 s_j3 the
            // coefficients are integers below 10^12
            long long g[STAGES];
            for (int k = 0; k < STAGES; k++)
                g[k] = (s[j][k] - s[i][k]) * (s[j][(k + 1) % STAGES] * s[j][(k + 2) % STAGES]);
            // u_3 = 1 - x - y on the triangle
            Line l = {g[0] - g[2], g[1] - g[2], g[2]};
            if (l.a == 0 && l.b == 0) {
                if (l.c >= 0)
                    edges.clear();
                continue;
            }
            edges = clip(edges, l);
        }
        puts(edges.empty() ? "No" : "Yes");
    }
}
