#include <iostream>
#include <utility>
#include <vector>

int requiredInput(int current, const std::vector<std::pair<int, int>> &history) {
    int answer = current - 2;
    for (const auto &reading : history) {
        answer += reading.first - reading.second - 2;
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count, current;
    std::cin >> count >> current;
    std::vector<std::pair<int, int>> history(count);
    for (auto &reading : history) {
        std::cin >> reading.first >> reading.second;
    }
    int answer = requiredInput(current, history);
    if (answer >= 0) {
        std::cout << answer << '\n';
    } else {
        std::cout << "Big Bang!\n";
    }
    return 0;
}
