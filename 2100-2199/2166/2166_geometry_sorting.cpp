#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

constexpr std::int64_t DECIMAL_SCALE = 1000000;
constexpr std::size_t PRECISION = 6;

struct Line {
    std::int64_t dx;
    std::int64_t dy;
    std::int64_t c;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::size_t count;
    std::cin >> count;
    std::vector<Line> lines(count);
    for (Line &line : lines) {
        std::int64_t x1, y1, x2, y2;
        std::cin >> x1 >> y1 >> x2 >> y2;
        line.dx = x2 - x1;
        line.dy = y2 - y1;
        if (line.dx < 0 || (line.dx == 0 && line.dy < 0)) {
            line.dx = -line.dx;
            line.dy = -line.dy;
        }
        line.c = line.dy * x1 - line.dx * y1;
    }

    std::sort(lines.begin(), lines.end(),
              [](const Line &a, const Line &b) { return a.dy * b.dx < b.dy * a.dx; });

    std::int64_t best_num = 0;
    std::int64_t best_den = 1;
    // A farthest intersection belongs to neighboring directions in cyclic order.
    for (std::size_t i = 0; i < count; ++i) {
        const Line &a = lines[i];
        const Line &b = lines[(i + 1) % count];
        const std::int64_t num =
            std::abs(a.dx * b.c - a.c * b.dx) + std::abs(a.dy * b.c - a.c * b.dy);
        const std::int64_t den = std::abs(a.dx * b.dy - a.dy * b.dx);
        if (num * best_den > best_num * den) {
            best_num = num;
            best_den = den;
        }
    }

    const std::int64_t rounded = (best_num * DECIMAL_SCALE + best_den / 2) / best_den;
    std::cout << rounded / DECIMAL_SCALE;
    const std::int64_t remainder = rounded % DECIMAL_SCALE;
    if (remainder != 0) {
        std::string fractional = std::to_string(remainder);
        fractional.insert(0, PRECISION - fractional.size(), '0');
        while (fractional.back() == '0') {
            fractional.pop_back();
        }
        std::cout << '.' << fractional;
    }
    std::cout << '\n';
}
