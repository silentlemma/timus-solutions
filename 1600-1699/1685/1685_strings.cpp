#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::string text;
    std::getline(std::cin, text);
    while (!text.empty() && (text.back() == '\r' || text.back() == '\n')) {
        text.pop_back();
    }
    int n = text.size();
    std::string out(n, ' ');
    // the encoded text lists the middle of a range, then its left part,
    // then its right part: replay that order and put each letter back
    std::vector<std::pair<int, int>> stack = {{0, n - 1}};
    int at = 0;
    while (!stack.empty()) {
        auto [lo, hi] = stack.back();
        stack.pop_back();
        if (lo > hi) {
            continue;
        }
        int mid = (lo + hi) / 2;
        out[mid] = text[at++];
        stack.push_back({mid + 1, hi});
        stack.push_back({lo, mid - 1});
    }
    std::cout << out << "\n";
}
