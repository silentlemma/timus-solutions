#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Palindromes {
    std::vector<int> odd, even;
    explicit Palindromes(const std::string &word) : odd(word.size()), even(word.size()) {
        int size = static_cast<int>(word.size()), left = 0, right = -1;
        for (int center = 0; center < size; ++center) {
            int radius =
                center > right ? 1 : std::min(odd[left + right - center], right - center + 1);
            while (center >= radius && center + radius < size &&
                   word[center - radius] == word[center + radius])
                ++radius;
            odd[center] = radius;
            if (center + radius - 1 > right) {
                left = center - radius + 1;
                right = center + radius - 1;
            }
        }
        left = 0;
        right = -1;
        for (int center = 0; center < size; ++center) {
            int radius =
                center > right ? 0 : std::min(even[left + right - center + 1], right - center + 1);
            while (center > radius && center + radius < size &&
                   word[center - radius - 1] == word[center + radius])
                ++radius;
            even[center] = radius;
            if (center + radius - 1 > right) {
                left = center - radius;
                right = center + radius - 1;
            }
        }
    }
    bool palindrome(int start, int end) const {
        int length = end - start, center = (start + end) / 2;
        return length % 2 ? odd[center] >= length / 2 + 1 : even[center] >= length / 2;
    }
};

std::pair<int, int> solve(const std::string &word) {
    int size = static_cast<int>(word.size());
    Palindromes radii(word);
    std::vector<int> maximum(size + 1, -1), first(size / 2 + 1, -1), last(size / 2 + 1, -1);
    maximum[0] = 0;
    int highest = -1;
    for (int end = 1; end <= size; ++end) {
        int position = end - 2;
        if (position >= 0 && maximum[position] >= 0) {
            int value = maximum[position];
            if (first[value] < 0)
                first[value] = position;
            last[value] = position;
            highest = std::max(highest, value);
        }
        for (int value : {highest, highest - 1}) {
            if (value >= 0 && first[value] >= 0 &&
                (!radii.palindrome(first[value], end) || !radii.palindrome(last[value], end))) {
                maximum[end] = value + 1;
                break;
            }
        }
    }
    if (maximum[size] < 0)
        return {-1, -1};
    return {radii.palindrome(0, size) ? 2 : 1, maximum[size]};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string word;
    std::cin >> word;
    auto answer = solve(word);
    if (answer.first < 0)
        std::cout << -1 << '\n';
    else
        std::cout << answer.first << ' ' << answer.second << '\n';
}
