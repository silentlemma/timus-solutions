#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>

constexpr int DIMENSION = 3;
constexpr int POINTS = 4;
constexpr double AXIS_THRESHOLD = 1900;
constexpr double AXIS_STEP = 2;
constexpr int ANGLE = 180;
constexpr int OUTPUT_DIGITS = 15;
using Vec = std::array<double, DIMENSION>;
using Answer = std::array<Vec, 2>;

double dot(const Vec &a, const Vec &b) {
    double result = 0;
    for (int i = 0; i < DIMENSION; ++i)
        result += a[i] * b[i];
    return result;
}

Vec normalize(Vec a) {
    double length = std::sqrt(dot(a, a));
    for (double &value : a)
        value /= length;
    return a;
}

Answer axis(const Vec &middle, const Vec &displacement, const Vec &direction,
            const Vec &difference) {
    double coefficient = dot(displacement, direction) / (2 * dot(direction, direction));
    Vec center{}, unit = normalize(direction);
    for (int i = 0; i < DIMENSION; ++i)
        center[i] = middle[i] + coefficient * difference[i];
    double projection = dot(center, unit);
    Answer result{};
    for (int i = 0; i < DIMENSION; ++i) {
        result[0][i] = center[i] - projection * unit[i];
        result[1][i] = result[0][i] + AXIS_STEP * unit[i];
    }
    return result;
}

Answer solve(const std::array<Vec, POINTS> &points) {
    const auto &a = points[0];
    const auto &b = points[1];
    const auto &c = points[2];
    const auto &d = points[POINTS - 1];
    Vec first{}, second{}, middle{}, displacement{}, plus{}, minus{};
    for (int i = 0; i < DIMENSION; ++i) {
        first[i] = b[i] - a[i];
        second[i] = d[i] - c[i];
        middle[i] = (a[i] + c[i]) / 2;
        displacement[i] = c[i] - a[i];
    }
    if (dot(first, second) < 0)
        for (double &value : second)
            value = -value;
    Vec u = normalize(first), v = normalize(second);
    for (int i = 0; i < DIMENSION; ++i) {
        plus[i] = u[i] + v[i];
        minus[i] = u[i] - v[i];
    }
    Answer result = axis(middle, displacement, plus, minus);
    if (dot(result[0], result[0]) > AXIS_THRESHOLD * AXIS_THRESHOLD)
        result = axis(middle, displacement, minus, plus);
    return result;
}

int main() {
    std::array<Vec, POINTS> points{};
    for (auto &row : points)
        for (double &value : row)
            std::cin >> value;
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS);
    for (const auto &row : solve(points)) {
        for (double value : row)
            std::cout << value << ' ';
        std::cout << '\n';
    }
    std::cout << ANGLE << '\n';
}
