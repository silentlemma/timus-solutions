#include <cmath>
#include <complex>
#include <cstdio>
#include <set>
#include <vector>

using namespace std;

typedef complex<double> Pt;
const int MOST = 6;          // dots in one square
const int FULL = 4;          // from four dots on, all corners of the inner square are used
const double QUARTER = 0.25; // the inner square's corners are L / 4 from the centre

const double SMALLEST = 1, LARGEST = 100;
const double EPS = 2e-3; // the coordinates are given to 1e-4, and a fit spreads that error

// the dots of a square with k dots around centre, for L = 1, with the
// domino lying along the x axis
vector<Pt> square(int k, Pt centre) {
    double q = QUARTER;
    vector<Pt> dots;
    if (k >= 2)
        dots.insert(dots.end(), {{-q, -q}, {q, q}});
    if (k >= FULL)
        dots.insert(dots.end(), {{q, -q}, {-q, q}});
    if (k == MOST) {
        dots.push_back({0, -q}); // beside the long sides
        dots.push_back({0, q});
    }
    if (k % 2 == 1)
        dots.push_back(0);
    for (Pt &d : dots)
        d += centre;
    return dots;
}

// whether a similarity, maybe mirrored, with scale in the allowed range
// takes the template onto the given dots
bool fits(vector<Pt> pts, const vector<Pt> &given) {
    Pt g0 = given[0], g1 = given[0];
    for (Pt g : given)
        if (abs(g - g0) > abs(g1 - g0))
            g1 = g;
    for (int mirror = 0; mirror < 2; mirror++) {
        if (mirror)
            for (Pt &t : pts)
                t = conj(t);
        for (Pt a : pts)
            for (Pt b : pts) {
                if (a == b)
                    continue;
                Pt turn = (g1 - g0) / (b - a); // rotation times the scale L
                if (abs(turn) < SMALLEST - EPS || abs(turn) > LARGEST + EPS)
                    continue;
                set<int> hit;
                bool ok = true;
                for (Pt t : pts) {
                    Pt image = g0 + (t - a) * turn;
                    int near = 0;
                    for (size_t i = 1; i < given.size(); i++)
                        if (abs(given[i] - image) < abs(given[near] - image))
                            near = i;
                    if (abs(given[near] - image) > EPS) {
                        ok = false;
                        break;
                    }
                    hit.insert(near);
                }
                if (ok && hit.size() == given.size())
                    return true;
            }
    }
    return false;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<Pt> given(n);
    for (Pt &g : given) {
        double x, y;
        scanf("%lf %lf", &x, &y);
        g = {x, y};
    }
    for (int a = 0; a <= MOST; a++) {
        int b = n - a;
        if (a > b || b > MOST)
            continue;
        vector<Pt> pts = square(a, 0), right = square(b, 1);
        pts.insert(pts.end(), right.begin(), right.end());
        if (n == 1 || fits(pts, given))
            printf("%d %d\n", a, b);
    }
}
