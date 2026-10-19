#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

constexpr int OUTPUT_PRECISION = 12;

struct Point {
    std::int64_t x, y;
};
struct Direction {
    double key;
    std::int64_t x, y;
    int other;
};

double minimumDistance(const std::vector<Point> &points) {
    double best = std::numeric_limits<double>::infinity();
    const int n = static_cast<int>(points.size());
    std::vector<Direction> directions;
    directions.reserve(points.size());
    for (int pivot = 0; pivot + 1 < n; ++pivot) {
        directions.clear();
        std::int64_t totalX = 0, totalY = 0;
        for (int other = 0; other < n; ++other) {
            auto dx = points[other].x - points[pivot].x;
            auto dy = points[other].y - points[pivot].y;
            if (dx == 0 && dy == 0)
                continue;
            if (dy < 0 || (dy == 0 && dx < 0)) {
                dx = -dx;
                dy = -dy;
            }
            directions.push_back({-static_cast<double>(dx) / (std::abs(dx) + dy), dx, dy, other});
            totalX += dx;
            totalY += dy;
        }
        std::sort(directions.begin(), directions.end(),
                  [](const Direction &a, const Direction &b) { return a.key < b.key; });
        for (const auto &d : directions) {
            if (d.other > pivot) {
                const auto numerator = d.x * totalY - d.y * totalX;
                if (numerator == 0)
                    return 0.0;
                const double value = static_cast<double>(numerator) /
                                     std::sqrt(static_cast<double>(d.x * d.x + d.y * d.y));
                best = std::min(best, value);
            }
            totalX -= 2 * d.x;
            totalY -= 2 * d.y;
        }
    }
    return std::isfinite(best) ? best : 0.0;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<Point> points(n);
    for (auto &p : points)
        std::cin >> p.x >> p.y;
    std::cout << std::fixed << std::setprecision(OUTPUT_PRECISION) << minimumDistance(points)
              << '\n';
}
