#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <utility>
#include <vector>
using namespace std;

const double HALF = 0.5; // rounds to the nearest mile

int gcd(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return abs(a);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> xs(n), ys(n);
    for (int i = 0; i < n; i++)
        if (scanf("%d %d", &xs[i], &ys[i]) != 2)
            return 0;
    double total = 0;
    for (int i = 0; i < n; i++) {
        // the farthest city in each reduced direction from city i, in steps
        map<pair<int, int>, int> far;
        for (int j = 0; j < n; j++) {
            if (j == i)
                continue;
            int dx = xs[j] - xs[i], dy = ys[j] - ys[i];
            int g = gcd(dx, dy);
            int &steps = far[{dx / g, dy / g}];
            if (g > steps)
                steps = g;
        }
        for (auto &[d, steps] : far) {
            // city i ends the road in this direction when nothing lies behind it
            if (far.count({-d.first, -d.second}) == 0)
                total += steps * hypot((double)d.first, (double)d.second);
        }
    }
    // every road is found from both of its ends
    printf("%.0f\n", floor(total / 2 + HALF));
}
