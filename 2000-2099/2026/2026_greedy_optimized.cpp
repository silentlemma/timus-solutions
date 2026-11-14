#include <algorithm>
#include <array>
#include <cstdio>

constexpr int ALPHABET = 26;
constexpr int MAX_LENGTH = 100000;

int main() {
    char pattern[MAX_LENGTH + 1];
    int limit;
    if (std::scanf("%100000s%d", pattern, &limit) != 2)
        return 0;

    std::array<bool, ALPHABET> fixed{};
    std::array<int, 2> holes{};
    for (int i = 0; pattern[i]; ++i) {
        if (pattern[i] == '?')
            ++holes[i % 2];
        else
            fixed[pattern[i] - 'a'] = true;
    }
    std::array<int, ALPHABET> missing{};
    int absent = 0;
    for (int letter = 0; letter < ALPHABET; ++letter) {
        if (!fixed[letter])
            missing[absent++] = letter;
    }
    const int needed = std::max(0, limit - (ALPHABET - absent));
    if (holes[0] + holes[1] < needed) {
        std::puts("-1");
        return 0;
    }

    std::array<int, ALPHABET + 1> low{}, high{};
    for (int i = 0; i < absent; ++i) {
        low[i + 1] = low[i] + missing[i];
        high[i + 1] = high[i] + ALPHABET - 1 - missing[absent - 1 - i];
    }
    int positive = 0, best = ALPHABET * ALPHABET;
    for (int take = std::max(0, needed - holes[1]); take <= std::min(needed, holes[0]); ++take) {
        const int cost = high[take] + low[needed - take];
        if (cost < best) {
            best = cost;
            positive = take;
        }
    }

    // Rescan the input instead of storing every hole index.
    std::array<int, 2> remaining{positive, needed - positive};
    int left = 0, right = absent;
    for (int i = 0; pattern[i]; ++i) {
        if (pattern[i] != '?')
            continue;
        const int sign = i % 2;
        if (remaining[sign] == 0) {
            pattern[i] = sign == 0 ? 'z' : 'a';
        } else {
            pattern[i] = 'a' + (sign == 0 ? missing[--right] : missing[left++]);
            --remaining[sign];
        }
    }
    std::puts(pattern);
}
