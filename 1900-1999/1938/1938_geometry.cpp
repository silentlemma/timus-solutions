#include <array>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>

constexpr int LINE_COUNT = 3;
constexpr int OUTPUT_DIGITS = 15;
constexpr double ROTATION_COSINE = 0.5;
const double ROTATION_SINE = std::sqrt(3.0) / 2;

struct Point {
    double x, y;
};

struct Line {
    long long x, y, u, v;
};

double cross(Point first, Point second) { return first.x * second.y - first.y * second.x; }

long long integerArea(const Line &line, long long x, long long y) {
    return (line.u - line.x) * (y - line.y) - (line.v - line.y) * (x - line.x);
}

Point rotate(Point vector, int orientation) {
    const double sine = orientation * ROTATION_SINE;
    return {ROTATION_COSINE * vector.x - sine * vector.y,
            sine * vector.x + ROTATION_COSINE * vector.y};
}

std::array<Point, LINE_COUNT> equilateralPoints(const std::array<Line, LINE_COUNT> &lines) {
    const Line &first = lines[0];
    const Line &second = lines[1];
    const Line &third = lines[2];
    const bool useBeginning = std::abs(integerArea(second, first.x, first.y)) >=
                              std::abs(integerArea(second, first.u, first.v));
    const Point base{static_cast<double>(useBeginning ? first.x : first.u),
                     static_cast<double>(useBeginning ? first.y : first.v)};
    const Point anchorSecond{static_cast<double>(second.x), static_cast<double>(second.y)};
    const Point anchorThird{static_cast<double>(third.x), static_cast<double>(third.y)};
    const Point directionSecond{static_cast<double>(second.u - second.x),
                                static_cast<double>(second.v - second.y)};
    const Point directionThird{static_cast<double>(third.u - third.x),
                               static_cast<double>(third.v - third.y)};
    const Point positive = rotate(directionSecond, 1);
    const Point negative = rotate(directionSecond, -1);
    const bool usePositive =
        std::abs(cross(positive, directionThird)) >= std::abs(cross(negative, directionThird));
    const int orientation = usePositive ? 1 : -1;
    const Point direction = usePositive ? positive : negative;
    const Point offset = rotate({anchorSecond.x - base.x, anchorSecond.y - base.y}, orientation);
    const Point rotatedAnchor{base.x + offset.x, base.y + offset.y};
    const Point delta{anchorThird.x - rotatedAnchor.x, anchorThird.y - rotatedAnchor.y};
    const double determinant = cross(direction, directionThird);
    const double secondParameter = cross(delta, directionThird) / determinant;
    const double thirdParameter = cross(delta, direction) / determinant;
    const Point pointSecond{anchorSecond.x + secondParameter * directionSecond.x,
                            anchorSecond.y + secondParameter * directionSecond.y};
    const Point pointThird{anchorThird.x + thirdParameter * directionThird.x,
                           anchorThird.y + thirdParameter * directionThird.y};
    return {base, pointSecond, pointThird};
}

int main() {
    std::array<Line, LINE_COUNT> lines{};
    for (Line &line : lines) {
        std::cin >> line.x >> line.y >> line.u >> line.v;
    }
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS);
    for (Point point : equilateralPoints(lines)) {
        std::cout << point.x << ' ' << point.y << '\n';
    }
    return 0;
}
