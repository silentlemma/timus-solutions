#include <iostream>
#include <string>
#include <vector>

constexpr int TRIANGLE = 3, CORNERS = 4, CLOSED = 5;
struct Point {
    long long x, y;
};
long long cross(Point a, Point b, Point p) {
    return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x);
}
bool same_sum(Point a, Point b, Point c, Point d) {
    return a.x + b.x == c.x + d.x && a.y + b.y == c.y + d.y;
}
bool parallelogram(const std::vector<Point> &p) {
    return same_sum(p[0], p[1], p[2], p[TRIANGLE]) || same_sum(p[0], p[2], p[1], p[TRIANGLE]) ||
           same_sum(p[0], p[TRIANGLE], p[1], p[2]);
}
std::string solve(const std::vector<Point> &points) {
    int n = static_cast<int>(points.size());
    if (n <= TRIANGLE)
        return std::to_string(n);
    for (int i = 0; i < TRIANGLE; ++i)
        for (int j = i + 1; j < TRIANGLE; ++j) {
            int outside = 0;
            for (Point p : points)
                if (cross(points[i], points[j], p) != 0 && ++outside > 1)
                    break;
            if (outside <= 1)
                return std::to_string(n);
        }
    if (n == CORNERS)
        return parallelogram(points) ? std::to_string(CLOSED) : "oo";
    if (n == CLOSED)
        for (int center = 0; center < n; ++center) {
            std::vector<Point> others;
            long long sx = 0, sy = 0;
            for (int i = 0; i < n; ++i)
                if (i != center) {
                    others.push_back(points[i]);
                    sx += points[i].x;
                    sy += points[i].y;
                }
            if (parallelogram(others) && sx == CORNERS * points[center].x &&
                sy == CORNERS * points[center].y)
                return std::to_string(CLOSED);
        }
    return "oo";
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<Point> points(n);
    for (Point &p : points)
        std::cin >> p.x >> p.y;
    std::cout << solve(points) << '\n';
}
