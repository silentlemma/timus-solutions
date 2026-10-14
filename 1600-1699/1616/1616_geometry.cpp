#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const double EPS = 1e-9;
const double HALF = 0.5; // a cell goes to an owner who held more than half of it
const int LETTERS = 26;
const double PI = acos(-1.0);
const double STRAIGHT = 180; // degrees in a half turn
const int CORNERS = 4;
const size_t TRIANGLE = 3; // the fewest corners of a polygon with area

struct P {
    double c[2];
};

// the part of a convex polygon with coordinate axis >= bound (or <=)
vector<P> clip(const vector<P> &poly, int axis, double bound, bool keepAbove) {
    vector<P> out;
    size_t count = poly.size();
    for (size_t i = 0; i < count; i++) {
        const P &a = poly[i], &b = poly[(i + 1) % count];
        bool inA = keepAbove ? a.c[axis] >= bound - EPS : a.c[axis] <= bound + EPS;
        bool inB = keepAbove ? b.c[axis] >= bound - EPS : b.c[axis] <= bound + EPS;
        if (inA != inB) {
            double t = (bound - a.c[axis]) / (b.c[axis] - a.c[axis]);
            out.push_back({{a.c[0] + (b.c[0] - a.c[0]) * t, a.c[1] + (b.c[1] - a.c[1]) * t}});
        }
        if (inB)
            out.push_back(b);
    }
    return out;
}

double area(const vector<P> &poly) {
    double total = 0;
    for (size_t i = 0; i < poly.size(); i++) {
        const P &a = poly[i], &b = poly[(i + 1) % poly.size()];
        total += a.c[0] * b.c[1] - b.c[0] * a.c[1];
    }
    return fabs(total) / 2;
}

int main() {
    int n;
    double alpha;
    if (!(cin >> n >> alpha))
        return 0;
    vector<string> grid(2 * n);
    for (auto &row : grid)
        cin >> row;
    int size = 2 * (2 * n); // the new map covers twice the old side
    // owned area of each new cell, per owner letter
    vector<vector<double>> held(size * size, vector<double>(LETTERS, 0));
    double rad = alpha * PI / STRAIGHT, cosA = cos(rad), sinA = sin(rad);
    for (int row = 0; row < 2 * n; row++) {
        int y = n - 1 - row;
        for (int col = 0; col < 2 * n; col++) {
            char owner = grid[row][col];
            if (owner == '.')
                continue;
            int x = col - n;
            // the axes turn clockwise, so the cell turns counterclockwise
            int cx[] = {x, x + 1, x + 1, x}, cy[] = {y, y, y + 1, y + 1};
            vector<P> square;
            double xLo = INFINITY, xHi = -INFINITY, yLo = INFINITY, yHi = -INFINITY;
            for (int k = 0; k < CORNERS; k++) {
                P p = {{cx[k] * cosA - cy[k] * sinA, cx[k] * sinA + cy[k] * cosA}};
                square.push_back(p);
                xLo = min(xLo, p.c[0]), xHi = max(xHi, p.c[0]);
                yLo = min(yLo, p.c[1]), yHi = max(yHi, p.c[1]);
            }
            int x0 = max(-2 * n, (int)floor(xLo + EPS)), x1 = min(2 * n, (int)ceil(xHi - EPS));
            int y0 = max(-2 * n, (int)floor(yLo + EPS)), y1 = min(2 * n, (int)ceil(yHi - EPS));
            int letter = owner - 'a';
            for (int gy = y0; gy < y1; gy++)
                for (int gx = x0; gx < x1; gx++) {
                    vector<P> part = clip(square, 0, gx, true);
                    part = clip(part, 0, gx + 1, false);
                    part = clip(part, 1, gy, true);
                    part = clip(part, 1, gy + 1, false);
                    if (part.size() >= TRIANGLE)
                        held[(2 * n - 1 - gy) * size + gx + 2 * n][letter] += area(part);
                }
        }
    }
    string out;
    for (int r = 0; r < size; r++) {
        for (int c = 0; c < size; c++) {
            char best = '.';
            for (int i = 0; i < LETTERS; i++)
                if (held[r * size + c][i] > HALF + EPS) {
                    best = 'a' + i;
                    break;
                }
            out += best;
        }
        out += '\n';
    }
    fputs(out.c_str(), stdout);
}
