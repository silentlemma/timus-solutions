#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int TRIANGLE_SIDES = 3;

struct Point {
    std::int64_t x;
    std::int64_t y;

    bool operator<(const Point &other) const {
        return x < other.x || (x == other.x && y < other.y);
    }
};

std::int64_t cross(const Point &a, const Point &b, const Point &c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

template <class Iterator> std::size_t chain_length(Iterator first, Iterator last) {
    std::vector<Point> chain;
    for (; first != last; ++first) {
        while (chain.size() >= 2 && cross(chain[chain.size() - 2], chain.back(), *first) < 0) {
            chain.pop_back();
        }
        chain.push_back(*first);
    }
    return chain.size();
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<Point> points(n);
    for (Point &point : points) {
        std::cin >> point.x >> point.y;
    }
    std::sort(points.begin(), points.end());

    // Keeping collinear points also gives the correct count for a single line.
    const auto boundary = chain_length(points.begin(), points.end()) +
                          chain_length(points.rbegin(), points.rend()) - 2;
    std::cout << TRIANGLE_SIDES * n - TRIANGLE_SIDES - boundary << '\n';
}
