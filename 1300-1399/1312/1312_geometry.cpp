#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const double EPS = 1e-9; // relative to the size of the tray
const int PLATES = 3;

struct P {
    double x, y;
};

double H, W, tol;
double radii[PLATES];
int order[PLATES];
P pos[PLATES];

bool fits(P p, double r) {
    return p.x >= r - tol && p.x <= H - r + tol && p.y >= r - tol && p.y <= W - r + tol;
}

// centres of a circle touching circles (a, ra) and (b, rb) from outside,
// with ra and rb already increased by its radius
void touching(P a, double ra, P b, double rb, std::vector<P> &out) {
    double dx = b.x - a.x, dy = b.y - a.y, d2 = dx * dx + dy * dy;
    if (d2 == 0)
        return;
    double d = std::sqrt(d2), x = (d2 + ra * ra - rb * rb) / (2 * d), h2 = (ra - x) * (ra + x);
    if (h2 < 0)
        return;
    double h = std::sqrt(h2), mx = a.x + dx * x / d, my = a.y + dy * x / d;
    out.push_back({mx - dy * h / d, my + dx * h / d});
    out.push_back({mx + dy * h / d, my - dx * h / d});
}

bool place(int k) {
    if (k == PLATES)
        return true;
    double r = radii[order[k]];
    double xs[] = {r, H - r}, ys[] = {r, W - r};
    std::vector<P> cand;
    for (double x : xs)
        for (double y : ys)
            cand.push_back({x, y}); // the four corners
    for (int i = 0; i < k; i++) {
        P q = pos[order[i]];
        double s = radii[order[i]] + r;
        for (double x : xs) { // against a side wall and a placed plate
            double t = s * s - (x - q.x) * (x - q.x);
            if (t >= 0) {
                cand.push_back({x, q.y - std::sqrt(t)});
                cand.push_back({x, q.y + std::sqrt(t)});
            }
        }
        for (double y : ys) {
            double t = s * s - (y - q.y) * (y - q.y);
            if (t >= 0) {
                cand.push_back({q.x - std::sqrt(t), y});
                cand.push_back({q.x + std::sqrt(t), y});
            }
        }
        for (int j = 0; j < i; j++) { // against two placed plates
            touching(q, s, pos[order[j]], radii[order[j]] + r, cand);
        }
    }
    for (P p : cand) {
        if (!fits(p, r))
            continue;
        bool ok = true;
        for (int i = 0; i < k && ok; i++) {
            P q = pos[order[i]];
            ok = std::hypot(p.x - q.x, p.y - q.y) >= r + radii[order[i]] - tol;
        }
        if (!ok)
            continue;
        pos[order[k]] = p;
        if (place(k + 1))
            return true;
    }
    return false;
}

int main() {
    if (scanf("%lf %lf %lf %lf %lf", &H, &W, &radii[0], &radii[1], &radii[2]) != PLATES + 2)
        return 0;
    tol = EPS * (H + W);
    // pushing every plate down and to the left as far as it goes leaves each
    // one held by two walls or plates placed before it, so some order of the
    // plates and some choice of two such supports finds a placement
    for (int i = 0; i < PLATES; i++)
        order[i] = i;
    do {
        if (place(0)) {
            for (int i = 0; i < PLATES; i++)
                printf(i ? " %.4f %.4f" : "%.4f %.4f", pos[i].x, pos[i].y);
            printf("\n");
            return 0;
        }
    } while (std::next_permutation(order, order + PLATES));
    printf("0\n");
    return 0;
}
