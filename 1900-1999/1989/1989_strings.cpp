#include <cstring>
#include <iostream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string word;
    std::cin >> word;
    std::string reverse(word.rbegin(), word.rend());
    const int size = static_cast<int>(word.size());
    int operations;
    std::cin >> operations;
    std::string answer;
    while (operations-- > 0) {
        std::string operation;
        int left;
        std::cin >> operation >> left;
        if (operation == "change") {
            char value;
            std::cin >> value;
            word[left - 1] = value;
            reverse[size - left] = value;
        } else {
            int right;
            std::cin >> right;
            const auto length = static_cast<std::size_t>((right - left + 1) / 2);
            answer +=
                std::memcmp(word.data() + left - 1, reverse.data() + size - right, length) == 0
                    ? "Yes\n"
                    : "No\n";
        }
    }
    std::cout << answer;
}
