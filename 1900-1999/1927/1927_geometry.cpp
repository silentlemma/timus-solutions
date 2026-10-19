#include <algorithm>
#include <array>
#include <cstdint>
#include <iomanip>
#include <iostream>

constexpr int SEGMENT_COORDINATES = 4;
using Segment = std::array<std::int64_t, SEGMENT_COORDINATES>;

double intersectionArea(const Segment &first, const Segment &second) {
    const auto vx = first[2] - first[0];
    const auto vy = first[SEGMENT_COORDINATES - 1] - first[1];
    const auto wx = second[2] - second[0];
    const auto wy = second[SEGMENT_COORDINATES - 1] - second[1];
    const auto determinant = vx * wy - vy * wx;
    if (determinant != 0) {
        const auto numerator = (vx * vx + vy * vy) * (wx * wx + wy * wy);
        const auto magnitude = determinant < 0 ? -determinant : determinant;
        return static_cast<double>(numerator) / static_cast<double>(magnitude);
    }
    const auto a = vx * first[0] + vy * first[1];
    const auto b = vx * first[2] + vy * first[SEGMENT_COORDINATES - 1];
    const auto c = vx * second[0] + vy * second[1];
    const auto d = vx * second[2] + vy * second[SEGMENT_COORDINATES - 1];
    return std::max(std::min(a, b), std::min(c, d)) < std::min(std::max(a, b), std::max(c, d)) ? -1
                                                                                               : 0;
}

int main() {
    Segment first{}, second{};
    for (auto &coordinate : first) {
        std::cin >> coordinate;
    }
    for (auto &coordinate : second) {
        std::cin >> coordinate;
    }
    std::cout << std::fixed << std::setprecision(10) << intersectionArea(first, second) << '\n';
    return 0;
}
