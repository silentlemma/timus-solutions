#include <cmath>
#include <iomanip>
#include <iostream>

constexpr int output_digits = 10;

double radius(int count) {
    if (count == 1)
        return 1;
    const double pi = std::acos(-1.0);
    return 1 + 1 / std::sin(pi / count);
}

int main() {
    int count;
    std::cin >> count;
    std::cout << std::fixed << std::setprecision(output_digits) << radius(count) << '\n';
}
