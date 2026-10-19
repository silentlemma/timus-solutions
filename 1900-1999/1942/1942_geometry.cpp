#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

constexpr int SCALE = 1000;
constexpr int FRACTION_DIGITS = 3;
constexpr int OUTPUT_DIGITS = 9;

int scaled(const std::string &token) {
    int sign = 1, fraction = 0, digits = 0;
    bool afterPoint = false;
    for (char symbol : token) {
        if (symbol == '-')
            sign = -1;
        else if (symbol == '+')
            continue;
        else if (symbol == '.')
            afterPoint = true;
        else if (afterPoint) {
            fraction = fraction * 10 + symbol - '0';
            ++digits;
        }
    }
    while (digits++ < FRACTION_DIGITS)
        fraction *= 10;
    return sign * fraction;
}

struct Answer {
    int count;
    int norm;
};

Answer bestGroup(const std::vector<std::pair<int, int>> &points) {
    std::vector<int> counts(SCALE * SCALE);
    Answer best{0, 0};
    for (const auto &point : points) {
        const int rx = (point.first % SCALE + SCALE) % SCALE;
        const int ry = (point.second % SCALE + SCALE) % SCALE;
        const int count = ++counts[rx * SCALE + ry];
        const int dx = std::min(rx, SCALE - rx), dy = std::min(ry, SCALE - ry);
        const int norm = dx * dx + dy * dy;
        if (count > best.count || (count == best.count && norm < best.norm))
            best = {count, norm};
    }
    return best;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::cin >> size;
    std::vector<std::pair<int, int>> points;
    for (int index = 0; index < size; ++index) {
        std::string x, y;
        std::cin >> x >> y;
        points.emplace_back(scaled(x), scaled(y));
    }
    const auto best = bestGroup(points);
    std::cout << best.count << ' ' << std::fixed << std::setprecision(OUTPUT_DIGITS)
              << std::sqrt(best.norm) / SCALE << '\n';
    return 0;
}
