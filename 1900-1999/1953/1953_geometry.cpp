#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>

constexpr double FOCAL_SCALE = 3;
constexpr double AXIS_SCALE = 6;

int main() {
    int64_t a, b, c;
    std::cin >> a >> b >> c;
    int64_t x = a * a, y = b * b, z = c * c;
    int64_t discriminant = 2 * ((x - y) * (x - y) + (y - z) * (y - z) + (z - x) * (z - x));
    double gap = std::sqrt(static_cast<double>(discriminant));
    double focal_distance = std::sqrt(2 * gap) / FOCAL_SCALE;
    double radius = std::sqrt(x + y + z + gap) / AXIS_SCALE;
    constexpr int OUTPUT_PRECISION = 12;
    std::cout << std::fixed << std::setprecision(OUTPUT_PRECISION) << focal_distance << ' '
              << radius << '\n';
}
