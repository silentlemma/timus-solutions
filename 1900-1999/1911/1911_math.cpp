#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

using Wide = __int128;
constexpr int OUTPUT_PRECISION = 12;

struct Parameters {
    Wide speed, length, fire_speed, fire_width, gap, natural, shield, braking;
};

Wide positive_part(Wide value) { return std::max<Wide>(0, value); }

long double minimum_energy(const Parameters &p,
                           const std::vector<std::pair<Wide, Wide>> &branches) {
    const Wide difference = p.fire_speed - p.speed;
    long double best = std::numeric_limits<long double>::infinity();
    for (const auto &branch : branches) {
        const Wide left = branch.first, right = branch.second;
        const Wide entry = left + p.length, distance = right - entry;
        const Wide held = entry * difference - p.gap * p.speed;
        const Wide shield_numerator = positive_part(held) * p.shield;
        const Wide shield_denominator = p.speed * difference;
        const Wide delay_numerator = p.speed * (right - left + p.fire_width) + positive_part(-held);
        Wide brake_numerator, brake_denominator;
        if (delay_numerator >= 2 * distance * p.fire_speed) {
            brake_numerator = p.speed * p.speed;
            brake_denominator = 2 * distance;
        } else if (delay_numerator <= distance * p.fire_speed) {
            brake_numerator = 0;
            brake_denominator = 1;
        } else {
            brake_numerator =
                2 * p.speed * p.speed * p.fire_speed * (delay_numerator - distance * p.fire_speed);
            brake_denominator = delay_numerator * delay_numerator;
        }
        const Wide extra = positive_part(brake_numerator - p.natural * brake_denominator);
        const long double cost = static_cast<long double>(shield_numerator) / shield_denominator +
                                 static_cast<long double>(p.braking * extra) / brake_denominator;
        best = std::min(best, cost);
    }
    return best;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t speed, length, fire_speed, fire_width, gap, natural, shield, braking;
    std::cin >> speed >> length >> fire_speed >> fire_width >> gap >> natural >> shield >> braking;
    const Parameters parameters{speed, length,  fire_speed, fire_width,
                                gap,   natural, shield,     braking};
    int count;
    std::cin >> count;
    std::vector<std::pair<Wide, Wide>> branches;
    for (int index = 0; index < count; ++index) {
        int64_t left, right;
        std::cin >> left >> right;
        branches.emplace_back(left, right);
    }
    std::cout << std::fixed << std::setprecision(OUTPUT_PRECISION)
              << minimum_energy(parameters, branches) << '\n';
}
