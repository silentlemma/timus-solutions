#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

struct Point {
    long long x;
    long long y;
};

bool reversed(const Point &point) { return point.y < 0 || (point.y == 0 && point.x < 0); }

bool direction_less(const Point &a, const Point &b) {
    long long cross = a.x * b.y - a.y * b.x;
    if (reversed(a) != reversed(b)) {
        cross = -cross;
    }
    return cross > 0;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    std::cin >> count;
    std::vector<Point> points(count);
    bool has_origin = false;
    for (Point &point : points) {
        std::cin >> point.x >> point.y;
        has_origin = has_origin || (point.x == 0 && point.y == 0);
    }

    double answer = 0;
    if (!has_origin) {
        // A line direction is unchanged when its vector is reversed.
        std::sort(points.begin(), points.end(), direction_less);
        answer = std::numeric_limits<double>::infinity();
        Point previous = points.back();
        for (const Point &point : points) {
            const long long cross = previous.x * point.y - previous.y * point.x;
            const long long dx = previous.x - point.x;
            const long long dy = previous.y - point.y;
            const double distance = std::abs(static_cast<double>(cross)) /
                                    std::sqrt(static_cast<double>(dx * dx + dy * dy));
            answer = std::min(answer, distance);
            previous = point;
        }
    }

    constexpr int PRECISION = 10;
    std::cout << std::fixed << std::setprecision(PRECISION) << answer << '\n';
}
