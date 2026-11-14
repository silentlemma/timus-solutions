#include <algorithm>
#include <array>
#include <cstdio>

constexpr int MAX_CARS = 300;
constexpr int PER_METRE = 9;
constexpr int LANE_TIME = 72;
constexpr int CAR_LENGTH = 5;
constexpr int UNITS_PER_SECOND = 50;

int main() {
    std::array<std::array<int, MAX_CARS>, 2> left_end;
    std::array<int, 2> count{}, next{};
    for (int lane = 0; lane < 2; ++lane) {
        if (std::scanf("%d", &count[lane]) != 1)
            return 0;
        for (int i = 0; i < count[lane]; ++i) {
            int distance;
            if (std::scanf("%d", &distance) != 1)
                return 0;
            left_end[lane][i] = PER_METRE * distance - (lane + 1) * LANE_TIME;
        }
    }

    int wait = 0;
    constexpr int WIDTH = LANE_TIME + PER_METRE * CAR_LENGTH;
    while (next[0] < count[0] || next[1] < count[1]) {
        const int lane = next[0] < count[0] && (next[1] == count[1] ||
                                                left_end[0][next[0]] <= left_end[1][next[1]])
                             ? 0
                             : 1;
        const int start = left_end[lane][next[lane]++];
        if (start >= wait)
            break;
        wait = std::max(wait, start + WIDTH);
    }
    std::printf("%.6f\n", static_cast<double>(wait) / UNITS_PER_SECOND);
}
