#include <algorithm>
#include <cstdint>
#include <iostream>

std::int64_t bestCount(std::int64_t sample, std::int64_t successes, std::int64_t population) {
    return std::min(population, successes * (population + 1) / sample);
}

int main() {
    std::int64_t sample, successes, population;
    if (!(std::cin >> sample >> successes >> population))
        return 0;
    std::cout << bestCount(sample, successes, population) << '\n';
}
