#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

constexpr int dimensions = 3;
constexpr long long radius = 100;
constexpr int output_digits = 10;
using IntVector = std::array<long long, dimensions>;
using Vector = std::array<double, dimensions>;

template <class T> T dot(const std::array<T, dimensions> &a, const std::array<T, dimensions> &b) {
    T result = 0;
    for (int i = 0; i < dimensions; ++i)
        result += a[i] * b[i];
    return result;
}

template <class T>
std::array<T, dimensions> cross(const std::array<T, dimensions> &a,
                                const std::array<T, dimensions> &b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}

double area(const std::array<IntVector, dimensions> &points) {
    IntVector first{}, second{};
    for (int i = 0; i < dimensions; ++i) {
        first[i] = points[1][i] - points[0][i];
        second[i] = points[2][i] - points[0][i];
    }
    const auto normal = cross(first, second);
    const auto norm_squared = dot(normal, normal);
    const auto offset = dot(normal, points[0]);
    const auto residual = radius * radius * norm_squared - offset * offset;
    if (residual <= 0)
        return 0;
    const double radius_squared = static_cast<double>(residual) / norm_squared;
    Vector axis{}, unit_normal{};
    for (int i = 0; i < dimensions; ++i) {
        axis[i] = first[i] / std::sqrt(static_cast<double>(dot(first, first)));
        unit_normal[i] = normal[i] / std::sqrt(static_cast<double>(norm_squared));
    }
    const auto other = cross(unit_normal, axis);
    std::array<std::array<double, 2>, dimensions> projected{};
    for (int i = 0; i < dimensions; ++i)
        for (int j = 0; j < dimensions; ++j) {
            projected[i][0] += points[i][j] * axis[j];
            projected[i][1] += points[i][j] * other[j];
        }
    double total = 0;
    for (int i = 0; i < dimensions; ++i) {
        const int following = (i + 1) % dimensions;
        IntVector delta{};
        for (int j = 0; j < dimensions; ++j)
            delta[j] = points[following][j] - points[i][j];
        const auto quadratic = dot(delta, delta);
        const auto linear = dot(points[i], delta);
        const auto constant = dot(points[i], points[i]) - radius * radius;
        const auto discriminant = linear * linear - quadratic * constant;
        std::vector<double> cuts{0, 1};
        double low = 1, high = 0;
        if (discriminant > 0) {
            const double stable = -linear - std::copysign(std::sqrt(discriminant), linear);
            low = stable / quadratic;
            high = constant / stable;
            if (low > high)
                std::swap(low, high);
            if (0 < low && low < 1)
                cuts.push_back(low);
            if (0 < high && high < 1)
                cuts.push_back(high);
        }
        std::sort(cuts.begin(), cuts.end());
        const auto x = projected[i][0], y = projected[i][1];
        const auto dx = projected[following][0] - x, dy = projected[following][1] - y;
        for (std::size_t j = 1; j < cuts.size(); ++j) {
            const auto left = cuts[j - 1], right = cuts[j];
            const auto ax = x + left * dx, ay = y + left * dy;
            const auto bx = x + right * dx, by = y + right * dy;
            const auto signed_area = ax * by - ay * bx;
            const auto middle = (left + right) / 2;
            total += low < middle && middle < high
                         ? signed_area
                         : radius_squared * std::atan2(signed_area, ax * bx + ay * by);
        }
    }
    return std::abs(total) / 2;
}

int main() {
    std::array<IntVector, dimensions> points{};
    for (auto &point : points)
        for (auto &value : point)
            std::cin >> value;
    std::cout << std::fixed << std::setprecision(output_digits) << area(points) << '\n';
}
