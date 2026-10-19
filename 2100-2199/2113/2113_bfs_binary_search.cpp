#include <array>
#include <iostream>
#include <vector>

namespace {
constexpr int kBlocked = -1;
constexpr int kMaximumHeight = 100000;
constexpr int kDirectionCount = 2 * 2;

bool canEscape(const std::vector<int> &height, const std::vector<int> &water,
               const std::array<int, kDirectionCount> &offsets, int start, int jump, int infinity) {
    if (water[start] == infinity) {
        return true;
    }

    std::vector<int> distance(height.size(), kBlocked);
    std::vector<int> queue(height.size());
    int head = 0;
    int tail = 0;
    queue[tail++] = start;
    distance[start] = 0;

    while (head < tail) {
        const int current = queue[head++];
        const int arrival = distance[current] + 1;
        for (const int offset : offsets) {
            const int next = current + offset;
            if (height[next] == kBlocked || distance[next] != kBlocked ||
                height[next] - height[current] > jump || arrival >= water[next]) {
                continue;
            }
            if (water[next] == infinity) {
                return true;
            }
            distance[next] = arrival;
            queue[tail++] = next;
        }
    }
    return false;
}
} // namespace

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int rows;
    int columns;
    std::cin >> rows >> columns;
    const int stride = columns + 2;
    const int size = (rows + 2) * stride;
    const int infinity = size + 1;
    std::vector<int> height(size, kBlocked);
    for (int row = 1; row <= rows; ++row) {
        for (int column = 1; column <= columns; ++column) {
            std::cin >> height[row * stride + column];
        }
    }
    int row;
    int column;
    std::cin >> row >> column;
    const int start = row * stride + column;
    std::cin >> row >> column;
    const int source = row * stride + column;
    const std::array<int, kDirectionCount> offsets = {-stride, -1, 1, stride};

    std::vector<int> water(size, infinity);
    std::vector<int> queue(size);
    int head = 0;
    int tail = 0;
    queue[tail++] = source;
    water[source] = 0;
    while (head < tail) {
        const int current = queue[head++];
        for (const int offset : offsets) {
            const int next = current + offset;
            if (height[next] == kBlocked || height[next] > height[current] ||
                water[next] != infinity) {
                continue;
            }
            water[next] = water[current] + 1;
            queue[tail++] = next;
        }
    }

    if (!canEscape(height, water, offsets, start, kMaximumHeight, infinity)) {
        std::cout << -1 << '\n';
        return 0;
    }
    int low = 0;
    int high = kMaximumHeight;
    while (low < high) {
        const int middle = low + (high - low) / 2;
        if (canEscape(height, water, offsets, start, middle, infinity)) {
            high = middle;
        } else {
            low = middle + 1;
        }
    }
    std::cout << low << '\n';
}
