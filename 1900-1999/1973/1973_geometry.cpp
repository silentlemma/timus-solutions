#include <cstdint>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

constexpr int kDiagonalWeight = 2;
constexpr int kPairWeight = 3;
constexpr int kNormalizer = 27;
constexpr int kOutputPrecision = 12;
using Point = std::pair<std::int64_t, std::int64_t>;

long double expectation(const std::vector<Point> &vertices) {
    auto [originX, originY] = vertices[0];
    auto [previousX, previousY] = vertices[1];
    previousX -= originX;
    previousY -= originY;
    __int128 weightedX = 0, weightedY = 0;
    std::int64_t doubledArea = 0;
    long double numerator = 0;
    for (std::size_t i = 2; i < vertices.size(); ++i) {
        auto [x, y] = vertices[i];
        x -= originX;
        y -= originY;
        std::int64_t area = previousX * y - previousY * x;
        std::int64_t sumX = previousX + x, sumY = previousY + y;
        __int128 between = weightedX * sumY - weightedY * sumX;
        long double d = static_cast<long double>(area);
        numerator +=
            kDiagonalWeight * d * d * d + kPairWeight * d * static_cast<long double>(between);
        weightedX += static_cast<__int128>(area) * sumX;
        weightedY += static_cast<__int128>(area) * sumY;
        doubledArea += area;
        previousX = x;
        previousY = y;
    }
    long double total = static_cast<long double>(doubledArea);
    return numerator / (kNormalizer * total * total);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<Point> vertices(count);
    for (auto &[x, y] : vertices)
        std::cin >> x >> y;
    std::cout << std::fixed << std::setprecision(kOutputPrecision) << expectation(vertices) << '\n';
}
