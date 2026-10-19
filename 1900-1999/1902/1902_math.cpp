#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count, duration, start;
    std::cin >> count >> duration >> start;
    for (int i = 0; i < count; ++i) {
        int other;
        std::cin >> other;
        int doubled_time = start + duration + other;
        std::cout << doubled_time / 2
                  << (doubled_time % 2 == 0 ? ".000000\n" : ".500000\n");
    }
}
