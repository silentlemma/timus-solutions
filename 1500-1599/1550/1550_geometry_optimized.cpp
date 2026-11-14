#include <cmath>
#include <cstdio>

constexpr long double PI = 3.141592653589793238462643383279502884L;

constexpr int INPUT_FIELDS = 5;

int main() {
    long double height, width, x, y, radius;
    if (std::scanf("%Lf%Lf%Lf%Lf%Lf", &height, &width, &x, &y, &radius) != INPUT_FIELDS)
        return 0;

    // The height is affine over the whole disc, so its average is the center height.
    const auto offset = std::fmax(std::fabs(x), std::fabs(y));
    const auto center_height = height * (width - 2 * offset) / width;
    const auto volume = height * width * width / 3 - PI * radius * radius * center_height;
    std::printf("%.5Lf\n", volume);
}
