#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

const int STRIPS = 20000;
const double PERCENT = 100;
const int FIELDS = 3;
const double MIDDLE = 0.5; // where in its strip the line is taken

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<double> cx(n), cy(n), r(n);
    for (int i = 0; i < n; i++) {
        if (scanf("%lf %lf %lf", &cx[i], &cy[i], &r[i]) != FIELDS)
            return 0;
    }
    // the area is the sum over thin vertical strips of the covered part of
    // the line through the middle of each strip
    double covered = 0;
    std::vector<std::pair<double, double>> pieces;
    for (int k = 0; k < STRIPS; k++) {
        double x = (k + MIDDLE) / STRIPS;
        pieces.clear();
        for (int i = 0; i < n; i++) {
            if (std::fabs(x - cx[i]) < r[i]) {
                double half = std::sqrt(r[i] * r[i] - (x - cx[i]) * (x - cx[i]));
                double low = std::max(0.0, cy[i] - half), high = std::min(1.0, cy[i] + half);
                if (low < high)
                    pieces.push_back({low, high});
            }
        }
        std::sort(pieces.begin(), pieces.end());
        double end = 0;
        for (auto &p : pieces) {
            if (p.second > end) {
                covered += p.second - std::max(p.first, end);
                end = p.second;
            }
        }
    }
    printf("%.6f\n", covered / STRIPS * PERCENT);
    return 0;
}
