#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>
#include <numeric>
#include <vector>

// halvings of the radius interval; far more than double precision needs
const int STEPS = 200;
const double PI = std::acos(-1.0);

// the largest area belongs to the polygon inscribed in a circle; a side of
// length l sees the centre at the angle 2 asin(l / 2R)
double angle(double length, double r) { return 2 * std::asin(std::min(1.0, length / (2 * r))); }

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> sides(n);
    for (int &s : sides)
        if (scanf("%d", &s) != 1)
            return 0;
    std::sort(sides.begin(), sides.end());
    int longest = sides.back();
    std::vector<int> rest(sides.begin(), sides.end() - 1);
    if (longest >= std::accumulate(rest.begin(), rest.end(), 0)) {
        puts("0.00");
        return 0;
    }
    auto sum = [](const std::vector<int> &v, double r) {
        double total = 0;
        for (int s : v)
            total += angle(s, r);
        return total;
    };
    double low = longest / 2.0;
    bool inside = sum(sides, low) >= 2 * PI;
    // with the centre inside, the angles fill the full turn; otherwise the
    // longest side's angle equals the sum of the others
    std::function<double(double)> surplus = [&](double r) {
        return inside ? sum(sides, r) - 2 * PI : angle(longest, r) - sum(rest, r);
    };
    double high = low;
    while (surplus(high) > 0)
        high *= 2;
    for (int k = 0; k < STEPS; k++) {
        double mid = (low + high) / 2;
        if (surplus(mid) > 0)
            low = mid;
        else
            high = mid;
    }
    double r = (low + high) / 2, area = 0;
    for (int s : rest)
        area += std::sin(angle(s, r));
    area += (inside ? 1 : -1) * std::sin(angle(longest, r));
    printf("%.2f\n", r * r * area / 2);
}
