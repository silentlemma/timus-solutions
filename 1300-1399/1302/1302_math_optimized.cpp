#include <array>
#include <cmath>
#include <cstdio>
#include <cstdlib>

constexpr int AXES = 3;

int number() {
    int ch = std::getchar();
    while (ch != EOF && ch <= ' ') {
        ch = std::getchar();
    }
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = 10 * value + ch - '0';
        ch = std::getchar();
    }
    return value;
}

std::array<int, AXES> strips(int cell) {
    // All possible integer squares fit exactly in double precision.
    int row = static_cast<int>(std::sqrt(static_cast<double>(cell)));
    row += row * row < cell;
    const int position = cell - (row - 1) * (row - 1);
    return {row, (position + 1) / 2, row - position / 2};
}

int main() {
    const auto a = strips(number());
    const auto b = strips(number());
    int total = 0;
    for (int i = 0; i < AXES; ++i) {
        total += std::abs(a[i] - b[i]);
    }
    std::printf("%d\n", total);
}
