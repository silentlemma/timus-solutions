#include <array>
#include <cstdint>
#include <cstdio>
#include <string>
#include <unordered_map>
#include <vector>

const int ALPHABET = 26;
const char *WORDS[] = {"out", "output", "puton", "in", "input", "one"};

const int BUFFER_SIZE = 4096;
// refillable storage bounds memory independently of the input length.
int nextByte() {
    static unsigned char buffer[BUFFER_SIZE];
    static int at = 0, size = 0;
    if (at == size) {
        size = static_cast<int>(std::fread(buffer, 1, BUFFER_SIZE, stdin));
        at = 0;
        if (!size)
            return EOF;
    }
    return buffer[at++];
}
int nextInt() {
    int c;
    do {
        c = nextByte();
    } while (c <= ' ' && c != EOF);
    int sign = 1, value = 0;
    if (c == '-') {
        sign = -1;
        c = nextByte();
    }
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = nextByte();
    }
    return value * sign;
}

int main() {
    std::array<int, ALPHABET> empty;
    empty.fill(-1);
    std::vector<std::array<int, ALPHABET>> trie(1, empty);
    std::vector<bool> terminal(1, false);
    for (const char *word : WORDS) {
        int node = 0;
        for (const char *p = word; *p; ++p) {
            int c = *p - 'a';
            if (trie[node][c] < 0) {
                trie[node][c] = static_cast<int>(trie.size());
                trie.push_back(empty);
                terminal.push_back(false);
            }
            node = trie[node][c];
        }
        terminal[node] = true;
    }
    // the six words have 24 letters in total, so all trie nodes fit in 32 bits.
    // bit zero permits a new word; other bits are unfinished matching prefixes.
    std::vector<std::uint32_t> masks{1};
    std::unordered_map<std::uint32_t, int> ids{{1, 0}};
    std::vector<std::array<int, ALPHABET>> table;
    for (size_t s = 0; s < masks.size(); ++s) {
        std::array<int, ALPHABET> row;
        for (int c = 0; c < ALPHABET; ++c) {
            std::uint32_t mask = 0;
            for (size_t node = 0; node < trie.size(); ++node) {
                int to = trie[node][c];
                if ((masks[s] & (std::uint32_t{1} << node)) && to >= 0) {
                    mask |= std::uint32_t{1} << to;
                    if (terminal[to])
                        mask |= 1;
                }
            }
            auto result = ids.emplace(mask, static_cast<int>(masks.size()));
            if (result.second)
                masks.push_back(mask);
            row[c] = result.first->second;
        }
        table.push_back(row);
    }
    int n = nextInt(), state = 0, lines = 0;
    bool started = false;
    // each input byte makes one transition; even a rejected line is consumed fully.
    for (int c; (c = nextByte()) != EOF;) {
        if (c >= 'a' && c <= 'z') {
            state = table[state][c - 'a'];
            started = true;
        } else if (started) {
            std::puts(masks[state] & 1 ? "YES" : "NO");
            state = 0;
            started = false;
            ++lines;
        }
    }
    if (started && lines < n)
        std::puts(masks[state] & 1 ? "YES" : "NO");
}
