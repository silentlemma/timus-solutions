#include <algorithm>
#include <iostream>
#include <vector>

constexpr int GOALS = 3;
constexpr int MODULUS = 1000000007;

int countForecasts(int size) {
    const int total = GOALS * size * (size - 1) / 2;
    const int maximum = GOALS * (size - 1), stride = maximum + 1;
    int maxRows = 1;
    for (int used = 0; used <= size; ++used) {
        maxRows = std::max(maxRows, total * used / size - GOALS * used * (used - 1) / 2 + 1);
    }
    std::vector<int> current(maxRows * stride), following(maxRows * stride);
    current[0] = 1;
    int lower = 0, upper = 0;
    for (int used = 0; used < size; ++used) {
        const int nextUsed = used + 1;
        const int nextLower = GOALS * nextUsed * used / 2;
        const int nextUpper = total * nextUsed / size;
        std::fill(following.begin(), following.end(), 0);
        for (int partial = lower; partial <= upper; ++partial) {
            const int minimumLast = used ? (partial + used - 1) / used : 0;
            const int first = std::max({0, nextLower - partial, minimumLast});
            const int last =
                std::min({maximum, nextUpper - partial, (total - partial) / (size - used)});
            if (first > last)
                continue;
            const int row = (partial - lower) * stride;
            long long prefix = 0;
            for (int value = 0; value < first; ++value)
                prefix += current[row + value];
            for (int value = first; value <= last; ++value) {
                prefix += current[row + value];
                if (prefix != 0) {
                    following[(partial + value - nextLower) * stride + value] =
                        static_cast<int>(prefix % MODULUS);
                }
            }
        }
        current.swap(following);
        lower = nextLower;
        upper = nextUpper;
    }
    long long answer = 0;
    for (int value = 0; value < stride; ++value)
        answer += current[value];
    return static_cast<int>(answer % MODULUS);
}

int main() {
    int size;
    std::cin >> size;
    std::cout << countForecasts(size) << '\n';
    return 0;
}
