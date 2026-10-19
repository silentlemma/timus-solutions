#include <cstdint>
#include <iomanip>
#include <iostream>
#include <string>

constexpr std::int64_t DECIMAL_SCALE = 1000;
constexpr int DECIMAL_PLACES = 3;
constexpr std::int64_t SIDE = 10 * DECIMAL_SCALE;
constexpr int CUTS = 30;
constexpr std::int64_t GRID_SCALE = std::int64_t{1} << CUTS;
constexpr double INITIAL_AREA = 50.0;
constexpr int OUTPUT_DIGITS = 10;

struct Point {
    std::int64_t x, y;
};

std::int64_t parseCoordinate(std::string text) {
    if (text[0] == '+')
        text.erase(0, 1);
    const auto dot = text.find('.');
    const std::string whole = dot == std::string::npos ? text : text.substr(0, dot);
    std::string fractional = dot == std::string::npos ? "" : text.substr(dot + 1);
    fractional.resize(DECIMAL_PLACES, '0');
    return std::stoll(whole.empty() ? "0" : whole) * DECIMAL_SCALE + std::stoll(fractional);
}

std::int64_t sign(std::int64_t value) { return (value > 0) - (value < 0); }

bool opposite(std::int64_t first, std::int64_t second) {
    return (first < 0 && second > 0) || (second < 0 && first > 0);
}

double areaForSale(std::int64_t x, std::int64_t y) {
    const Point target{x * GRID_SCALE, y * GRID_SCALE};
    Point right{SIDE * GRID_SCALE, 0}, first{0, 0}, second{SIDE * GRID_SCALE, SIDE * GRID_SCALE};
    double area = INITIAL_AREA, answer = 0.0;
    for (int cut = 0; cut < CUTS; ++cut) {
        const Point middle{(first.x + second.x) / 2, (first.y + second.y) / 2};
        const auto normalX = sign(middle.y - right.y), normalY = -sign(middle.x - right.x);
        const auto originSide = -normalX * right.x - normalY * right.y;
        const auto targetSide = normalX * (target.x - right.x) + normalY * (target.y - right.y);
        const auto rayRight = x * right.y - y * right.x;
        const auto rayMiddle = x * middle.y - y * middle.x;
        const double half = area / 2;
        if (opposite(rayRight, rayMiddle) && (opposite(originSide, targetSide) || targetSide == 0))
            answer += half;
        if (targetSide == 0)
            break;
        const auto firstSide = normalX * (first.x - right.x) + normalY * (first.y - right.y);
        if ((targetSide > 0) == (firstSide > 0))
            second = right;
        else
            first = right;
        right = middle;
        area = half;
    }
    return answer;
}

int main() {
    std::string x, y;
    std::cin >> x >> y;
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS)
              << areaForSale(parseCoordinate(x), parseCoordinate(y)) << '\n';
    return 0;
}
