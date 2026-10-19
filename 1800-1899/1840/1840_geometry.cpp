#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const double TOP = 10.0;  // the speed limit; both accelerations are limited by 1
const double EPS = 1e-12;
const double PI = std::acos(-1.0);

struct Piece {
    double length, cap;
};

// fastest run over a piece entered at v0 and left at v1: speed up,
// perhaps cruise at the cap, slow down
double pieceTime(const Piece &p, double v0, double v1) {
    if (p.length <= EPS) return 0;
    double up = (p.cap * p.cap - v0 * v0) / 2, down = (p.cap * p.cap - v1 * v1) / 2;
    if (up + down <= p.length) return (p.cap - v0) + (p.cap - v1) + (p.length - up - down) / p.cap;
    double peak = std::sqrt(p.length + (v0 * v0 + v1 * v1) / 2);
    return (peak - v0) + (peak - v1);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<double> ax(n), ay(n), bx(n), by(n), ux(n), uy(n), len(n), extra(n, 0);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf %lf %lf", &ax[i], &ay[i], &bx[i], &by[i]);
        len[i] = std::hypot(bx[i] - ax[i], by[i] - ay[i]);
        ux[i] = (bx[i] - ax[i]) / len[i];
        uy[i] = (by[i] - ay[i]) / len[i];
    }
    std::vector<Piece> arcs;
    for (int i = 0; i + 1 < n; i++) {
        double dx = ax[i + 1] - bx[i], dy = ay[i + 1] - by[i];
        double sine = ux[i] * uy[i + 1] - uy[i] * ux[i + 1];
        double cosine = ux[i] * ux[i + 1] + uy[i] * uy[i + 1];
        double radius, angle;
        if (std::fabs(sine) > EPS) {
            // the lines meet t past the end of this segment and back before
            // the start of the next one; the arc touches both lines at the
            // same distance from that point, as far as it can
            double t = (dx * uy[i + 1] - dy * ux[i + 1]) / sine;
            double back = -(dx * uy[i] - dy * ux[i]) / sine;
            double nearest = std::min(t, back);
            extra[i] += t - nearest;
            extra[i + 1] += back - nearest;
            if (std::fabs(nearest) <= EPS) {
                arcs.push_back({0, 0});
                continue;
            }
            radius = std::fabs(nearest) * (1 + cosine) / std::fabs(sine);
            double turn = std::atan2(std::fabs(sine), cosine);
            // a meeting point behind forces the long way around the circle
            angle = nearest > 0 ? turn : 2 * PI - turn;
        } else {
            // opposite directions: a half circle across the gap
            double along = dx * ux[i] + dy * uy[i], across = -dx * uy[i] + dy * ux[i];
            if (along > 0) {
                extra[i] += along;
            } else {
                extra[i + 1] -= along;
            }
            radius = std::fabs(across) / 2;
            angle = PI;
        }
        arcs.push_back({radius * angle, std::min(TOP, std::sqrt(radius))});
    }
    std::vector<Piece> pieces;
    for (int i = 0; i < n; i++) {
        pieces.push_back({len[i] + extra[i], TOP});
        if (i + 1 < n) pieces.push_back(arcs[i]);
    }
    // the speed where pieces meet: what acceleration from the start and
    // braking before the end allow, within the caps on both sides
    int m = pieces.size();
    std::vector<double> reach(m + 1, 0), stop(m + 1, 0);
    for (int i = 0; i < m; i++) {
        double free = std::sqrt(reach[i] * reach[i] + 2 * pieces[i].length);
        reach[i + 1] = std::min(pieces[i].cap, free);
    }
    for (int i = m - 1; i >= 0; i--) {
        double free = std::sqrt(stop[i + 1] * stop[i + 1] + 2 * pieces[i].length);
        stop[i] = std::min(pieces[i].cap, free);
    }
    double total = 0;
    for (int i = 0; i < m; i++) {
        double v0 = std::min(reach[i], stop[i]), v1 = std::min(reach[i + 1], stop[i + 1]);
        total += pieceTime(pieces[i], v0, v1);
    }
    printf("%.10f\n", total);
    return 0;
}
