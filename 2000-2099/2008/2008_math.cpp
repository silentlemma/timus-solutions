#include <array>
#include <iostream>

constexpr long long GRAVITY_NUMERATOR = 49;
constexpr long long GRAVITY_DENOMINATOR = 5;
constexpr int POINT_COUNT = 3;

struct Point {
    long long x, y;
};

bool canReach(long long speed, long long dx, long long dy) {
    long long threshold = GRAVITY_DENOMINATOR * speed * speed - GRAVITY_NUMERATOR * dy;
    return threshold >= 0 &&
           threshold * threshold >= GRAVITY_NUMERATOR * GRAVITY_NUMERATOR * (dx * dx + dy * dy);
}

bool solve(long long speed, Point head, Point left, Point right) {
    auto jump = [speed](Point start, Point target) {
        return canReach(speed, target.x - start.x, target.y - start.y);
    };
    return jump(left, right) && jump(right, left) && (jump(left, head) || jump(right, head));
}

int main() {
    long long speed;
    std::cin >> speed;
    std::array<Point, POINT_COUNT> points{};
    for (auto &point : points)
        std::cin >> point.x >> point.y;
    std::cout << (solve(speed, points[0], points[1], points[2]) ? "Yes" : "No") << '\n';
}
