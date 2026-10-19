#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

std::string solve(std::string pattern, int limit) {
    constexpr int ALPHABET = 26;
    std::array<bool, ALPHABET + 1> fixed{};
    std::vector<int> positive, negative;
    for (int index = 0; index < static_cast<int>(pattern.size()); ++index) {
        if (pattern[index] != '?')
            fixed[pattern[index] - 'a' + 1] = true;
        else if (index % 2 == 0)
            positive.push_back(index);
        else
            negative.push_back(index);
    }
    int fixed_count = std::count(fixed.begin(), fixed.end(), true);
    int needed = std::max(0, limit - fixed_count);
    if (static_cast<int>(positive.size() + negative.size()) < needed)
        return "-1";
    std::vector<int> missing;
    for (int value = 1; value <= ALPHABET; ++value)
        if (!fixed[value])
            missing.push_back(value);
    int count = static_cast<int>(missing.size());
    std::vector<int> low(count + 1), high(count + 1);
    for (int index = 0; index < count; ++index) {
        low[index + 1] = low[index] + missing[index] - 1;
        high[index + 1] = high[index] + ALPHABET - missing[count - 1 - index];
    }
    int lower = std::max(0, needed - static_cast<int>(negative.size()));
    int upper = std::min(needed, static_cast<int>(positive.size()));
    int best_cost = ALPHABET * ALPHABET;
    int chosen = 0;
    for (int take = lower; take <= upper; ++take) {
        int cost = high[take] + low[needed - take];
        if (cost < best_cost) {
            best_cost = cost;
            chosen = take;
        }
    }
    for (int index : positive)
        pattern[index] = 'z';
    for (int index : negative)
        pattern[index] = 'a';
    for (int index = 0; index < chosen; ++index)
        pattern[positive[index]] = 'a' + missing[count - 1 - index] - 1;
    for (int index = 0; index < needed - chosen; ++index)
        pattern[negative[index]] = 'a' + missing[index] - 1;
    return pattern;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string pattern;
    int limit;
    if (!(std::cin >> pattern >> limit))
        return 0;
    std::cout << solve(pattern, limit) << '\n';
    return 0;
}
