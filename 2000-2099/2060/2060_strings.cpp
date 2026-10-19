#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

std::pair<std::vector<int>, std::vector<int>> palindrome_counts(const std::string &word) {
    int n = static_cast<int>(word.size());
    std::vector<int> radii(n), ending(n + 1), starting(n + 1);
    int left = 0, right = -1;
    for (int center = 0; center < n; ++center) {
        int radius =
            center > right ? 1 : std::min(radii[left + right - center], right - center + 1);
        while (center - radius >= 0 && center + radius < n &&
               word[center - radius] == word[center + radius])
            ++radius;
        radii[center] = radius;
        if (center + radius - 1 > right) {
            left = center - radius + 1;
            right = center + radius - 1;
        }
        ++ending[center];
        --ending[center + radius];
        ++starting[center - radius + 1];
        --starting[center + 1];
    }
    left = 0;
    right = -1;
    for (int center = 0; center < n; ++center) {
        int radius =
            center > right ? 0 : std::min(radii[left + right - center + 1], right - center + 1);
        while (center - radius - 1 >= 0 && center + radius < n &&
               word[center - radius - 1] == word[center + radius])
            ++radius;
        radii[center] = radius;
        if (center + radius - 1 > right) {
            left = center - radius;
            right = center + radius - 1;
        }
        if (radius != 0) {
            ++ending[center];
            --ending[center + radius];
            ++starting[center - radius];
            --starting[center];
        }
    }
    int count_ending = 0, count_starting = 0;
    for (int i = 0; i < n; ++i) {
        count_ending += ending[i];
        count_starting += starting[i];
        ending[i] = count_ending;
        starting[i] = count_starting;
    }
    return {std::move(ending), std::move(starting)};
}

std::int64_t solve(const std::string &word) {
    auto counts = palindrome_counts(word);
    std::int64_t answer = 0;
    for (std::size_t cut = 0; cut + 1 < word.size(); ++cut)
        answer += static_cast<std::int64_t>(counts.first[cut]) * counts.second[cut + 1];
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string word;
    std::cin >> word;
    std::cout << solve(word) << '\n';
}
