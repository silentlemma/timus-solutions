#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const double SAFE = 0.1;
const double INF = 1e300;
const double SAME = 1e-9;

struct Pt {
    double x, y;
};

struct Polygon {
    std::vector<Pt> v, d; // corners and the edge vectors leaving them
    double cx, cy, r;
};

// A place on a boundary: edge index and position along that edge.
struct Pos {
    int edge;
    double t;
};

// The nearest point of the edges to p if closer than best; updates best
// (squared distance) and where.
static bool pointEdges(Pt p, const Polygon &poly, double &best, Pos &where) {
    bool found = false;
    for (size_t i = 0; i < poly.v.size(); i++) {
        double wx = p.x - poly.v[i].x, wy = p.y - poly.v[i].y;
        double dx = poly.d[i].x, dy = poly.d[i].y, d2 = dx * dx + dy * dy;
        double t = wx * dx + wy * dy, q;
        if (t <= 0) {
            q = wx * wx + wy * wy, t = 0;
        } else if (t >= d2) {
            q = (wx - dx) * (wx - dx) + (wy - dy) * (wy - dy), t = 1;
        } else {
            double c = wx * dy - wy * dx;
            q = c * c / d2, t /= d2;
        }
        if (q < best) {
            best = q, where = {(int)i, t}, found = true;
        }
    }
    return found;
}

// Squared distance between two polygons and where it is reached on each.
static double polyPoly(const Polygon &a, const Polygon &b, Pos &onA, Pos &onB) {
    double best = INF;
    for (int side = 0; side < 2; side++) {
        const Polygon &own = side ? b : a;
        const Polygon &other = side ? a : b;
        for (size_t k = 0; k < own.v.size(); k++) {
            Pos there;
            if (pointEdges(own.v[k], other, best, there)) {
                Pos here = {(int)k, 0};
                onA = side ? there : here;
                onB = side ? here : there;
            }
        }
    }
    return best;
}

static Pt at(const Polygon &poly, Pos p) {
    return {poly.v[p.edge].x + poly.d[p.edge].x * p.t, poly.v[p.edge].y + poly.d[p.edge].y * p.t};
}

// Corners passed going along the boundary from src to dst, in the direction
// with fewer of them.
static void walk(const Polygon &poly, Pos src, Pos dst, std::vector<Pt> &path) {
    int k = (int)poly.v.size();
    int fwd = ((dst.edge - src.edge) % k + k) % k, back = ((src.edge - dst.edge) % k + k) % k;
    if (fwd == 0) {
        fwd = dst.t >= src.t ? 0 : k;
    }
    if (back == 0) {
        back = dst.t <= src.t ? 0 : k;
    }
    if (fwd <= back) {
        for (int s = 0; s < fwd; s++) {
            path.push_back(poly.v[(src.edge + 1 + s) % k]);
        }
    } else {
        for (int s = 0; s < back; s++) {
            path.push_back(poly.v[((src.edge - s) % k + k) % k]);
        }
    }
}

static Pt toward(Pt f, Pt p, double len) {
    double d = std::hypot(p.x - f.x, p.y - f.y);
    return {f.x + (p.x - f.x) * len / d, f.y + (p.y - f.y) * len / d};
}

int main() {
    Pt mouse, cheese;
    int n;
    scanf("%lf %lf %lf %lf %d", &mouse.x, &mouse.y, &cheese.x, &cheese.y, &n);
    std::vector<Polygon> polys(n);
    for (auto &poly : polys) {
        int k;
        scanf("%d", &k);
        poly.v.resize(k);
        poly.cx = poly.cy = 0;
        for (auto &p : poly.v) {
            scanf("%lf %lf", &p.x, &p.y);
            poly.cx += p.x / k, poly.cy += p.y / k;
        }
        // the corners may come in any order, so sort them around the centre
        std::sort(poly.v.begin(), poly.v.end(), [&](Pt a, Pt b) {
            return std::atan2(a.y - poly.cy, a.x - poly.cx) <
                   std::atan2(b.y - poly.cy, b.x - poly.cx);
        });
        poly.r = 0;
        for (int i = 0; i < k; i++) {
            Pt next = poly.v[(i + 1) % k];
            poly.d.push_back({next.x - poly.v[i].x, next.y - poly.v[i].y});
            poly.r = std::max(poly.r, std::hypot(poly.v[i].x - poly.cx, poly.v[i].y - poly.cy));
        }
    }

    // nodes 0..n-1 are the safe zones around the furniture, n the mouse and
    // n + 1 the cheese; an edge costs the dangerous length between them
    auto toPoint = [&](Pt p, int a) {
        double best = INF;
        Pos where;
        pointEdges(p, polys[a], best, where);
        return std::max(0.0, std::sqrt(best) - SAFE);
    };
    int start = n, goal = n + 1;
    std::vector<double> dist(n + 2, INF);
    std::vector<int> parent(n + 2, -1);
    std::vector<bool> done(n + 2, false);
    dist[start] = 0;
    while (true) {
        int u = -1;
        for (int v = 0; v < n + 2; v++) {
            if (!done[v] && (u < 0 || dist[v] < dist[u])) {
                u = v;
            }
        }
        if (u == goal) {
            break;
        }
        done[u] = true;
        for (int v = 0; v < n + 2; v++) {
            if (done[v]) {
                continue;
            }
            double w;
            if (v == goal && u == start) {
                w = std::hypot(mouse.x - cheese.x, mouse.y - cheese.y);
            } else if (v == goal) {
                w = toPoint(cheese, u);
            } else if (u == start) {
                w = toPoint(mouse, v);
            } else {
                const Polygon &a = polys[u], &b = polys[v];
                double gap = std::hypot(a.cx - b.cx, a.cy - b.cy) - a.r - b.r - 2 * SAFE;
                if (dist[u] + gap >= dist[v]) {
                    continue;
                }
                Pos pa, pb;
                w = std::sqrt(polyPoly(a, b, pa, pb)) - 2 * SAFE;
            }
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w, parent[v] = u;
            }
        }
    }
    std::vector<int> route = {goal};
    while (route.back() != start) {
        route.push_back(parent[route.back()]);
    }
    std::reverse(route.begin(), route.end());

    std::vector<Pt> path = {mouse};
    if (route.size() == 2) {
        path.push_back(cheese);
    } else {
        // step from the mouse onto the nearest point of the first piece
        const Polygon &first = polys[route[1]];
        double q = INF;
        Pos here;
        pointEdges(mouse, first, q, here);
        Pt foot = at(first, here);
        if (std::sqrt(q) > SAFE) {
            path.push_back(toward(foot, mouse, SAFE));
        }
        path.push_back(foot);
        for (size_t i = 1; i + 2 < route.size(); i++) {
            const Polygon &a = polys[route[i]], &b = polys[route[i + 1]];
            Pos outPos, inPos;
            polyPoly(a, b, outPos, inPos);
            Pt fa = at(a, outPos), fb = at(b, inPos);
            walk(a, here, outPos, path);
            path.push_back(fa);
            path.push_back(toward(fa, fb, SAFE));
            path.push_back(toward(fb, fa, SAFE));
            path.push_back(fb);
            here = inPos;
        }
        const Polygon &last = polys[route[route.size() - 2]];
        q = INF;
        Pos end;
        pointEdges(cheese, last, q, end);
        foot = at(last, end);
        walk(last, here, end, path);
        path.push_back(foot);
        if (std::sqrt(q) > SAFE) {
            path.push_back(toward(foot, cheese, SAFE));
        }
        path.push_back(cheese);
    }

    std::vector<Pt> out = {path[0]};
    for (size_t i = 1; i < path.size(); i++) {
        if (std::hypot(path[i].x - out.back().x, path[i].y - out.back().y) > SAME) {
            out.push_back(path[i]);
        }
    }
    if (out.size() == 1) {
        out.push_back(path.back());
    }
    printf("%d\n", (int)out.size());
    for (Pt p : out) {
        printf("%.9f %.9f\n", p.x, p.y);
    }
}
