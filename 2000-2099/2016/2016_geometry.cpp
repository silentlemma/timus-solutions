#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <utility>

using Real = long double;
constexpr int DIMENSIONS = 3;
constexpr int CIRCLES = 3;
constexpr int PERIOD_SHIFTS = 2;
constexpr int OUTPUT_DIGITS = 12;
using Vec = std::array<Real, DIMENSIONS>;
const Real TAU = 2 * std::acos(-1.L);

Vec add(Vec a, Vec b) {
    for (int i = 0; i < DIMENSIONS; ++i)
        a[i] += b[i];
    return a;
}
Vec sub(Vec a, Vec b) {
    for (int i = 0; i < DIMENSIONS; ++i)
        a[i] -= b[i];
    return a;
}
Vec scale(Vec a, Real value) {
    for (Real &x : a)
        x *= value;
    return a;
}
Real sum_three(Real a, Real b, Real c) {
    Real sum = 0, correction = 0;
    for (Real value : Vec{a, b, c}) {
        Real next = sum + value;
        correction +=
            std::abs(sum) >= std::abs(value) ? (sum - next) + value : (value - next) + sum;
        sum = next;
    }
    return sum + correction;
}
Real dot(Vec a, Vec b) { return sum_three(a[0] * b[0], a[1] * b[1], a[2] * b[2]); }
Vec cross(Vec a, Vec b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}
std::pair<Vec, Real> unit(Vec a) {
    Real length = std::sqrt(dot(a, a));
    return {scale(a, 1 / length), length};
}
Real above(Vec center, Real radius, Vec radial, Vec tangent, Real angle, Real height) {
    Real amplitude = radius * std::hypot(radial[2], tangent[2]);
    if (amplitude == 0)
        return center[2] >= height ? radius * angle : 0;
    Real ratio = (height - center[2]) / amplitude;
    if (ratio <= -1)
        return radius * angle;
    if (ratio >= 1)
        return 0;
    Real half = std::acos(ratio), phase = std::atan2(tangent[2], radial[2]), measure = 0;
    for (int shift = -PERIOD_SHIFTS; shift <= PERIOD_SHIFTS; ++shift) {
        Real left = phase - half + shift * TAU, right = phase + half + shift * TAU;
        measure += std::max(0.L, std::min(angle, right) - std::max(0.L, left));
    }
    return radius * measure;
}
Real solve(int speed, int acceleration, const std::array<Vec, CIRCLES> &centers) {
    Vec start = scale(centers[0], -1);
    Real squared = dot(start, start);
    auto [radial, radius] = unit(start);
    Vec raw{-centers[0][1], centers[0][0], 0};
    Vec tangent = unit(cross(raw, radial)).first;
    Real height = static_cast<Real>(speed) * speed / (2 * acceleration), answer = 0;
    for (int i = 0; i < CIRCLES; ++i) {
        Real angle = TAU;
        Vec relative{}, normal{}, toward{};
        Real rho = 0, distance = 0;
        if (i + 1 < CIRCLES) {
            relative = sub(centers[i + 1], centers[i]);
            auto [n, normal_length] = unit(raw);
            normal = n;
            auto [direction, cross_length] = unit(cross(raw, relative));
            toward = unit(cross(direction, normal)).first;
            rho = cross_length / normal_length;
            distance = dot(relative, raw) / normal_length;
            angle = std::atan2(dot(toward, tangent), dot(toward, radial));
            if (angle <= 0)
                angle += TAU;
        }
        answer += above(centers[i], radius, radial, tangent, angle, height);
        if (i + 1 < CIRCLES) {
            Real difference = sum_three(squared, -dot(relative, relative), distance * distance);
            Real delta = difference / (radius + rho);
            radius = std::hypot(delta, distance);
            radial = scale(sub(scale(toward, delta), scale(normal, distance)), 1 / radius);
            squared = sum_three(delta * delta, distance * distance, 0);
            if (distance == 0) {
                if (delta < 0)
                    raw = scale(raw, -1);
            } else
                raw = add(scale(normal, delta), scale(toward, distance));
            tangent = unit(cross(raw, radial)).first;
        }
    }
    return answer;
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS);
    while (count--) {
        int speed, acceleration;
        std::cin >> speed >> acceleration;
        std::array<Vec, CIRCLES> centers;
        for (auto &c : centers)
            for (Real &x : c)
                std::cin >> x;
        std::cout << solve(speed, acceleration, centers) << '\n';
    }
}
