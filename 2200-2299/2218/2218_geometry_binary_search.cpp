#include <algorithm>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

using Coordinate = std::int64_t;
using Point = std::pair<Coordinate, Coordinate>;

int count_segment(const std::vector<Point> &points, Coordinate fixed, Coordinate low,
                  Coordinate high) {
    auto first = std::lower_bound(points.begin(), points.end(), Point{fixed, low});
    auto last = std::upper_bound(points.begin(), points.end(), Point{fixed, high});
    return static_cast<int>(last - first);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    std::cin >> count;
    std::vector<Point> by_u(count);
    std::vector<Point> by_v(count);
    for (int i = 0; i < count; ++i) {
        Coordinate x, y;
        std::cin >> x >> y;
        by_u[i] = {x + y, x - y};
        by_v[i] = {x - y, x + y};
    }
    std::sort(by_u.begin(), by_u.end());
    std::sort(by_v.begin(), by_v.end());

    int queries;
    std::cin >> queries;
    while (queries--) {
        Coordinate x, y, distance;
        std::cin >> x >> y >> distance;
        Coordinate u = x + y;
        Coordinate v = x - y;
        if (distance == 0) {
            std::cout << count_segment(by_u, u, v, v) << '\n';
            continue;
        }

        int answer = count_segment(by_u, u - distance, v - distance, v + distance);
        answer += count_segment(by_u, u + distance, v - distance, v + distance);
        // The other two sides exclude corners already counted above.
        answer += count_segment(by_v, v - distance, u - distance + 1, u + distance - 1);
        answer += count_segment(by_v, v + distance, u - distance + 1, u + distance - 1);
        std::cout << answer << '\n';
    }
}
