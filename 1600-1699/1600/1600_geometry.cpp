#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

const int DIM = 3; // x, y, z, then vx, vy, vz
const int COORDS = 2 * DIM;

int main() {
    int n;
    double d;
    if (scanf("%d %lf", &n, &d) != 2)
        return 0;
    vector<vector<double>> obj(n, vector<double>(COORDS));
    for (auto &o : obj)
        for (double &v : o)
            if (scanf("%lf", &v) != 1)
                return 0;
    double best = INFINITY;
    int bestA = -1, bestB = -1;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            const vector<double> &p = obj[i], &q = obj[j];
            // |p + v t| = d for the relative position p and velocity v:
            // (v.v) t^2 + 2 (p.v) t + (p.p - d^2) = 0
            double a = 0, b = 0, c = -d * d;
            for (int k = 0; k < DIM; k++) {
                double dp = q[k] - p[k], dv = q[DIM + k] - p[DIM + k];
                a += dv * dv;
                b += dp * dv;
                c += dp * dp;
            }
            if (a == 0)
                continue;
            double disc = b * b - a * c;
            if (disc < 0)
                continue;
            // the earlier root; the pair starts apart, so a negative one
            // means they are moving away
            double t = (-b - sqrt(disc)) / a;
            if (t >= 0 && t < best) {
                best = t;
                bestA = i + 1;
                bestB = j + 1;
            }
        }
    if (bestA < 0)
        printf("OK\n");
    else
        printf("ALARM!\n%.3f %d %d\n", best, bestA, bestB);
}
