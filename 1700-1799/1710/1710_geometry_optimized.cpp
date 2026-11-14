#include <cstdio>

constexpr int COORDINATE_COUNT = 6;

int main() {
    int ax, ay, bx, by, cx, cy;
    if (std::scanf("%d%d%d%d%d%d", &ax, &ay, &bx, &by, &cx, &cy) != COORDINATE_COUNT) {
        return 0;
    }
    const int dx = cx - ax, dy = cy - ay;
    const int squared = dx * dx + dy * dy;
    // Reflect C across the projection of B onto the line AC.
    const int other = 2 * ((bx - ax) * dx + (by - ay) * dy) - squared;
    if (other <= 0 || other == squared) {
        std::puts("YES");
        return 0;
    }
    const double x = ax + static_cast<double>(dx * other) / squared;
    const double y = ay + static_cast<double>(dy * other) / squared;
    std::printf("NO\n%d %d\n%d %d\n%.12f %.12f\n", ax, ay, bx, by, x, y);
}
