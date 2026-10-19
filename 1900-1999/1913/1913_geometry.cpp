#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <optional>
#include <utility>

using Integer = long long;
using Wide = __int128_t;
using Point = std::pair<Integer, Integer>;
using Position = std::pair<double, double>;
constexpr int TERMINALS = 3;
constexpr int DECIMALS = 12;
constexpr Integer DISCRIMINANT_SCALE = 4;
using Points = std::array<Point, TERMINALS>;
using Answer = std::array<Position, 2>;

Integer squaredDistance(Point first, Point second) {
    const Integer dx = first.first - second.first;
    const Integer dy = first.second - second.second;
    return dx * dx + dy * dy;
}

bool radicalAtMost(Integer target, Integer coefficient, Integer radicand) {
    if (coefficient == 0 || radicand == 0) {
        return target >= 0;
    }
    const Wide left = Wide(target) * target;
    const Wide right = Wide(coefficient) * coefficient * radicand;
    if (coefficient > 0) {
        return target >= 0 && left >= right;
    }
    return target >= 0 || left <= right;
}

std::optional<Position> commonPoint(const Points &points,
                                    const std::array<Integer, TERMINALS> &radii) {
    for (Point point : points) {
        bool inside = true;
        for (int index = 0; index < TERMINALS; ++index) {
            inside = inside && squaredDistance(point, points[index]) <= radii[index] * radii[index];
        }
        if (inside) {
            return Position{double(point.first), double(point.second)};
        }
    }
    for (int first = 0; first < TERMINALS; ++first) {
        for (int second = first + 1; second < TERMINALS; ++second) {
            const int third = TERMINALS - first - second;
            const Point origin = points[first];
            const Integer dx = points[second].first - origin.first;
            const Integer dy = points[second].second - origin.second;
            const Integer distance = dx * dx + dy * dy;
            const Integer radiusSquared = radii[first] * radii[first];
            const Integer along = distance + radiusSquared - radii[second] * radii[second];
            const Integer discriminant =
                DISCRIMINANT_SCALE * radiusSquared * distance - along * along;
            if (discriminant < 0) {
                continue;
            }
            const Integer wx = origin.first - points[third].first;
            const Integer wy = origin.second - points[third].second;
            const Integer target =
                distance * (radii[third] * radii[third] - radiusSquared - wx * wx - wy * wy) -
                along * (wx * dx + wy * dy);
            const Integer cross = wy * dx - wx * dy;
            for (int sign : {-1, 1}) {
                if (radicalAtMost(target, sign * cross, discriminant)) {
                    const double height = sign * std::sqrt(double(discriminant));
                    return Position{
                        origin.first + (double(along) * dx - height * dy) / (2 * distance),
                        origin.second + (double(along) * dy + height * dx) / (2 * distance)};
                }
            }
        }
    }
    return std::nullopt;
}

std::optional<Answer> solve(Integer radius, const Points &points) {
    if (squaredDistance(points[0], points[1]) <= (2 * radius) * (2 * radius) &&
        squaredDistance(points[0], points[2]) <= (2 * radius) * (2 * radius)) {
        Answer result{};
        for (int index = 0; index < 2; ++index) {
            result[index] = {(points[0].first + points[index + 1].first) / 2.0,
                             (points[0].second + points[index + 1].second) / 2.0};
        }
        return result;
    }
    for (int doubled = 0; doubled < TERMINALS; ++doubled) {
        std::array<Integer, TERMINALS> radii{radius, radius, radius};
        radii[doubled] *= 2;
        const auto hub = commonPoint(points, radii);
        if (hub) {
            const Position midpoint{(hub->first + points[doubled].first) / 2,
                                    (hub->second + points[doubled].second) / 2};
            return Answer{*hub, midpoint};
        }
    }
    return std::nullopt;
}

int main() {
    Integer radius;
    std::cin >> radius;
    Points points{};
    for (Point &point : points) {
        std::cin >> point.first >> point.second;
    }
    const auto answer = solve(radius, points);
    if (!answer) {
        std::cout << "Death\n";
    } else {
        std::cout << "Now we have enough power\n" << std::fixed << std::setprecision(DECIMALS);
        for (Position point : *answer) {
            std::cout << point.first << ' ' << point.second << '\n';
        }
    }
    return 0;
}
