#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;

const double THIRD = 1.0 / 3; // a pyramid is a third of its prism

int main() {
    double h, w, x, y, r;
    cin >> h >> w >> x >> y >> r;
    // the hole meets no edge, so it lies over a single face, where the height
    // is linear: the cut-out volume is the hole's area times the height at
    // its centre, and that height falls from H to 0 with max(|x|, |y|)
    double centre = h * (1 - max(fabs(x), fabs(y)) / (w / 2));
    printf("%.5f\n", h * w * w * THIRD - acos(-1.0) * r * r * centre);
}
