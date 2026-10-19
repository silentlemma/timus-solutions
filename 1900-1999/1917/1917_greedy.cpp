#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

std::pair<int, int> safeRemovals(std::vector<int> values, long long budget) {
    std::sort(values.begin(), values.end());
    int removed = 0;
    int spells = 0;
    int active = 0;
    for (std::size_t start = 0; start < values.size();) {
        std::size_t end = start + 1;
        while (end < values.size() && values[end] == values[start]) {
            ++end;
        }
        const int count = int(end - start);
        const long long threshold = values[start];
        if (count * threshold > budget) {
            break;
        }
        if ((active + count) * threshold > budget) {
            ++spells;
            active = 0;
        }
        active += count;
        removed += count;
        start = end;
    }
    return {removed, spells + (active > 0)};
}

int main() {
    int count;
    long long budget;
    std::cin >> count >> budget;
    std::vector<int> values(count);
    for (int &value : values) {
        std::cin >> value;
    }
    const auto answer = safeRemovals(values, budget);
    std::cout << answer.first << ' ' << answer.second << '\n';
    return 0;
}
