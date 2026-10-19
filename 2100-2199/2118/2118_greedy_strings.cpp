#include <array>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

constexpr int BYTE_VALUES = 256;
const string ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

struct Node {
    array<int, 2> next = {0, 0};
    int failure = 0;
    bool terminal = false;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int size;
    string message;
    cin >> size >> message;
    vector<string> codes(size);
    array<int, BYTE_VALUES> index{};
    int singles = 0;
    int good = 0;
    for (int letter = 0; letter < size; ++letter) {
        cin >> codes[letter];
        index[static_cast<unsigned char>(ALPHABET[letter])] = letter;
        if (codes[letter].size() == 1) {
            ++singles;
            good = codes[letter][0] - '0';
        }
    }
    if (singles == 2) {
        cout << -1 << '\n';
        return 0;
    }

    const int bad = 1 - good;
    vector<int> counts(size);
    vector<vector<int>> words(size);
    for (int letter = 0; letter < size; ++letter) {
        for (auto it = codes[letter].rbegin(); it != codes[letter].rend(); ++it) {
            const int bit = *it - '0';
            words[letter].push_back(bit);
            counts[letter] += singles == 0 || bit == bad;
        }
    }
    int total = 0;
    for (char &letter : message) {
        letter = static_cast<char>(index[static_cast<unsigned char>(letter)]);
        total += counts[static_cast<unsigned char>(letter)];
    }
    if (singles == 0 || total == 0) {
        cout << (singles == 0 ? total : -1) << '\n';
        return 0;
    }

    vector<Node> trie(1);
    for (const auto &word : words) {
        int state = 0;
        for (int bit : word) {
            if (trie[state].next[bit] == 0) {
                trie[state].next[bit] = static_cast<int>(trie.size());
                trie.emplace_back();
            }
            state = trie[state].next[bit];
        }
        trie[state].terminal = true;
    }
    queue<int> pending;
    for (int child : trie[0].next) {
        if (child != 0) {
            pending.push(child);
        }
    }
    while (!pending.empty()) {
        const int state = pending.front();
        pending.pop();
        const int fallback = trie[state].failure;
        trie[state].terminal = trie[state].terminal || trie[fallback].terminal;
        for (int bit = 0; bit < 2; ++bit) {
            const int child = trie[state].next[bit];
            if (child != 0) {
                trie[child].failure = trie[fallback].next[bit];
                pending.push(child);
            } else {
                trie[state].next[bit] = trie[fallback].next[bit];
            }
        }
    }

    // A cached transition consumes a whole reversed codeword.
    vector<vector<int>> cache(trie.size(), vector<int>(size));
    int state = 0;
    int tail = 0;
    for (auto it = message.rbegin(); it != message.rend(); ++it) {
        const int letter = static_cast<unsigned char>(*it);
        int &edge = cache[state][letter];
        if (edge == 0) {
            int current = state;
            int consumed = 0;
            for (int bit : words[letter]) {
                consumed += bit == bad;
                current = trie[current].next[bit];
                if (!trie[current].terminal) {
                    edge = -consumed;
                    break;
                }
            }
            if (edge == 0) {
                edge = current + 1;
            }
        }
        if (edge < 0) {
            cout << total - tail + edge + 1 << '\n';
            return 0;
        }
        state = edge - 1;
        tail += counts[letter];
    }
    cout << -1 << '\n';
}
