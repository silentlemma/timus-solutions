#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

std::int64_t minimumCommon(std::int64_t population, const std::vector<std::int64_t> &lowerBounds) {
    auto answer = population;
    for (auto lower : lowerBounds)
        answer -= population - lower;
    return std::max<std::int64_t>(0, answer);
}

int main() {
    std::int64_t population;
    int count;
    std::cin >> population >> count;
    std::vector<std::int64_t> lowerBounds(count);
    for (auto &lower : lowerBounds)
        std::cin >> lower;
    std::cout << minimumCommon(population, lowerBounds) << '\n';
}
