#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

constexpr int DECIMAL_PLACES = 12;

struct Point {
    std::int64_t x, y;
};
struct Fraction {
    std::int64_t numerator, denominator;
};

double vertex_clearance(const std::vector<Point> &vertices, const std::vector<Point> &other,
                        std::int64_t sign) {
    double result = std::numeric_limits<double>::infinity();
    std::size_t index = 0;
    for (const auto &point : vertices) {
        while (index + 1 < other.size() && other[index + 1].y <= point.y)
            ++index;
        double gap;
        if (index + 1 == other.size())
            gap = static_cast<double>(sign * (other[index].x - point.x));
        else {
            const auto &a = other[index];
            const auto &b = other[index + 1];
            const auto numerator =
                (a.x - point.x) * (b.y - point.y) + (b.x - point.x) * (point.y - a.y);
            gap = static_cast<double>(sign * numerator) / static_cast<double>(b.y - a.y);
        }
        result = std::min(result, gap);
    }
    return result;
}

Fraction fraction_at(const std::vector<Point> &vertices, std::size_t &index, std::int64_t y) {
    while (index + 1 < vertices.size() && vertices[index + 1].y <= y)
        ++index;
    if (index + 1 == vertices.size())
        return {vertices[index].x, 1};
    const auto &a = vertices[index];
    const auto &b = vertices[index + 1];
    return {a.x * (b.y - y) + b.x * (y - a.y), b.y - a.y};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<Point> left(count);
    for (auto &point : left)
        std::cin >> point.x >> point.y;
    std::cin >> count;
    std::vector<Point> right(count);
    for (auto &point : right)
        std::cin >> point.x >> point.y;
    double answer = std::min(vertex_clearance(left, right, 1), vertex_clearance(right, left, -1));
    std::size_t first = 0, second = 0;
    std::vector<std::int64_t> group;
    auto process = [&](std::int64_t y) {
        if (y < left.front().y || y > left.back().y)
            return;
        const auto l = fraction_at(left, first, y), r = fraction_at(right, second, y);
        std::sort(group.begin(), group.end());
        bool found = false;
        std::int64_t previous = 0;
        double best = 0;
        for (const auto x : group) {
            if (x * l.denominator < l.numerator || x * r.denominator > r.numerator)
                continue;
            const double gap = found ? static_cast<double>(x - previous)
                                     : static_cast<double>(x * l.denominator - l.numerator) /
                                           static_cast<double>(l.denominator);
            best = std::max(best, gap);
            previous = x;
            found = true;
        }
        if (found) {
            best = std::max(best, static_cast<double>(r.numerator - previous * r.denominator) /
                                      static_cast<double>(r.denominator));
            answer = std::min(answer, best);
        }
    };
    std::cin >> count;
    std::int64_t current_y = 0;
    for (int i = 0; i < count; ++i) {
        std::int64_t x, y;
        std::cin >> x >> y;
        if (!group.empty() && y != current_y) {
            process(current_y);
            group.clear();
        }
        current_y = y;
        group.push_back(x);
    }
    if (!group.empty())
        process(current_y);
    std::cout << std::fixed << std::setprecision(DECIMAL_PLACES) << answer << '\n';
}
