#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

const double SHORTEST = 1.0, LONGEST = 50.0; // the allowed rope lengths
const double EPS = 1e-9;
const double PI = acos(-1.0);

// the largest a^2 + b^2 with 1 <= a <= topA, 1 <= b <= topB, a + b <= d, or -1
double bestPair(double topA, double topB, double d) {
    if (topA < SHORTEST - EPS || topB < SHORTEST - EPS || d < 2 * SHORTEST - EPS)
        return -1;
    // a convex function is largest at a corner of the region
    double corners[][2] = {
        {topA, topB},     {topA, SHORTEST},         {SHORTEST, topB},        {topA, d - topA},
        {d - topB, topB}, {d - SHORTEST, SHORTEST}, {SHORTEST, d - SHORTEST}};
    double best = -1;
    for (auto &c : corners) {
        double a = c[0], b = c[1];
        if (a >= SHORTEST - EPS && a <= topA + EPS && b >= SHORTEST - EPS && b <= topB + EPS &&
            a + b <= d + EPS)
            best = max(best, a * a + b * b);
    }
    return best;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<double> x(n), y(n), top(n, LONGEST);
    for (int i = 0; i < n; i++)
        scanf("%lf %lf", &x[i], &y[i]);
    // the longest rope at each tree: up to the nearest other tree and 50 meters
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (j != i)
                top[i] = min(top[i], hypot(x[i] - x[j], y[i] - y[j]));
    double best = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            best = max(best, bestPair(top[i], top[j], hypot(x[i] - x[j], y[i] - y[j])));
    printf("%.4f\n", PI * best);
}
