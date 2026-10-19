#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

constexpr int DECIMAL_PLACES = 12;

std::vector<std::vector<double>> build(int limit, int maximum_spies) {
    std::vector<std::vector<double>> choose(limit + 1);
    for (int size = 0; size <= limit; ++size) {
        choose[size].assign(size + 1, 1.0);
        for (int j = 1; j < size; ++j)
            choose[size][j] = choose[size - 1][j - 1] + choose[size - 1][j];
    }
    std::vector<std::vector<double>> table(limit + 1, std::vector<double>(maximum_spies + 1));
    for (int size = 1; size <= limit; ++size) {
        table[size][0] = size;
        for (int spies = 1; spies <= std::min(maximum_spies, size - 1); ++spies) {
            const int loyal = size - spies;
            double best = 0;
            for (int retained = 1; retained < size; ++retained) {
                const int lower = std::max(0, retained - loyal);
                const int upper = std::min(spies, (retained - 1) / 2);
                double weighted = 0;
                for (int remaining = lower; remaining <= upper; ++remaining) {
                    weighted += choose[spies][remaining] * choose[loyal][retained - remaining] *
                                table[retained - remaining][remaining];
                }
                best = std::max(best, weighted / choose[size][retained]);
            }
            table[size][spies] = best;
        }
    }
    return table;
}
int main() {
    int total, spies;
    std::cin >> total >> spies;
    double answer = 0;
    if (total > 2 * spies)
        answer = build(total - spies, spies)[total - spies][spies];
    std::cout << std::fixed << std::setprecision(DECIMAL_PLACES) << answer << '\n';
    return 0;
}
