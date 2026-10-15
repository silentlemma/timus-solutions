#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>

const double EPS = 1e-9;
const double INF = 1e18;
const int SIDES = 4;
const int POINTS = SIDES + 1;

double px[POINTS], py[POINTS];  // the mouse, then the corners of the book
double cx, cy, r;

double cross(double ax, double ay, double bx, double by) { return ax * by - ay * bx; }

// positive inside the book (the corners go counterclockwise)
double side(int i, double x, double y) {
    int a = 1 + i, b = 1 + (i + 1) % SIDES;
    return cross(px[b] - px[a], py[b] - py[a], x - px[a], y - py[a]);
}

bool outside(double x, double y) {
    for (int i = 0; i < SIDES; i++) {
        if (side(i, x, y) < -EPS) return true;
    }
    return false;
}

// whether the segment passes through the inside of the book
bool blocks(double ax, double ay, double bx, double by) {
    double lo = 0, hi = 1;
    for (int i = 0; i < SIDES; i++) {
        double f0 = side(i, ax, ay), f1 = side(i, bx, by);
        if (f0 <= EPS && f1 <= EPS) return false;
        if (f0 < f1 && f0 <= EPS) lo = std::max(lo, (EPS - f0) / (f1 - f0));
        if (f1 < f0 && f1 <= EPS) hi = std::min(hi, (f0 - EPS) / (f0 - f1));
    }
    return hi - lo > EPS;
}

// the closest point of the disk outside the book that (sx, sy) sees
double nearest(double sx, double sy) {
    double best = INF;
    double d = std::hypot(sx - cx, sy - cy);
    if (d > EPS) {
        double qx = cx + (sx - cx) * r / d, qy = cy + (sy - cy) * r / d;
        if (outside(qx, qy) && !blocks(sx, sy, qx, qy)) best = std::max(0.0, d - r);
    }
    for (int i = 0; i < SIDES; i++) {
        if (side(i, sx, sy) > EPS) continue;
        // the part of side i inside the disk, as a parameter range on it
        int a = 1 + i, b = 1 + (i + 1) % SIDES;
        double ex = px[b] - px[a], ey = py[b] - py[a];
        double qa = ex * ex + ey * ey;
        double qb = (px[a] - cx) * ex + (py[a] - cy) * ey;
        double qc = (px[a] - cx) * (px[a] - cx) + (py[a] - cy) * (py[a] - cy) - r * r;
        double disc = qb * qb - qa * qc;
        if (disc <= 0) continue;
        double lo = std::max(0.0, (-qb - std::sqrt(disc)) / qa);
        double hi = std::min(1.0, (-qb + std::sqrt(disc)) / qa);
        if ((hi - lo) * std::sqrt(qa) <= EPS) continue;
        double t = ((sx - px[a]) * ex + (sy - py[a]) * ey) / qa;
        t = std::min(std::max(t, lo), hi);
        best = std::min(best, std::hypot(px[a] + t * ex - sx, py[a] + t * ey - sy));
    }
    return best;
}

int main() {
    for (int i = 1; i < POINTS; i++) std::cin >> px[i] >> py[i];
    std::cin >> cx >> cy >> r >> px[0] >> py[0];
    // the mouse goes straight or around corners of the book; Dijkstra over
    // the mouse and the corners gives each its shortest way from the start
    double dist[POINTS];
    bool done[POINTS] = {};
    std::fill(dist, dist + POINTS, INF);
    dist[0] = 0;
    for (int step = 0; step < POINTS; step++) {
        int u = -1;
        for (int w = 0; w < POINTS; w++) {
            if (!done[w] && (u < 0 || dist[w] < dist[u])) u = w;
        }
        done[u] = true;
        for (int w = 1; w < POINTS; w++) {
            int gap = (u - w + SIDES) % SIDES;
            bool joined = gap == 1 || gap == SIDES - 1;
            if (u == 0) joined = !blocks(px[0], py[0], px[w], py[w]);
            if (w != u && joined) {
                dist[w] = std::min(dist[w], dist[u] + std::hypot(px[w] - px[u], py[w] - py[u]));
            }
        }
    }
    double answer = INF;
    for (int k = 0; k < POINTS; k++) answer = std::min(answer, dist[k] + nearest(px[k], py[k]));
    printf("%.5f\n", answer);
}
