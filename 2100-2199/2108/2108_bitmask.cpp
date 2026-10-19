#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

constexpr int WORD_BITS = 64;

void read_set(std::vector<std::uint64_t> &masks, int offset, int n) {
    std::string token;
    std::cin >> token;
    for (int bit = 0; bit < n; ++bit) {
        if (token[bit] == '1') {
            masks[offset + bit / WORD_BITS] |= std::uint64_t{1} << (bit % WORD_BITS);
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    std::cin >> n >> m;
    const int words = (n + WORD_BITS - 1) / WORD_BITS;
    std::vector<std::uint64_t> required(m * words), added(m * words), owned(words);
    for (int rule = 0; rule < m; ++rule) {
        read_set(required, rule * words, n);
        read_set(added, rule * words, n);
    }
    read_set(owned, 0, n);

    std::vector<char> fired(m, false);
    bool changed = true;
    while (changed) {
        changed = false;
        for (int rule = 0; rule < m; ++rule) {
            if (fired[rule]) {
                continue;
            }
            const int offset = rule * words;
            bool ready = true;
            for (int word = 0; word < words; ++word) {
                if ((required[offset + word] & ~owned[word]) != 0) {
                    ready = false;
                    break;
                }
            }
            if (!ready) {
                continue;
            }
            fired[rule] = true;
            for (int word = 0; word < words; ++word) {
                const auto merged = owned[word] | added[offset + word];
                changed |= merged != owned[word];
                owned[word] = merged;
            }
        }
    }

    std::string answer(n, '0');
    for (int bit = 0; bit < n; ++bit) {
        if ((owned[bit / WORD_BITS] >> (bit % WORD_BITS)) & 1) {
            answer[bit] = '1';
        }
    }
    std::cout << answer << '\n';
}
