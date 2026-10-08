#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

const int MAX_WORD_LENGTH = 50;
const char *const KEYPAD = "22233344115566070778889990";
const std::string END_OF_INPUT = "-1";

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string phone;
    while (std::cin >> phone && phone != END_OF_INPUT) {
        int n;
        std::cin >> n;
        std::vector<std::string> words(n);
        std::unordered_map<std::string, int> byDigits;
        for (int i = 0; i < n; i++) {
            std::cin >> words[i];
            std::string digits = words[i];
            for (char &c : digits)
                c = KEYPAD[c - 'a'];
            byDigits.emplace(digits, i);
        }
        // best[i]: fewest words for the first i digits; how[i]: last word used
        int m = phone.size();
        std::vector<int> best(m + 1, -1), how(m + 1, -1);
        best[0] = 0;
        for (int i = 0; i < m; i++) {
            if (best[i] < 0)
                continue;
            for (int len = 1; len <= MAX_WORD_LENGTH && i + len <= m; len++) {
                auto it = byDigits.find(phone.substr(i, len));
                if (it != byDigits.end() && (best[i + len] < 0 || best[i] + 1 < best[i + len])) {
                    best[i + len] = best[i] + 1;
                    how[i + len] = it->second;
                }
            }
        }
        if (best[m] < 0) {
            std::cout << "No solution.\n";
            continue;
        }
        std::vector<int> used;
        for (int pos = m; pos > 0; pos -= words[how[pos]].size())
            used.push_back(how[pos]);
        for (int i = used.size() - 1; i >= 0; i--)
            std::cout << words[used[i]] << (i ? ' ' : '\n');
    }
    return 0;
}
