#include <algorithm>
#include <cstdio>

constexpr int AXES = 3;

struct Axis {
    int size, position = 0, low = 0, high = 0;

    void move(int step) {
        position += step;
        low = std::min(low, position);
        high = std::max(high, position);
    }

    int count() const { return std::max(1, size - (high - low)); }
};

int main() {
    Axis width{}, height{}, depth{};
    if (std::scanf("%d%d%d", &width.size, &height.size, &depth.size) != AXES)
        return 0;
    for (int ch = std::getchar(); ch != EOF; ch = std::getchar()) {
        switch (ch) {
        case 'l':
            width.move(-1);
            break;
        case 'r':
            width.move(1);
            break;
        case 'd':
            height.move(-1);
            break;
        case 'u':
            height.move(1);
            break;
        case 'b':
            depth.move(-1);
            break;
        case 'f':
            depth.move(1);
            break;
        }
    }
    const long long total = static_cast<long long>(width.count()) * height.count() * depth.count();
    std::printf("%lld\n", total);
}
