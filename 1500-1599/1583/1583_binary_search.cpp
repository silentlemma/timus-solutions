#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

const double AREA = 100; // the cross-section of the bar, 10 by 10 cm
const double LENGTH = 100;
const double PIECE = 500;        // grams, at one gram per cubic centimetre
const long long MICRONS = 10000; // in a centimetre
const int STEPS = 100;
const double CAP = 3; // a cap of height h has volume pi h^2 (3 r - h) / 3
const double HALF = 0.5;

vector<pair<double, double>> holes; // centre along the bar, radius

// the weight of the bar from its start to the mark at (in cm): the full volume
// minus the part of every hole below the mark, a spherical cap of height h
// with volume pi h^2 (3 r - h) / 3
double cheese(double at) {
    double weight = AREA * at;
    for (auto [centre, r] : holes) {
        double h = min(max(at - (centre - r), 0.0), 2 * r);
        weight -= acos(-1.0) * h * h * (CAP * r - h) / CAP;
    }
    return weight;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; i++) {
        double x, y, z, r;
        if (scanf("%lf %lf", &x, &y) != 2 || scanf("%lf %lf", &z, &r) != 2)
            return 0;
        holes.push_back({y, r});
    }
    vector<long long> cuts;
    long long start = 0;
    while (cheese(LENGTH) - cheese((double)start / MICRONS) >= PIECE) {
        // the mark where the next piece reaches 500 grams, then rounded to the
        // micrometre grid; the next piece starts at the cut actually made
        double base = cheese((double)start / MICRONS);
        double lo = (double)start / MICRONS, hi = LENGTH;
        for (int i = 0; i < STEPS; i++) {
            double mid = (lo + hi) / 2;
            if (cheese(mid) - base < PIECE)
                lo = mid;
            else
                hi = mid;
        }
        start = (long long)floor(hi * MICRONS + HALF);
        if (start >= (long long)LENGTH * MICRONS)
            break;
        cuts.push_back(start);
    }
    printf("%d\n", (int)cuts.size());
    for (long long c : cuts)
        printf("%lld\n", c);
}
