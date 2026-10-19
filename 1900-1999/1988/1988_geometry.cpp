#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>

constexpr int dimensions = 3;
constexpr int iterations = 80;
constexpr int output_digits = 10;
using Vector = std::array<long long, dimensions>;

long long dot(const Vector &a, const Vector &b) {
    long long total = 0;
    for (int i = 0; i < dimensions; ++i)
        total += a[i] * b[i];
    return total;
}

double meeting_time(const Vector &carrier, const Vector &ship, double speed) {
    const auto radius_squared = dot(carrier, carrier);
    const auto distance_squared = dot(ship, ship);
    const double radius = std::sqrt(radius_squared), distance = std::sqrt(distance_squared);
    const auto delta = distance_squared - radius_squared;
    const double tangent = std::sqrt(delta), radial_gap = delta / (distance + radius);
    const Vector cross{carrier[1] * ship[2] - carrier[2] * ship[1],
                       carrier[2] * ship[0] - carrier[0] * ship[2],
                       carrier[0] * ship[1] - carrier[1] * ship[0]};
    const double angle = std::atan2(std::sqrt(dot(cross, cross)), dot(carrier, ship));
    const double visible_angle = std::atan2(tangent, radius);
    auto ship_length = [&](double beta) {
        if (beta <= visible_angle) {
            const double sideways = 2 * std::sqrt(distance * radius) * std::sin(beta / 2);
            return std::hypot(radial_gap, sideways);
        }
        return tangent + radius * (beta - visible_angle);
    };
    const double radial_time = radial_gap / speed;
    if (radius * angle <= radial_time)
        return radial_time;
    double low = 0, high = angle;
    for (int step = 0; step < iterations; ++step) {
        const double beta = (low + high) / 2;
        if (radius * (angle - beta) > ship_length(beta) / speed)
            low = beta;
        else
            high = beta;
    }
    const double beta = (low + high) / 2;
    return std::max(radius * (angle - beta), ship_length(beta) / speed);
}

int main() {
    Vector carrier{}, ship{};
    for (auto &value : carrier)
        std::cin >> value;
    for (auto &value : ship)
        std::cin >> value;
    double speed;
    std::cin >> speed;
    std::cout << std::fixed << std::setprecision(output_digits)
              << meeting_time(carrier, ship, speed) << '\n';
}
