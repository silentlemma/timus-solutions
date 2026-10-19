#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

constexpr int ALPHABET_SIZE = 26;

std::vector<int> palindromeRadii(const std::string &text, bool odd) {
    const int count = static_cast<int>(text.size());
    std::vector<int> radius(count, 0);
    int left = 0, right = -1;
    if (odd) {
        for (int center = 0; center < count; ++center) {
            int current =
                center > right ? 0 : std::min(radius[left + right - center], right - center);
            while (center - current - 1 >= 0 && center + current + 1 < count &&
                   text[center - current - 1] == text[center + current + 1]) {
                ++current;
            }
            radius[center] = current;
            if (center + current > right) {
                left = center - current;
                right = center + current;
            }
        }
    } else {
        for (int center = 0; center < count; ++center) {
            int current = center > right
                              ? 0
                              : std::min(radius[left + right - center + 1], right - center + 1);
            while (center - current - 1 >= 0 && center + current < count &&
                   text[center - current - 1] == text[center + current]) {
                ++current;
            }
            radius[center] = current;
            if (center + current - 1 > right) {
                left = center - current;
                right = center + current - 1;
            }
        }
    }
    return radius;
}

struct SuffixAutomaton {
    std::vector<std::array<int, ALPHABET_SIZE>> transitions;
    std::vector<int> length, link, firstEnd;

    explicit SuffixAutomaton(const std::string &pattern)
        : transitions(2 * pattern.size()), length(2 * pattern.size(), 0),
          link(2 * pattern.size(), -1), firstEnd(2 * pattern.size(), -1) {
        for (auto &row : transitions) {
            row.fill(-1);
        }
        int states = 1, last = 0;
        for (int position = 0; position < static_cast<int>(pattern.size()); ++position) {
            const int symbol = pattern[position] - 'a';
            const int current = states++;
            length[current] = length[last] + 1;
            firstEnd[current] = position;
            int previous = last;
            while (previous >= 0 && transitions[previous][symbol] < 0) {
                transitions[previous][symbol] = current;
                previous = link[previous];
            }
            if (previous < 0) {
                link[current] = 0;
            } else {
                const int following = transitions[previous][symbol];
                if (length[previous] + 1 == length[following]) {
                    link[current] = following;
                } else {
                    const int clone = states++;
                    length[clone] = length[previous] + 1;
                    link[clone] = link[following];
                    firstEnd[clone] = firstEnd[following];
                    transitions[clone] = transitions[following];
                    while (previous >= 0 && transitions[previous][symbol] == following) {
                        transitions[previous][symbol] = clone;
                        previous = link[previous];
                    }
                    link[following] = link[current] = clone;
                }
            }
            last = current;
        }
    }
};

std::pair<int, int> findRotations(const std::string &first, const std::string &second) {
    const int firstSize = static_cast<int>(first.size());
    const int secondSize = static_cast<int>(second.size());
    const int middleSize = firstSize - secondSize;
    const std::string doubled = first + first;
    const auto radius = palindromeRadii(doubled, middleSize % 2 != 0);
    const int half = middleSize / 2, centerOffset = secondSize + half;
    bool candidateExists = false;
    for (int start = 0; start < firstSize; ++start) {
        if (radius[start + centerOffset] >= half) {
            candidateExists = true;
            break;
        }
    }
    if (!candidateExists) {
        return {-1, -1};
    }
    const std::string reversedSecond(second.rbegin(), second.rend());
    const std::string pattern = reversedSecond + reversedSecond.substr(0, secondSize - 1);
    const SuffixAutomaton automaton(pattern);
    int state = 0, matched = 0;
    for (int position = 0; position < firstSize + secondSize - 1; ++position) {
        const int symbol = doubled[position] - 'a';
        while (state != 0 && automaton.transitions[state][symbol] < 0) {
            state = automaton.link[state];
            matched = automaton.length[state];
        }
        const int following = automaton.transitions[state][symbol];
        if (following >= 0) {
            state = following;
            ++matched;
        } else {
            state = matched = 0;
        }
        const int start = position - secondSize + 1;
        if (start >= 0 && matched >= secondSize && radius[start + centerOffset] >= half) {
            const int reversedStart = automaton.firstEnd[state] - secondSize + 1;
            return {start, (secondSize - reversedStart) % secondSize};
        }
    }
    return {-1, -1};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string first, second;
    std::cin >> first >> second;
    const auto answer = findRotations(first, second);
    if (answer.first < 0) {
        std::cout << "No\n";
    } else {
        std::cout << "Yes\n" << answer.first + 1 << ' ' << answer.second + 1 << '\n';
    }
    return 0;
}
