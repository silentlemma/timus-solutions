#include <cmath>
#include <cstdio>

constexpr int SCALE = 1000;
constexpr int HALF_TURN = 180 * SCALE;

int main() {
    double radius, angle;
    if (std::scanf("%lf%lf", &radius, &angle) != 2)
        return 0;

    // The input has at most three fractional digits, so rounding recovers it exactly.
    const int width = static_cast<int>(std::lround(angle * SCALE));
    const int full_chords = HALF_TURN / width - 1;
    const int remainder = HALF_TURN % width;
    const double radians_per_unit = std::acos(-1.0) / HALF_TURN;
    const double shore =
        full_chords * std::sin(width * radians_per_unit) + std::sin(remainder * radians_per_unit);
    std::printf("%.9f\n", radius + 2 * radius * shore);
}
