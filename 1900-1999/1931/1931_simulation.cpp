#include <iostream>
#include <vector>

int mostCompared(const std::vector<int> &values) {
    int championValue = values[0];
    int champion = 0;
    int best = 0;
    int currentCount = 0;
    int bestCount = 0;
    for (int index = 1; index < static_cast<int>(values.size()); ++index) {
        ++currentCount;
        if (currentCount > bestCount) {
            bestCount = currentCount;
            best = champion;
        }
        if (values[index] < championValue) {
            championValue = values[index];
            champion = index;
            currentCount = 1;
        }
    }
    return best + 1;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int> values(count);
    for (int &value : values) {
        std::cin >> value;
    }
    std::cout << mostCompared(values) << '\n';
    return 0;
}
