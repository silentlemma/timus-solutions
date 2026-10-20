#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using Integer = std::int64_t;
constexpr Integer SCALE = 1000;

struct Point {
    Integer x, y;
};

Integer coordinate(const std::string &token) {
    Integer value = 0;
    for (char digit : token) {
        if (digit != '.') {
            value = value * 10 + digit - '0';
        }
    }
    return value;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<Point> points(n);
    Integer minimum = 0, maximum = 0;
    for (int i = 0; i < n; ++i) {
        std::string x, y;
        std::cin >> x >> y;
        points[i] = {coordinate(x), coordinate(y)};
        if (i == 0 || points[i].x < minimum) {
            minimum = points[i].x;
        }
        maximum = std::max(maximum, points[i].x);
    }
    int left = (minimum + SCALE - 1) / SCALE;
    int right = maximum / SCALE;
    if (left > right) {
        std::cout << 0 << '\n';
        return 0;
    }
    std::vector<int> lower(right + 1), upper(right + 1);
    for (int i = 0; i < n; ++i) {
        Point a = points[i], b = points[(i + 1) % n];
        if (a.x == b.x) {
            continue;
        }
        bool bottom = a.x < b.x;
        if (!bottom) {
            std::swap(a, b);
        }
        int begin = (a.x + SCALE - 1) / SCALE;
        int end = b.x / SCALE;
        Integer dx = b.x - a.x, dy = b.y - a.y;
        Integer denominator = dx * SCALE;
        Integer numerator = a.y * dx + (begin * SCALE - a.x) * dy - bottom;
        auto &target = bottom ? lower : upper;
        for (int column = begin; column <= end; ++column) {
            target[column] = numerator / denominator;
            numerator += dy * SCALE;
        }
    }
    int limit = std::min(right, *std::max_element(upper.begin(), upper.end()));
    std::vector<int> mu(limit + 1, 1);
    std::vector<bool> composite(limit + 1);
    for (int prime = 2; prime <= limit; ++prime) {
        if (composite[prime]) {
            continue;
        }
        for (int multiple = prime; multiple <= limit; multiple += prime) {
            composite[multiple] = true;
            mu[multiple] = -mu[multiple];
        }
        Integer square = Integer(prime) * prime;
        for (Integer multiple = square; multiple <= limit; multiple += square) {
            mu[multiple] = 0;
        }
    }
    // Mobius inversion counts only pairs with greatest common divisor one.
    Integer answer = 0;
    for (int divisor = 1; divisor <= limit; ++divisor) {
        if (mu[divisor] == 0) {
            continue;
        }
        Integer subtotal = 0;
        int begin = ((left + divisor - 1) / divisor) * divisor;
        for (int column = begin; column <= right; column += divisor) {
            subtotal += upper[column] / divisor - lower[column] / divisor;
        }
        answer += mu[divisor] * subtotal;
    }
    std::cout << answer << '\n';
}
