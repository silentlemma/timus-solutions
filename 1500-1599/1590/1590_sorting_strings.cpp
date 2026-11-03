#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string text;
    std::cin >> text;
    std::vector<std::string_view> suffixes;
    for (int i = 0; i < int(text.size()); i++)
        suffixes.push_back(std::string_view(text).substr(i));
    std::sort(suffixes.begin(), suffixes.end());
    long long answer = 1LL * text.size() * (text.size() + 1) / 2;
    // Only the immediate predecessor is needed: all previously encountered
    // prefixes of this suffix are also prefixes of that predecessor.
    for (int i = 1; i < int(suffixes.size()); i++) {
        int common = 0;
        while (common < int(std::min(suffixes[i - 1].size(), suffixes[i].size())) &&
               suffixes[i - 1][common] == suffixes[i][common])
            common++;
        answer -= common;
    }
    std::cout << answer << '\n';
}
