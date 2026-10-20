#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int exponent;
    int query_count;
    std::cin >> exponent >> query_count;
    const int count = 1 << exponent;
    std::vector<std::int64_t> prefix(count + 1, 0);
    for (int index = 0; index < count; ++index) {
        int temperature;
        std::cin >> temperature;
        prefix[index + 1] = prefix[index] + temperature;
    }

    std::vector<std::vector<std::int64_t>> time(exponent + 1);
    time[0].resize(count, 0);
    for (int power = 1; power <= exponent; ++power) {
        const int half = 1 << (power - 1);
        const int width = 2 * half;
        const int starts = count - width + 1;
        time[power].resize(starts);
        for (int left = 0; left < starts; ++left) {
            std::int64_t difference = 2 * prefix[left + half] - prefix[left] - prefix[left + width];
            if (difference < 0) {
                difference = -difference;
            }
            // The two halves finish independently before their final merge.
            time[power][left] =
                std::max(time[power - 1][left], time[power - 1][left + half]) + difference;
        }
    }

    for (int query = 0; query < query_count; ++query) {
        int left;
        int power;
        std::cin >> left >> power;
        std::cout << time[power][left - 1] << ".0\n";
    }
}
