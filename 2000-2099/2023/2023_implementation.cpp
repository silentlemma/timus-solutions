#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

int solve(const std::vector<std::string> &names) {
    const std::string left = "APOR";
    const std::string middle = "BMS";
    int position = 0;
    int steps = 0;
    for (const std::string &name : names) {
        const char initial = name.front();
        const int target = left.find(initial) != std::string::npos     ? 0
                           : middle.find(initial) != std::string::npos ? 1
                                                                       : 2;
        steps += std::abs(target - position);
        position = target;
    }
    return steps;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    if (!(std::cin >> count))
        return 0;
    std::vector<std::string> names(count);
    for (std::string &name : names)
        std::cin >> name;
    std::cout << solve(names) << '\n';
    return 0;
}
