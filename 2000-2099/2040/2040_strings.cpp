#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

struct Node {
    int32_t length = 0;
    int32_t link = 0;
    std::array<int32_t, 2> next{};
};

std::string solve(const std::string &word) {
    std::vector<Node> nodes(word.size() + 2);
    nodes[0].length = -1;
    int32_t last = 1, used = 2;
    std::string output(word.size(), '0');
    for (int pos = 0; pos < static_cast<int>(word.size()); ++pos) {
        const int letter = word[pos] - 'a';
        int32_t parent = last;
        while (true) {
            const int before = pos - 1 - nodes[parent].length;
            if (before >= 0 && word[before] == word[pos])
                break;
            parent = nodes[parent].link;
        }
        int32_t current = nodes[parent].next[letter];
        if (current == 0) {
            current = used++;
            nodes[current].length = nodes[parent].length + 2;
            nodes[parent].next[letter] = current;
            if (nodes[current].length == 1) {
                nodes[current].link = 1;
            } else {
                int32_t candidate = nodes[parent].link;
                while (true) {
                    const int before = pos - 1 - nodes[candidate].length;
                    if (before >= 0 && word[before] == word[pos])
                        break;
                    candidate = nodes[candidate].link;
                }
                nodes[current].link = nodes[candidate].next[letter];
            }
            output[pos] = '1';
        }
        last = current;
    }
    return output;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string word;
    if (std::cin >> word)
        std::cout << solve(word) << '\n';
}
