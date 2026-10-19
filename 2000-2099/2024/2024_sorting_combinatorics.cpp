#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <utility>

std::pair<int, long long> solve(const std::string &text, int limit) {
    constexpr int ALPHABET = 26;
    std::array<int, ALPHABET> counts{};
    for (char letter : text)
        ++counts[letter - 'a'];
    std::sort(counts.rbegin(), counts.rend());
    int size = 0;
    for (int index = 0; index < limit; ++index)
        size += counts[index];
    int boundary = counts[limit - 1];
    if (boundary == 0)
        return {size, 1};
    int greater = 0;
    int tied = 0;
    for (int count : counts) {
        greater += count > boundary;
        tied += count == boundary;
    }
    int chosen = std::min(limit - greater, tied - (limit - greater));
    long long ways = 1;
    for (int index = 1; index <= chosen; ++index)
        ways = ways * (tied - index + 1) / index;
    return {size, ways};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string text;
    int limit;
    if (!(std::cin >> text >> limit))
        return 0;
    auto answer = solve(text, limit);
    std::cout << answer.first << ' ' << answer.second << '\n';
    return 0;
}
