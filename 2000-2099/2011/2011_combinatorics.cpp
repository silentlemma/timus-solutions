#include <array>
#include <iostream>
#include <vector>

constexpr int ALPHABET = 3;
constexpr int TARGET = 6;

bool solve(const std::vector<int> &values) {
    std::array<int, ALPHABET> counts{};
    int ways = 1, length = 0;
    for (int value : values) {
        ++length;
        ++counts[value - 1];
        ways = ways * length / counts[value - 1];
        if (ways >= TARGET)
            return true;
    }
    return false;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> values(n);
    for (int &value : values)
        std::cin >> value;
    std::cout << (solve(values) ? "Yes" : "No") << '\n';
}
