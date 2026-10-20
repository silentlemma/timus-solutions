#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

constexpr int COORDINATE_LIMIT = 10000;
constexpr int GRAVITY = 10;
constexpr int HALF_GRAVITY = GRAVITY / 2;
constexpr int OUTPUT_DIGITS = 9;

struct Point {
    int height;
    int column;
    int density;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count, start_x, start_y;
    std::cin >> count >> start_x >> start_y;
    std::vector<Point> points(count + 1);
    for (int i = 0; i < count; ++i) {
        int x, y, density;
        std::cin >> x >> y >> density;
        points[i] = {y, x + COORDINATE_LIMIT, density};
    }
    points[count] = {start_y, start_x + COORDINATE_LIMIT, 0};
    std::sort(points.begin(), points.end(),
              [](const Point &a, const Point &b) { return a.height < b.height; });

    std::vector<double> fall_time(start_y + 1);
    for (int height = 0; height <= start_y; ++height) {
        fall_time[height] = std::sqrt(static_cast<double>(height) / HALF_GRAVITY);
    }

    const int column_count = 2 * COORDINATE_LIMIT + 1;
    std::vector<std::vector<int>> heights(column_count);
    std::vector<std::vector<double>> durations(column_count);
    double answer = 0;
    for (const Point &point : points) {
        double best = fall_time[point.height];
        const int radius = static_cast<int>(fall_time[point.height - 1]);
        const int left = std::max(0, point.column - radius);
        const int right = std::min(column_count - 1, point.column + radius);
        for (int column = left; column <= right; ++column) {
            const auto &levels = heights[column];
            if (levels.empty()) {
                continue;
            }
            const int dx = column - point.column;
            const int ceiling = point.height - HALF_GRAVITY * dx * dx;
            const auto after = std::upper_bound(levels.begin(), levels.end(), ceiling);
            if (after == levels.begin()) {
                continue;
            }
            // The highest reachable cloud dominates all lower clouds in its column.
            const auto index = static_cast<std::size_t>(after - levels.begin() - 1);
            best =
                std::max(best, fall_time[point.height - levels[index]] + durations[column][index]);
        }
        answer = best + point.density;
        heights[point.column].push_back(point.height);
        durations[point.column].push_back(answer);
    }

    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS) << answer << '\n';
}
