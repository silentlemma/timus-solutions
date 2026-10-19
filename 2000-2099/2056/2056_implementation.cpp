#include <algorithm>
#include <iostream>
#include <string>

constexpr int LOW_MARK = 3;
constexpr int TOP_MARK = 5;
constexpr int DOUBLED_THRESHOLD = 9;

std::string classify(int count, int total, int lowest) {
    if (lowest == LOW_MARK)
        return "None";
    if (lowest == TOP_MARK)
        return "Named";
    if (2 * total >= DOUBLED_THRESHOLD * count)
        return "High";
    return "Common";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    int total = 0, lowest = TOP_MARK;
    for (int i = 0; i < count; ++i) {
        int grade;
        std::cin >> grade;
        total += grade;
        lowest = std::min(lowest, grade);
    }
    std::cout << classify(count, total, lowest) << '\n';
}
