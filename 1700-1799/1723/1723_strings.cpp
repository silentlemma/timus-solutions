#include <iostream>
#include <string>

const int LETTERS = 26;

// every occurrence of a spell starts with an occurrence of its first
// letter, so a most frequent single letter is a strongest spell
int main() {
    std::string s;
    std::cin >> s;
    int count[LETTERS] = {};
    int best = 0;
    for (char c : s) {
        count[c - 'a']++;
        if (count[c - 'a'] > count[best])
            best = c - 'a';
    }
    std::cout << char('a' + best) << "\n";
}
