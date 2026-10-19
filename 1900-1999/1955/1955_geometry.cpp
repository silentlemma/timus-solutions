#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <utility>
#include <vector>

using Integer = std::int64_t;
struct Point {
    Integer x, y;
};
struct Edge {
    Integer x, y, constant;
};
struct Span {
    double length;
    bool visible;
};

Span lineSpan(const std::vector<Point> &points, const std::vector<Edge> &edges, Integer px,
              Integer py, Integer dx, Integer dy) {
    const int n = static_cast<int>(points.size());
    const Integer offset = dx * py - dy * px, squared = dx * dx + dy * dy;
    std::vector<Integer> heights(n);
    for (int i = 0; i < n; ++i)
        heights[i] = dx * points[i].y - dy * points[i].x - offset;
    std::vector<double> hits;
    std::vector<std::pair<double, double>> intervals;
    Integer previous = heights.back();
    for (int i = 0; i < n; ++i) {
        Integer height = heights[i];
        if ((previous > 0) != (height > 0)) {
            const auto &edge = edges[i];
            hits.push_back(static_cast<double>(edge.constant - px * edge.y + py * edge.x) /
                           static_cast<double>(height - previous));
        } else if (height == 0 && previous == 0) {
            const auto &a = points[(i + n - 1) % n];
            const auto &b = points[i];
            double first = static_cast<double>((a.x - px) * dx + (a.y - py) * dy) / squared;
            double second = static_cast<double>((b.x - px) * dx + (b.y - py) * dy) / squared;
            intervals.emplace_back(std::min(first, second), std::max(first, second));
        }
        previous = height;
    }
    std::sort(hits.begin(), hits.end());
    for (std::size_t i = 0; i < hits.size(); i += 2)
        intervals.emplace_back(hits[i], hits[i + 1]);
    if (intervals.empty())
        return {0.0, false};
    std::sort(intervals.begin(), intervals.end());
    double left = intervals[0].first, right = intervals[0].second, best = 0;
    bool visible = false;
    for (std::size_t i = 1; i < intervals.size(); ++i) {
        auto [start, end] = intervals[i];
        if (start <= right)
            right = std::max(right, end);
        else {
            best = std::max(best, right - left);
            visible = visible || (left <= 0 && right >= 1);
            left = start;
            right = end;
        }
    }
    return {std::max(best, right - left), visible || (left <= 0 && right >= 1)};
}

double longestSegment(const std::vector<Point> &points) {
    int n = static_cast<int>(points.size());
    std::vector<Edge> edges(n);
    Integer lower = 0, diameter = 0;
    Integer minX = points[0].x, maxX = minX, minY = points[0].y, maxY = minY;
    Point endpoint{}, direction{};
    for (int i = 0; i < n; ++i) {
        const auto &a = points[(i + n - 1) % n];
        const auto &b = points[i];
        edges[i] = {b.x - a.x, b.y - a.y, a.x * b.y - a.y * b.x};
        lower = std::max(lower, edges[i].x * edges[i].x + edges[i].y * edges[i].y);
        minX = std::min(minX, b.x);
        maxX = std::max(maxX, b.x);
        minY = std::min(minY, b.y);
        maxY = std::max(maxY, b.y);
        for (int j = 0; j < i; ++j) {
            Integer dx = points[j].x - b.x, dy = points[j].y - b.y;
            Integer squared = dx * dx + dy * dy;
            if (squared > diameter) {
                diameter = squared;
                endpoint = b;
                direction = {dx, dy};
            }
        }
    }
    Span initial = lineSpan(points, edges, endpoint.x, endpoint.y, direction.x, direction.y);
    if (initial.visible)
        return std::sqrt(static_cast<double>(diameter));
    double best = std::max(static_cast<double>(lower), initial.length * initial.length * diameter);
    Integer widthSquared = (maxX - minX) * (maxX - minX);
    Integer heightSquared = (maxY - minY) * (maxY - minY);
    std::set<std::tuple<Integer, Integer, Integer>> seen;
    for (int i = 0; i < n; ++i) {
        const auto &p = points[i];
        for (int j = 0; j < i; ++j) {
            Integer dx = points[j].x - p.x, dy = points[j].y - p.y;
            Integer squared = dx * dx + dy * dy;
            if (widthSquared * squared < lower * dx * dx ||
                heightSquared * squared < lower * dy * dy)
                continue;
            Integer divisor = std::gcd(dx, dy), nx = dx / divisor, ny = dy / divisor;
            if (nx < 0 || (nx == 0 && ny < 0)) {
                nx = -nx;
                ny = -ny;
            }
            if (!seen.emplace(nx, ny, nx * p.y - ny * p.x).second)
                continue;
            Span span = lineSpan(points, edges, p.x, p.y, dx, dy);
            if (span.visible) {
                lower = std::max(lower, squared);
                if (lower == diameter)
                    return std::sqrt(static_cast<double>(diameter));
            }
            best =
                std::max({best, span.length * span.length * squared, static_cast<double>(lower)});
        }
    }
    return std::sqrt(best);
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Point> points(n);
    for (auto &point : points)
        std::cin >> point.x >> point.y;
    constexpr int OUTPUT_PRECISION = 12;
    std::cout << std::fixed << std::setprecision(OUTPUT_PRECISION) << longestSegment(points)
              << '\n';
}
