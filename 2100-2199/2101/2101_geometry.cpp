#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>

using Integer = std::int64_t;
using Wide = __int128_t;

constexpr int VERTEX_COUNT = 3;
constexpr int DECIMAL_PLACES = 10;
constexpr Integer SCALE = 10000000000LL;

struct Point {
    Integer x;
    Integer y;
};

Point subtract(Point a, Point b) { return {a.x - b.x, a.y - b.y}; }

Integer dot(Point a, Point b) { return a.x * b.x + a.y * b.y; }

Integer cross(Point a, Point b) { return a.x * b.y - a.y * b.x; }

int main() {
    std::array<Point, VERTEX_COUNT> vertices;
    for (Point &point : vertices) {
        std::cin >> point.x >> point.y;
    }
    Point hole;
    std::cin >> hole.x >> hole.y;

    Integer best = 0;
    int count = 0;
    auto consider = [&](Wide numerator, Wide denominator) {
        Integer rounded = static_cast<Integer>((numerator * SCALE + denominator / 2) / denominator);
        best = std::max(best, rounded);
        ++count;
    };

    for (int index = 0; index < VERTEX_COUNT; ++index) {
        Point origin = vertices[index];
        Point base = subtract(vertices[(index + 1) % VERTEX_COUNT], origin);
        Point apex = subtract(vertices[(index + 2) % VERTEX_COUNT], origin);
        Point inside = subtract(hole, origin);
        Integer length = dot(base, base);
        Integer projection = dot(base, apex);
        if (projection < 0 || projection >= length) {
            continue;
        }

        Integer position = dot(base, inside);
        Integer height = std::abs(cross(base, apex));
        Integer offset = std::abs(cross(base, inside));
        // Omitting one right-angle base also removes all repeated rectangles.
        consider(static_cast<Wide>(offset) * (height - offset), height);
        if (position < projection) {
            consider(static_cast<Wide>(height) * position * (projection - position),
                     static_cast<Wide>(projection) * projection);
        } else if (position > projection) {
            Integer remaining = length - projection;
            consider(static_cast<Wide>(height) * (length - position) * (position - projection),
                     static_cast<Wide>(remaining) * remaining);
        }
    }

    std::cout << best / SCALE << '.' << std::setfill('0') << std::setw(DECIMAL_PLACES)
              << best % SCALE << '\n'
              << count << '\n';
}
