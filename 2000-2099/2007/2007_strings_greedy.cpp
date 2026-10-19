#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

constexpr int ALPHABET = 26;
constexpr char FIRST = 'a';

std::string solve(const std::string &source, const std::string &modifiers) {
    int size = static_cast<int>(source.size());
    std::array<std::vector<int>, ALPHABET> positions;
    for (int at = 0; at < size; ++at)
        positions[source[at] - FIRST].push_back(at);
    std::array<int, ALPHABET> frequency{}, counts{}, head{}, cut{}, next_position{}, next_cut{},
        delta{};
    for (char ch : modifiers)
        ++counts[ch - FIRST];
    unsigned int bad = 0, available = 0, present = 0;
    for (int c = 0; c < ALPHABET; ++c) {
        frequency[c] = static_cast<int>(positions[c].size());
        positions[c].push_back(size);
        cut[c] = counts[c];
        next_position[c] = positions[c][0];
        next_cut[c] = cut[c] < frequency[c] ? positions[c][cut[c]] : size;
        delta[c] = counts[c] - frequency[c];
        if (delta[c] < 0 || (delta[c] & 1))
            bad |= 1U << c;
        if (counts[c])
            available |= 1U << c;
        if (frequency[c])
            present |= 1U << c;
    }
    int at = 0, original = ALPHABET;
    bool dirty = true;
    std::string answer;
    answer.reserve(source.size() + modifiers.size());
    while (bad) {
        if (dirty) {
            if (at == size)
                original = ALPHABET;
            else if (counts[source[at] - FIRST] == 0)
                original = source[at] - FIRST;
            else {
                int limit = *std::min_element(next_cut.begin(), next_cut.end());
                unsigned int candidates = present;
                while (candidates) {
                    int c = __builtin_ctz(candidates);
                    if (next_position[c] <= limit) {
                        original = c;
                        break;
                    }
                    candidates &= candidates - 1;
                }
            }
            dirty = false;
        }
        int modifier = available ? __builtin_ctz(available) : ALPHABET;
        int c;
        if (original <= modifier) {
            c = original;
            int to = next_position[c];
            while (at < to) {
                int removed = source[at++] - FIRST;
                --counts[removed];
                next_position[removed] = positions[removed][++head[removed]];
                if (counts[removed] == 0)
                    available &= ~(1U << removed);
                if (head[removed] == frequency[removed])
                    present &= ~(1U << removed);
            }
            next_position[c] = positions[c][++head[c]];
            ++at;
            if (head[c] == frequency[c])
                present &= ~(1U << c);
            ++cut[c];
            ++delta[c];
            dirty = true;
        } else {
            c = modifier;
            if (--counts[c] == 0)
                available &= ~(1U << c);
            --cut[c];
            --delta[c];
        }
        next_cut[c] = cut[c] < frequency[c] ? positions[c][cut[c]] : size;
        if (delta[c] < 0 || (delta[c] & 1))
            bad |= 1U << c;
        else
            bad &= ~(1U << c);
        answer.push_back(static_cast<char>(FIRST + c));
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string source, modifiers;
    std::cin >> source >> modifiers;
    std::cout << solve(source, modifiers) << '\n';
}
