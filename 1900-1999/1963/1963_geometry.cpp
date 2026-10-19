#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <utility>

constexpr int kVertexCount = 4;
using Point = std::pair<std::int64_t, std::int64_t>;
using Polygon = std::array<Point, kVertexCount>;

int boundaryCount(const Polygon &points) {
    std::set<Point> boundary;
    for (int shift = 0; shift < kVertexCount; ++shift) {
        Point a, b;
        if (shift % 2 == 0) {
            int first = shift / 2, opposite = (first + 2) % kVertexCount;
            a = {2 * points[first].first, 2 * points[first].second};
            b = {2 * points[opposite].first, 2 * points[opposite].second};
        } else {
            a = {points[0].first + points[shift].first, points[0].second + points[shift].second};
            std::array<int, 2> remaining{};
            int count = 0;
            for (int i = 0; i < kVertexCount; ++i) {
                if (i != 0 && i != shift)
                    remaining[count++] = i;
            }
            const auto &p = points[remaining[0]];
            const auto &q = points[remaining[1]];
            b = {p.first + q.first, p.second + q.second};
        }
        auto dx = b.first - a.first, dy = b.second - a.second;
        if (dx == 0 && dy == 0)
            continue;
        bool valid = true;
        for (int i = 0; i < kVertexCount; ++i) {
            const auto &p = points[i];
            const auto &q = points[(shift - i + kVertexCount) % kVertexCount];
            if ((p.first + q.first - a.first) * dy != (p.second + q.second - a.second) * dx ||
                (p.first - q.first) * dx + (p.second - q.second) * dy != 0) {
                valid = false;
                break;
            }
        }
        if (valid) {
            boundary.insert(a);
            boundary.insert(b);
        }
    }
    return static_cast<int>(boundary.size());
}

int main() {
    Polygon points{};
    for (auto &point : points)
        std::cin >> point.first >> point.second;
    std::cout << boundaryCount(points) << '\n';
}
